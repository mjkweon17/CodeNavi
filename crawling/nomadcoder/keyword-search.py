import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from course_detail_search import course_detail_search
import json
import os

course_info_list = []


def keyword_search():
  base_url = "https://nomadcoders.co/courses"
  search_query = base_url
  response = requests.get(search_query)
  soup = BeautifulSoup(response.text, 'html.parser')
  
  # 강의 제목
  course_titles = soup.find_all('h3', class_='text-xl')
  for course_title in course_titles:
    print(course_title.text.strip())
      
  # 강사
  instructors = "니콜라스"
  
  # 강의 링크
  courses_card_list_body = soup.find_all('div', class_= 'text-center')
  for i in courses_card_list_body:
    hrefs = courses_card_list_body.find('a')["href"]
    print(hrefs)
  
  
  
  for i in range(len(course_titles)):
    course_info = {}
    
    if course_titles[i]:
      course_info['title'] = course_titles[i].text.strip()
      course_info['keyword'] = keyword
      
    if hrefs[i]:
      
      course_info['link'] = hrefs[i]['href']
    if instructors[i]:
      course_info['lecturer'] = instructors[i].text.strip()

    if course_prices[i]:
      course_price = course_prices[i].text.strip()
      course_price = course_price.replace('₩', '')
      course_info['price'] = course_price
      

    course_info_list.append(course_info)


result = keyword_search()

print(result)


if not os.path.exists(folder_path):
    os.makedirs(folder_path)
  

json_file_path = os.path.join("./", "inflearn_data12.json")

with open(json_file_path, 'w', encoding='utf-8') as json_file:
  json.dump(result, json_file)


print("함수 결과를 파일로 저장했습니다.")

