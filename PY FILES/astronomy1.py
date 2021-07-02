# -*- coding: utf-8 -*-
"""Astronomy1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t9Wo6DyuIWEZxvGCm8onUVoev4-2tiDn
"""

import requests
import pandas as pd
import json
import datetime

cityname = ["London", "Toronto", "Rome", "Sydney"]
country = ["United Kingdom", "Canada", "Italy", "Australia"]
region = ["City of London, Greater London", "Ontario", "Lazio", "New South Wales"]


key = "5f7c9d283060480d857194323212906"

count = 0

def astro_check(json_data): #WeatherAPI site has extra sunrise https://www.weatherapi.com/docs/
  print(json_data['astronomy'])
  astro_dict = json_data['astronomy']
  properties = ["sunrise", "sunset", "moonrise", "moonset", "moon_phase", "moon_illumination"]
  i = 0


  for p in properties:
    if p == "moon_illumination":
      if int(astro_dict['astro'][p]) <= 100:
        print("PASS: moon_illumination percent value appears to be valid")
      else:
        print("FAIL: moon_illumination percent value appears to be valid")
    elif p == "moon_phase":
      moon_phase_list = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous", "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]
      i = 0
      for m in moon_phase_list:
        if m == astro_dict['astro']['moon_phase']:
          print("MOON PHASE is {} and is valid".format(m))
          break
        i = i + 1

      if i >= len(moon_phase_list):
        print("MOON PHASE {} entry appears to be INVALID".format(m))
    else:
      print("{}".format(p))
      time_stamp1 = astro_dict['astro'][p] 
      timeck(time_stamp1)

estamp_ch

# Function to check for text terms in json info
def check_name(x, keyname, name): 
  checktext = '"{}":"{}"'.format(keyname, name)
  print("Name Search Term: {}".format(checktext))
  if checktext in x:
    print("{} found in json info".format(checktext))
  else:
    print("{} not found in json info: json appears to be not valid".format(checktext))

#Function for datetime validation
def timestamp_check(timestamp1):
  if len(timestamp1) == 8:
     print(">> Timestamp DIGIT COUNT test PASS")
  else:
     print(">> Timestamp DIGIT COUNT NOT CORRECT!!!!!")

  try:
    t = datetime.datetime.strptime(timestamp1,"%H:%M %p")
    print("m: {}".format(timestamp1))
    print("PASS: Timestamp: {} is A VALID".format(timestamp1))
  except ValueError:
    print("FAIL: Timestamp: {} is INVALID".format(timestamp1))

for name in cityname:
  timezone = "http://api.weatherapi.com/v1/astronomy.json?key={}&q={}".format(key, cityname[count])
  x = requests.get(timezone)
  z = x.json()

  astro_check(z)
  #print(x.text)
  #print("** LOCALTIME: {}".format(z['location']['localtime']))
  #localtime_list = z['location']['localtime'].split(' ')

  #datetime_check(localtime_list, z['location']['localtime'])

  print("Call Status for {} call: {}".format(name, x))
  check_name(x.text, "name", cityname[count])
  check_name(x.text, "country", country[count])
  check_name(x.text, "region", region[count])
  print("___")
  count = count + 1

