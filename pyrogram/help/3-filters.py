from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters

api_id = int()
api_hash = ''

app = Client('robot',api_id,api_hash,enabled=True,hostname='127.0.0.1',port=3004,phonenumber='+989035224478')


@app.on_message(filters.text)
async def test(client,message):
    userText = message.text
    userId = message.chat.id
    print(message)
    await message.reply('you send a text Not a Photo')
    
#--------------------------
@app.on_message(filters.photo)
async def test1(client,message):
    userText = message.text
    userId = message.chat.id
    print(message)
    await message.reply('you send a photo Not a text')
    
@app.on_message(filters.me) # channel , group, private , video , ....
async def test2(client,message):
    userText = message.text
    userId = message.chat.id
    print(message)
    await message.reply('you send a you')

#----upload , download
@app.on_message(filters.me)
async def upddow(client,message):
    app.download_media(message)
    app.send_message(message.chat.id,'file uploaded')
    print(message.document.file_name)
    
app.run()