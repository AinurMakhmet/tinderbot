# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:04:10 2020

@author: Asus
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.inline_keyboard import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
import time
from constants import (
    BASE_URL,
    COOKIES_ACCEPT_PATH,
    AUTH_VIA_PHONE_PATH,
    FILL_OUT_PHONE_PATH,
    MODAL_BUTTON_PATH,
    OTP_CODE_INPUT_PATH,
    POPUP_BUTTON_PATH,
    TOKEN
)
from tinder_bot import TinderAPI

bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
tinder=TinderAPI()
@dp.message_handler(commands=['start', 'go'])
async def hellower(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}")
    
@dp.message_handler(commands=['login'])
async def login(message: types.Message):
    tinder=TinderAPI()
    time.sleep(1.7)  
    tinder.login_page()
    time.sleep(3)  
    tinder.cookies_accept(xpath = '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
    time.sleep(1.7)  
    
    handles = tinder.driver.window_handles
    for idx in range(len(handles)):
        if handles[idx] != tinder.driver.current_window_handle:
            tinder.driver.switch_to.window(handles[0])
            tinder.login_via_phone(xpath='//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
    await message.answer("You have chosen login via phone, please enter your number with the command <code>/phone 'your_phone_number'</code> <b>(without country code)</b>")    

@dp.message_handler(commands=['phone'])
async def phone(message: types.Message):
    print(len(message.text.strip()))
    phone_number = message.text.strip()[6:].strip()
    print(phone_number)
    if len(phone_number)!=10:
        await message.answer("You have entered wrong number")
        return
        #tinder.fill_out_phone(phone_number=message.text.strip(''))
    print(dir(message))
    tinder.fill_out_phone(phone_number=phone_number, xpath=FILL_OUT_PHONE_PATH)
    tinder.click_send_sms_button(xpath='//*[@id="modal-manager"]/div/div/div[1]/button')   
    
    await message.answer(f"Enter your otp code")    

@dp.message_handler(commands=['code'])
async def fill_out_code(message: types.Message):
    print(len(message.text.strip()))
    code = message.text.strip()[5:].strip()
    print(code)
    if len(code)!=6:
        await message.answer("You have entered wrong code")
        return
        #tinder.fill_out_phone(phone_number=message.text.strip(''))
    
    tinder.fill_out_otp_code(code=code, xpath='//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[{}]')
    tinder.click_send_sms_button(xpath='//*[@id="modal-manager"]/div/div/div[1]/button')
    tinder.click_button(xpath='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    tinder.click_button(xpath='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    tinder.click_button(xpath='//*[@id="modal-manager"]/div/div/div[1]/button')
    # 1. 
    last_messages_inline_button = InlineKeyboardButton("Show last messages", callback_data = "last_messages")
    last_matches_inline_button = InlineKeyboardButton("show last matches", callback_data = "last_matches")
    show_users = InlineKeyboardButton("Show users", callback_data="show_users")
    inline_keyboard_markup = InlineKeybpardMarkup()
    inline_keyboard_markup.add(last_messages_inline_button)
    inline_keyboard_markup.add(last_matches_inline_button)
    inline_keyboard_markup.add(show_users)
    await message.answer("You have entered to tinder. Please choose the next action.",
                         reply_markup = inline_keyboard_markup)    
    
if __name__ =='__main__':
    print("Im running")
    executor.start_polling(dp, skip_updates=True)