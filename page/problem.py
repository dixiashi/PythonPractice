from page.base_page import BasePage
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys
from common.consts import consts
import time


class ProblemPage(BasePage):

    code_selector = ""
    submit_button_selector = ""

    def __init__(self):
        super().__init__()

    def submit_code(self, url, python_code):

        try:
            url = consts.BASE_URL
            self.navigate_to(url)
            self.wait_page_completed()

            time.sleep(10)
            element = self.Driver.find_element_by_css_selector("body")
            print(element)
            element.send_keys(Keys.CONTROL + "a")
            print("body selected all")


            
            time.sleep(10)
            element = self.Driver.find_element_by_css_selector(".CodeMirror-line")
            element.click()

            print(element)
            print("ctrl + a")
            element.click()
            element.send_keys(Keys.CONTROL + "a")
            print("element selected all")

            time.sleep(10)

            #".CodeMirror-code .CodeMirror-line:first span:last"
            # self.click(by.CSS_SELECTOR, ".CodeMirror-code .CodeMirror-line:first span:last")

            # self.input_value(by.NAME, "", python_code)

            # self.click(by.ID, "graderAnalyze")
            # self.wait_element_display(by.CSS_SELECTOR, "")
            # self.wait_element_disappear(by.CSS_SELECTOR, "")
        except Exception as ex:
            print(ex)

        finally:
            self.Driver.close()
