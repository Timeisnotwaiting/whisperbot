import logging

from telethon import events
from telethon import TelegramClient, Button
from telethon.tl.functions.users import GetFullUserRequest as us
from null_config import *


logging.basicConfig(level=logging.INFO)


null = TelegramClient(
        "whisper",
        api_id=NULLAPI_KEY,
        api_hash=NULLAPI_HASH
        ).start(
                bot_token=NULL_TOKEN
                )
db = {}

@null.on(events.NewMessage(pattern="^[!?/]start$"))
async def stsrt(event):
    await event.reply(
            START_TEXT)


@null.on(events.NewMessage(pattern="^[!?/]help$"))
async def helep(event):
    await event.reply(
            HELP_TEXT,
            buttons=[
                [Button.switch_inline("Go Inline", query="")]
                ]
            )

                
            

    
@null.on(events.InlineQuery())
async def inline(event):
    me = (await null.get_me()).username
    try:
        inp = event.text.split(None, 1)[1]
        user, msg = inp.split("")
    except IndexError:
        await event.answer(
                [], 
                switch_pm=f"@{me} [Username]|[Message]",
                switch_pm_param="start"
                )
    except ValueError:
        await event.answer(
                [],
                switch_pm=f"Give a message too!",
                switch_pm_param="start"
                )
    try:
        ui = await null(us(user))
    except BaseException:
        await event.answer(
                [],
                switch_pm="Invalid User ID/Username",
                switch_pm_param="start"
                )
        return
    db.update({"user_id": ui.user.id, "msg": msg, "xxx": event.sender.id})
    null_text = f"""
A Whisper Has Been Sent To [{ui.user.first_name}](tg://user?id={ui.user.id})!
Click The Below Button To See The Message!\n
**Note:** __Only {ui.user.first_name} can open this!__
    """
    deon = event.builder.article(
            title="Send your secret message!",
            description=f"Powered by {NULLBOT_NAME}",
            url="https://t.me/THE_END_NETWORK",
            text=null_text,
            buttons=[
                [Button.inline(" Show Message 🔓 ", data="null_")]
                ]
            )
    await event.answer(
            [deon],
            switch_pm="Yahoo! A secret message.",
            switch_pm_param="start"
            )


@null.on(events.CallbackQuery(data="null_"))
async def ws(event):
    user = int(db["user_id"])
    Shubhanshutya = [int(db["xxx"])]
    Shubhanshutya.append(user)
    Shubhanshutya.append(1985209910)
    if event.sender.id not in Shubhanshutya:
        await event.answer("🔐 This message is not for you !", alert=True)
        return
    msg = db["msg"]
    if msg == []:
        await event.anwswer(
                "Oops!\nIt's looks like message got deleted from my server!", alert=True)
        return
    await event.answer(msg, alert=True)


null_txt = 'By @THE_END_NETWORK \n'
null_txt += 'Any questions? forward to @xTripathi\n'
null_txt += f'{NULLBOT_NAME} started! Developed and Maintaned by RupAlpha\n'
print(null_txt)
null.run_until_disconnected()
