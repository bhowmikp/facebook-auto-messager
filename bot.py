'''Login to facebook and send message to friend'''

import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import constants


class Bot:
    '''Creates bot to send message on facebook

    Attributes:
        driver: interface of selenium webdriver
        actions: generate user actions
    '''

    def __init__(self):
        '''Initializes bot'''
        _browser_profile = webdriver.FirefoxProfile()
        _browser_profile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile=_browser_profile)
        self.actions = ActionChains(self.driver)

    def login(self, friend):
        '''Login to facebook with uesrname and password

        Args:
            friend: str. Username of friend to inbox
        '''
        self.driver.get("https://www.facebook.com/messages/t/" + friend)

        email = self.driver.find_element_by_id("email")
        email.clear()
        email.send_keys(constants.USERNAME)

        password = self.driver.find_element_by_id("pass")
        password.clear()
        password.send_keys(constants.PASSWORD)

        self.driver.find_element_by_id("loginbutton").send_keys(Keys.RETURN)

    def send_message(self, messages):
        '''Sends the messages

        Args:
            messages: list of str containing the messages to send. Each element
                represents one message
        '''
        for message in messages:
            self.actions.send_keys(message)
            self.actions.send_keys(Keys.RETURN)
        self.actions.perform()

    def __del__(self):
        '''Deinitilizates bot'''
        self.driver.close()


def execute(friend, messages):
    '''Creates the bot and send the messages

    Args:
        friend: str containing facebook username of friend
        messages: list of str containing the messages to send. Each element
            represents one message
    '''
    bot = Bot()
    bot.login(friend)
    time.sleep(10)
    bot.send_message(messages)
    del bot


if __name__ == "__main__":
    execute(constants.FRIEND_USERNAME, constants.MESSAGES)
