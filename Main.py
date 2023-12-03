# Selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# PATH = r"C:\Users\hpalm\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome()


driver.get("https://www.mercadolibre.com.co/")
print(driver.title)

search = driver.find_element("name","as_word")
search.send_keys("Logitech MX Master 3s")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "andes-money-amount__fraction"))
    )
    print(main.text)
except:
    driver.quit()


time.sleep(5)

driver.quit()

