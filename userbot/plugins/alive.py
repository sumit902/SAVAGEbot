# stickery alive by @hellboi_atul
# I won't change the credits , Just kanged by @sensei_nex for SenseiMAX-Kingbot
# credits @xditya

import os
import requests
import time
from PIL import Image
from io import BytesIO
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
from datetime import datetime

ALIVE_PHOTTO = os.environ.get("ALIVE_PHHOTO" , None)

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "This user"

@borg.on(admin_cmd(outgoing=True, pattern="salive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTTO:
        pm_caption = f"-`ღ´-ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot is alive !-`ღ´- \n"
        pm_caption += "ᗰY ᑭEᖇO ᔕᗯᗩᗰI            : {DEFAULTUSER}\n"
        pm_caption += "●тєℓєтнση 𝚅𝙴𝚁𝚂𝙸𝙾𝙽●          : 15.0\n"
        pm_caption += "P̶y̶t̶h̶o̶n̶ ̶V̶e̶r̶s̶i̶o̶n̶               : 3.8.5\n"
        pm_caption += "OS                           : Kali Linux/Gnu rolling x64"
        pm_caption += "『𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻           : [ᴊᴏɪɴ]((https://t.me/SenseiMAXprojects)\n"
        pm_caption += "『𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿             : [ᴊᴏɪɴ](https://t.me/senseiBOT_supportchat)\n"
        pm_caption += "𝘓𝘐CENCE                       : MIT License](https://t.me/Sensei_nex)\n"


        pm_caption += "C̲O̲P̲Y̲R̲I̲G̲H̲T̲ 𝘽𝙔              : [ @Sensei_nex](https://t.me/Sensei_nex)\n"
        
        pm_caption += "[╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮╭━┳━━━┳━╮╭━╮╭━━━╮\n╱╱╱╱╱╱╱╱╱╱╱╭╮┃╭━╮\n┃╱╱╱╱╱╱╱╱╱╱╱╱┃┃\n╰╯┃┃╭━╮┣╮╰╯╭╰━━━(https://t.me/SenseiMAXprojects)"

                 



        chat = await alive.get_chat()
        await alive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALIVE_PIC,caption=pm_caption, link_preview = False)
        await allive.delete()
        return
    req = requests.get("https://media.giphy.com/media/Lkn0vwucikQ6Y/giphy.gif")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(alive.chat_id,"-`ღ´-ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot is alive !-`ღ´-"
                      f"ᗰY ᑭEᖇO ᔕᗯᗩᗰI           : {DEFAULTUSER}\n"
                      "●тєℓєтнση 𝚅𝙴𝚁𝚂𝙸𝙾𝙽●          : 15.0\n"
                      "P̶y̶t̶h̶o̶n̶ ̶V̶e̶r̶s̶i̶o̶n̶               : 3.8.5\n"
                      "OS                           : Kali Linux/Gnu rolling x64"
                      "『𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻           : [ᴊᴏɪɴ](https://t.me/SenseiMAXprojects)\n"
                      "『𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿             : [ᴊᴏɪɴ](https://t.me/senseiBOT_supportchat)\n"
                      "𝘓𝘐CENCE                       : MIT License](https://t.me/Sensei_nex)\n"
                                
                                

                      "C̲O̲P̲Y̲R̲I̲G̲H̲T̲ 𝘽𝙔              : [ @Sensei_nex](https://t.me/Sensei_nex)\n]
                                
                       "[╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮╭━┳━━━┳━╮╭━╮╭━━━╮\n╱╱╱╱╱╱╱╱╱╱╱╭╮┃╭━╮\n┃╱╱╱╱╱╱╱╱╱╱╱╱┃┃\n╰╯┃┃╭━╮┣╮╰╯╭╰━━━\n(https://t.me/SenseiMAXprojects)",link_preview = False ) 
        await alive.delete()
