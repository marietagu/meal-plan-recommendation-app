import os
import requests
import json
import streamlit as st

backend_url = os.getenv('BACKEND_URL', 'https://web-production-2e40.up.railway.app')

class Generator:
    def __init__(self, nutrition_input: list, ingredients: list = [], params: dict = {'n_neighbors': 5, 'return_distance': False}):
        self.nutrition_input = nutrition_input
        self.ingredients = ingredients
        self.params = params

    def set_request(self, nutrition_input: list, ingredients: list, params: dict):
        self.nutrition_input = nutrition_input
        self.ingredients = ingredients
        self.params = params

    def generate(self):
        request = {
            'nutrition_input': self.nutrition_input,
            'ingredients': self.ingredients,
            'params': self.params
        }
        try:
            response = requests.post(url=f'{backend_url}/predict/', json=request)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()  # Return the JSON data
        except requests.RequestException as e:
            st.error(f"Error connecting to backend: {e}")
            return None
        except json.JSONDecodeError:
            st.error("Failed to decode JSON from backend response")
            return None
