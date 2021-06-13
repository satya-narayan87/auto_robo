"""
This is simple test suit. The test suit must be start with "test" or end with "test".
It must be annoted with pytest fixture.
"""

import logging
import os
from posixpath import basename
from typing import List
import glob
import time
import re
import pytest
import json
from pathlib import Path
import inspect

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



# uses the root logger - automatically will be enabled
logger = logging.getLogger(__name__)
cur_path = os.path.dirname(__file__)


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    """
    Base Test class.
    """


    def test_site_map(self,site_name):

        ##This will return data of websitedatetime A combination of a date and a time. Attributes: ()
        
        f = open('tests/conf_data/site_conf.json')

        self.site_data = json.load(f)
        return self.site_data[site_name]


    def lunch_site(self):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        base = os.path.basename(filename).replace(".py","").split("test_")[1]
        print(base)

        #Collect data with map
        data = self.test_site_map(base)
        print(data["name"])
        self.driver.get(data["name"])








