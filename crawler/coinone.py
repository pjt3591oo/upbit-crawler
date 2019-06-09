import requests as rq
import datetime
from utils.t import getToday, dayMinuteCalc, converted, beautify
from random import randint
from time import sleep
import json
import os

COINTICKER = "BTC"

fileName = "coinone_"+COINTICKER+".csv"
isExist = os.path.exists('{fileName}'.format(fileName=fileName))
f = open(fileName, 'a')
print(isExist)
if not isExist:
    f.write('DT,Open,Low,High,Close,Volume,Adj_Close\n',)

def save(dataset):
  global f
  form = '{DT},{Open},{Low},{High},{Close},{Volume},{Adj_Close}\n'
  for data in dataset:
    f.write(
      form.format(
        DT=data['DT'],
        Open=data['Open'],
        Low=data['Low'],
        High=data['High'],
        Close=data['Close'],
        Volume=data['Volume'],
        Adj_Close=data['Adj_Close']
      )
    )


def start():
  TO = ''
  COINTICKER = '' # ''는 btc, 코인원은 cointicker를 소문자로 처리함
  BASE_URL = "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinone{cointicker}&type=1m&last_time={to}"
  
  while True:
    url = BASE_URL.format(to=TO, cointicker=COINTICKER)
    res = rq.get(url)
    dataset = reversed(list(res.json()['data']))

    save(dataset)

    print(url)
    print(beautify(res.json()['data'][-1]['DT']))
    print(beautify(res.json()['data'][0]['DT']))
    print(len(res.json()['data']))
    TO = int(res.json()['data'][0]['DT']) - 60000
    print('================***=================')
    # sleep(1)

  f.close()

  