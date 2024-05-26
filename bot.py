#@title Working BOT CODE WITH .m3u8
from pyrogram import Client, filters
import shutil
import glob
import os
import time

# Define your Pyrogram API ID, API HASH, and bot token here
API_ID = "6"
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = "1759107987:AAGAT2RB2NnSlccEPTOzgSHZUYRZA6UVmmM"

# Paths
# Get the current working directory
current_directory = os.getcwd()

# Define relative paths
RELATIVE_TEMPORARY_PATH = "accounts/DRMv1.7.AUM.Linux/cache"
RELATIVE_OUTPUT_PATH = "accounts/DRMv1.7.AUM.Linux/output"
RELATIVE_UTILS = "accounts/DRMv1.7.AUM.Linux/utils"

# Construct absolute paths
TEMPORARY_PATH = os.path.join(current_directory, RELATIVE_TEMPORARY_PATH)
OUTPUT_PATH = os.path.join(current_directory, RELATIVE_OUTPUT_PATH)
UTILS = os.path.join(current_directory, RELATIVE_UTILS)
TAG = "JoyBangla"

# Create a Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

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

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("Welcome to Telegram bot!")

@app.on_message(filters.command(["download", "Download", "DOWNLOAD"], case_sensitive=False))
async def download_command(client, message):
    await message.reply_text("Please enter the URL:")
    chat_state[message.chat.id] = {"step": "url"}

@app.on_message(filters.text & filters.private)
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

# Run the bot
app.run()
