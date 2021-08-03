from selenium import webdriver
from credentials import email, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(r'C:\chromedriver.exe')
        self.driver.maximize_window()

    def get_main_page(self):
        self.driver.get("https://tinder.com/")

    def action_on_fb_login_page(self):
        self.driver.switch_to_window(self.driver.window_handles[1])
        accept_cookie_btn = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]')
        accept_cookie_btn.click()
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
        print(self.driver.window_handles)
        login_with_fb_btn.click()
        time.sleep(1)
        print(self.driver.window_handles)
        self.action_on_fb_login_page()
        time.sleep(1)
        print("hantl", self.driver.window_handles)
        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(5)
        allow_localisation_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        allow_localisation_btn.click()
        allow_cookies_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
        allow_cookies_btn.click()
        not_allow_notification_about_likes_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]/span')
        not_allow_notification_about_likes_btn.click()
        time.sleep(6)
        swipe_right_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        swipe_right_btn.click()

if __name__ == '__main__':
    run = TinderBot()
    run.get_main_page()
    run.login()