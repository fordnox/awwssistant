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
    def get_vin_info(vin: str):
        url = 'https://api.api-ninjas.com/v1/vinlookup?vin=' + vin
        return Functions.call_ninja_api(url)

    get_vin_info_JSON = {
        "name": "get_vin_info",
        "description": "Returns key vehicle information including manufacturer, country of origin and model "
                       "year for a given VIN.",
        "parameters": {
            "type": "object",
            "properties": {
                "vin": {
                    "type": "string",
                    "description": "valid VIN to check. Must be a 17-character string, e.g. JH4KA7561PC008269"},
            },
            "required": ["vin"]
        }
    }

    @staticmethod
    def get_whois_info(domain: str):
        url = 'https://api.api-ninjas.com/v1/whois?domain=' + domain
        return Functions.call_ninja_api(url)

    get_whois_info_JSON = {
        "name": "get_whois_info",
        "description": "Returns domain registration details (e.g. registrar, contact information, "
                       "expiration date, name servers) about a particular domain name.",
        "parameters": {
            "type": "object",
            "properties": {
                "domain": {
                    "type": "string",
                    "description": "domain name, e.g. google.com"},
            },
            "required": ["domain"]
        }
    }

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
