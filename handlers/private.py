
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**Hᴇʏ Hᴏᴛᴛɪᴇ Sʜᴏᴛᴛɪᴇ {message.from_user.first_name}** \n
**I Aᴍ A Mᴜsɪᴄ Sᴇʀᴠᴇʀ Fᴏʀ Yᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ Vᴏɪᴄᴇ Cʜᴀᴛ & Cʜᴀɴɴᴇʟs 😉🌸 Usᴇ Mᴇ Hᴀʀᴅʟʏ & Eɴᴊᴏʏ Mᴜsɪᴄ Wɪᴛʜ Sᴜᴘᴇʀ Dᴜᴘᴇʀ Qᴜᴀʟɪᴛʏ 😈❣️
Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ : [𝑹𝑼𝑷𝑷𝑨](https://t.me/ITZ_RUPU)**.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💞 ᴏᴡɴᴇʀ ", url="https://t.me/ITZ_RUPU")
                  ],[
                    InlineKeyboardButton(
                        "🔥Aɴʏ Pʀᴏʙʟᴇᴍ", url="https://t.me/shivamdemon"
                    ),
                    InlineKeyboardButton(
                        "🐬 Cᴏᴍᴍᴀɴᴅ", url="https://telegra.ph/%F0%9D%90%92%F0%9D%9F%92%F0%9D%90%92%F0%9D%90%87%F0%9D%90%88%F0%9D%90%95-%F0%9D%90%97%F0%9D%90%83--%F0%9D%99%B8-%F0%9D%90%80%F0%9D%94%AA-E-%F0%9D%97%A0%F0%9D%94%AC%E2%84%95%F0%93%82%B8-10-16"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Aᴅᴅ ᴍʏ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴅᴀʀʟɪɴɢ🤭.", url=f"https://t.me/itzrupu_vcbot"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("alive") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""Bᴏᴛ ᴏɴ Fᴏʀᴍ ʙᴀʙʏ 😈""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😎 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Shivamdemon")
                ]
            ]
        )
   )
