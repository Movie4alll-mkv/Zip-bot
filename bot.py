import pyrogram
from zipfile import ZipFile

class ZipBot(pyrogram.Client):
    async def zip(self, message: pyrogram.Message):
        """Zips the source code from GitHub and sends it to the user."""

        # Get the GitHub repository URL from the user.
        github_repo_url = message.text.split()[1]

        # Download the source code from GitHub.
        source_code_file_path = await self.download_file(github_repo_url)

        # Create a zip file of the source code.
        zip_file_path = source_code_file_path + ".zip"
        with ZipFile(zip_file_path, "w") as zip_file:
            zip_file.write(source_code_file_path)

        # Send the zip file to the user.
        await self.send_document(message.chat.id, zip_file_path)

# Create a new bot.
bot = ZipBot("5053402593:AAGDN6XuOz4qKWgPIatEGfkJqoporK94h78")

# Start the bot.
bot.run()
