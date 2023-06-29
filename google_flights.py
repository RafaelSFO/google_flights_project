# %%
## Importing libraries used in this project
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import pandas as pd
import time
# %%

## Creating a instance of Google Chrome
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.maximize_window()

## Passing the link of Google Flights
google_flights = 'https://www.google.com/travel/flights?hl=pt-BR'
browser.get(google_flights)
# %%

## By default the site comes with round-trip mode selected, but you can choose among the options
mode_menu = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[1]'
browser.find_element(By.XPATH, mode_menu).click()
mode = {'one-way': 2, 'round-trip': 1, 'multi-city': 3}
mode_xpath = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[{}]'.format(mode['round-trip'])
browser.find_element(By.XPATH, mode_xpath).click()
# %%

# Choosing how many people will travel 
#people_buttom = '//*[@id="ow42"]/div[1]/div/button/span' # Open menu
people_buttom = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div/button/span'
browser.find_element(By.XPATH, people_buttom).click()
add_adult = '//*[@id="i10-1"]/div/span[3]/button' # Buttom to add more adults
browser.find_element(By.XPATH, add_adult).click()
continue_buttom = '//*[@id="ow38"]/div[2]/div[2]/button[1]'
# Button to continue searching in the site
browser.find_element(By.XPATH, continue_buttom).click()
# %%

# Opening travel class menu
browser.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[1]').click()
travel_class = {'economy': 1, 'premium_economy': 2, 'business': 3, 'first': 4}
travel_class_xpath = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[3]/div/div/div/div[2]/ul/li[{}]'.format(travel_class['premium_economy'])

browser.find_element(By.XPATH, travel_class_xpath).click()
# %%
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(browser)
# %%
# São Paulo comes as default because of my location, then I will clean the input
from_city = '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input'
browser.find_element(By.XPATH, from_city).clear()
browser.find_element(By.XPATH, from_city).send_keys('Salvador')
# %%
list_box = browser.find_element(By.CLASS_NAME, 'DFGgtd')
list_box.id

# %%
site = soup(browser.page_source, 'html.parser')

# %%
site.find_all(class_='DFGgtd')
# %%
browser.find_element(By.XPATH, '//*[@id="c28"]').click()

# %%
actions.send_keys(Keys.ENTER)
# %%
browser.find_element(By.XPATH, from_city).send_keys(Keys.ENTER)

# %%
to_city = '/html/body/c-wiz[4]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input'
browser.find_element(By.XPATH, to_city).clear()
browser.find_element(By.XPATH, to_city).send_keys('Cidade do Cabo')
# %%
