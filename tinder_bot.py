import logging
import time
from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

BASE_URL = "https://tinder.com"


COOKIE_ACCEPTANCE_BUTTON = '//*[@id="content"]/div/div[2]/div/div/div/button'

VIA_PHONE_LOGIN_BUTTON = (
    '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button'
)

PHONE_INPUT_PATH = '//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input'
PHONE_CONTINUE_BUTTON = '//*[@id="modal-manager"]/div/div/div[2]/button'
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
class TinderAPI:
    """
    Для автоматизации взаимодействия с приложением Тиндер.
    """
#'C:/Users/Asus/Documents/chromedriver_win32'
    def __init__(self):
        self.driver= webdriver.Chrome('C:/Users/Asus/Documents/chromedriver_win32/chromedriver.exe')
        self.logger = logging.getLogger(__name__)

    def login_page(self):
        self.driver.get(BASE_URL)

    def cookies_accept(self, xpath:str):
        self._find_and_click_button(
            by=By.XPATH, value=xpath
        )

    def login_via_phone(self, xpath:str):
        if not xpath:
            xpath = AUTH_VIA_PHONE_PATH
        try:
            self._find_and_click_button(by=By.XPATH, value=xpath)
        except NoSuchElementException as error:
            self.logger.info(error.msg)
            self._find_and_click_button(by = By.XPATH, value = '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/button')
        
    def _find_and_click_button(self, *, by: str, value: str):
        try:
            button = self.driver.find_element(by=by, value=value)
            button.click()
        except NoSuchElementException as error:
            self.logger.info(error.msg)
            print(error.msg)

    def fill_out_phone(self, *, phone_number: str, xpath:str):
        phone_input = self.driver.find_element(
            by=By.XPATH, value=xpath
        )
        phone_input.send_keys(phone_number)
    
    def click_send_sms_button(self, xpath:str):
        self._find_and_click_button(by=By.XPATH, value=xpath)
        
    def click_button(self, xpath:str):
        self._find_and_click_button(by=By.XPATH, value=xpath)

    def fill_out_otp_code(self, code:str, xpath:str):
        code_numbers_list= code.strip().split()
        for idx, element in enumerate(code_numbers_list):
            time.sleep(2)            
            self.fill_out_phone(phone_number=element, xpath=xpath.format(idx+1))
    

