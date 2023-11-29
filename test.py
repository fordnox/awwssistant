from awwsistant import Awwsistant
import logging
from functions import Functions


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def test_functions():
    functions = Functions()

    functions.get_random_digit()
    functions.get_random_letters(5)

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
    aww.id = 'asst_kvdDfyGGGUwrNQvFPx6UhgmW'
    # assistant = aww.create_assistant()
    # logger.info('Assistant id %s', assistant.id)
    assistant = aww.refresh_assistant()
    aww.chat('give me a details for this iban: DE89370400440532013000')
    # aww.chat('give me a details for this iban: GB29NWBK60161331926819')
    # aww.chat('write me a random quote about money.')

