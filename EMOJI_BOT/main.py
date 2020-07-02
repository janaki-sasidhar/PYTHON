import requests
url="https://api.telegram.org/bot"
api_id="951920235:AAFAi38QF14elZ9oaUCgKL76t4p1defnKkY"
command="/getUpdates"
response=requests.get(url+api_id+command)
response=response.json()
if response['ok']==True:
        update_ids=[]
        for i in response['result']:
                update_ids.append(i['update_id'])
#print(update_ids)
latest_text=response['result'][-1]['message']['text'].lower()
chat_id=response['result'][-1]['message']['chat']['id']
print("The chat id is " ,chat_id)
print(latest_text)
#print(response['result'][-1].keys())
#city=latest_text[12:]
api_table=requests.get("https://api.github.com/emojis").json()
new_url=api_table[latest_text]
requests.get(url+api_id+"/sendPhoto"+"?chat_id="+str(chat_id)+"&photo="+new_url)
#requests.get(url+api_id+"/sendPhoto"+"?chat_id="+str(chat_id)+"&photo="+"https://thispersondoesnotexist.com/image")
