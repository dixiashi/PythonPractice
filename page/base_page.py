from common.consts import consts
from browser.browser import BrowserDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(BrowserDriver):

    implicit_wait = consts.IMPLICIT_WAIT_TIME_OUT

    def __init__(self):
        super().__init__()

    def navigate_to(self, url):
        try:
            self.Driver.get(url)
        except Exception as ex:
            print(ex)

    def wait_until(self, by, value, time_out=consts.TIME_OUT):
        WebDriverWait(self.Driver, time_out).until(
            lambda result: self.is_element_present(by, value))

    def is_element_present(self, by, value):

        try:
            self.Driver.find_element(by, value)
            return True
        except Exception as ex:
            print(ex)
            return False
        finally:
            # set back to where you once belonged
            self.Driver.implicitly_wait(self.implicit_wait)

    def execute_script(self, jquery_string):
        result = ""
        try:
            result = self.Driver.execute_script(
                "return {};".format(jquery_string))
        except Exception as ex:
            print(ex)
        finally:
            return result

    def wait_page_completed(self):
        WebDriverWait(self.Driver, consts.WAIT_PAGE_TIME_OUT).until(
            lambda result: self.execute_script("document.readyState") == "complete")

    def wait_element_display(self, by, value):
        WebDriverWait(self.Driver, consts.WAIT_PAGE_TIME_OUT).until(
            lambda result: self.is_element_present(by, value))

    def wait_element_disappear(self, by, value):
        WebDriverWait(self.Driver, consts.WAIT_PAGE_TIME_OUT).until(
            lambda result: not self.is_element_present(by, value))

    def input_value(self, by, value, input_value):
        self.wait_element_display(by, value)

        if self.is_element_present(by, value):
            elem = self.Driver.find_element(by, value)
            elem.clear()
            elem.send_keys(input_value)
            
    def click(self,by,value):
        self.wait_element_display(by, value)
        if self.is_element_present(by, value):
            self.Driver.find_element(by, value).click()
