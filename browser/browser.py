from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BrowserDriver(object):
    Driver = None

    def __init__(self):
        driver_path = "driver\chromedriver.exe"
        try:
            self.Driver = webdriver.Chrome(driver_path)
        except Exception as e:
            print(e)
        finally:
            self.Driver = webdriver.Ie(driver_path)
