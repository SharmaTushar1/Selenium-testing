'''
- Wasn't able to solve this problem. 
- This is the halfway code for it. I have to figure out a way on how to get the latitude and longitude out of the page even though there is no address or other thing mentioned. We do have the location but that won't be the coordinates of the restaurant itself.

'''

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://www.bigbasket.com/'
driver = webdriver.Chrome()
driver.get(url)

# Wait for the page to load
driver.implicitly_wait(10)

# Get the page's HTML
html = driver.page_source

# Assuming you have the HTML of the page stored in a variable called 'html'
soup = BeautifulSoup(html, 'html.parser')
# Use BeautifulSoup's methods to find and extract data from the HTML

show_categories_button = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbar"]/ul/li[1]/a')))

# click the button to show all categories

show_categories_button.click()

category_list = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navBarMegaNav"]'))
)
categories = category_list.find_elements(By.XPATH, './/li/a')
for category in categories[:5]: # getting the first five for now
  actions = ActionChains(driver)
  actions.move_to_element(category).perform()
  
  category_id = category.get_attribute('data-submenu-id')

  print("category_id => ", category_id)

  # Wait for the inner content to load
  driver.implicitly_wait(10)

  # Find all inner elements within the current category
  xpath = f'//*[@id="{category_id}"]/div/div/div[1]/ul/'
  inner_elements = category.find_elements(By.XPATH, xpath)

  print(inner_elements)

  # Loop over the inner elements and extract data as needed
  for inner_element in inner_elements:
    print(inner_element.text)
    
    
time.sleep(100000)
# category_links = []
# for category in categories[:5]: 
#     subcategories = category.find_next()

# url = 'https://www.bigbasket.com/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

# # Find and extract categories and subcategories using BeautifulSoup methods
# categories = soup.find_all('a', class_='category-name')

# category_links = []
# for category in categories[:5]:  # To get 5 categories
#     subcategories = category.find_next('div').find_all('a')
#     for subcategory in subcategories:
#         category_links.append(subcategory['href'])
