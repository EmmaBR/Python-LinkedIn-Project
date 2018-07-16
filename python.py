from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#imported for tabs
from selenium.webdriver.common.action_chains import ActionChains
# imported to wait for element to appear before performing an action
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome() 

# make sure to hard code your job interest in title variable below
# also hard code your login information (email and password)
# to stop running the code: in the terminal type type contol + c (if on a mac)

title = "" 
title.replace(' ', '%20')

page = driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords={}&location=United%20States&locationId=us%3A0'.format(title))

def login():
	
   #userEmail = '' 
   #userPassword = ''
   
   signIn = '//*[@id="mobile-chrome"]/nav/div/ul/li[1]/a'
   driver.find_element_by_xpath(signIn).click()
  
   formEmail = '//*[@id="session_key-login"]'
   formPassword = '//*[@id="session_password-login"]'
   formSubmit = '//*[@id="btn-primary"]'

   form = WebDriverWait(driver, 20).until(
       EC.element_to_be_clickable((By.XPATH, formEmail))
   )

   driver.find_element_by_xpath(formEmail).send_keys(userEmail)
   driver.find_element_by_xpath(formPassword).send_keys(userPassword)
   driver.find_element_by_xpath(formSubmit).click()

login()

time.sleep(2) # added because page hasn't loaded, can't load link
elements = driver.find_elements_by_css_selector('a')
validJobs = []

for e in elements:
   if '/jobs/view/' in str(e.get_attribute('href')):
       validJobs.append(str(e.get_attribute('href')))

def userProfile():
   time.sleep(3)

   try:
      easyApplyButton = driver.find_element_by_css_selector("button.jobs-s-apply__button")
      easyApplyButton.click()
   except NoSuchElementException:
      easyApplyButton2 = driver.find_element_by_css_selector("button.jobs-apply-form__submit-button")
      easyApplyButton2.click()
   

   N = 8  # number of times you want to press TAB

   actions = ActionChains(driver) 
   for i in range(N):
       actions = actions.send_keys(Keys.TAB)
   actions = actions.send_keys(Keys.ENTER)
   actions.perform()

for i in range(0, len(validJobs), 2): #0
   driver.get(validJobs[i])
   userProfile()

