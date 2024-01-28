import logging  

from pyrogram import Client 

from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

OWNER_ID = '5932230962'
sudo_users = ["5932230962", "6591212980", "6090374191", "5513694222", "5316914263", "5538108947"]
GROUP_ID = "-1001875834087"
TOKEN = "6304832083:AAH2r5CjrSmIa2GKxVBDmjxuDjQy9dsykZo"
mongo_url = "mongodb+srv://vikas:vikas@vikas.yfezexk.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL = ["/https://telegra.ph/file/aa06eb4b312f456e1fd28.jpg", "https://telegra.ph/file/aa06eb4b312f456e1fd28.jpg"]
SUPPORT_CHAT = "shizka_x_sukuna"
UPDATE_CHAT = "shizka_x_sukuna"
BOT_USERNAME = "Dark_waifu_Bot"
CHARA_CHANNEL_ID = "-1001875834087"
api_id = "25635673"
api_hash = "ec69ce8b56c71541499c914fabd08286"


application = Application.builder().token(TOKEN).build()
Grabberu = Client("Grabber", api_id, api_hash, bot_token=TOKEN)
client = AsyncIOMotorClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters']
user_totals_collection = db['user_totals']
user_collection = db["user_collection"]
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']
