import os
import time
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.types import MessageService, DocumentAttributeVideo, DocumentAttributeFilename
from config import Config as BOT_SETTING

TEMP_DIR = "temp_media"
os.makedirs(TEMP_DIR, exist_ok=True)

def log(message):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def is_video(message):
    """Check if the media is a video based on attributes."""
    if message.document:
        for attr in message.document.attributes:
            if isinstance(attr, DocumentAttributeVideo):
                return True
    return False

def is_round_video(message):
    """Check if the video should be sent as a round video."""
    if message.document:
        for attr in message.document.attributes:
            if isinstance(attr, DocumentAttributeVideo) and attr.round_message:
                return True
    return False

with TelegramClient(BOT_SETTING.NAME, BOT_SETTING.API_ID, BOT_SETTING.API_HASH) as client:
    amount_sent = 0
    log("Starting message transfer...")

    for message in client.iter_messages(BOT_SETTING.SRC_CHAT_ID, reverse=True):
        if isinstance(message, MessageService):
            continue

        try:
            if message.text and not message.media:
                log(f"Sending text message: {message.text[:30]}...")
                client.send_message(BOT_SETTING.DEST_CHAT_ID, message.text)

            elif message.media:
                log("Downloading media...")
                file_path = client.download_media(message, file=os.path.join(TEMP_DIR, "media"))

                if file_path:
                    caption = message.text or ''
                    if is_video(message) and is_round_video(message):
                        log(f"Sending round video with caption: {caption}")
                        client.send_file(
                            BOT_SETTING.DEST_CHAT_ID,
                            file_path,
                            caption=caption,
                            attributes=[
                                DocumentAttributeVideo(duration=0, w=240, h=240, round_message=True, supports_streaming=True),
                                DocumentAttributeFilename(file_path.split('/')[-1])
                            ]
                        )
                    elif is_video(message):
                        log(f"Sending video as document with caption: {caption}")
                        client.send_file(
                            BOT_SETTING.DEST_CHAT_ID,
                            file_path,
                            caption=caption,
                            force_document=True
                        )
                    else:
                        log(f"Sending media with caption: {caption}")
                        client.send_file(BOT_SETTING.DEST_CHAT_ID, file_path, caption=caption)

                    os.remove(file_path)
                    log(f"Deleted local file: {file_path}")

            amount_sent += 1
            log(f"Messages sent: {amount_sent}")

            if amount_sent >= 48:
                log("Pausing to prevent rate-limits...")
                amount_sent = 0
                time.sleep(5)

        except Exception as e:
            log(f"Error encountered: {e}")
            time.sleep(10)

    log("Message transfer complete.")
