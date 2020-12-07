from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="chromedriver.exe")

file = open("finalout.txt", "r+")
file.truncate(0)
file.close()

with open("output2a.txt", "r") as bible:
    # with open('2.LINKSHERE.txt', 'r') as bible:
    for b in bible:
        driver.get(b)
        time.sleep(1)
        # elements = driver.find_elements_by_class_name("div.col-md-7")
        elements = driver.find_elements_by_css_selector("#mainPageBody")
        for element in elements:
            f = open("finalout.txt", "a")
            print(element.text, file=f)
            f.close()
        time.sleep(1)


driver.quit()
