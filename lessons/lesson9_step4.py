from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def formula(x1):
    return str(math.log(abs(12 * math.sin(int(x1)))))


try:
    link = ("http://suninjuly.github.io/alert_accept.html")
    browser = webdriver.Chrome()
    browser.get(link)
    # находим и нажимаем кнопку submit
    btn_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn_submit.click()
    # находим и нажимаем конфирм окно
    confirm = browser.switch_to.alert
    confirm.accept()
    x1_element = browser.find_element(By.ID, "input_value" )
    x1 = x1_element.text
    y1 = formula(x1)
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y1)
    btn_submit_2 = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    btn_submit_2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

