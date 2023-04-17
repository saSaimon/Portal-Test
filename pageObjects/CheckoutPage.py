from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    btnPrimary = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    btnSuccess = (By.CSS_SELECTOR, ".btn-success")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getBtnPrimary(self):
        return self.driver.find_element(*CheckOutPage.btnPrimary)

    def getBtnSuccess(self):
        return self.driver.find_element(*CheckOutPage.btnSuccess)
