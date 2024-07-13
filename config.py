import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID",25837852 "")

API_HASH = os.environ.get("API_HASH",10b0caa8ae92bf5fb5e086d2fae9928c "")

BOT_TOKEN = os.environ.get("BOT_TOKEN",7441208412:AAGnFvrQPAydLNbmDEWLwxXpuz3tG1P0c8c "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","")     

DB_URL = os.environ.get("DB_URL","")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN',@Varunkumaran04 '').split()]

PORT = os.environ.get("PORT", "8080")
