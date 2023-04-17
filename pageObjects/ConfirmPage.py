from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    india = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    alertSuccess = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getIndia(self):
        return self.driver.find_element(*ConfirmPage.india)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def getAlertSuccess(self):
        return self.driver.find_element(*ConfirmPage.alertSuccess)


