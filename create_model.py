import requests
import json

def create_model():
    url = 'http://localhost:11434/api/create'
    headers = {
        'Content-Type': 'application/json',
    }
    
    with open('Modelfile', 'r') as file:
        modelfile_content = file.read()
    
    data = {
        "model": "command_executer",
        "modelfile": modelfile_content
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        print("Model created successfully:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error creating model: {e}")

if __name__ == "__main__":
    create_model()
