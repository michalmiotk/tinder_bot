import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import selenium.common.exceptions

from credentials import email, password


class TinderBot():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(r'C:\chromedriver.exe', chrome_options=options)

        self.driver.maximize_window()
        self.fb_cookie_btn_xpath = "//button[contains(@data-cookiebanner, 'accept_button')]"
    def get_main_page(self):
        self.driver.get("https://tinder.com/")
        time.sleep(1)

    def config_tinder_user_page(self):
        allow_localisation_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        allow_localisation_btn.click()
        allow_cookies_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
        allow_cookies_btn.click()
        not_allow_notification_about_likes_btn = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div/div[3]/button[2]/span')
        not_allow_notification_about_likes_btn.click()

    def wait_for_cookie_window_dissapear(self):
        while True:
            try:
                WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, self.fb_cookie_btn_xpath)))
                break
            except TimeoutException:
                print("waiting for cookie window dissapear")
    def handle_two_similar_fb_cookie_windows(self):
        while not self.driver.find_element_by_xpath(self.fb_cookie_btn_xpath):
            time.sleep(0.1)
        accept_cookie_btn = self.driver.find_element_by_xpath(self.fb_cookie_btn_xpath)
        accept_cookie_btn.click()
        self.wait_for_cookie_window_dissapear()
        time.sleep(6) #waiting to possible new appear same window
        if self.driver.find_elements_by_xpath(self.fb_cookie_btn_xpath):
            accept_cookie_btn = self.driver.find_element_by_xpath(self.fb_cookie_btn_xpath)
            accept_cookie_btn.click()
            self.wait_for_cookie_window_dissapear()


    def action_on_fb_login_page(self):
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.handle_two_similar_fb_cookie_windows()
        email_input = self.driver.find_element_by_xpath('//input[contains(@name, "email")]')
        email_input.send_keys(email)
        pass_input = self.driver.find_element_by_xpath('//input[contains(@type, "password")]')
        pass_input.send_keys(password)
        login_fb_btn = self.driver.find_element_by_xpath('//button[contains(@name, "login")]')
        login_fb_btn.click()

    def login(self):
        login_btn_path = '//body/div/div/div/div/main/div/div/div/div/div/header/div/div[2]/div[2]'
        login_btn = self.driver.find_element_by_xpath(login_btn_path)
        login_btn.click()
        time.sleep(1)
        login_with_fb_xpath = '/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button'
        login_with_fb_btn = self.driver.find_element_by_xpath(login_with_fb_xpath)
        login_with_fb_btn.click()
        time.sleep(1)
        self.action_on_fb_login_page()

        time.sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[0])

    def click_heart_when_match(self):
        #not implemented yet
        any_btn = self.driver.find_element_by_xpath('//button/[contains')
        any_btn.click()

    def swipe_right_once(self):
        like_xpath = "//button[contains(@class, 'like-green')]"
        try:
            swipe_right_btn = self.driver.find_element_by_xpath(like_xpath)
            swipe_right_btn.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            print("problem z kliknięciem - inny element otrzymał kliknięcie")
            add_tinder_to_welcome_screen_xpath = "//button[contains(@data-testid, 'addToHomeScreen')]"
            if self.driver.find_elements_by_xpath(add_tinder_to_welcome_screen_xpath):
                add_tinder_to_welcome_screen_btn = self.driver.find_element_by_xpath(add_tinder_to_welcome_screen_xpath)
                add_tinder_to_welcome_screen_btn.click()
            else:
                print("klikaj serce")


    def swipe_right_loop(self):
        while True:
            self.swipe_right_once()
            print("succes swipe")
            time.sleep(1)

if __name__ == '__main__':
    run = TinderBot()
    run.get_main_page()
    run.login()
    time.sleep(5)
    run.config_tinder_user_page()
    time.sleep(8)
    run.swipe_right_loop()