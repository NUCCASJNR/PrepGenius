from bs4 import BeautifulSoup
import requests

url = 'https://myschool.ng/classroom/mathematics?exam_type=jamb&exam_year=&topic=algebra'
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

question_divs = soup.find_all('div', class_='question-card')

for i, question_div in enumerate(question_divs):
    if i == 5:
        break
    question = question_div.find('div', class_='question-text').text.strip()
    print(f"Question {i+1}: {question}")
    print('-' * 50)
