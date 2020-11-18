#credits to @kraken_the_badass
#kanged by @sensei_nex for @senseiMAXprojects

#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://media.giphy.com/media/Lopx9eUi34rbq/giphy.gif"
pm_caption = "`ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot IS:` **ONLINE**\n\n"
pm_caption += "🔸**SYSTEM STATUS**\n"
pm_caption += "🔹TELETHON VERSION             : **6.0.9**\n`Python:` **3.7.4**\n"
pm_caption += "🔸DATABASE STATUS              : **Functional**\n"
pm_caption += "🔹**Current Branch**           : `Master`\n"
pm_caption += "🔸**ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot OS**  : `1.14`\n"
pm_caption += f"🔹**My Boss**                 : {DEFAULTUSER} \n"
pm_caption += "🔸**Made By 😎**               : [Sensei](https://t.me/sensei_nex)\n\n"
pm_caption += "🔻Deploy Your Own              : [Repo](https://github.com/SenseiMAX/SenseiMAX-Kingbot)\n"

@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
