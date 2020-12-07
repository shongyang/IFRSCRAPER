from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.iasplus.com/en/standards")

file = open("output1.txt", "r+")
file.truncate(0)
file.close()

elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    f = open("output1.txt", "a")
    print(elem.get_attribute("href"), file=f)
    f.close()

for num, elem in enumerate(elems, start=0):
    print("{}: {}".format(num, elem.get_attribute("href")))

with open("output1.txt") as f2:
    linesss = f2.readlines()

startaa = int(input("starting number = "))
endaa = int(input("ending number = ")) + 1
stepaa = 1

desired_lines = linesss[startaa:endaa:stepaa]

file = open("output2.txt", "r+")
file.truncate(0)
file.close()

for desired_line in desired_lines:
    f = open("output2.txt", "a")
    print(desired_line, file=f)
    f.close()

with open("output2.txt") as infile, open("output2a.txt", "w") as outfile:
    for line in infile:
        if not line.strip():
            continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output

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