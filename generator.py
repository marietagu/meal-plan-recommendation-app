import requests
import json

class Generator:
    def __init__(self, nutrition_input: list, ingredients_include: list = [], ingredients_exclude: list = [], params: dict = {'n_neighbors': 5, 'return_distance': False}):
        self.nutrition_input = nutrition_input
        self.ingredients_include = ingredients_include
        self.ingredients_exclude = ingredients_exclude
        self.params = params

    def set_request(self, nutrition_input: list, ingredients_include: list, ingredients_exclude: list, params: dict):
        self.nutrition_input = nutrition_input
        self.ingredients_include = ingredients_include
        self.ingredients_exclude = ingredients_exclude
        self.params = params

    def generate(self):
        request = {
            'nutrition_input': self.nutrition_input,
            'ingredients_include': self.ingredients_include,
            'ingredients_exclude': self.ingredients_exclude,
            'params': self.params
        }
        response = requests.post(url='http://127.0.0.1:8000/predict/', data=json.dumps(request))
        return response
