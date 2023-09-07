from selenium import webdriver
from selenium.webdriver.common.by import By
import time

links = ("http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html")
for link in links:
    print("Try to processing", link)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    last_name.send_keys("Pirogov")

    email = browser.find_element(By.CSS_SELECTOR, "input[class='form-control third']")
    email.send_keys("mail.ru")

    # phone = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your phone:']")
    # phone.send_keys("12345")

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()

