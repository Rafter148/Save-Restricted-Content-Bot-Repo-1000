import os
from .. import bot as gagan
from telethon import events, Button
from telethon.tl.types import InputMediaPhoto

S = "/start"
START_PIC = "https://graph.org/file/05be568f195e32e75f32f.jpg"
TEXT = "𝗦𝗘𝗡𝗗 𝗠𝗘 𝗧𝗛𝗘 𝗟𝗜𝗡𝗞 𝗢𝗙 𝗔𝗡𝗬 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗢𝗙 𝗥𝗘𝗦𝗧𝗥𝗜𝗖𝗧𝗘𝗗 𝗖𝗛𝗔𝗡𝗡𝗘𝗟𝗦 𝗧𝗢 𝗖𝗟𝗢𝗡𝗘 𝗜𝗧 𝗛𝗘𝗥𝗘\n𝗙𝗢𝗥 𝗣𝗥𝗜𝗩𝗔𝗧𝗘 𝗖𝗛𝗔𝗡𝗡𝗘𝗟'𝗦 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦, 𝗦𝗘𝗡𝗗 𝗧𝗛𝗘 𝗜𝗡𝗩𝗜𝗧𝗘 𝗟𝗜𝗡𝗞 𝗙𝗜𝗥𝗦𝗧\n\n👉🏻𝗘𝗫𝗘𝗖𝗨𝗧𝗘 /batch 𝗙𝗢𝗥 𝗕𝗨𝗟𝗞 𝗣𝗥𝗢𝗖𝗘𝗦𝗦 𝗨𝗣𝗧𝗢 10𝗞 𝗙𝗜𝗟𝗘𝗦 𝗥𝗔𝗡𝗚𝗘.\n\n    𝗧𝗛𝗜𝗦 𝗕𝗢𝗔𝗧 𝗠𝗔𝗗𝗘 𝗕𝗬\n\n 🌹✴️ [ 🇭 🇪 🇲 🇺  ] ✴️🌹\n    𝗝𝗢𝗜𝗡 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n         @Hemendra148"

def is_set_button(data):
    return data == "set"

def is_rem_button(data):
    return data == "rem"

@gagan.on(events.CallbackQuery(pattern=b"set"))
async def sett(event):    
    gagan = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with gagan.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
            return
        mime = x.file.mime_type
        if 'png' not in mime and 'jpg' not in mime and 'jpeg' not in mime:
            return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")

@gagan.on(events.CallbackQuery(pattern=b"rem"))
async def remt(event):  
    gagan = event.client            
    await event.edit('Trying... to save Bamby ... Wait')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        

@gagan.on(events.NewMessage(pattern=f"^{S}"))
async def start_command(event):
    # Creating inline keyboard with buttons
    buttons = [
        [Button.inline("SET THUMB", data="set"),
         Button.inline("REM THUMB", data="rem")],
        [Button.url("Join Channel", url="https://t.me/+nr3UBRp6uhA5Y2Vl")]
    ]

    # Sending photo with caption and buttons
    await gagan.send_file(
        event.chat_id,
        file=START_PIC,
        caption=TEXT,
        buttons=buttons
    )

