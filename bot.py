import time
from datetime import datetime

import constants
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Bot:

    def __init__(self):
        _browser_profile = webdriver.FirefoxProfile()
        _browser_profile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile=_browser_profile)
        self.actions = ActionChains(self.driver)

    def login(self, friend):
        self.driver.get("https://www.facebook.com/messages/t/" + friend)

        email = self.driver.find_element_by_id("email")
        email.clear()
        email.send_keys(constants.USERNAME)

        password = self.driver.find_element_by_id("pass")
        password.clear()
        password.send_keys(constants.PASSWORD)

        self.driver.find_element_by_id("loginbutton").send_keys(Keys.RETURN)

    def send_message(self, messages):
        for message in messages:
            self.actions.send_keys(message)
            self.actions.send_keys(Keys.RETURN)
        self.actions.perform()

    def __del__(self):
        self.driver.close()

def execute(friend, messages):
    bot = Bot()
    bot.login(friend)
    time.sleep(10)
    bot.send_message(messages)
    del bot

if __name__ == "__main__":
    execute(constants.FRIEND_USERNAME, ["Hello", "This is a test"])
