import pyrogram
import zipfile
from pyrogram.types import User, Message
from pyrogram import filters
from pyrogram.filters import Message

class ZipRarBot(pyrogram.Client):
    def __init__(self, api_id, api_hash, bot_token, owner_id):
        super().__init__(api_id, api_hash, bot_token)
        self.owner_id = owner_id

    async def zip(self, message: pyrogram.types.Message):
        """Zips the file sent by the user and sends it back to them."""

        # Get the file path from the user.
        file_path = message.document.file_path

        # Create a zip file of the file.
        zip_file_path = file_path + ".zip"
        with zipfile.ZipFile(zip_file_path, "w") as zip_file:
            zip_file.write(file_path)

        # Send the zip file to the user.
        await self.send_document(message.chat.id, zip_file_path)

    async def zip_with_password(self, message: pyrogram.types.Message):
        """Zips the file sent by the user and sends it back to them with a password."""

        # Get the file path from the user.
        file_path = message.document.file_path

        # Get the password from the user.
        password = message.text.split()[1]

        # Create a zip file of the file with a password.
        zip_file_path = file_path + ".zip"
        with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.write(file_path, password)

        # Send the zip file to the user.
        await self.send_document(message.chat.id, zip_file_path)

# Create a new bot.
bot = ZipRarBot("4bcc61d959a9f403b2f20149cbbe627a", "6534707", "5053402593:AAGDN6XuOz4qKWgPIatEGfkJqoporK94h78", 1430593323)

# Add handlers for the /zip and /zip_with_password commands.
bot.add_handler(filters.command("zip") & filters.document, zip)
# Start the bot.
bot.run()
