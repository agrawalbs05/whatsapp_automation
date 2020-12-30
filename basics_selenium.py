# install selenium on same path pip3 isstall selenium
# Down load web driver for browser ex-chrome
from selenium import webdriver
browser = webdriver.Chrome("/Applications/Android/WA_automation/chromedriver")  #run chrome,specify web driver path
browser.get("https://www.selenium.dev/") # the opened empty browser is loaded with this website
download_button = browser.find_element_by_link_text("Downloads")
download_button.click()
#search = browser.find_elements_by_id("gsc-i-id1") #Not working #to get ID right click on that element>>Inspect>>cursor arrow and get ID
#search.send_keys('Downloads')