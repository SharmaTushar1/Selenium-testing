from geopy.geocoders import Nominatim
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://food.grab.com/ph/en/')

# time.sleep(60)

location_input = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="location-input"]'))
)

location_input.send_keys('Okada Manila - New Seaside Drive, Parañaque City, Tambo, Paranaque City, Metro Manila, 1701, National Capital Region (Ncr), Philippines')

# search button

search_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div[3]/div/button')))

time.sleep(10)

# search for the location

search_button.click()

time.sleep(10)

# scroll endlessly to load all restaurants.

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  time.sleep(10)
  new_height = driver.execute_script("return document.body.scrollHeight")

  # all content has been loaded so height has not changed.

  if new_height == last_height:
    break
  else:
    last_height = new_height

restaurant_elements = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div[5]/div/div/div[4]/div/div/div/div[171]')))

# Remaining code should come here.

time.sleep(100000000)





