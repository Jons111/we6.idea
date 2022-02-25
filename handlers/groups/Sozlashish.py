from aiogram import types
from loader import dp
from filters import gurux, Guruh
from filters import Shaxsiy


# Echo bot
@dp.message_handler(Guruh(),text="Salom" )
async def bot_echo(message: types.Message):
    await message.reply(text='Va alaykum assalom')

@dp.message_handler(Guruh(),text="qalesz" )
async def bot_echo(message: types.Message):
    await message.reply(text='Zor ozizchi')


@dp.message_handler(Guruh(),text="salom" )
async def bot_echo(message: types.Message):
    await message.reply(text='Va alaykum assalom')


@dp.message_handler(Guruh(),text="nma gap" )
async def bot_echo(message: types.Message):
    await message.reply(text='Tinchli ozizdachi')

@dp.message_handler(Guruh(),text="Bot" )
async def bot_echo(message: types.Message):
    await message.reply(text='Sanmi')

@dp.message_handler(Guruh(),text="Zo'r" )
async def bot_echo(message: types.Message):
    await message.reply(text="Zo'r bolin")

@dp.message_handler(Guruh(),text="zor" )
async def bot_echo(message: types.Message):
    await message.reply(text="Zo'r bolin")

@dp.message_handler(Guruh(),text="bot" )
async def bot_echo(message: types.Message):
    await message.reply(text="Sanmi")

@dp.message_handler(Guruh(),text="lic otin" )
async def bot_echo(message: types.Message):
    await message.reply(text="spamman sax qlin")

@dp.message_handler(Guruh(),text="Qaleysn" )
async def bot_echo(message: types.Message):
    await message.reply(text="Yaxshi ozizchi")











