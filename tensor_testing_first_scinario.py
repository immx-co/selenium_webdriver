from selenium import webdriver
import time
from selenium.webdriver.common.by import By


if __name__ == "__main__":
    link = "https://sbis.ru/"
    browser = webdriver.Chrome()
    browser.get(link)

    contacts_button = browser.find_element(By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a').click()

    time.sleep(10)
    browser.quit()