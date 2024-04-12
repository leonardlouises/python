from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\Google\chromedriver.exe"

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")
web_element = driver.find_element(By.NAME, 'search_query')
web_element.send_keys("curso python" + Keys.ENTER)
time.sleep(10)
print(driver.title)
driver.quit()