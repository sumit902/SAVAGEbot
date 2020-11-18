from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.utils import load_module
from userbot import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio
import telethon.utils


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("❣➖➖➖ Initiating Inline Bot ➖➖➖❣")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("❮❮❮ ❍Initialisation finished with no errors , Your ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot will be ready in sometime❍ ❯❯❯")
        print("Starting ♛ ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot ♛→→")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot's Startup Completed ➠➠
                        ░░░░░░░░░░░█▀▀░░█░░░░░░
                        ░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░
                        ░░░░░░█░█░░░░░░░░░░▐░░░
                        ░░░░░░▐▐░░░░░░░░░▄░▐░░░
                        ░░░░░░█░░░░░░░░▄▀▀░▐░░░
                        ░░░░▄▀░░░░░░░░▐░▄▄▀░░░░
                        ░░▄▀░░░▐░░░░░█▄▀░▐░░░░░
                        ░░█░░░▐░░░░░░░░▄░█░░░░░
                        ░░░█▄░░▀▄░░░░▄▀▐░█░░░░░
                        ░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░
                        ░░▐█▐▄░░▀░░░░░░▐░█▄▄░░░
                        ░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░
                        ░░░░░░░░░░░░░░░░░░░░░░░")
    else:
        bot.start()
    

import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print("➠ The most Powerful ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot is on fire 🔥. Check .alive to test that bot is functioning or not . Join https://t.me/SenseiMAXprojects for any assistance 👀  ")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()


