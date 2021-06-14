from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

from src.base_test import BaseTest


class Testmarktplatz(BaseTest):

    def test_search_flight(self):
        wait = WebDriverWait(self.driver, 3)
        self.lunch_site()
        #Mazimize current window
        sleep(2)
        self.driver.maximize_window()
        sleep(3)
        try:
            #self.driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
            self.accept_cookies()
            WebDriverWait(self.driver, 3)
            
        except:
            pass
        self.driver.find_element_by_xpath('//*[@id="container"]/div[1]/div/a[2]').click()
        sleep(3)



