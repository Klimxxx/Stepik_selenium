from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


browser = webdriver.Chrome()
try:
    browser.get("https://google.com")
    search_input = browser.find_element(By.NAME, "q")
    search_input.click()
    search_input.send_keys("yashaka/selene")
    search_input.send_keys(Keys.ENTER)
    time.sleep(1)









finally:
    time.sleep(100)
    browser.quit()






# browser.open('https://google.com')
# browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))Python