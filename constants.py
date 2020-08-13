# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:06:39 2020

@author: Asus
"""


BASE_URL="https://tinder.com"

#get token from @botFather
TOKEN=""

COOKIES_ACCEPT_PATH = '//*[@id="content"]/div/div[2]/div/div/div[1]'
AUTH_VIA_PHONE_PATH = (
    '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button'
)
FILL_OUT_PHONE_PATH = (
    '//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input'
)
MODAL_BUTTON_PATH = '//*[@id="modal-manager"]/div/div/div[1]/button'
POPUP_BUTTON_PATH = '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]'
OTP_CODE_INPUT_PATH = (
    '//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[{}]'
)