from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
import math

def formula(x1):
    return str(math.log(abs(12 * math.sin(int(x1)))))

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )

    book = browser.find_element(By.ID, "book").click()

    number = browser.find_element(By.ID, "input_value")
    x1 = number.text
    y = formula(x1)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    btn_submit = browser.find_element(By.ID, "solve").click()








    # button_book = browser.find_element(By.ID, "book")
    # button_book.click()







finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(110)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

