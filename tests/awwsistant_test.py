import os
import logging
import json
from pathlib import Path
from awwsistant import Awwsistant, Functions, VisionAssistant

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def test_functions():
    functions = Functions()

    result = functions.get_vin_info('JH4KA7561PC008269')
    logger.info('Result: %s', result)

    result = functions.get_whois_info('openai.com')
    logger.info('Result: %s', result)

    iban_info = functions.get_iban_info('DE89370400440532013000')
    logger.info('IBAN info: %s', iban_info)

    iban_info = functions.get_iban_info('GB29NWBK60161331926819')
    logger.info('IBAN info: %s', iban_info)

    iban_info = functions.get_quote('love')
    logger.info('quote: %s', iban_info)

    iban_info = functions.get_quote('art')
    logger.info('quote: %s', iban_info)


def test_assistant():
    aww = Awwsistant()
    aww.id = os.getenv('OPENAI_API_ASSISTANT_ID')
    # assistant = aww.create_assistant()
    # logger.info('Assistant id %s', assistant.id)
    assistant = aww.refresh_assistant()
    aww.chat(
        'What is the IBAN number? and give me a details for these ibans: DE89370400440532013000 and for GB29NWBK60161331926819')
    # aww.chat('give me a details for this iban: GB29NWBK60161331926819')
    # aww.chat('write me a random quote about money.')


def test_vision():
    v = VisionAssistant()
    r = v.describe_image(Path('../images/1985_European_GP_Stefan_Johansson_01.jpg'))
    logger.info('Result: %s', r)


def test_read_article():
    v = VisionAssistant()
    r = v.get_article_from_image(Path('../images/magazine_page_2.jpg'))
    logger.info('Result: %s', json.dumps(r, indent=4))

