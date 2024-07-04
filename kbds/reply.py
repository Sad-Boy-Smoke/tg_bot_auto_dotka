import sys
sys.path.append('d:/pth_fun')

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

main_kbds = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Уничтожить личную жизнь', callback_data='launch_dotka')],
    [InlineKeyboardButton(text='Залететь в voice к фидерам', callback_data='ds')], 
    [InlineKeyboardButton(text='ВКЛ подсветку', callback_data='yeelight_on')], 
    [InlineKeyboardButton(text='ВЫКЛ подсветку', callback_data='yeelight_off')],
    [InlineKeyboardButton(text='Включить световое сопровождение подсветки за экраном', callback_data='yeelight_color_switch')]
    ])

