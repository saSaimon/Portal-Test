import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkOutPage = homepage.getShopItems()
        log.info("gettng all the cards title")
        cards = checkOutPage.getCardTitle()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)

            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.getBtnPrimary().click()
        checkOutPage.getBtnSuccess().click()

        confirmPage = ConfirmPage(self.driver)
        log.info("Entering Country as ind")
        confirmPage.getCountry().send_keys("ind")
        # time.sleep(5)

        self.verifyLinkPresence("India")

        confirmPage.getIndia().click()
        confirmPage.getCheckbox().click()
        confirmPage.getSubmit().click()
        textMatch = confirmPage.getAlertSuccess().text
        log.info("Text recieved from applicatio is "+textMatch)

        assert ("Success! Thank you!" in textMatch)


