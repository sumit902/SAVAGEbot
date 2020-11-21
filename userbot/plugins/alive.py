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
PM_IMG = "https://telegra.ph/file/869c33d8840ab471a5737.jpg"
pm_caption = "➥ **💥𝕃𝔼𝔾𝔼ℕ𝔻💥 IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.15.0` \n"
pm_caption += "➥ **Python:** `3.7.4` \n"
# pm_caption += f"➥ **Uptime** : `1.0` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
# pm_caption += f"➥ **Version** : `{currentversion}`\n"
pm_caption += f"➥ **//💥  ᵐ𝕐 𝓫ⓞร丂  💀//** \n {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](github.com/TeamLEGENDX/LegendBOT/blob/master/LICENSE)\n"
# pm_caption += "➥ **Copyright** : By [StarkGang@Github](GitHub.com/StarkGang)\n"

pm_caption += " MY CREATOR 😎 \n [LEGEND X](https://t.me/legendx22)\n\n"

pm_caption += "[🇮🇳 Deploy 𝕃𝔼𝔾𝔼ℕ𝔻в𝓞Ⓣ 🇮🇳](https://github.com/legendx22/LegendBOT)"


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
