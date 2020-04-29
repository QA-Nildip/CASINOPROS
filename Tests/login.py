__author__ = 'AK'
import time

from Setting.constants import *
from selenium import webdriver

''''
This file contains the logic of login
'''


class Login:
    """
    This is the class for login
    """
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox(executable_path=r"C:\Users\Nildip\PycharmProjects\CASINOPROS\driver\geckodriver.exe")

    def test_registration(self):
        driver = self.driver
        action = 'registration'

        def get_url(url):
            """
            this method basically
            :param url:url of the game page
            :return: nothing
            """
            driver.get(url)
            print (url)
            pass

        def screenshot():
            """
            this method is only to take screenshot
            :return: nothing
            """
            driver.get(login_screenshot)
            time.sleep(2)
            pass

        get_url(registration_btn)
        screenshot()
        get_url(reg_uname)
        screenshot()
        get_url(reg_email)
        screenshot()
        get_url(reg_pwd)
        screenshot()
        get_url(reg_confirmpwd)
        screenshot()
        get_url(reg_submit_btn)
        time.sleep(5)
        get_url(reg_err_msg)
        err_text = driver.page_source
        if err_text.find('failed') != -1:
            print ("failed while trying to ", action)
        screenshot()
        self.action_validation(err_text, action)
        driver.close()

    def test_login(self):
        driver = self.driver
        action = 'login'

        def get_url(url):
            """
            this method basically
            :param url:url of the game page
            :return: nothing
            """
            driver.get(url)
            print (url)
            pass

        def screenshot():
            """
            this method is only to take screenshot
            :return: nothing
            """
            driver.get(login_screenshot)
            time.sleep(2)
            pass

        get_url(login_hud)
        screenshot()
        get_url(login_uname)
        screenshot()
        get_url(login_pwd)
        screenshot()
        get_url(login_submit)
        time.sleep(10)
        screenshot()

    def action_validation(self, err_text, action):
        """

        :param err_text:
        :param action:
        :return:
        """
        if err_text.find('failed') != -1:
            print ("failed while trying to ", action)
            msg = "failed while trying to ", action
        else:
            msg = 'pass'
        return msg


if __name__ == '__main__':
    obj = Login()
    #obj.test_registration()
    obj.test_login()