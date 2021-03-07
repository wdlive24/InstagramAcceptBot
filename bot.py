import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import selenium

class FollowerBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(
            "./chromedriver.exe")

    def WaitForObject(self, type, string):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((type, string)))

    def WaitForObjects(self, type, string):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((type, string)))

    def login(self):
        self.browser.get("https://www.instagram.com/accounts/login")

        login_objects = self.WaitForObjects(
            By.CSS_SELECTOR, "input._2hvTZ.pexuQ.zyHYP")

        login_objects[0].send_keys(self.username)
        login_objects[1].send_keys(self.password)
        login_objects[1].send_keys(Keys.ENTER)

        self.WaitForObject(By.CLASS_NAME, "coreSpriteKeyhole")

        self.WaitForObject(By.CSS_SELECTOR, "button.sqdOP.yWX7d.y3zKF").click()

        self.WaitForObject(By.CSS_SELECTOR, "button.aOOlW.HoLwm").click()

    def AcceptFollowers(self):
        self.browser.get("https://www.instagram.com/accounts/activity/?followRequests")

        try:
            requests = self.WaitForObjects(By.CLASS_NAME, "sqdOP.L3NKy.y3zKF")

            follow_buttons = []
            #wir filtern die bestätigen schnell
            for x in requests:
                if x.text == "Bestätigen":
                    follow_buttons.append(x)
            requests_count = 0
            for request in follow_buttons:
                request.click()
                requests_count +=1    
                time.sleep(1)

            print("{} new Follower".format(request_count))

        except selenium.common.exceptions.TimeoutException:
            print("No new Requests....")

bot = FollowerBot("milkymahomes", "bradbeal4life")

bot.login()


while True:
    print("Accepting Followers....")
    bot.AcceptFollowers()
    time.sleep(10)
