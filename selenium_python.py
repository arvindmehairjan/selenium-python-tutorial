from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Open Chrome Browser using Chromedriver
driver = webdriver.Chrome("chromedriver.exe")

# Change browser window
driver.set_window_size(1080, 1080)

# Navigate to python.org
driver.get("https://www.python.org/")
time.sleep(3)

# Enter text search bar
enter_searchbar = driver.find_element_by_id("id-search-field")
enter_searchbar.send_keys("loops")

# Click on the button to display results
press_enter = driver.find_element_by_xpath("//button[normalize-space()='GO']")
press_enter.send_keys(Keys.ENTER)

time.sleep(3)

# Scroll down using Page_Down key
scroll_down = driver.find_element_by_tag_name('body')
scroll_down.send_keys(Keys.PAGE_DOWN)

time.sleep(3)

# Move backwards in the browser history
driver.back()

# Wait for 2 seconds
time.sleep(2)

# Move forwards in the browser history
driver.forward()

# Wait for 2 seconds
time.sleep(2)

# Close Browser 
driver.close()