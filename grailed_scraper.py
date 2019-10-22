import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException

import json
import os
from setup import setup

filename = 'search_terms.json'

if not os.path.isfile(filename):
    setup()

with open(filename) as json_file:
    data = json.load(json_file)

    # options = webdriver.ChromeOptions()
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    url = 'https://www.grailed.com'
    driver.get(url)
    driver.implicitly_wait(10)

    search_bar = driver.find_element_by_id('globalheader_search')

    print('Searching for ' + data['brand'] + ' ...')
    search_bar.send_keys(data['brand'])
    search_bar.send_keys(Keys.ENTER)

    try:
        click_price = WebDriverWait(driver, 5).until (
        EC.presence_of_element_located((By.XPATH, '//*[@class="-collapsible-target"]//*[text()="Price"]')))
        click_price.click()
        set_price = WebDriverWait(driver, 5).until (
        EC.presence_of_element_located((By.XPATH, '//*[@title="Max Price"]')))
        set_price.send_keys(data['price'])
        set_price.send_keys(Keys.ENTER)

    except ElementClickInterceptedException:
        print("couldn't set price")

    except ElementNotInteractableException:
        print("idk chief")

    try:
        click_category = WebDriverWait(driver, 5).until (
        EC.presence_of_element_located((By.XPATH, '//*[@class="Filters--GroupHeader"]//*[text()="Bottoms"]')))
        click_category.click()
        set_size = WebDriverWait(driver, 5).until (
        EC.presence_of_element_located((By.ID, 'FilterToggle_checkbox_bottoms.' + data['waist_size'] + '_' + data['waist_size'])))
        set_size.click()
    except ElementClickInterceptedException:
        print("couldn't set bottoms size")

    try:
        click_category = WebDriverWait(driver, 5).until (
        EC.presence_of_element_located((By.XPATH, '//*[@class="Filters--GroupHeader"]//*[text()="Tops"]')))
        click_category.click()
        set_size = WebDriverWait(driver, 5).until (
        EC.presence_of_element_located((By.ID, 'FilterToggle_checkbox_tops.' + data['shirt_size'].lower() + '_' + data['shirt_size'] + '/52-54')))
        set_size.click()
    except ElementClickInterceptedException:
        print("couldn't set shirt size")

    try:
        click_category = WebDriverWait(driver, 5).until (
        EC.presence_of_element_located((By.XPATH, '//*[@class="Filters--GroupHeader"]//*[text()="Footwear"]')))
        click_category.click()
        set_size = WebDriverWait(driver, 5).until (
        EC.presence_of_element_located((By.ID, 'FilterToggle_checkbox_footwear.' + data['shoe_size'] + '_' + data['shoe_size'])))
        set_size.click()
    except ElementClickInterceptedException:
        print("couldn't set shoe size")

    click_listing = driver.find_elements_by_class_name('feed-item')
    click_listing[0].click()