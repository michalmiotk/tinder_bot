from selenium import webdriver

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(r'C:\chromedriver.exe')
        self.driver.maximize_window()

    def get_main_page(self):
        self.driver.get("https://tinder.com/")

    def login(self):
        login_btn_path = '//body/div/div/div/div/main/div/div/div/div/div/header/div/div[2]/div[2]'
        login_btn = self.driver.find_element_by_xpath(login_btn_path)

        login_btn.click()

if __name__ == '__main__':
    run = TinderBot()
    run.get_main_page()
    run.login()