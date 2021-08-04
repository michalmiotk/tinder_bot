from selenium import webdriver
from credentials import email, password
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TinderBot():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(r'C:\chromedriver.exe', chrome_options=options)

        self.driver.maximize_window()

    def get_main_page(self):
        self.driver.get("https://tinder.com/")

    def config_tinder_user_page(self):
        allow_localisation_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        allow_localisation_btn.click()
        allow_cookies_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
        allow_cookies_btn.click()
        not_allow_notification_about_likes_btn = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div/div[3]/button[2]/span')
        not_allow_notification_about_likes_btn.click()

    def action_on_fb_login_page(self):
        self.driver.switch_to_window(self.driver.window_handles[1])
        time.sleep(3)
        cookie_btn_xpath = '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]'
        accept_cookie_btn = self.driver.find_element_by_xpath(cookie_btn_xpath)
        accept_cookie_btn.click()


        while True:
            try:
                WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, cookie_btn_xpath)))
            except TimeoutException:
                print("waiting for cookie window dissapear")
                break
        email_input = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
        email_input.send_keys(email)
        pass_input = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
        pass_input.send_keys(password)
        login_fb_btn = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        login_fb_btn.click()

    def login(self):
        login_btn_path = '//body/div/div/div/div/main/div/div/div/div/div/header/div/div[2]/div[2]'
        login_btn = self.driver.find_element_by_xpath(login_btn_path)
        login_btn.click()
        import time
        time.sleep(1)
        login_with_fb_xpath = '/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button'
        login_with_fb_btn = self.driver.find_element_by_xpath(login_with_fb_xpath)
        login_with_fb_btn.click()
        time.sleep(1)
        self.action_on_fb_login_page()

        time.sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(5)
        self.config_tinder_user_page()
        time.sleep(8)
        self.swipe_right_loop()

    def swipe_right_once(self):
        #like_xpath = '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button'

        swipe_right_btn = self.driver.find_element_by_xpath("//button[contains(@class, 'like-green')]")

        swipe_right_btn.click()

    def swipe_right_loop(self):
        while True:
            self.swipe_right_once()
            print("succes swipe")
            time.sleep(1)

if __name__ == '__main__':
    run = TinderBot()
    run.get_main_page()
    run.login()