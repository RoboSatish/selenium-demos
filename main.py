import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
prefs = {"profile.default_content_setting_values.notifications": 2}

chrome_options.add_experimental_option("prefs", prefs)


class demoFindId():
    def locate_byId(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        #driver.find_element(By.CLASS_NAME,"email-login-box").send_keys("sat@gmail.com")
        #driver.find_element(By.CSS_SELECTOR,"#login-continue-btn").click()
        d1 = driver.find_elements(By.TAG_NAME,"input")
        d1 = driver.find_elements(By.TAG_NAME, "input")
        d1 = driver.find_elements(By.TAG_NAME, "input")
        print(len(d1))

        time.sleep(5)
        driver.close()
f1 = demoFindId()
f1.locate_byId()
