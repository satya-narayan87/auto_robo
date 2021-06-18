import selenium

from selenium import webdriver
import pytest
from src.base_test import BaseTest






class Testbyte(BaseTest):
    def test_byte(self):
        self.lunch_site()
        self.site_navigator("search").fill()







