import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25943549")

API_HASH = os.environ.get("API_HASH", "bd7960c74ffdff6f8e84328aa7f2d7da")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8174304470:AAF49E9HNuPk7nMZnxU0EwPkDDNQSXvQEmc") 

FORCE_SUB = os.environ.get("FORCE_SUB", "https://t.me/+10ym8n0JSBg5MTM9") 

DB_NAME = os.environ.get("DB_NAME","vk63692543")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://vk63692543:varun@varunkumaran.sbzhefr.mongodb.net/?retryWrites=true&w=majority&appName=Varunkumaran")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/PXk.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6300548815').split()]

PORT = os.environ.get("PORT", "8080")
