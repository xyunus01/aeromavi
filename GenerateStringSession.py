import os

print("String session generator hoşgeldiniz")
	
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
APP_ID = 22106294
API_HASH = "ce3d3c805ace40c4822688c6170f0a78"
client = TelegramClient(StringSession(), APP_ID, API_HASH)
client.start()
session_str = client.session.save()
	
s_m = client.send_message("me", session_str)
s_m.reply(("⬆️ String sessionunuz "))
	
print("Lütfen telegram kayıtlı mesajlarınızı kontrol ediniz. ")

