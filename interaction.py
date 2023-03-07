from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\development\chromedriver.exe")

while True:
    driver.get("https://orteil.dashnet.org/cookieclicker")
    search = driver.find_element(By.ID,"bigCookie")
    search.click()
# search_icon = driver.find_element(By.CSS_SELECTOR,"cds-button")
# search_icon.click()



