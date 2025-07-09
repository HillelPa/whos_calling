from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


# === RENSEIGNE ICI TES INFOS ===
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
from_number = os.getenv("FROM_NUMBER")
to_number = os.getenv("TO_NUMBER")

client = Client(account_sid, auth_token)

url = os.getenv("BELLA")

call = client.calls.create(
    to=to_number,
    from_=from_number,
    url=url
)

print("✅ Appel lancé ! SID :", call.sid)