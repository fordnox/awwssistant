#!/usr/bin/env python
# pylint: disable=unused-argument

import logging
import os
import locale
from awwsistant import Awwsistant

from telegram import LabeledPrice, InlineKeyboardMarkup, InlineKeyboardButton, Update, helpers
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    PicklePersistence,
    InvalidCallbackData,
    PreCheckoutQueryHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8')


async def handle_all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("handle: %s", update)
    aww = Awwsistant()
    #aww.create_assistant()

    await update.message.reply_text(
        "Todo: implement this function",
    )


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).arbitrary_callback_data(True).build()

    # Simple commands handlers
    application.add_handler(MessageHandler(filters.ALL, handle_all_messages))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

