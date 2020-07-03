import requests,pprint
response=requests.get("https://api.covid19api.com/summary").json()
country=input("Enter country...").capitalize()
for i in response['Countries']:
    if i['Country'].find(country)!=-1:
        pprint.pprint(i)
