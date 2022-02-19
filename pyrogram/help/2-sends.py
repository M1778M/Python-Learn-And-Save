from pyrogram import Client
from pyrogram.types import Message
api_id = int()
api_hash = ''

app = Client('robot',api_id,api_hash,enabled=True,hostname='127.0.0.1',port=3004,phonenumber='+989035224478')

app.start()
app.send_message(chat_id='me',text='Salam')
app.stop()

#-------------------

with app:
    app.send_message(chat_id='1016213663',text='Hello M1778')
    
#----------------

async def sendmsg():
    async with app:
        await app.send_message(chat_id='1016213663',text='Hello Man')


#----------img/video/all
with app:
    #app.send_   -> to see all sends
    app.send_photo(chat_id='1016213663','C:\\Users\\m1778\\Desktop\\M1778\\p.png',caption='This is a png')

#-------------------------

@app.on_message()
async def test(client,message):
    userText = message.text
    print('UserMessage: ',message,'\n User Text : ',userText)
    userid = Message.chat.id
    if userText == 'Hello':
        await message.reply(text='Hello , How are You man?')
    elif userText == 'hack':
        await message.reply(text='You Are Hacked!')
    elif userText == 'photo':
        await message.reply_photo('C:\\Users\\m1778\\Desktop\\M1778\\p.png',caption='photo Man')
    else:
        await message.reply('Ican\'t UnderStand Maaaan?')
    

app.run()