import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\Windows\webdriver\chromedriver.exe")

driver.get('https://connectstudio-portal-staging.world-television.com/62beb34ef530d24874686b44/registration');

time.sleep(10)

email="test56@gmail.com"

search_box1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/form/div[1]/div[1]/div/input')
search_box2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/form/div[1]/div[2]/div/input')
search_box3 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/form/div[1]/div[3]/div/input')
search_box4 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/form/div[2]/div/div/input')
reg_button = driver.find_element(By.XPATH,  '//*[@id="__next"]/div/div[1]/div/form/div[3]/div/button')

search_box1.send_keys('etyserty6')
search_box2.send_keys('yurtyurtyu6')
search_box3.send_keys(email)
search_box4.click()
reg_button.click()
time.sleep(15)

search_box_login = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/small')
search_box_login.click()
time.sleep(15)

login_1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/form/div[1]/input')
login_2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/form/div[2]/div/input')
login = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/form/div[3]/button')

login_1.send_keys(email)
login_2.click()
login.click()
time.sleep(10)

session = driver.find_element(By.XPATH, '//*[@id="navbar-toggle"]/div[2]/a[2]')
session.click()
time.sleep(6)
webcast = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/div/div/div[2]/div[2]')
webcast.click()
time.sleep(80)

qanda = driver.find_element(By.XPATH, '//*[@id="email"]')
qanda.send_keys(email)
qbody = driver.find_element(By.XPATH, '//*[@id="formQuestion"]')
qbody.send_keys('test888 is asking')
qsubmit = driver.find_element(By.XPATH, '//*[@id="formQa"]/div[4]/button')
qsubmit.click()
time.sleep(6)


#email = email.replace("'","\\'");







#search_box.submit()

time.sleep(5)

driver.quit()