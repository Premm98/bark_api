from fastapi import FastAPI
import requests

app = FastAPI()

BARK_API_URL = "https://barkapi.com"

@app.post("/prompt")
def process_prompt(prompt: str):
    payload = {"prompt": prompt}
    response = requests.post(BARK_API_URL, json=payload)
    result = response.json()
    return result
