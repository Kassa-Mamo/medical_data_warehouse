import os
import logging
import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError




# Ensure logs directory exists
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Configure logging
log_file = os.path.join(log_dir, "scraper.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



# Set up logging (logs will be written to the logs folder)
logging.basicConfig(
    filename='../logs/scraper.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
logger = logging.getLogger(__name__)

# API credentials – replace with your own
api_id = 20173022
api_hash = "bab4a3351ed7634a8c1a3f8767fcf75c"
phone_number = "+251913423473"
session_name = "my_telegram_session"

# Channels to scrape
CHANNELS = [
    "https://t.me/DoctorsET",
    "Chemed Telegram Channel",  # If not URL, ensure your get_entity call can resolve it
    "https://t.me/lobelia4cosmetics",
    "https://t.me/yetenaweg",
    "https://t.me/EAHCI"
    # You can add more channels here or dynamically fetch from https://et.tgstat.com/medicine
]

async def scrape_channel(client, channel):
    try:
        logger.info(f"Scraping channel: {channel}")
        # Resolve channel entity
        entity = await client.get_entity(channel)
        # Fetch the latest 100 messages (adjust limit as needed)
        messages = await client.get_messages(entity, limit=100)
        # Process messages – here we simply log message IDs and texts.
        for msg in messages:
            logger.info(f"Message ID: {msg.id}, Text: {msg.text}")
            # TODO: Save to a temporary local database or file for further processing.
        logger.info(f"Completed scraping {channel}")
    except Exception as e:
        logger.error(f"Error scraping {channel}: {e}")

async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        logger.info("Not authorized – sending code request.")
        await client.send_code_request(phone_number)
        code = input("58868")
        try:
            await client.sign_in(phone_number, code)
        except SessionPasswordNeededError:
            password = input("Ka@10702025")
            await client.sign_in(password=password)
    
    # Loop through channels and scrape data
    for channel in CHANNELS:
        await scrape_channel(client, channel)
    
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
