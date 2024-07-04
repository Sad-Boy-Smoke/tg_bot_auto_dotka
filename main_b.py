import sys
sys.path.append('d:/pth_fun')

import asyncio
import os

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from aiogram import Bot, Dispatcher, types
from handlers.iser_private import user_private_router
from common.bot_cmds_list import private

ALLOWED_UPDATE = ['message, edit_message']

bot=Bot(token=os.getenv('tokio'))
dp = Dispatcher()

dp.include_router(user_private_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATE)


asyncio.run(main())