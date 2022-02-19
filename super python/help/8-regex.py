import re

#string = "Im masih hello programer or hacker i get 100 dolar in evry days"
#result = re.findall(r'Im masih hello .*', string)
#print(result)
########################################################3

str = "salam mamad. Salam sara. salam ahmand."
result = re.sub(r'[sS]alam \w+\.', 'HI', str)
print(result)
