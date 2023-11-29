from awwsistant import Awwsistant
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def test_assistant():
    aww = Awwsistant()
    aww.id = 'asst_kvdDfyGGGUwrNQvFPx6UhgmW'
    # assistant = aww.create_assistant()
    # logger.info('Assistant id %s', assistant.id)
    assistant = aww.refresh_assistant()
    aww.chat('give me a details for this iban: DE89370400440532013000')
    # aww.chat('give me a details for this iban: GB29NWBK60161331926819')
    # aww.chat('write me a random quote about money.')

