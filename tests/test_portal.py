import pytest

from Portal.loginpage import loginpage
from utilities.BaseClass import BaseClass


class TestPortal(BaseClass):
    def test_portal(self, getData):
        loginPage = loginpage(self.driver)
        loginPage.getfirstname().send_keys("Sadiqul")
        loginPage.getsecondname().send_keys("Alam")
        loginPage.getemail().send_keys("asadiqul0@gmail.com")
        loginPage.getterms().click()
        loginPage.getregister().click()

    # @pytest.fixture(params=["Rahul", "Shetty", "a@a.com"])
    # def getData(self, request):
    #      return request.param