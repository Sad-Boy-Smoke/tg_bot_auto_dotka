import sys
sys.path.append('d:/pth_fun')

from time import sleep

from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram import  types
from aiogram.types import CallbackQuery

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from local_host.local_task import dt_launch
from local_host.local_task import check_start
from local_host.local_task import discord_voice
from local_host.local_task import yeelight_on
from local_host.local_task import yeelight_off
from local_host.local_task import yeelight_color_switcher

from kbds import reply

user_private_router = Router()

@user_private_router.message(CommandStart())
async def posil_nahui(message: types.Message):
    await message.answer('77+33 = 100 - это не алегбра, это характер', reply_markup=reply.main_kbds)

@user_private_router.callback_query(F.data == 'launch_dotka')
async def call_back_launch_dotka(callback: CallbackQuery):
    dt_launch()
    await callback.message.answer('Начал запуск')
    sleep(2)
    await callback.message.answer('Начал отслеживать запуск')
    check_start()

@user_private_router.callback_query(F.data == 'ds')
async def call_back_ds(callback: CallbackQuery):
    await callback.message.answer('Уже захожу к фидерам!')
    discord_voice()
    await callback.message.answer('Ты теперь часть фид комьюнити')

@user_private_router.callback_query(F.data == 'yeelight_on')
async def call_back_yeelight_on(callback: CallbackQuery):
    yeelight_on()
    await callback.message.answer('Подсветка ВКЛ')

@user_private_router.callback_query(F.data == 'yeelight_off')
async def call_back_yeelight_off(callback: CallbackQuery):
    yeelight_off()
    await callback.message.answer('Подсветка ВЫКЛ')

@user_private_router.callback_query(F.data == 'yeelight_color_switch')
async def call_back_yeelight_color_switch(callback: CallbackQuery):
    yeelight_color_switcher()
    await callback.message.answer('Включено отслеживание цветов монитора и их передача на подсветку')
