import re
#sstr = "slam khobi? are to khobi"

#result = re.search(r'salam', sstr)
#####################################################

email = "ali@gmail.com"
result = re.search(r'.+\@.+\..{2,3}', email)

if result == None:
    print("Email not valid")
else:
    print("email found")