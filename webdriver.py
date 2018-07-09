import os
import time
from pprint import pprint

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

BASE_DIR = os.path.dirname(__file__)

# Create a new instance of the Google driver
executable_path = os.path.join(BASE_DIR, 'drivers', 'chromedriver')
driver = WebDriver(executable_path=executable_path)

# go to the google home page
driver.get('https://www.google.com')

# find the element that's name attribute is lst-ib (the google search box)
search = driver.find_element_by_id('lst-ib')
search.send_keys('Hillsong')
search.submit()

# find the elements that's names attributes are r (the google search box)
related_search = driver.find_elements_by_class_name('r')

# running script from python with selenium to javascript
driver.execute_script("console.log('Hello from python to js')")

# search all the links that contain the word Church
links = driver.find_elements_by_partial_link_text('Church')
pprint([item.text for item in links])

# running javascript code to get all the search results
list_hillsong_search = driver.execute_script("return document.querySelectorAll('.r > a')")
pprint([item.text for item in list_hillsong_search])

# opening first link using selectors css
song_hillsong = driver.find_element_by_css_selector('.r a')
song_hillsong.click()


def enter_to_iframe_select_and_deselect_selectHTML():
    driver.get('https://www.w3schools.com/TAGs/tryit.asp?filename=tryhtml_select_multiple')

    driver.switch_to.frame("iframeResult")
    select = Select(driver.execute_script("return document.querySelector('[name=cars]')"))
    select.select_by_value("volvo")

    time.sleep(2)
    select.deselect_all()

    time.sleep(10)
    driver.close()
    driver.quit()


# closing driver and quiting
driver.close()
driver.quit()
