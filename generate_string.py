import asyncio
from pyrogram import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def generate_string_session():
    print("=== Pyrogram String Session Generator ===")
    
    # Get API credentials
    api_id = input("Enter your API ID: ")
    api_hash = input("Enter your API Hash: ")
    
    # Create a temporary client
    async with Client(
        name="user",
        api_id=api_id,
        api_hash=api_hash,
        in_memory=True
    ) as app:
        print("\nSuccessfully generated string session!\n")
        print("Your string session:")
        print("\n" + await app.export_session_string() + "\n")
        print("Please store this string session safely and DO NOT share it with anyone!")
        print("This string session can be used to access your Telegram account!")

if __name__ == "__main__":
    # Run the async function
    asyncio.run(generate_string_session()) 