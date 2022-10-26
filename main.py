from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://wikipedia.org")

input_box = driver.find_element(By.ID, "searchInput")

input_box.send_keys("selenium")

input_box.send_keys(Keys.ENTER)

import time

print('esperaremos 5 segundos' )
time.sleep(5)

driver.get("https://www.contraloria.cl")

input_box = driver.find_element(By.CLASS_NAME, "_1qG0")

input_box.send_keys("MUNICIPALIDAD")

input_box.send_keys(Keys.ENTER)

import time

print('esperaremos 5 segundos' )
time.sleep(5)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

input_box = driver.find_element(By.ID, "my-text-id")

input_box.send_keys("Text input")

input_box = driver.find_element(By.NAME, "my-password")

input_box.send_keys("pass")

input_box = driver.find_element(By.NAME, "my-textarea")

input_box.send_keys("texta area")

driver.find_element(By.CSS_SELECTOR, ".btn").click()


