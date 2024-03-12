#@title Working BOT CODE WITH API
from pyrogram import Client, filters
import os
import requests
import shutil
import glob
import time

# Define your Pyrogram API ID, API HASH, and bot token here
API_ID = "6"
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
BOT_TOKEN = "1759107987:AAFjRXR5h6w-c090Jj61IInoXpJIuTfFeOg"

# Paths
TEMPORARY_PATH =  "/accounts/DRMv1.7.AUM.Linux/cache"
OUTPUT_PATH = "/accounts/DRMv1.7.AUM.Linux/output"
UTILS = "/accounts/DRMv1.7.AUM.Linux/utils"
TAG = "JoyBangla"

# Create a Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Dictionary to store state for each chat
chat_state = {}

# Your API endpoint URL
API_URL = "https://api.bongo-solutions.com/ironman/api/v1/content/detail/"

# Define headers for the API request
headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIzMzlmNTRjYi1kYmY1LTRkMjgtYWY2OC1mZDYwYTkzZDMxNDkiLCJpc3MiOiJIRUlNREFMTCIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJ1c2VybmFtZSI6Ijg4MDE5OTc3OTEyODYiLCJ2ZXJpZmllZF9waG9uZV9udW1iZXIiOiI4ODAxOTk3NzkxMjg2IiwiY2xpZW50X2xvZ2luX2lkIjoiMGUzYmJjZjUtZTQ5MS00N2Y0LTg3NjEtYzQzYTNiNzY4ZTc1IiwidXNlcl90eXBlIjoicmVndWxhciIsInBsYXRmb3JtX2lkIjoiYWJmZWE0NjItZjY0ZC00OTFlLTljZDktNzVlZTAwMWY0NWIwIiwiY2xpZW50X2lkIjoiMDFjZGQwNzQtZDgwZS00MGI5LWI1MTYtODNmNmFhYWE5YmZmIiwiYm9uZ29faWQiOiIzMzlmNTRjYi1kYmY1LTRkMjgtYWY2OC1mZDYwYTkzZDMxNDkiLCJpYXQiOjE3MDc5OTYyOTUsImV4cCI6MTcxNTc3MjMwNS4wLCJjb3VudHJ5Q29kZSI6IkJEIiwicHJlZmVycmVkX3VzZXJuYW1lIjpudWxsfQ.UB0VFQHKFs8DNw9Ph5MhhVME0uIy6gz-I1vxWcVAcZpwb1QSSC9tA0AdDa3qHwDGjN8jXKIalIciU89MUxYfuRRiuYHQ2fc7tBFNB3ksE4DetAVYBQtbhGtQpCk2HZTdmw9T59TZpzJLRCTYXTPXJMbr7Lv5kKuqLzWS5r4ffOPwL8a2RIJ7t_GFSQT20Y77h8mDmlF0iI7lXgEwtIuEkb_NKm-6G-aUW5eBPHKzPQIRHwcuwwinFXDbxCNvzWurgwO3OGSDThNShmaBQJq32xj871WqhuS-O9kj_8aZI3eMUN5I1bkYiZZZ09OAg76YxLM1FZAxIifEdFIjdL2zq9MC-f04J5uHxvoT8V6StwQT6YJtUsrcZ068yGMDh2BmfVRyN02aM6ptArcQ2dTb3fft1gmVb4sOAQb8GXJyAADQNQ2ySNQRBDI9ZPgDmJm9Wz_4gxn7Zufb15JnYiCONrkLlCdbZFjNxmE5dx4y3Xo34V9rTNesAzsjQ8V_tiCict9ZLP91gh18NIB1gLxZAqVhEExO4tFcpu8uCJAJF-3ldiTXJdlDA6UJGBhf5fjeFbW3z6YjIX8xzFu_08UGmrJQWKIn3-PFr8C16-NAHKLwBVhhB_chjKHvlVMWozjbLal7KTFi-eIeJMhtnBfq3umaPQz0yk-4SB6zgQ0OgjA',
    'access-code': 'QkQ%3D',
    'platform-id': 'abfea462-f64d-491e-9cd9-75ee001f45b0',
    'country-code': 'QkQ%3D',
    'accept-language': 'en',
    'content-type': 'application/json; charset=UTF-8',
    'user-agent': 'okhttp/5.0.0-alpha.3',
}

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
    os.system('rclone --config=/accounts/DRMv1.7.AUM.Linux/utils/rclone.conf copy --update --verbose --transfers 30 --checkers 8 --contimeout 60s --timeout 300s --retries 3 --low-level-retries 10 --stats 1s "/usr/src/app/accounts/DRMv1.6.AUM.Linux/output" "onedrive:/BUP"')
    print("Gdrive Upload Complete!")

def fetch_hls_url(content_id):
    url = f"{API_URL}{content_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        hls_url = json_data.get("vod", {}).get("activeEncode", {}).get("urls", {}).get("hls", {}).get("url")
        if hls_url:
            # Replace the URL part
            hls_url = hls_url.replace("https://vod.bongobd.com", "https://global.bongobd.com")
        return hls_url
    return None

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
            url = message.text
            content_id = url.split("/watch/")[-1]
            hls_url = fetch_hls_url(content_id)
            if hls_url:
                chat_state[chat_id]["hls_url"] = hls_url
                await message.reply_text("HLS URL fetched successfully. Enter the 1080p FileName:")
                chat_state[chat_id]["step"] = "filename1"
            else:
                await message.reply_text("Failed to fetch HLS URL from the API. Please try again.")
                del chat_state[chat_id]
        elif chat_state[chat_id]["step"] == "filename1":
            FILENAME = message.text
            await message.reply_text("Enter the 720p FileName:")
            chat_state[chat_id]["FILENAME"] = FILENAME
            chat_state[chat_id]["step"] = "filename2"
        elif chat_state[chat_id]["step"] == "filename2":
            FILENAME2 = message.text
            hls_url = chat_state[chat_id]["hls_url"]
            FILENAME = chat_state[chat_id]["FILENAME"]
            await message.reply_text("Processing...")
            download_drm_content(hls_url, FILENAME, FILENAME2)
            drive_upload()
            # Delete temporary files after uploading
            for file_path in glob.glob(os.path.join(TEMPORARY_PATH, "*")):
                os.remove(file_path)
            await message.reply_text("Process Finished. Final Video File is saved in /output directory.")
            del chat_state[chat_id]
    else:
        await message.reply_text("Invalid command sequence. Please use /download command first.")

# Run the bot
app.run()
