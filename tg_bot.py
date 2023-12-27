import sys
from telegram import Bot

# Замените на ваш токен Telegram бота и ваш chat_id
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def send_telegram_message(message):
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        message_to_send = sys.argv[1]
        send_telegram_message(message_to_send)
