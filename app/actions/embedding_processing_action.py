# app/actions/embedding_processing_action.py

import json
import time
import os
import httpx
from openai import OpenAIError, RateLimitError, APIConnectionError, BadRequestError
from dotenv import load_dotenv

class EmbeddingProcessingAction:
    def __init__(self):
        """Initialize the OpenAI API client."""
        load_dotenv(override=True)
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("API key is missing. Check your .env configuration.")

        self.base_url = "https://api.openai.com/v1/embeddings"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_embedding_for_chunk(self, chunk, max_retries=3, delay=5):
        """Obtain the embedding for a text chunk with retries and improved error handling."""
        retries = 0

        while retries < max_retries:
            try:
                response = httpx.post(
                    self.base_url,
                    headers=self.headers,
                    json={"input": chunk, "model": "text-embedding-ada-002"},
                    timeout=30.0  # Ensure the request times out properly
                )
                response.raise_for_status()  # Raise HTTPError for bad responses
                return response.json()["data"][0]["embedding"]

            except httpx.ConnectError as e:
                print(f"Connection error: {e}. Retrying...")
            except httpx.ReadTimeout as e:
                print(f"Request timed out: {e}. Retrying...")
            except RateLimitError:
                print("Rate limit exceeded. Retrying after delay...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            except BadRequestError as e:
                print(f"Bad request: {e}. Please check your input data.")
                break
            except OpenAIError as e:
                print(f"OpenAI API error: {e}. Retrying...")
            except httpx.HTTPStatusError as e:
                print(f"HTTP error: {e.response.status_code} - {e.response.text}")
                break

            retries += 1
            time.sleep(delay)

        return None

