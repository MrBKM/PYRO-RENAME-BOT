import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25085908")

API_HASH = os.environ.get("API_HASH", "86b8a77b1ecb0507a3da3934e6a2c184")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5856415590:AAEXZ3DrVKO9MwZ-_YQHJc3kFS6q-EO__CI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001515447343") 

DB_NAME = os.environ.get("DB_NAME","Shyamal")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Shyamal:Shyamal@cluster0.orhkhyo.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ac801d22d7049e08a35f0.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5970680890').split()]

