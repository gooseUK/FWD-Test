from dependencies.dependencies import *
from enum import Enum

#pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager

