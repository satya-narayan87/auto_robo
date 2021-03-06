import string
import selenium
from random import randint
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, InvalidElementStateException

class element_action:

    def __init__(self,driver,locator: string, locator_name: string, id=False, name=False, xpath=False, link_text=False, partial_link_text=False, tag_name=False, class_name=False, css_selector=False ):
        
        """
        Args:
            driver (WebDriver): [Current Instance of the web Driver]
            locator_value (string) : [Value of the search query]
            locator_name (string): [Name of the locator for loggin purpose]
            id (bool, optional): [True if find by ID]. Defaults to False.
            name (bool, optional): [True if find by NAME]. Defaults to False.
            xpath (bool, optional): [True if find by XPATH]. Defaults to False.
            link_text (bool, optional): [True if find by LINK_TEXT]. Defaults to False.
            partial_link_text (bool, optional): [True if find by PARTIAL_LINK_TEXT]. Defaults to False.
            tag_name (bool, optional): [True if find by TAG_NAME]. Defaults to False.
            class_name (bool, optional): [True if find by CLASS_NAME]. Defaults to False.
            css_selector (bool, optional): [True if find by CSS_SELECTOR]. Defaults to False.
        """
        self.driver = driver
        self.locator = locator
        self.locator_name = locator_name

        self.id = id
        self.name = name
        self.xpath = xpath
        self.link_text = link_text
        self.partial_link_text = partial_link_text
        self.tag_name = tag_name
        self.class_name = class_name
        self.css_selector = css_selector

        self.element_value = {"id" : self.id, "XPath" : self.xpath , "name" : self.name, "link_list" : self.link_text, 
            "partial_link_test" : self.partial_link_text, "tag_name" : self.tag_name, "class_name" : self.class_name, "css_selector" : self.css_selector}

        self.element_map_to_locator = {"id" : By.ID, "XPath" : By.XPATH , "name" : By.NAME, "link_list" : By.LINK_TEXT, 
            "partial_link_test" : By.PARTIAL_LINK_TEXT, "tag_name" : By.TAG_NAME, "class_name" : By.CLASS_NAME, "css_selector" : By.CSS_SELECTOR}

        self.final_element
        self.final_locator = self.find_locator()

    def element_finder(self):
        for key in self.element_value.keys():
            if self.element_value[key] == True:
                return key

    def find_locator(self):
        self.final_element = self.element_finder()
        _final_locator = self.element_map_to_locator[self.final_element]
        return _final_locator


    def click(self):
        """This Function will click on a web elemen"""

        try:
            self.driver.find_element(self.final_locator, self.locator_value).click()

        except Exception as e : 
            print(e)


    def send_keys(self,text):
        """This Function will send keys to a web elemen
        """

        try:
            self.driver.find_element(self.final_locator, self.locator_value).clear()
            self.driver.find_element(self.final_locator, self.locator_value).send_keys(text)

        except Exception as e : 
            print(e)

    def wait_for_element_present(self):
        """[This function will wait for the element to be present ]

        """

        try:
            web_driver_wait = WebDriverWait(self.driver , 10)
            web_driver_wait.until(EC.presence_of_element_located((self.final_locator, self.locator_value)))

        except Exception as e : 
            print(e)

    def wait_for_element_clickable(self):
        """[This function will wait for the element to be clickable ]
        """
        try:
            web_driver_wait = WebDriverWait(self.driver , 10)
            web_driver_wait.until(EC.element_to_be_clickable((self.final_locator, self.locator_value)))

        except Exception as e : 
            print(e)

    def select_by_visible_text(self,visible_text):
        """This Function will select from dropdown using visible text
        """
        try:
            select = Select(self.driver.find_element(self.final_locator, self.locator_value))
            select.select_by_visible_text(visible_text)

        except Exception as e : 
            print(e)

    def select_by_value(self,select_value):
        """This Function will select from dropdown using value
        """
        try:
            select = Select(self.driver.find_element(self.final_locator, self.locator_value))
            select.select_by_value(select_value)

            
            
        except Exception as e : 
            print(e)


    def is_element_present(self):
        try:
            if (self.driver.find_element(self.final_locator, self.locator_value)):
                return True
            
        except NoSuchElementException as e : 
            print("Element" + self.final_locator + " not found")
            return False
        except InvalidElementStateException as e:
            print("Element" + self.final_locator + " state is invalid")
            return False    

    def JS_click(self):
        try:
            element = self.driver.find_element(self.final_locator, self.locator_value)

            self.driver.execute_script("arguments[0].click();", element)

        except Exception as e:
            print(e)

    def delay():
        time.sleep(randint(2,5))
