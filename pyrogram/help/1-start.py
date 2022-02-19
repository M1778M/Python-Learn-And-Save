from pyrogram import Client

api_id = int()
api_hash = ''

app = Client('robot',api_id,api_hash,enabled=True,hostname='127.0.0.1',port=3004,phonenumber='+989035224478')

@app.on_message()
async def hello(client,message):
    await message.reply_text(f'Hello {message.from_user.mention}') # message.from_user.mention == user_id


    
app.run()