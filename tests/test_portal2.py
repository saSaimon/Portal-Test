import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

email = "test8@test.com"
firstname = "Sadiqul"
lastname = "Alam"
driver = webdriver.Chrome("C:\Windows\webdriver\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
link = "https://connectstudio-portal-staging.world-television.com/626b73d8007dfc0ba2605d4b/registration"
driver.get(link)


def test_portal():
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']").send_keys(firstname)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']").send_keys(lastname)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "input[name='agree']").click()
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    driver.find_element(By.CSS_SELECTOR, ".registration-success-login").click()
    driver.find_element(By.CSS_SELECTOR, ".login-input-field").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, ".form-check-input").click()
    driver.find_element(By.CSS_SELECTOR, ".login-button").click()
    driver.find_element(By.LINK_TEXT, "Sessions").click()
    driver.find_element(By.CSS_SELECTOR, "[data-icon='angle-right']").click()
    time.sleep(15)
    driver.find_element(By.LINK_TEXT, "Agenda & Speakers").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".resource-card-download-visit-icon").click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    video_library = driver.find_element(By.LINK_TEXT, "Video Library")
    video_library.click()
    text = video_library.text
    driver.find_element(By.CSS_SELECTOR, ".fp-play-stroke").click()
    time.sleep(20)
    assert ("Video" in text)
    driver.get(link)

    driver.close()
