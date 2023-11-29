#!/usr/bin/env python
# pylint: disable=unused-argument

import logging
import os
import locale
from awwsistant import Awwsistant

from telegram import BotCommand, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

aww = Awwsistant()
aww.id = os.getenv('OPENAI_API_ASSISTANT_ID')
aww.refresh_assistant()


async def post_init(application: Application):
    await application.bot.set_my_commands([
        BotCommand("/start", "Start new dialog"),
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_text = "Hello there! I'm a bot that can test custom OpenAI Functions. Try me out!"
    await update.message.reply_text(reply_text)


async def handle_all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.debug("handle: %s", update)
    waiting_message = await update.message.reply_text("Please wait while I think...")
    response = aww.chat(update.message.text)
    await waiting_message.delete()
    await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = (
        Application.builder()
        .token(os.getenv('TELEGRAM_TOKEN'))
        .arbitrary_callback_data(True)
        .post_init(post_init)
        .build()
    )

    # Simple commands handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL, handle_all_messages))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
