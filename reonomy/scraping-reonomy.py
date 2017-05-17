# coding: utf-8

from bs4 import BeautifulSoup
import requests

url = "https://reonomy.com/about-us/"
r = requests.get(url)
# check status code for any error
r.status_code

# save page source to Reonomy.html
with open("Reonomy.html", "r") as f:
    content = f.read()

soup = BeautifulSoup(content, "html5lib")


# to find the class *desc_wrapper* and its parent *div*
divs = soup.find_all("div", class_="desc_wrapper")

# divs is a list of 4
divs[0].h4.text

# to print all names, use iteration
for div in divs:
    print(div.h4.text)

# save the 4 names in a list
full_names = [div.h4.text for div in divs]for i

# write the names in a csv file
with open("names.csv", "w") as fw:
    for fullname in full_names:
        first, last = fullname.split(" ")
        fw.write("{},{}\n".format(first, last))

# names are written into names.csv
ps = soup.find_all("p", class_="subtitle")

for p in ps:
    print(p.text)

subtitles = [p.text for p in ps]

for i in range(len(ps)):
    print("{} - {}".format(full_names[i], subtitles[i]))

# a = [["rich", "ceo"], ["chris", "cto"]]
# print a

a = [full_names, subtitles]
# print a

bl = [(full_names[i], subtitles[i]) for i in range(len(full_names))]
# print bl

# for (full_names[i], subtitles[i]) it will be tuple - meaning it is immunable and cannot be changed. a constant
# can still put as a list, just use [ful...i]] open and close brackets
with open("nameAndSubtitles.csv", "w") as fw2:
    for biglist in bl:
        print(biglist[0]+", " + biglist[1])
        fw2.write(biglist[0] + ", " + biglist[1] + "\n")

# tuple for description
descs = soup.find_all("div", class_="desc")

for desc in descs:
    print desc.text

descriptions = [desc.text for desc in descs]

for i in range(len(descs)):
    print("{} - {} - {}".format(full_names[i], subtitles[i], descriptions[i]))

listOfThree = [(full_names[i], subtitles[i], descriptions[i]) for i in range(len(full_names))]
print listOfThree

with open("listOfThree.csv", "w") as fw3:
    for listOfThrees in listOfThree:
        print(listOfThrees[0]+"- " + listOfThrees[1] + ": " + listOfThrees[2] + "\n\n")
        fw3.write(listOfThrees[0] + "- " + listOfThrees[1] + ": " + listOfThrees[2] + "\n\n")
