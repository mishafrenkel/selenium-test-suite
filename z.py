from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("http://www.gap.com")


try:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "universal-modal__close-button")))
    element.click()
    driver.get_screenshot_as_file('modal-removed.png')
    driver.save_screenshot('modal-removed.png')
    elem =  wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "divisionLink")))
    elem.click()
    driver.get_screenshot_as_file('denim.png')
    driver.save_screenshot('denim.png')
    e =  wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mkt-svg-overlay__link")))
    e.click()
    driver.get_screenshot_as_file('products.png')
    driver.save_screenshot('products.png')
finally:
    driver.quit()
