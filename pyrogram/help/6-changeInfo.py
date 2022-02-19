from pyrogram import Client
from pyrogram.raw import functions
from datetime import datetime
import schedule
import time


api_id = int()
api_hash = ''

app = Client('robot',api_id,api_hash,enabled=True,hostname='127.0.0.1',port=3004,phonenumber='+989035224478')

def job():
    now_h = datetime.now().strftime('%H')
    now_m = datetime.now().strftime('%M')
    
    with app:
        app.send(
            functions.account.UpdateProfile(
                about=f"time:{now_h}:{now_m}"
            )
        )
        print('ok')
    
        app.set_profile_photo(photo='{path}')


schedule.every(1).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
    
app.run()