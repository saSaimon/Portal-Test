import time
from logggg import test_logDemo
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\Windows\webdriver\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
link = "https://connectstudio-admin-dev.world-television.com/login"
driver.get(link)
email = "sadiqul.alam@wtvglobal.com"
password = "123456"
action = ActionChains(driver)
#variables
fieldEmail = driver.find_element(By.ID, "email")
fieldPass = driver.find_element(By.ID, "password")
buttonLogin = driver.find_element(By.CSS_SELECTOR, ".login-button")
def get_login():
    fieldEmail.send_keys(email)
    fieldPass.send_keys(password)
    buttonLogin.click()
    test_logDemo()


def test_organization():
    get_login()
    time.sleep(10)
    #organization
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/aside[1]/ul/li[3]'))).click()

    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/aside[2]/div[2]/div/div[4]/ul/li[3]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/aside[2]/div[2]/div/div[3]/div[5]/div/div/div[3]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/aside[2]/div[2]/div/div[1]/div[2]/div/div[2]/table/tbody/tr/td[3]').click()
    time.sleep(5)
    driver.close()
    test_logDemo()


def test_createPortal():

    get_login()

    #click create portal
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/aside[1]/ul/li[6]'))).click()


    #click select organization
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/aside[2]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div'))).click()


    #Selecting the organization name
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[3]'))).click()
    time.sleep(3)
    # Click Client
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[1]/aside[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div'))).click()
    #select Client
    driver.find_element(By.CSS_SELECTOR, "div[title='Sadiq Client'] div[class='ant-select-item-option-content']").click()
    # Uploading File
    s = driver.find_element(By.XPATH, "//input[@type='file']")
    s.send_keys('E:\\qa\\photo1.jpg')

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='custom-save-btn text-center my-2 btn btn-primary']"))).click()
    #Select Primary Color
    # WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable(
    #         (By.CSS_SELECTOR, ".rcp-saturation-cursor"))).click()