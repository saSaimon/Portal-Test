import select
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


s = Service("C:\Windows\webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=s)


def test_text():

    driver.get("https://demo.zeuz.ai/web/level/one/actions/save_text")
    text = driver.find_element(By.XPATH, '//*[@id="randomText"]').text
    driver.find_element(By.XPATH, '//*[@id="enter_text"]').send_keys(text)
    driver.find_element(By.CSS_SELECTOR, '.btn-primary ').click()
    confirmation  = driver.find_element(By.ID, 'text_showing').text
    assert "You have successfully verified the text" in confirmation