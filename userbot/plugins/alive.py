#credits to @kraken_the_badass
#kanged by @sensei_nex for @senseiMAXprojects

mport asyncio
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, hellversion
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

kraken = bot.uid

PM_IMG = "https://media.giphy.com/media/Lopx9eUi34rbq/giphy.gif"
pm_caption = "__**🔥🔥ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot  IS ONLINE🔥🔥**__\n\n"

pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={Sensei})』**\n\n"

pm_caption += "🛡️TELETHON🛡️ : 1.15.0 \n"

pm_caption += f"ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot      : `{ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot}`\n"

pm_caption += "⚠️CHANNEL⚠️                : [ᴊᴏɪɴ](https://t.me/HellBot_Official)\n"

pm_caption += "🔱GROUP🔱.                 : [ᴊᴏɪɴ](https://t.me/HellBot_Official_Chat)\n"

pm_caption += "🔥CREATOR🔥    : [Nub Here](https://t.me/sensei_nex)\n\n"

pm_caption += "         [✨REPO✨](https://github.com/SenseiMAX/SenseiMAX-Kingbot) 🔹 [📜License📜](https://github.com/SenseiMAX/SenseiMAX-Kingbot/blob/master/LICENSE)"
#@command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
