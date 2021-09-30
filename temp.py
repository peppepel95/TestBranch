import json
import requests
from termcolor import colored

r = requests.get('https://www.crealatuafragranza.it/api/v1/items/public?skip=0&limit=100000')
data = r.json()

partecipanti = {}
for d in data:
  #print (d['id'], d['votes_count'])
  partecipanti[d['id']] = d['votes_count']

i = 0
oldId = [1708, 443, 1649, 1645, 1653, 937, 577, 579, 412, 440, 188, 20]
for k, v in sorted(partecipanti.items(), key=lambda item: item[1], reverse=True):
  i = i + 1
  if (k == 3446 or k == 4194):
      print(colored('{0:2d}). Punti: {1:5d}\tid: {2:5d} (Noi)'.format(i, v, k), 'blue'))
  elif (k in oldId):
      print(colored('{0:2d}). Punti: {1:5d}\tid: {2:5d}'.format(i, v, k), 'yellow'))
  else:
      print('{0:2d}). Punti: {1:5d}\tid: {2:5d}'.format(i, v, k))
  if i == 30:
    break
