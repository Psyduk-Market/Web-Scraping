from bs4 import BeautifulSoup
from selenium import webdriver
import selenium as se
from selenium.webdriver.chrome.options import Options

# This is the temporary url **** Need to make it dynamic
url = "https://www.realestate.co.nz/residential/sale?by=featured&lct=d225&maxba=2&maxbe=4&maxp=1400000&ql=80&scat=1"

# Component to fetch elements headless (expanded html)
options = se.webdriver.ChromeOptions()                              # weddriver library
options.add_argument('headless')                                    # Type of fetching = headless
driver = se.webdriver.Chrome('/Users/Thyme/chromedriver')           # PATH for chromedriver without fetching data will fail
driver.get(url)
data = driver.page_source
soup = BeautifulSoup(data, 'html.parser')                           # Using name soup just to respect its library
houses = str(soup)                                                  # transform bs4 type to string
houses = houses.split("\n")                                         # Extract each lines into a list

# Realstate.co.nz

print("**********")

house_numbers = []
numbers = []
http_head = "https://www.realestate.co.nz/"
http_houses = []
# Extract all lines of element that contains house ID
for house in houses:
    if "id=\"orbit-" in house:
        house_numbers.append(house)

for number in house_numbers:
    pos = number.index("id=\"orbit-")
    result = number[pos+10:pos+17]
    if result not in numbers:
        numbers.append(result)

# print(numbers)
# print(len(numbers))

for number in numbers:
    http = http_head + str(number)
    http_houses.append(http)

print(http_houses)


# After first page http will adds "qo=80" the number represent total number houses shown start counting from second page
# Eg, first page "", second page "qo=80", third page "qo=160", fourth page "qo=240" and so on
# On the last page, if the numbers of houses less than 80 the number of increment will remain constant
# 2*(n-1) where "n" is number of page
# bbb = "https://www.realestate.co.nz/residential/sale?by=featured&lct=d225&maxba=2&maxbe=4&maxp=1400000&ql=80&scat=1"
# aaa = "https://www.realestate.co.nz/residential/sale?by=featured&lct=d225&maxba=2&maxbe=4&maxp=1400000&ql=80&qo=80&scat=1"

