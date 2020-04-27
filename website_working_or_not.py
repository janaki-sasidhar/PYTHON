#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:00:22 2020

@author: sasidhar
"""

import requests
print("Enter the number of websites you want to check if they are working")
num=int(input('>'))
website_list=[]
working_site=[]
non_working_site={}
for i in range(num):
    print(f"Enter the website {i+1}")
    hi=input('>')
    website_list.append(hi)
for i in website_list:
    try:
        resp=requests.get(i)
        print(f"website {i} is working")
        working_site.append(i)
               
    except Exception as exp:
        non_working_site[i]=exp
print(working_site)
print(non_working_site)
