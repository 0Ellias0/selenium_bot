# Selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 

# PATH = r"C:\Users\hpalm\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.mercadolibre.com.co/")
print(driver.title)

search = driver.find_element("name","as_word")
search.send_keys("Logitech MX Master 3s")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()

