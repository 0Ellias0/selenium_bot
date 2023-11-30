# Selenium 
from selenium import webdriver

# PATH = r"C:\Users\hpalm\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://github.com/0Ellias0")

print(driver.title)

