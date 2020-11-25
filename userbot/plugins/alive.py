#credits to @kraken_the_badass
#beautification credits to @sensei_nex for @senseiMAXprojects

#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins

# uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/547da1967cf2a4b75daad.mp4"
pm_caption = "➥ **💥 𝐒𝐀𝐕𝐀𝐆𝐄 𝐁𝐎𝐓 💥 IS:** `ONLINE`\n\n"
pm_caption += "➥ **👺🐚𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍  👊♢:** `1.18.0` \n"
pm_caption += "➥ ** 𝐏𝐘𝐓𝐇𝐎𝐍 ♡☞:** `3.7.4` \n"
pm_caption += "➥ **👊  𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄 𝐒𝐓𝐀𝐓𝐔𝐒  ♗:**  `Functional`\n"
pm_caption += f"➥ **// ✎  𝐌𝐘 𝐁𝐎𝐒𝐒  ☞ //** \n {DEFAULTUSER} \n"

pm_caption += " ♕ 𝐌𝐘 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ♕ 😎 \n [CHANNEL]()\n\n"
pm_caption += " 𝐌𝐘 𝐂𝐑𝐄𝐀𝐓𝐎𝐑 😎 \n [SAMEER] \n\n"
pm_caption += " 𝐆𝐑𝐎𝐔𝐏 😎 \n [GROUP]( @SAVAGEuserbot )\n"
pm_caption += "[🇮🇳 𝐃𝐄𝐏𝐋𝐎𝐘 𝐘𝐎𝐔𝐑 𝐒𝐀𝐕𝐀𝐆𝐄 𝐁𝐎𝐓 🇮🇳](https://github.com/legendx22/LegendBOT)"


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
