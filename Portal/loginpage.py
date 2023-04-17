from selenium.webdriver.common.by import By

class loginpage:

    def __init__(self, driver):
        self.driver = driver

    firstname = (By.CSS_SELECTOR, "input[placeholder='First Name']")
    secondname = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    email = (By.CSS_SELECTOR, "input[placeholder='Email']")
    terms = (By.CSS_SELECTOR, "input[name='agree']")
    register = (By.CSS_SELECTOR, ".btn")

    def getfirstname(self):
        return self.driver.find_elements(*loginpage.firstname)

    def getsecondname(self):
        return self.driver.find_elements(*loginpage.secondname)

    def getemail(self):
        return self.driver.find_elements(*loginpage.email)

    def getterms(self):
        return self.driver.find_elements(*loginpage.terms)

    def getregister(self):
        return self.driver.find_elements(*loginpage.register)


