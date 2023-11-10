import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def course_detail_search(course_link):
  base_url = "https://www.inflearn.com"
  search_query = base_url + quote(course_link)  # base + course_link
  
  response = requests.get(search_query)
  soup = BeautifulSoup(response.text, 'html.parser')
  
  # 총 강의 시간
  course_time = soup.find('span', class_= 'cd-curriculum__sub-title')
  course_time_join = ''
  if course_time:
    course_time = soup.find('span', class_= 'cd-curriculum__sub-title').text.strip().split()
    course_time_join = "".join(course_time)
    course_time_join = course_time_join.split('˙')
    if len(course_time_join) > 1:
      course_time_join = course_time_join[1]
      course_time_join = course_time_join.split('의')[0]
    else:
      course_time_join = "".join(course_time_join)
    
  else:
    course_time = ''
  
  
  #강의 요약 제목
  course_description_title = soup.find('div', class_= 'cd-body__title')
  if course_description_title:
    course_description_title = course_description_title.text.strip()
    course_description_title = course_description_title.replace("\n", "")
  else:
    course_description_title = ''
  
  

  # 강의 요약 설명
  course_description_content = soup.find('p', class_= 'cd-body__description')
  if course_description_content:
    course_description_content = course_description_content.text.strip()
  else: 
    course_description_content = ''
  
  
  # 할인 가격
  course_discount_price = soup.find('div', class_= 'cd-floating__price')
  # 할인 안하는 강의도 있음
  if len(course_discount_price.find_all('h4')) > 1:
    course_discount_price = course_discount_price.find_all('h4')[1].text.strip()
  else: 
    course_discount_price = ''
    
  # 이미지 소스 링크
  img_element = soup.find('img')
  src = img_element.get('src')
  if src:
    pass
  else:
    src = ''
  
  # 기술 스택 태그
  course_stacks = soup.find('div', class_= 'cd-header__tags')
  a_tags = course_stacks.find_all('a')
  if len(a_tags) < 1:
    course_stacks = ''
  else:
    course_stacks = str([tag.text for tag in a_tags])
  
  return course_time_join, course_description_title, course_description_content, course_discount_price, course_stacks, src

