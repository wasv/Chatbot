#!/usr/bin/env python
import urllib
import json
import datetime
from sys import argv

ZIPCODE="01010"
day = argv[1].upper()

try:
  if day == 'TODAY':
    day = 0
  elif day == 'TOMORROW':
    day = 1
  else:
    weekday = (datetime.datetime.today().isoweekday())%7
    week  = ['SUNDAY', 
	      'MONDAY', 
	      'TUESDAY', 
	      'WEDNESDAY', 
	      'THURSDAY',  
	      'FRIDAY', 
	      'SATURDAY']
    day = week.index(day)+weekday+1
    
  JSONresponse=urllib.urlopen('http://api.wunderground.com/api/56ecf7782fa3d07a/forecast10day/q/'+ZIPCODE+'.json').read()
  weatherReport=json.loads(JSONresponse)
  weatherReport=weatherReport['forecast']
  if day == 0:
    print "Today, it will be",weatherReport['simpleforecast']['forecastday'][day]['conditions'],"with a high of",weatherReport['simpleforecast']['forecastday'][day]['high']['fahrenheit'],"degrees and a low of",weatherReport['simpleforecast']['forecastday'][day]['low']['fahrenheit'],"degrees."
  else:
    print weatherReport['simpleforecast']['forecastday'][day]['date']['weekday'],"it will be",weatherReport['simpleforecast']['forecastday'][day]['conditions'],"with a high of",weatherReport['simpleforecast']['forecastday'][day]['high']['fahrenheit'],"degrees and a low of",weatherReport['simpleforecast']['forecastday'][day]['low']['fahrenheit'],"degrees."
except:
  print "Something went wrong"
