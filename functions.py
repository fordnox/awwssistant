import string
import random


class Functions:

    @staticmethod
    def get_iban_info(iban: str):
        return {
              "iban": iban,
              "bank_name": "Deutsche Bank",
              "account_number": "0532013000",
              "bank_code": "20070000",
              "country": "DE",
              "checksum": "16",
              "valid": True,
              "bban": "200700000532013000"
            }

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
        return f'Quote in category {category}: The best way to cheer yourself up is to try to cheer somebody else up.'

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
