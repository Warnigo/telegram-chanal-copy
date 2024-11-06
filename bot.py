import os
import time
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.types import MessageService, DocumentAttributeVideo
from config import Config as BOT_SETTING

TEMP_DIR = "temp_media"

os.makedirs(TEMP_DIR, exist_ok=True)

def log_message(action, message_type, details=""):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {action}: {message_type} {details}")

with TelegramClient(BOT_SETTING.NAME, BOT_SETTING.API_ID, BOT_SETTING.API_HASH) as client:
    amount_sent = 0
    for message in client.iter_messages(BOT_SETTING.SRC_CHAT_ID, reverse=True):
        if isinstance(message, MessageService):
            continue
        try:
            if message.text and not message.media:
                log_message("Loading", "Text Message", f"Content: {message.text[:50]}")
                client.send_message(BOT_SETTING.DEST_CHAT_ID, message.text)
                log_message("Sent", "Text Message", f"Content: {message.text[:50]}")
            
            elif message.media:
                if message.document and message.document.mime_type == "application/pdf":
                    log_message("Loading", "PDF File")
                    file_path = client.download_media(message, file=os.path.join(TEMP_DIR, "media"))
                    if file_path:
                        client.send_file(BOT_SETTING.DEST_CHAT_ID, file_path, caption=message.message)
                        log_message("Sent", "PDF File", f"Path: {file_path}")
                        os.remove(file_path)
                
                elif message.document and any(isinstance(attr, DocumentAttributeVideo) and attr.round_message for attr in message.document.attributes):
                    log_message("Loading", "Round Video")
                    file_path = client.download_media(message, file=os.path.join(TEMP_DIR, "media"))
                    if file_path:
                        attributes = message.document.attributes
                        client.send_file(
                            BOT_SETTING.DEST_CHAT_ID,
                            file_path,
                            caption=message.message,
                            attributes=attributes,
                            video_note=True
                        )
                        log_message("Sent", "Round Video", f"Path: {file_path}")
                        os.remove(file_path)
                
                elif message.photo:
                    log_message("Loading", "Image")
                    file_path = client.download_media(message, file=os.path.join(TEMP_DIR, "media"))
                    if file_path:
                        client.send_file(BOT_SETTING.DEST_CHAT_ID, file_path, caption=message.message)
                        log_message("Sent", "Image", f"Path: {file_path}")
                        os.remove(file_path)
                
                elif message.text and message.video:
                    log_message("Loading", "Text with Video", f"Text: {message.text[:50]}")
                    client.send_message(BOT_SETTING.DEST_CHAT_ID, message.text)
                    log_message("Sent", "Text with Video (Only Text Sent)", f"Text: {message.text[:50]}")
            
            amount_sent += 1
            if amount_sent >= 48:
                log_message("Paused", "Waiting 2 seconds to avoid spam")
                amount_sent = 0
                time.sleep(2)
                
        except Exception as e:
            log_message("Error", f"{e}")
            time.sleep(5)
