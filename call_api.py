import requests

# Set the URL of your FastAPI endpoint
url = "http://localhost:8000/analyze"


messages = ["This api is fun", "I did not sleep well so I am grumpy"]


for message in messages:

    data = {"input_string": message}

    try:
        
        # Make a POST request to the endpoint
        response = requests.post(url, json=data)
        print(f"The sentiment is {response.json()['result']['sentiment']} with a score of {round(response.json()['result']['score'], 3)}")

    except Exception as e:

        print(f"Error: {response.status_code} - {e}")