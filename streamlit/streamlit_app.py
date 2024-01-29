import streamlit as st
import requests
import json
from langchain.llms import OpenAI

st.title('🦜🔗 Demo App')

#openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

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


with st.form('my_form'):
    text = st.text_area('Enter text:', "What is Tony's experience with AWS and on-prem applications?")
    submitted = st.form_submit_button('Submit')
    #if not openai_api_key.startswith('sk-'):
    #    st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted:
        generate_response(text)


