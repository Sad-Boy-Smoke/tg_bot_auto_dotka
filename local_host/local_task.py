import subprocess as sb
import datetime
from time import sleep
import pyautogui
import cv2 as cv
import psutil
import numpy as np
import keyboard
from pynput.keyboard import Key, Controller
import mss
import os
import random
import string
from yeelight import Bulb, LightType
import requests
from ahk import AHK
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

global bot, file_path, id_chat, Dota_path, Discord_path, screen_dota_path, screen_discord_path, screen_launch_dota_path

bot=os.getenv('tokio')
id_chat=os.getenv('CHAT_ID')
Dota_path = os.getenv('Dota_path')
Discord_path = os.getenv('Discord_path')
screen_dota_path = os.getenv('screen_dota_path')
screen_discord_path = os.getenv('screen_discord_path')
screen_launch_dota_path = os.getenv('screen_launch_dota_path')

def kill_process(kill_name):

    processes_name = psutil.process_iter(['pid', 'name'])

    for process in processes_name:
        try:
            if process.info['name'] == kill_name:
                process.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def screen_and_message(path_for_screen, monitor_number):

    TOKEN = bot
    CHAT_ID = id_chat
    with mss.mss() as sct:

        monitor = sct.monitors[monitor_number]

        screenshot = sct.grab(monitor)

        path_for_screen = os.path.join(os.getcwd(), path_for_screen)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=path_for_screen)

        sleep(1)

    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    files = {'photo': open(path_for_screen, 'rb')}
    data = {'chat_id': CHAT_ID}
    requests.post(url, files=files, data=data)

def dt_launch():

    kill_process('dota2.exe')

    # sb.Popen(str('"') + sb.check_output(r'where /R "C:\Program Files (x86)" dota2.exe', shell=True).decode('utf-8').strip() + str('"')) - ВНИМАНИЕ: эта строчка кода нужна для того чтобы автоматически найти в директории Prog Files (86) файл dota2.exe, 
    # при поиске на всем простренстве диска, а именно "C:\" выдает ошибку, возможно,
    # по этому для простоты закидывания своих путей, все готовые пути до .exe вынес в .env
    #C:\Windows\system32>where /R "C:\" dota2.exe
    #ОШИБКА: Синтаксическая ошибка. Потерян аргумент по умолчанию.
    #Введите "WHERE /?" для получения справки по использованию.
    #дай бог потом с этим разберусь

    sb.Popen(Dota_path, shell=True)

def check_start():
    while True:
        i = 10
        x = 320
        y = 1
        width = 1920
        height = 30
       
        sleep(i)

        myScreenshot = pyautogui.screenshot(region=(x, y, width, height))
        myScreenshot.save(screen_launch_dota_path)

        screen = cv.imread(screen_launch_dota_path)

        center_x = width // 2
        center_y = height // 2
        b, g, r  = screen[center_y, center_x]
        
        if b == 0 and g == 140 and r == 255:
            i -= 1
            print('Это пидарсная желтизна, нахуй ее')
            continue

        elif b == 0 and g == 0 and r == 0:
            i -= 1
            print('Да это блять белый, \n Молодой и белый, мы выросли не в LA \n Я хочу скупать одежду, в шоуруме sale \n Жёлтый дым - disable, какой нахуй лейбл \n В моей сумке полкило, я делаю деньги')
            continue

        elif b == 255 and g == 255 and r == 255:
            i -= 1
            print('Господь бог да это же black siemens, Скр-скр-скр-скр, в мёртвых Найках (Ва-ау!) \n Скр-скр-скр-скр, в белой майке (Скр, скр!) \n Скр-скр-скр-скр, чёрный сталкер (Па-па-па-пау!) \n Скр-скр-скр-скр, с зипом сканка (Тварь!) \n Скр-скр-скр-скр, в мёртвых Найках (Ва-ау!) \n Скр-скр-скр-скр, в белой майке (Скр, скр!) \n Скр-скр-скр-скр, чёрный сталкер (Па-па-па-пау!) \n Скр-скр-скр-скр, с зипом сканка (Скр!)')
            continue

        else:
            i = 10
            print('Да неужели дотка решила, что можно перестать делать хуйету и просто запуститься, не ну я просто в ахуе')
            keyboard.press_and_release('esc')
            break

    sleep(3)

    screen_and_message(screen_dota_path, 2)
    
def discord_voice():

    kill_process("DiscordPTB.exe")

    keyboard = Controller()
    ahk = AHK()

    sb.Popen(Discord_path, shell=True)

    sleep(7)

    win = ahk.active_window
    win = ahk.get_active_window()
    win.maximize()
    pos = win.get_position() 

    if pos.x == -8 and pos.y == -8 and pos.width == 2576 and pos.height == 1056:

        keyboard.press(Key.shift)
        keyboard.press(Key.cmd)
        keyboard.press(Key.right)

        keyboard.release(Key.right)
        keyboard.release(Key.cmd)
        keyboard.release(Key.shift)

    elif pos.x == 2552 and pos.y == -8 and pos.width == 1936 and pos.height == 1056:
        pass

    pyautogui.click(2590, 860)
    pyautogui.click(2590, 860)
    pyautogui.click(2590, 860)
    pyautogui.click(2560 + 137, 306)

    sleep(3)

    screen_and_message(screen_discord_path, 1)

def yeelight_color_switcher():

    ip_yeelight = "192.168.1.78"
    bulb = Bulb(ip_yeelight, duration=1000)
    bulb.turn_off()
    bulb.turn_on()

    def generate_string(length):
        all_symbols = string.ascii_uppercase + string.digits
        result = ''.join(random.choice(all_symbols) for _ in range(length))
        return result

    count_if = 0
    cap = cv.VideoCapture(0)

    while True:

        i = 10
        ret, frame = cap.read()
        hsv_img = cv.cvtColor(frame, cv.COLOR_RGB2HSV)

        h_mean = float(round(np.mean(hsv_img[:, :, 0]), 5))
        s_mean = float(round(np.mean(hsv_img[:, :, 1]), 5))
        v_mean = float(round(np.mean(hsv_img[:, :, 2]), 5))

        sleep(1)

        if count_if <= 50:
            bulb.set_hsv(h_mean, s_mean, v_mean, light_type=LightType.Main)
            count_if += 1

        else:

            try:
                bulb = Bulb(str(ip_address =  generate_string(i)))
                bulb.turn_off()
                bulb.turn_on()
                i += 1

            except:
                bulb = Bulb(ip_yeelight)
                bulb.turn_off()
                bulb.turn_on()
                count_if = 0

        print(h_mean, s_mean, v_mean)

        if cv.waitKey(1) == ord('q'):
            break

    cv.destroyAllWindows()

def yeelight_on():
    bulb = Bulb("192.168.1.78", duration=1000)
    bulb.turn_on()

def yeelight_off():
    bulb = Bulb("192.168.1.78", duration=1000)
    bulb.turn_off()
