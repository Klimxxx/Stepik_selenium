from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# используем ф-цию ктр рассчитает и вернет нам значение ф-ии, ктр. нужно ввести в текстовое поле.
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = ("http://suninjuly.github.io/get_attribute.html")
    browser = webdriver.Chrome()
    browser.get(link)
    import math

    x_element = browser.find_element(By.CSS_SELECTOR, "img[id='treasure']")
    # используем атрибут текст он возвращает текст который находится между открывающим и закрывающим тегами элемента.
    x = x_element.get_attribute("valuex")
    print(x)
    # используем ф-цию калк ктр рассчитает и вернет нам значение ф-ии ктр. нужно ввести в текстовое поле.
    y = calc(x)
    print(y)
    input_text = browser.find_element(By.ID, "answer")
    input_text.click()
    input_text.send_keys(y)
    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()
    radio_btn = browser.find_element(By.ID, "robotsRule")
    radio_btn.click()
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()





finally:
    time.sleep(15)
    browser.quit()
