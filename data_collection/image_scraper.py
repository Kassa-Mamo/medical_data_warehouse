import os
import logging
import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

logging.basicConfig(
    filename='../logs/scraper.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
logger = logging.getLogger(__name__)

# API credentials – same as before (or update if needed)
api_id = 20173022
api_hash = "bab4a3351ed7634a8c1a3f8767fcf75c"
phone_number = "+251913423473"
session_name = "image_scraper_session"

# Telegram channels for image scraping
IMAGE_CHANNELS = [
    "Chemed Telegram Channel",
    "https://t.me/lobelia4cosmetics"
]

# Set up a directory for downloaded images
BASE_DIR = os.path.dirname(__file__)
DOWNLOAD_DIR = os.path.join(BASE_DIR, '../images')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

async def download_images(client, channel):
    try:
        logger.info(f"Downloading images from channel: {channel}")
        entity = await client.get_entity(channel)
        async for message in client.iter_messages(entity, limit=100):
            if message.photo:
                filename = f"{channel.replace('https://t.me/', '')}_{message.id}.jpg"
                file_path = os.path.join(DOWNLOAD_DIR, filename)
                await client.download_media(message, file_path)
                logger.info(f"Downloaded image to {file_path}")
    except Exception as e:
        logger.error(f"Error downloading images from {channel}: {e}")

async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        logger.info("Not authorized – sending code request.")
        await client.send_code_request(phone_number)
        code = input("33574")
        try:
            await client.sign_in(phone_number, code)
        except SessionPasswordNeededError:
            password = input("Ka@10702025")
            await client.sign_in(password=password)
    
    for channel in IMAGE_CHANNELS:
        await download_images(client, channel)
    
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
