from selenium import webdriver
import time

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
click_button = driver.find_element_by_id("submit")
click_button.click()

time.sleep(3)

# Close Browser 
driver.close()