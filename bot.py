
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChatMemberHandler
import os

TOKEN = "8085404886:AAF5JXCI16gXsxkfpeWwXWy3m-4KltlyV7Y"
WELCOME_IMAGE_PATH = "welcome.jpg"

logging.basicConfig(level=logging.INFO)

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.chat_member.new_chat_member.status == 'member':
        chat_id = update.chat_member.chat.id
        if os.path.exists(WELCOME_IMAGE_PATH):
            await context.bot.send_photo(
                chat_id=chat_id,
                photo=open(WELCOME_IMAGE_PATH, 'rb')
            )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChatMemberHandler(welcome_new_member, ChatMemberHandler.CHAT_MEMBER))
    print("Bot is running...")
    app.run_polling()
