from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

SIMILAR_ACCOUNT = "your-account"
USERNAME = "your-username"
PASSWORD = "your-password"

service = Service("C:\Development\chromedriver.exe")

class InstaFollower:

    def __init__(self, service):
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        try:
            self.driver.get("https://www.instagram.com/accounts/login/")

            sleep(2)
            email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
            email.send_keys(USERNAME)

            senha = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
            senha.send_keys(PASSWORD)

            sleep(3)
            log_in_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
            log_in_btn.click()

        except:
            print('Erro: Execução da ação cancelada | login_error')
            pass

    def find_followers(self):
        sleep(3)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        sleep(3)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        followers.click()

        sleep(2)
        modal = self.driver.find_element(By.CSS_SELECTOR, '.isgrP')
        for i in range(2):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_element(By.XPATH, '//*[@id="f8b5004b30b7bc"]/button')
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "//*[text()='Cancelar']")
                cancel_button.click()


bot = InstaFollower(service)
bot.login()
bot.find_followers()
bot.follow()