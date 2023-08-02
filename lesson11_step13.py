from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import pytest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class Test_class(unittest.TestCase):
    def test_1(self):
        browser = webdriver.Chrome()
        browser.get(link1)

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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Регистрация успешна!")

    def test_2(self):
        browser = webdriver.Chrome()
        browser.get(link2)

        first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your name']")
        first_name.send_keys("Ivan")

        last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        last_name.send_keys("Pirogov")

        email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your phone']")
        email.send_keys("mail.ru")

        # phone = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your address']")
        # phone.send_keys("12345")

        button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Регистрация успешна!")


if __name__ == "__main__":
    unittest.main()
