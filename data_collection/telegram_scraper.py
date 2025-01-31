import logging
import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Your API credentials
api_id = 20173022  # Replace with your API ID
api_hash = "bab4a3351ed7634a8c1a3f8767fcf75c"  # Replace with your API hash
phone_number = "+251913423473"  # Replace with your phone number

# Use a session file to avoid repeated logins
session_name = "my_telegram_session"  # This will save login info

async def main():
    client = TelegramClient(session_name, api_id, api_hash)

    # Connect to Telegram
    logger.info("Connecting to Telegram...")
    await client.connect()

    if not await client.is_user_authorized():
        logger.info("Logging in...")
        await client.send_code_request(phone_number)

        # Ask user to enter the received code
        code = input("Enter the Telegram code you received:33574 ")  
        await client.sign_in(phone_number, code)

        # Handle two-step verification
        try:
            await client.get_me()
        except SessionPasswordNeededError:
            password = input("Enter your 2FA password:Ka@10702025 ")  # Securely enter password
            await client.sign_in(password=password)

    logger.info("Successfully logged in!")
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
