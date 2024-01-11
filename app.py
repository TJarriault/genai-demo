# app.py

import sys
import pickle
from flask import Flask, request, jsonify
from langchain.chains.retrieval_qa.base import RetrievalQA  # Import the specific class from langchain

app = Flask(__name__)

# Load the RetrievalQA instance from the saved file
try:
    with open('saved_chain.pkl', 'rb') as file:
        chain = pickle.load(file)
except FileNotFoundError:
    print("Error: Could not find the saved_chain.pkl file.")
    sys.exit(1)
except Exception as e:
    print(f"Error loading the 'chain' instance: {e}")
    sys.exit(1)

# Example data or function (replace with your actual implementation)
def process_query(query):
    # Replace this with your actual processing logic using the 'chain'
    result = chain.invoke(query)['result']
    return result

@app.route('/api/search', methods=['POST'])
def search_endpoint():
    # Get the JSON data from the request
    data = request.get_json()

    # Extract the query from the JSON data
    query = data.get('query', '')
    print(data)
    print(query)

    # Process the query using the 'chain'
    result = process_query(query)

    # Return the result as JSON
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
