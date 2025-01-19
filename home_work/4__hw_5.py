from selenium import webdriver
from selenium.webdriver.common.by import By

def check_elements_on_page():
    driver = webdriver.Chrome()

    driver.get('https://www.saucedemo.com/')

    username_field = driver.find_elements(By.CSS_SELECTOR, '#user-name')
    password_field = driver.find_elements(By.CSS_SELECTOR, '#password')
    submit_button = driver.find_elements(By.CSS_SELECTOR, '#login-button')

    if username_field and password_field and submit_button:
        print("Elements found")
    else:
        print("Elements not found")

    driver.quit()

check_elements_on_page()
