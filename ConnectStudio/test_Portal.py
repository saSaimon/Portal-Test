import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("C:\Windows\webdriver\chromedriver.exe")
email = "test376@test.com"
firstname = "Sadiqul"
lastname = "Alam"
link = "https://connectstudio-portal-staging.world-television.com/62beb34ef530d24874686b44/registration"


def test_portal():

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(link)
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
    time.sleep(50)
    # WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="formQuestion"]'))).send_keys("Hi")
    # driver.find_element(By.XPATH, '//*[@id="formQa"]/div[4]/button').click()
    # time.sleep(15)
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
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fp-play-stroke"))).click()
    time.sleep(20)
    assert ("Video" in text)
    driver.find_element(By.XPATH, '//*[@id="navbar-toggle"]/div[2]/a[4]').click()
    time.sleep(10)
    driver.close()