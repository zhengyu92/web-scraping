# To scrape data (profiles) from the SIOR website
#
# pip install regex
# pip install pandas
# pip install beautifulsoup4
# pip install selenium
# Install chromedriver

from bs4 import BeautifulSoup
import os
import pandas as pd
import re
import sys
import time
from selenium import webdriver as we

#use chromedriver to open up a browser
browser = we.Chrome("/Users/zhengyu92/Desktop/chromedriver")
#get the profile website
browser.get('http://www.sior.com/find-an-sior-member/find-an-individual-member/?search=F5AD18DC-2181-8ECE-8DE1-077D21689253')

#scroll to the bottom the document
#scrolling will stop at the last name starting at G, double-click the browser to continue
#inspect the browser once it reaches the bottom
for each in range(0,100000):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

content = browser.page_source
soup = BeautifulSoup(content, "html5lib")

# the commands are stored:
# <div id=results-wrapper>
#             <div[class==team-box]>
#              (PROFILES)
#              </div>
# <</div>
results = soup.select("div[id=results-wrapper] div[class==team-box]")
last = len(results)

#start scraping
profiles = []

#tags as shown below when you inspect the page
for i in range(0, last):
    name = results[i].select("div[class=row]")[1].select("a[data-bind]")[0].text
    firm = results[i].select("div[class=row]")[1].select("span[data-bind]")[0].text
    location = results[i].select("div[class=row]")[1].select("p")[0].text
    market = results[i].select("div[class=row]")[1].select("p")[1].text
    specialty = results[i].select("div[class=row]")[1].select("p")[2].text
    membership = results[i].select("div[class=row]")[1].select("i")[0].text
    phone = results[i].select("div[class=row]")[1].select("div")[2].text
    email = results[i].select("div[class=row]")[1].select("a[data-bind]")[-1]
    practice = results[i].select("div[class=row]")[2].text
    #Create a tuple for each profile 
    profiles.append((name,firm,location,market,specialty,membership,phone,email,practice))

df = pd.DataFrame(profiles,columns=["Name","Company","Location","Market","Specialty Type","Membership Since","Contact Number","Email","Area of Practice"])

#Data cleaning
##Strip away ",SIOR,...."
df["Name"] = df["Name"].str.split(",").apply(lambda x: x[0])
##Strip away "\n" and "Market: "
df["Market"] = df["Market"].str.replace(r'[\n\(\)]','').str.split(":").apply(lambda x: x[1])
##Strip away "\n" and "Specialty Type: "
df["Specialty Type"] = df["Specialty Type"].str.replace(r'[\n\(\)]','').str.split(":").apply(lambda x: x[1])
##Strip away "Member Since: "
##regex means anything that is NOT 0-9
df["Membership Since"] = df["Membership Since"].str.replace(r'[^0-9]','')
##Strip away anything that is NOT a digit, fullstop, plus, or brackets
df["Contact Number"] = df["Contact Number"].str.replace(r'[^0-9\.\+\(\)]','')

##update the email in pandas through iteration
for index, row in df.iterrows():
    href = row["Email"]["href"]
    df["Email"].iloc[index] = href[href.find(":")+1 : href.rfind("?")]
##Strip away "\n", "\" and "Area of Practive: "
df["Area of Practice"] = df["Area of Practice"].str.replace(r'[\n\(\)]','').str.split(":").apply(lambda x: x[1])

#to tackle the ascii code error
reload(sys)
sys.setdefaultencoding('UTF8')

#write to excel with pandas
writer = pd.ExcelWriter("SIOR Investors Profiles.xlsx")
df.to_excel(writer, encoding="utf-8")
writer.save()
