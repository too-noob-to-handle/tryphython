from flask import Flask, request, render_template_string
from pyrogram import Client, filters
import shutil
import glob
import os
import time
import threading

# Define your Pyrogram API ID, API HASH, and bot token here
API_ID = "6"
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = "1759107987:AAGAT2RB2NnSlccEPTOzgSHZUYRZA6UVmmM"

# Paths
TEMPORARY_PATH =  "/content/accounts/DRMv1.7.AUM.Linux/cache"
OUTPUT_PATH = "/content/accounts/DRMv1.7.AUM.Linux/output"
UTILS = "/content/accounts/DRMv1.7.AUM.Linux/utils"
TAG = "JoyBangla"

# Create a Pyrogram client with a session file
bot_app = Client("my_bot_session", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Flask app
flask_app = Flask(__name__)

# Dictionary to store state for each chat
chat_state = {}

def divider():
    print('-' * shutil.get_terminal_size().columns)

def download_drm_content(mpd_url, FILENAME, FILENAME2):
    divider()
    print("Downloading 1st Video from CDN..")
    os.system(f'{UTILS}/N_m3u8DL-RE -sv res="1080*" {mpd_url} --tmp-dir "{TEMPORARY_PATH}" --save-dir "{TEMPORARY_PATH}" --save-name "temp-BDH" -H "User-Agent: B Player" --del-after-done --log-level ERROR && mkvmerge --output "{OUTPUT_PATH}/{FILENAME}-{TAG}.mkv" --track-name "0:Join Us - @JoyBangla4U" --track-name "1:Join Us - @JoyBangla4U" \'(\' {TEMPORARY_PATH}/temp-BDH.mp4 \')\' --track-name "0:Join Us - @JoyBangla4U" \'(\' /content/ZGH596AF1426AF58623AGVH.srt \')\' --title "Join Us - @JoyBangla4U" --track-order 0:0,0:1,1:0 ')
    print("Downloading 2nd Video from CDN..")
    time.sleep(5)
    os.system(f'{UTILS}/N_m3u8DL-RE -sv res="720*" {mpd_url} --tmp-dir "{TEMPORARY_PATH}" --save-dir "{TEMPORARY_PATH}" --save-name "temp2-BDH" -H "User-Agent: B Player" --del-after-done --log-level ERROR && mkvmerge --output "{OUTPUT_PATH}/{FILENAME2}-{TAG}.mkv" --track-name "0:Join Us - @JoyBangla4U" --track-name "1:Join Us - @JoyBangla4U" \'(\' {TEMPORARY_PATH}/temp2-BDH.mp4 \')\' --track-name "0:Join Us - @JoyBangla4U" \'(\' /content/ZGH596AF1426AF58623AGVH.srt \')\' --title "Join Us - @JoyBangla4U" --track-order 0:0,0:1,1:0 ')

def drive_upload():
    print("Uploading.. (Takes some time)")
    time.sleep(5)
    os.system('rclone --config=/content/accounts/DRMv1.7.AUM.Linux/utils/rclone.conf copy --update --verbose --transfers 30 --checkers 8 --contimeout 60s --timeout 300s --retries 3 --low-level-retries 10 --stats 1s "/usr/src/app/accounts/DRMv1.7.AUM.Linux/output" "onedrive:/BUP"')
    print("Gdrive Upload Complete!")

@bot_app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("Welcome to Telegram bot!")

@bot_app.on_message(filters.command(["download", "Download", "DOWNLOAD"], case_sensitive=False))
async def download_command(client, message):
    await message.reply_text("Please enter the URL:")
    chat_state[message.chat.id] = {"step": "url"}

@bot_app.on_message(filters.text & filters.private)
async def handle_text(client, message):
    chat_id = message.chat.id
    if chat_id in chat_state:
        if chat_state[chat_id]["step"] == "url":
            mpd_url = message.text
            await message.reply_text("Enter the 1080p FileName:")
            chat_state[chat_id]["mpd_url"] = mpd_url
            chat_state[chat_id]["step"] = "filename1"
        elif chat_state[chat_id]["step"] == "filename1":
            FILENAME = message.text
            await message.reply_text("Enter the 720p FileName:")
            chat_state[chat_id]["FILENAME"] = FILENAME
            chat_state[chat_id]["step"] = "filename2"
        elif chat_state[chat_id]["step"] == "filename2":
            FILENAME2 = message.text
            mpd_url = chat_state[chat_id]["mpd_url"]
            FILENAME = chat_state[chat_id]["FILENAME"]
            await message.reply_text("Processing...")
            download_drm_content(mpd_url, FILENAME, FILENAME2)
            drive_upload()
            # Delete files
            for file_path in glob.glob(os.path.join(OUTPUT_PATH, "*")):
                os.remove(file_path)
            await message.reply_text("Process Finished. Final Video File is saved in /output directory.")
            del chat_state[chat_id]
    else:
        await message.reply_text("Invalid command sequence. Please use /download command first.")

# HTML content for the welcome page
WELCOME_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to My Telegram Bot</title>
</head>
<body>
    <h1>Welcome to My Telegram Bot!</h1>
    <p>This bot helps you entertain. Use the bot on Telegram to get started.</p>
</body>
</html>
"""

@flask_app.route('/')
def welcome():
    return render_template_string(WELCOME_PAGE)

def run_flask():
    flask_app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    # Run Flask app in a separate thread
    threading.Thread(target=run_flask).start()
    # Start Pyrogram Client
    bot_app.run()
