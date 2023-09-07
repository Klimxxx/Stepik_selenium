from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x1):
    return str(math.log(abs(12 * math.sin(int(x1)))))

try:
    link = ("https://SunInJuly.github.io/execute_script.html")
    browser = webdriver.Chrome()
    browser.get(link)
    # ищем элемент по айди и печатаем его в консоль для проверки
    x1_element = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
    x1 = x1_element.text
    print(x1)
    # считаем значение по формуле из функции
    y_1 = calc(x1)
    print(y_1)
    # ищем поле инпут и вводим туда функцию
    input_text = browser.find_element(By.ID, "answer")
    input_text.click()
    input_text.send_keys(y_1)
    # ищем чекбокс по айди и нажимаем на него
    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()
    # перематываем страницу вниз (скроллим)
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_box)
    # находим кнопку радиобаттон по айди и нажимаем на нее
    radio_btn = browser.find_element(By.ID, "robotsRule")
    radio_btn.click()
    #ищем кнопку по тэгу и нажимаем на нее
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(15)
    browser.quit()

