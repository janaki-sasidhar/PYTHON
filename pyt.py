import requests
api_id=""

from telegram.ext import Updater
updater = Updater(token=api_id, use_context=True)
dispatcher = updater.dispatcher
response=requests.get("https://api.covid19india.org/state_district_wise.json").json()

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''I'm a bot, please enter the "/get cityname" [in india] to get covid-19 stats''')
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def func(name):
        for i in response.keys():
                if name in response[i]['districtData']:
                    result=response[i]['districtData'][name]
                    result=f'''ACTIVE {result['active']}\nCONFIRMED {result['confirmed']}\nDECEASED {result['deceased']}\nRECOVERED {result['recovered']}'''
                    return result
        else:
                return "Please enter the correct district name(check spellings)"









def get(update, context):
    text_caps = ' '.join(context.args).capitalize()
    a=func(text_caps)
    context.bot.send_message(chat_id=update.effective_chat.id, text=a)

caps_handler = CommandHandler('get', get)
dispatcher.add_handler(caps_handler)

updater.start_polling()
