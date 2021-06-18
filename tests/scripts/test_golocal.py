from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep, time
from logging import log
from src.base_test import BaseTest

import logging

logger = logging.getLogger(__name__)


class TestGolocal(BaseTest):

    def test_golocal(self):
        wait = WebDriverWait(self.driver, 3)
        logger.info("Lunch site")
        self.lunch_site()

        sleep(2)
        #Mazimize current window
        self.driver.maximize_window()


        sleep(2)
        logger.info("Clear Cookies")

        #Accept cookies if any occurrence.
        self.accept_cookies()


        sleep(2)
        logger.info("Open registration")

        self.open_registration()
        sleep(2)

        #Register by using mail id
        self.site_navigator('register_per_email').click()
        sleep(2)

        ###Below list of registration field
        field_list = ["email","user_name","password","repeat_password","place_name"]
        for i in field_list:
            self.site_navigator(i).fill()
            sleep(2)

        sleep(2)
        logger.info("Finished!!")