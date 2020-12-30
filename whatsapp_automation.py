# whatsapp automation
#pip3 install selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

browser = webdriver.Chrome("/Applications/Android/WA_automation/chromedriver")  #run chrome,specify web driver path
browser.get("https://web.whatsapp.com") #Open whatsapp with QA code
wait = WebDriverWait(browser,600) # Scan QR code with mobile phone

target = '"Gary"'
#file_path = "/Applications/Android/WA_automation/ghost.jpg"
file_path = input("Please enter the file path(ex-/Applications/Android/WA_automation/XXX.jpg): ")
#string = "WA automation testing!!!!" 
string = input("Please enter the text to be sent:  ")
x_arg = '//span[contains(@title, ' + target +')]'  #WA is end-to-end encrypted so will not get ID #span is method or tag 
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box = browser.find_element_by_class_name('DuUXI')

for i in range(10):
    input_box.send_keys(string + Keys.ENTER)

attachment_section = browser.find_element_by_xpath('//div[@title = "Attach"]')
attachment_section.click()

image_box = browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(file_path)

sleep(3)

send_button =browser.find_element_by_xpath('//span[@data-icon="send"]') 
send_button.click()
