# E2E Sentiment Analysis using Hugging Face pipeline, FastAPI and Docker

This is a simple end-to-end Sentiment Analysis model which can be called in your pc. Follow the below steps to run it on your local machine.

## Setup ⚙️

### 1. Building Docker Image

```bash
docker build --network=host -t sentiment-app 
```
### 2. Running Docker Container

```bash
docker run -d -p 8000:8000 sentiment-app:latest
```

This will expose an API endpoint on `http://your_address:8000/analyze`

## Usage ⏏️

You can run the `call_api.py` file, where you specify the input data, using the command:
```bash
python call_api.py
```

Alternatively, you can call the API endpoint using curl with the following command:

```bash
curl -X 'POST' \ 'http://localhost:8000/analyze' \ -H 'accept: application/json' \ -H 'Content-Type: application/json' \ -d '{ "input_string": "This tutorial is very useful" }'
```
