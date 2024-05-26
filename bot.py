from flask import Flask, request, render_template_string
from pyrogram import Client, filters
import os
import requests
import shutil
import glob
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

# Create a Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Flask app
flask_app = Flask(__name__)

# Dictionary to store state for each chat
chat_state = {}

# Your API endpoint URL
API_URL = "https://api.bongo-solutions.com/ironman/api/v1/content/detail/"

# Define headers for the API request
headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI2OTRjYTNiZS1mZjBiLTRlYTctOWI1YS0xMWMwMGZjNTg4ZjciLCJpc3MiOiJIRUlNREFMTCIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJ1c2VybmFtZSI6Ijg4MDE3MTEzMzg0NjQiLCJ2ZXJpZmllZF9waG9uZV9udW1iZXIiOiI4ODAxNzExMzM4NDY0IiwiY2xpZW50X2xvZ2luX2lkIjoiYjQ2ZjA3YjktMGRlNy00MDI2LTg0N2YtYTQ2ZTdlMjI2OWUzIiwidXNlcl90eXBlIjoicmVndWxhciIsInBsYXRmb3JtX2lkIjoiYWJmZWE0NjItZjY0ZC00OTFlLTljZDktNzVlZTAwMWY0NWIwIiwiY2xpZW50X2lkIjpudWxsLCJib25nb19pZCI6IjY5NGNhM2JlLWZmMGItNGVhNy05YjVhLTExYzAwZmM1ODhmNyIsImlhdCI6MTcwNzcyNjg4MiwiZXhwIjoxNzE1NTAyODkyLjAsImNvdW50cnlDb2RlIjoiQkQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJUYWhtaWQgSGFzc2FuIiwiZmFjZWJvb2tfaWQiOiIxMzg1NTU4ODU1MzUwNjA4In0.p8Z-an8ONP30JFZNl-9RuymfsDOLIcMuf5tnIqnADjc9-vpCzfZewYyfSrHKNBBpNFIwmugcvmlxdsS4pVFCI-XnlAG7StzCbA5n67wW9j0Fs9fQ-EXOj5x5MtRM33ZwNQcBy6b3xNHmBK1Eem77hZUJ7NhP0PlnLlRcoBZDeeLrEmRsRJL5cIWLq4RVUvtnj6zFpTVBLuzRAmqUp1zIik5wmnR7-DBUGvUZJB1MxJ75zndPQe9_a_F5lG6eoLNKhgSCeagPw8KZmIMkPM8yFqbOGH8YTr_2DeHpVknWb6YEyi95q1KIjKk-Wt1LruLvhocRrlnpREtHEbTlO6o9FV-0pp6wcS8lXYtlsrTK89Hk9nZeKwfGpgJXImfB6twih2ubac_qxI-BXPPwElpQPIL9HLjnIoLZ52dF0JOpQes-ufMTJ-jyEQRZkEi_3FmJhUZgW6oTl2hyCR6DL8I8uTmm0g1_t5otw0HKblLGPjimZIdEV_sMT2A_1-eX4gi6QpR5GY8XbzPdmnpSB9P5iqK6mnLjDLrPKrEOTMuGjATeIvYuNoh_ZEWUrcD_9FjFFngbgO7BI1E1cYGJm7eCsfF2Dvi2ItSGM78ExcafXtZrp71ZKPy2OsJD799qA96tuVwSSwpCpU0gflifrDYtuVY9pf4w71fQEGXz-L9NwMg',
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
    os.system('rclone --config=/content/accounts/DRMv1.6.AUM.Linux/utils/rclone.conf copy --update --verbose --transfers 30 --checkers 8 --contimeout 60s --timeout 300s --retries 3 --low-level-retries 10 --stats 1s "/usr/src/app/accounts/DRMv1.6.AUM.Linux/output" "BDHWEB:Uploads"')
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







