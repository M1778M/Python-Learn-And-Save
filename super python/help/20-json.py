import json

dict = {
    'car' : 'bmw',
    'color' : 'black',
    'model' : '7series'
}

# with open("json-tr.json",'w') as f:
#     json.dump(dict,f)

# with open('json-tr.json','r') as f:
#     getjson = json.load(f)
#     print(getjson)


print(json.dumps(dict,indent=5))