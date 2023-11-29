import logging
import os
import string
import random
import requests


class Functions:

    @staticmethod
    def call_ninja_api(url):
        headers = {'X-Api-Key': os.environ.get('API_NINJA_KEY')}
        r = requests.get(url, headers=headers)
        return r.json()

    @staticmethod
    def get_iban_info(iban: str):
        url = 'https://api.api-ninjas.com/v1/iban?iban=' + iban
        return Functions.call_ninja_api(url)

    get_iban_info_JSON = {
        "name": "get_iban_info",
        "description": "Returns detailed information on a given IBAN.",
        "parameters": {
            "type": "object",
            "properties": {
                "iban": {
                    "type": "string",
                     "description": "The IBAN to look up"},
            },
            "required": ["iban"]
        }
    }

    @staticmethod
    def get_quote(category: str):
        url = 'https://api.api-ninjas.com/v1/quotes?category=' + category
        data = Functions.call_ninja_api(url)
        logging.debug('Quote: %s', data[0])
        return f'"{data[0]["quote"]}" - {data[0]["author"]}'

    get_quote_JSON = {
        "name": "get_quote",
        "description": "Get the quote in the given category.",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                     "description": "Category of the quote, available categories: age, alone, amazing, anger, "
                                    "architecture, art, attitude, beauty, best, birthday, business, car, change, "
                                    "communications, computers, cool, courage, dad, dating, death, design, "
                                    "dreams, education, environmental, equality, experience, failure, faith, "
                                    "family, famous, fear, fitness, food, forgiveness, freedom, friendship, "
                                    "funny, future, god, good, government, graduation, great, happiness, "
                                    "health, history, home, hope, humor, imagination, inspirational, "
                                    "intelligence, jealousy, knowledge, leadership, learning, legal, "
                                    "life, love, marriage, medical, men, mom, money, morning, movies, success."},
            },
            "required": ["category"]
        }
    }

    @staticmethod
    def get_random_digit():
        return random.randint(0, 9)

    get_random_digit_JSON = {
        "name": "get_random_digit",
        "description": "Get a random digit",
        "parameters": {
            "type": "object",
            "properties": {},
        }
    }

    @staticmethod
    def get_random_letters(count: int, case_sensitive: bool = False):
        return ''.join(random.choices(string.ascii_letters if case_sensitive else string.ascii_uppercase, k=count))

    get_random_letters_JSON = {
        "name": "get_random_letters",
        "description": "Get a string of random letters",
        "parameters": {
            "type": "object",
            "properties": {
                "count": {"type": "integer", "description": "Number of letters to return"},
                "case_sensitive": {"type": "boolean",
                                   "description": "Whether to include lower-case letters.  Default only returns upper-case letters."}
            },
            "required": ["count"]
        }
    }
