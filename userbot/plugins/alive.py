# stickery alive by @hellboi_atul
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
ALIVE_IMG = "https://tenor.com/9OER.gif"
ALIVE_caption = "`ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot IS:` **🔥on Fire🔥**\n\n"
ALIVE_caption += "**SYSTEM STATUS**\n\n"
ALIVE_caption += "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n\n"
ALIVE_caption += "`DATABASE STATUS:` **Functional**\n\n"
ALIVE_caption += "**Current Branch** : `master`\n\n"
ALIVE_caption += "**ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot  OS** : `1.0`\n\n"
ALIVE_caption += "**Current Sat** : `ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot 1.0`\n\n"
ALIVE_caption += f"**My Boss** : {DEFAULTUSER} \n\n"
ALIVE_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
ALIVE_caption += "**Bot Made By @Sensei_nex** \n\n"
ALIVE_caption += "Copyright By [Sensei](https://t.me/sensei_nex)\n\n"
ALIVE_caption += "[Deploy ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot](https://github.com/SenseiMAX/SenseiMAX-Kingbot)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def sensible(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete()
    await borg.send_file(alive.chat_id, ALIVE_IMG,caption=ALIVE_caption)

@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def sensible(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
