import json
import csv

# JSON 파일 읽기
with open('fastcampus.json', 'r') as json_file:
    data = json.load(json_file)

# CSV 파일로 쓰기
with open('fastcampus_data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # CSV 파일의 헤더 작성
    header = data[0].keys()
    csv_writer.writerow(header)

    # 데이터 작성
    for item in data:
        csv_writer.writerow(item.values())

print("JSON 파일을 CSV 파일로 변환했습니다.")
