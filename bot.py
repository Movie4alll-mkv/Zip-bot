import pyrogram
import zipfile
import rarfile
from pyrogram.types import User, Message
from pyrogram import filters
from pyrogram.filters import Message
from pyrogram import Client
# Replace the following values with your own API ID and API hash
api_id = 6534707
api_hash = "4bcc61d959a9f403b2f20149cbbe627a"
app = Client("my_account", api_id=api_id, api_hash=api_hash)
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

class ZipRarBot(pyrogram.Client):
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

    async def rar(self, message: pyrogram.types.Message):
        """Rars the file sent by the user and sends it back to them."""

        # Get the file path from the user.
        file_path = message.document.file_path

        # Create a rar file of the file.
        rar_file_path = file_path + ".rar"
        with rarfile.RarFile(rar_file_path, "w") as rar_file:
            rar_file.write(file_path)

        # Send the rar file to the user.
        await self.send_document(message.chat.id, rar_file_path)

    async def rar_with_password(self, message: pyrogram.types.Message):
        """Rars the file sent by the user and sends it back to them with a password."""

        # Get the file path from the user.
        file_path = message.document.file_path

        # Get the password from the user.
        password = message.text.split()[1]

        # Create a rar file of the file with a password.
        rar_file_path = file_path + ".rar"
        with rarfile.RarFile(rar_file_path, "w", mode="w") as rar_file:
            rar_file.write(file_path, password)

        # Send the rar file to the user.
        await self.send_document(message.chat.id, rar_file_path)

# Create a new bot.
bot = ZipRarBot("5053402593:AAGDN6XuOz4qKWgPIatEGfkJqoporK94h78")

# Add handlers for the /zip, /rar, /zip_with_password, and /rar_with_password commands.
bot.add_handler(filters.command("zip") & filters.document, zip)
bot.add_handler(filters.command("zip_with_password") & filters.document, zip_with_password)

# Start the bot.
bot.run()
