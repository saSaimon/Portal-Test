import time
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
link = "https://admin-dev.easywebcast.com/login"
driver.get(link)
email = "sadiqul.alam@wtvglobal.com"
password = "123456"

email_field = driver.find_element(By.XPATH, '//*[@id="email-input"]')
password_field = driver.find_element(By.XPATH, '//*[@id="password-input"]')
login_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/form/div[3]/button')


email_field.send_keys(email)
password_field.send_keys(password)
login_button.click()


def test_archive():

    email_field.send_keys(email)
    password_field.send_keys(password)
    login_button.click()

    organization = driver.find_element(By.XPATH, '//*[@id="mainNavigation"]/ul/li[4]')
    organization.click()

    A_QA_Test = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div[2]/div/div[4]/table/tbody/tr[7]/td[5]/div/a')
    A_QA_Test.click()

    sadiq_client = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div/div/div[4]/div[4]/table/tbody/tr[2]/td[4]/div/div/button')))
    sadiq_client.click()

    view_webcast = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div/div/div[4]/div[4]/table/tbody/tr[2]/td[4]/div/div/div/button[1]')))
    view_webcast.click()

    for i in range(0, 100):

        option = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div/div/div/div[4]/table/tbody/tr[1]/td[5]/div/div/button')))
        option.click()

        archive = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[3]/div[2]/div/div[2]/div/div/div/div[4]/table/tbody/tr[1]/td[5]/div/div/div/button[2]')))
        archive.click()

        confirm_archive = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[2]')))
        confirm_archive.click()

        time.sleep(2)
        

time.sleep(5)
driver.close()