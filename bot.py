from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes
import logging

TOKEN = "8085404886:AAF5JXCI16gXsxkfpeWwXWy3m-4KltlyV7Y"

logging.basicConfig(level=logging.INFO)

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for member in update.chat_member.new_chat_members:
        with open("welcome.jpg", "rb") as photo:
            await context.bot.send_photo(chat_id=update.chat_member.chat.id, photo=photo)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChatMemberHandler(welcome_new_member, ChatMemberHandler.CHAT_MEMBER))
    app.run_polling()