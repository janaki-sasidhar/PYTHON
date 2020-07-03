#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests,pprint
api=""
url="https://api.telegram.org/bot"+api+""

response=requests.get("https://api.covid19india.org/state_district_wise.json").json()
num=1
for i in response.keys():
    print(f'{num}. {i}')
    num+=1
number=int(input("Enter the number"))
city_name=list(response.keys())[number-1]
num2=1
for i in response[city_name]['districtData'].keys():
    print(f'{num2}. {i}')
    num2+=1
number2=int(input("Enter the number"))
dist_name=list(response[city_name]['districtData'].keys())[number2-1]
result=response[city_name]['districtData'][dist_name]
print(f'''ACTIVE - {result['active']}
CONFIRMED - {result['confirmed']}
DECEASED - {result['deceased']}
RECOVERED-{result['recovered']}''')

    
