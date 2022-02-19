from pyrogram import Client, filters
from pyrogram.types import Message

app = Client('robot',config_file='config.ini')


@app.on_message(filters.channel)
async def channel(Client,msg:Message):
    await app.forward_message('me',msg.chat.id,msg.message.id)


#------------------------------------------

@app.on_message(filters.chat('me')and filters.media)
async def download(Client,msg:Message):
    await app.download_media(msg.media.file_id)
    await app.send_message('me',f'''
        Download and uploaded!
        {Message.media.file_name}
    ''')
    
    
app.run()