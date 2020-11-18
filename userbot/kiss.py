#Made By @hackerprem. Keep Credits. Cause It hurts. Join @pyfilesofsensiemaxuserbot for more.



from telethon import events
import asyncio
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
import random
import re
from userbot import CMD_HELP
from collections import deque



@borg.on(admin_cmd(pattern=r"kiss$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.3
    animation_ttl = range(0, 54)
    animation_chars = [
            "😚",
            "😍",
            "😘",
            "😚",
            "😍",
            "😘",
            "😚",
            "😍",
            "😘",
            "😚",
            "😍",
            "😘",
            "😚",
            "😍",
            "😘",
            "😚",
            "😍",
            "😘",
            "😚",
            "😍",
            "😘",
            "LOVE YOU JANNU U GIVE ME A LONG KISS😘❤💖💘"
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 32])  
            
            
