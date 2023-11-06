from bs4 import BeautifulSoup
import requests

url = "https://imada.sdu.dk/u/kslarsen/dm565/E04.php"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

"""all exercise questions that have subquestions (all entries in an `ol`-tag that has `ol`-subtags),"""
files = soup.find_all('a', href=True)
for file in files:
    print(file['href'])


questions = soup.find_all('ol')
for question in questions:
    if question.find('ol'):
        print(question)

subquestions = soup.find_all('ol')
for subquestion in subquestions:
    if subquestion.find(subquestion)

