pip install bs4
import requests
import re
import time
from bs4 import BeautifulSoup

while(True):
  result = requests.get('https://lk.msu.ru/course/view?id=3393')
  soup = BeautifulSoup(result.text, 'lxml')
  box = soup.find('div', class_='well')
  destination = soup.find(string=re.compile("/ 500")).strip()
  if destination == "500 / 500":
    time.sleep(600)
    continue
  else: #запускаем событие отправки e-mail в случае обнаружения изменения
    try:
      resp = requests.get('https://eoxb0trpimm0lf2.m.pipedream.net')
      print(time.strftime("%H:%M:%S", time.localtime()), ' no request exception, request status code: ', resp.status_code, file = open("mfk-checker-success-log.txt", "a"))
    except requests.exceptions.RequestException as e:
      print(time.strftime("%H:%M:%S", time.localtime()), ' request exception with reason: ', e.reason, file = open("mfk-checker-error-log.txt", "a"))
      break
