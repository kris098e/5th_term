from bs4 import BeautifulSoup
import requests

url = "https://imada.sdu.dk/u/kslarsen/dm565/E04.php"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# find_all is your best friend in beuatiful soup
files = soup.find_all('a', href=True)
for file in files:
    print(file['href'])

#  all exercise questions that have subquestions (all entries in an `ol`-tag that has `ol`-subtags)
all_li = soup.find_all('li') # an li must be inside ol
for tag in all_li:
    li_child = tag.findChildren('ol') # if it has another unordered list
    if len(li_child):
        print(tag) # print original

# all the subquestions in exercises (all entries that have a parent that is an `li`-tag inside an `ol`-tag)
all_ol = soup.find_all("ol")
for tag in all_ol:
    if tag.parent.name == "li":
        print(tag)

# all 2nd subquestions
all_ol = soup.find_all("ol")
for tag in all_ol:
    if tag.parent.name == "li":
        sub_q = tag.findChildren("li")
        if len(sub_q) > 1:
            print(sub_q[1])

# all `li`-tags containing the word "Using"
for tag in all_li:
    if "Using" in tag.get_text():
        print(tag)
        print() #new line

# all texts in `code`-tags.
all_code = soup.find_all("code")
for tag in all_code:
    print(tag.string)
