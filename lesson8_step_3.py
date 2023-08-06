from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = ("https://suninjuly.github.io/selects1.html")
    browser = webdriver.Chrome()
    browser.get(link)
    import math

    x1_element = browser.find_element(By.CSS_SELECTOR, "span[id='num1']")
    x1 = x1_element.text
    x2_element = browser.find_element(By.CSS_SELECTOR, "span[id='num2']")
    x2 = x2_element.text
    sum_1 = int(x1) + int(x2)
    # импортируем селект
    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element(By.CSS_SELECTOR, "select[id='dropdown']"))
    # ищем селект по видимому тексту равному сум_1
    select.select_by_visible_text(str(sum_1))

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-default']").click()


finally:
    time.sleep(15)
    browser.quit()
