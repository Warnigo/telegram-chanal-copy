import os
import time
from telethon.sync import TelegramClient
from telethon.tl.types import MessageService
from config import Config as BOT_SETTING

TEMP_DIR = "temp_media"

os.makedirs(TEMP_DIR, exist_ok=True)

with TelegramClient(BOT_SETTING.NAME, BOT_SETTING.API_ID, BOT_SETTING.API_HASH) as client:
    amount_sent = 0
    for message in client.iter_messages(BOT_SETTING.SRC_CHAT_ID, reverse=True):
        if isinstance(message, MessageService):
            continue
        try:
            if message.text:  # Matnli xabarlar
                client.send_message(BOT_SETTING.DEST_CHAT_ID, message.text)
            elif message.media:
                file_path = client.download_media(message, file=os.path.join(TEMP_DIR, "media"))
                if file_path:
                    client.send_file(BOT_SETTING.DEST_CHAT_ID, file_path, caption=message.message)
                    os.remove(file_path)
            amount_sent += 1
            if amount_sent >= 48:
                amount_sent = 0
                time.sleep(2)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)
