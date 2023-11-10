
from urllib.parse import quote

def url_encode(input_text):
  # input_text = input_text.split()
  # input_text = "-".join(input_text)
  # print(input_text)
  return quote(input_text)