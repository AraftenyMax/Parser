import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class AvitoParser:
    def __init__(self):
        self.urls = {'add_item': 'https://www.avito.ru/additem'}
        self.xpaths = {'auth_account_button': "//p[contains(.,'Maxim Arafteny')]",
                       'auth_button': "//i[contains(@class,'gp')]",
                       'password': "//input[@aria-label='Enter your password']",
                       'proceed_button': "//span[contains(.,'Next')]",
                       'phone_field': "/html/body/div[2]/div[1]/div/form/div[2]/fieldset[9]/div/input",
                       'proceed_button_avito':
                           "/html/body/div[2]/div[1]/div/form/div[2]/fieldset[12]/div/button/span[1]",
                       'email_avito_field':
                           "/html/body/div[2]/div[1]/div/form/div[2]/fieldset[2]/div[1]/div[1]/div/input",
                       'root_category': "//div[.='Категория']"}
        self.iDS = {'login': 'identifierId'}
        self.credentials = {'login': 'maxtester2000@gmail.com', 'password': '789523746', 'phone': '(922) 555-1234'}
        self.main_window_handle = None
        self.current_handle = None
        self.driver = webdriver.Chrome()

    def authenticate(self):
        self.driver.find_element_by_xpath(self.xpaths['auth_button']).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        login_field = self.driver.find_element_by_id(self.iDS['login'])
        login_field.send_keys(self.credentials['login'])
        self.driver.find_element_by_xpath(self.xpaths['proceed_button']).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.xpaths['password']).send_keys(self.credentials['password'])
        self.driver.find_element_by_xpath(self.xpaths['proceed_button']).click()
        self.driver.switch_to.window(self.main_window_handle)
        time.sleep(10)
        self.driver.find_element_by_xpath(self.xpaths['email_avito_field']).send_keys(self.credentials['login'])
        self.driver.find_element_by_xpath(self.xpaths['phone_field']).send_keys(self.credentials['phone'])
        self.driver.find_element_by_xpath(self.xpaths['proceed_button_avito']).click()
        time.sleep(5)

    def collect_categories(self):
        root_section = self.driver.find_element_by_xpath(self.xpaths['root_category']).parent
        sections = root_section.find_by_tag_name('button')

    def run(self):
        self.driver.get(self.urls['add_item'])
        self.main_window_handle = self.driver.window_handles[0]
        self.authenticate()


parser = AvitoParser()
parser.run()