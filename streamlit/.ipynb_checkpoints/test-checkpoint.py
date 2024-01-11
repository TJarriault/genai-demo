import streamlit as st
import requests
import json
from langchain.llms import OpenAI

def generate_response(input_text):
    #llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    #print(input_text)
    url = 'http://127.0.0.1:5001/api/search'
    data = {
    "query": input_text
    }

    # Convert the Python dictionary to a JSON format
    json_data = json.dumps(data)

    # Define the headers, if required by the API
    headers = {
        "Content-Type": "application/json"
    }

    # Send a POST request to the API
    try:
       #Request backend
       response = requests.post(url, data=json_data, headers=headers)

       if response.status_code == 200:
           # Parse the response to JSON
           response_json = response.json()

           # Extract and print the value associated with the key 'result'
           result = response_json.get('result', 'No result key found in the response')
           print(result)
       else:
           print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    st.info(result)

text="What is the last name of Tony"
generate_response(text)

