from pyrogram.types import Message
import time
import schedule
from pyrogram import Client

api_id = int()
api_hash = ''

app = Client('robot',api_id,api_hash,enabled=True,hostname='127.0.0.1',port=3004,phonenumber='+989035224478')

def job():
    with app:
        app.send_message(chat_id='@username',text='Hello')
        

schedule.every(10).seconds.do(job)





while True:
    schedule.run_pending()
    time.sleep(1)


app.run()


















helpTime = """import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)
schedule.every(1).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)"""
    
