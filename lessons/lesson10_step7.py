from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def formula(x1):
    return str(math.log(abs(12 * math.sin(int(x1)))))

browser = webdriver.Chrome()

try:
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait2.html")

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

