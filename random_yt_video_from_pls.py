import logging
import requests
import random
import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext

# Replace with your own TELEGRAM API token, Google API key and YouTube playlist ID
api_token = 'TELEGRAM BOT TOKEN'
key = 'GOOGLE API KEY'
playlist_id = 'YOUTUBE PLAYLIST ID'
url = f'https://www.youtube.com/playlist?list={playlist_id}'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, I can give out random videos on the /video command")

async def echo(update: Update, context: CallbackContext) -> None:
    #extract playlist id from url
    query = parse_qs(urlparse(url).query, keep_blank_values=True)
    playlist_id = query["list"][0]
    print()
    print(f'get all playlist items links from {playlist_id}')
    print()
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = key)

    request = youtube.playlistItems().list(
        part = "snippet",
        playlistId = playlist_id,
        maxResults = 500
    )
    response = request.execute()

    playlist_items = []
    while request is not None:
        response = request.execute()
        playlist_items += response["items"]
        request = youtube.playlistItems().list_next(request, response)
    
    print()
    print(f"total: {len(playlist_items)}")
    print()
    
    allList = ([
        f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s'
        for t in playlist_items
    ])
    x = random.choice(allList)

    print()
    print('RANDOM = ', x)
    print()
    
    await update.message.reply_text(str(x))

# Main function to handle incoming updates
def main() -> None:
    """Start the bot."""
    application = ApplicationBuilder().token(api_token).build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    video_handler = CommandHandler('video', echo)
    application.add_handler(video_handler)
    application.run_polling()
if __name__ == '__main__':
    main()