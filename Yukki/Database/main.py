from telethon.sync import TelegramClient
from telethon.sessions import StringSession 
from pyrogram import Client 
import telethon.utils

HW_OP = "https://telegra.ph/file/e983d2b537b9c893c4207.jpg"

  print("Choose String Type \n1.Telethon\n2.Pyrogram")
  library = input("\nYour Choice:" )
  if library == "1":
    print("Welcome To Telethon String Generator")
    APP_ID = int(input("Enter APP ID - "))
    API_HASH = input("Enter API HASH - ")
    try:
      with TelegramClient(StringSession(), APP_ID, API_HASH) as bot:
        string_session = bot.session.save()
        print("You can Get Your String Session In Saved Message of Your Telegram Account. Remember To Make New String Session Whenever You Terminate Sessions.")
        bot.send_file("me", HW_OP, caption=f"`{string_session}`\n\n• __Dont Share String Session With Anyone__")
    except Exception as e:
      print(e)
  elif library == "2":
    APP_ID = int(input("\nEnter Ur APP ID ~: "))
    API_HASH = input("\nEnter Ur API_HASH ~: ")
    try:
      with Client(':memory:', api_id=APP_ID, api_hash=API_HASH) as boy:
        Hw = boy.export_session_string()
        print("Successfully String Session Has Been Generated \nCheck Ur Saved Message \nIf U Terminate Sessions Then U Have To Generate Gain\nDont Try To Share STRING SESSION with Anyone")
        boy.send_message("me", f"Pyrogram String Session\n\n`{Hw}`")
    except Exception as e:
      print(f"{e}")
  else:
    print("\nclick On Green Button And Start Again  \nChoose 1 For Userbot \nChoose 2 For Pyrogram \n Pahle Run karo fir se Tab 1 ya 2 Koi Ek Select Karna")