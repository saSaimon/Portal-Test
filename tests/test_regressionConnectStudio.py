import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("C:\Windows\webdriver\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
link = "https://connectstudio-admin-staging.world-television.com/login"
driver.get(link)
email = "sadiqul.alam@wtvglobal.com"
password = "123456"

#variables
fieldEmail = driver.find_element(By.ID, "email")
fieldPass = driver.find_element(By.ID, "password")
buttonLogin = driver.find_element(By.CSS_SELECTOR, ".login-button")



def test_regression():

    fieldEmail.send_keys(email)
    fieldPass.send_keys(password)
    buttonLogin.click()
    time.sleep(10)
    organization = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/aside[1]/ul/li[3]')
    organization.click()
    organization.click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '.active').click()
    time.sleep(3)

    # # driver.find_element(By.CSS_SELECTOR, ".connect-studio-search-input-small").send_keys("A ")
    # driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/aside[2]/div[2]/div/div[3]/div[5]').click()
    # time.sleep(10)
    # driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/aside[2]/div[2]/div/div[3]/div[5]/div/div/div[3]').click()



