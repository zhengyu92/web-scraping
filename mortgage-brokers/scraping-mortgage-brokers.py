import time
from bs4 import BeautifulSoup
from selenium import webdriver as we
from selenium.webdriver.support.ui import Select

url = "http://mortgage-brokers.credio.com/"
browser = we.Chrome("/Users/zhengyu/Desktop/chromedriver")
browser.get(url)

# selecting the commercial filter
# contents might not get loaded in first try
for i in range(10):
    try:
        browser.find_element_by_xpath(".//*[contains(text(), 'Commercial')]").click()
        break
    except NoSuchElementException as e:
        print('retry in 1s.')
        time.sleep(1)
else:
    raise e

#selecting the 100 per page from dropdownbox
select = Select(browser.find_element_by_id('num_results_val'))
select.select_by_visible_text('100 per page') 
select.select_by_value('100')

content = browser.page_source
soup = BeautifulSoup(content, "html5lib")

# the commands are stored:
# <div id=srp-results>
#             <tr[class==srp-row>
#              </table>
# <</div>
results = soup.select("div[id=srp-results] tr[class==srp-row]")
last = len(results)

# PRINTING TO CHECK
# for i in range(0,last):
#     print results[i].h3.text

#store names in a list
names = [result.h3.text for result in results]

ps = soup.find_all("p", class_="md-p")

# even numbers index are companies, odd numbers index are locations
# use slice to spearate two lists
companies, locations = ps[0::2], ps[1::2]
company = []
location = []
for i in range(0,last):
    company.insert(i, companies[i].text)
    # print companies[i].text
print "\n"
for j in range(0,last):
    location.insert(j, locations[j].text)
    # print locations[j].text

numbers = soup.find_all("a", class_="phone_number")
number = []
for i in range(0,last):
    if " x 100" in numbers[i].text:
        numbers[i] = numbers[i].text.replace(" x 100", "")
        number.insert(i, numbers[i])
        #print numbers[i]
    elif " x 201" in numbers[i].text:
        numbers[i] = numbers[i].text.replace(" x 201", "")
        number.insert(i, numbers[i])
        #print numbers[i]
    else:
        numbers[i] = numbers[i].text
        number.insert(i, numbers[i])
        #print numbers[i]

for i in range(0, last):
    print("{} -- {} -- {} -- {}".format(names[i], company[i], location[i], number[i]))

listOfProfiles = [(names[i], company[i], location[i], number[i]) for i in range(0,last)]
print listOfProfiles

with open("listOfProfiles.csv", "w") as fw:
    for listOfProfile in listOfProfiles:
        print(listOfProfile[0]+" -- " + listOfProfile[1] + " -- " + listOfProfile[2] + " -- " + listOfProfile[3] + "\n\n")
        fw.write(listOfProfile[0] + " - " + listOfProfile[1] + " -- " + listOfProfile[2] + " -- " + listOfProfile[3] + "\n\n")
