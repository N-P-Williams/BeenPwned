# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 15:55:46 2018

@author: Nic
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

hiddenCheck = "hidden"

driver = webdriver.Firefox()  # Optional argument, if not specified will search path.
driver.get("https://haveibeenpwned.com")
time.sleep(1) # Let the user actually see something!
print("Please enter an email you wish to check")
email = input()
insertField = driver.find_element_by_id("Account")
#
insertField.send_keys(email)
insertField.send_keys(Keys.ENTER)
try:
    outcome = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID,"noPwnage")))
    print(outcome.text)

except TimeoutException:
   outcome = driver.find_element_by_id("pwnedWebsitesContainer")
   print(outcome.text)
   time.sleep(5)

print("Please enter an password you would like to check")
password = input()
time.sleep(5)
driver.find_element_by_xpath('//a[@href="/Passwords"]').click() #clciiks on the box on the pwnded homepage to take you to the passwords page, works
passwordinsert = driver.find_element_by_id('searchContainer').click()
passwordinsert.send_keys(password)
passwordinsert.send_keys(Keys.ENTER)