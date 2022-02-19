from pyrogram import Client,filters
from pyrogram.types import Messge
from pyrogram.raw import functions


api_id = int()
api_hash = ''

app = Client('robot',api_id,api_hash,enabled=True,hostname='127.0.0.1',port=3004,phonenumber='+989035224478')

@app.on_message(filters.text and filters.chat('me'))
def getm(client,msg:Messge):
    usertext = msg.text
    # Get Chat Id
    try:
        app.join_chat(chat_id=usertext) # can send link or @namechat
    except:
        print('Invalid Channel')
    
    userlist = []
    for i in app.iter_chat_members(chat_id=usertext):
        userlist.append(i.user.id)
        
    print(userlist)
    
    app.send(
        functions.channels.InviteToChannel(
                channel = app.resolve_peer('@channelName'),
                users = [app.resolve_peer(peer_id=j) for j in userlist]
            )
    )
    
    
app.run()

