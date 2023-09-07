from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def formula(x1):
    return str(math.log(abs(12 * math.sin(int(x1)))))


try:
    link = ("http://suninjuly.github.io/redirect_accept.html")
    browser = webdriver.Chrome()
    browser.get(link)
    btn_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn_submit.click()
# В этой строке мы используем [1] для получения идентификатора второй открытой вкладки и сохраняем его в переменную new_window.
    new_window = browser.window_handles[1]
# Мы передаем new_window в качестве аргумента, чтобы указать, на какую вкладку мы хотим переключиться.
    browser.switch_to.window(new_window)
    x1_element = browser.find_element(By.ID, "input_value" )
    x1 = x1_element.text
    y1 = formula(x1)
    input_value = browser.find_element(By.ID, "answer")
    input_value.click()
    input_value.send_keys(y1)
    button_submit = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    button_submit.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

