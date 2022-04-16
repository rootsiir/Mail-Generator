from time import sleep
import requests
from colorama import Fore
import os
import re
os.system('cls')

#BU SCRİPT TAMAMEN ROOTSİİR TARAFINDAN YAZILMIŞ OLUP BLACK POETRY ADINA YAZILMIŞTIR. AYNI ZAMANDA ÜCRETSİZDİR

banner = (""" ____  _            _      ____            _
| __ )| | __ _  ___| | __ |  _ \ ___   ___| |_ _ __ _   _
|  _ \| |/ _` |/ __| |/ / | |_) / _ \ / _ \ __| '__| | | |
| |_) | | (_| | (__|   <  |  __/ (_) |  __/ |_| |  | |_| |
|____/|_|\__,_|\___|_|\_\ |_|   \___/ \___|\__|_|   \__, |
                                         rootsiir - |___/""")
print(Fore.RED+banner)

print(Fore.BLUE+'['+Fore.WHITE+'Welcome to Mail Generator'+Fore.BLUE+']')
print()
print(Fore.BLUE+'['+Fore.CYAN+''+Fore.BLUE+']'+Fore.WHITE+' -- '+Fore.BLUE+'['+Fore.CYAN+'Discord'+Fore.BLUE+']'+Fore.BLUE+' - '+Fore.BLUE+'['+Fore.CYAN+'rootsiir#3334'+Fore.BLUE+']')
print(Fore.BLUE+'['+Fore.CYAN+''+Fore.BLUE+']'+Fore.WHITE+' -- '+Fore.BLUE+'['+Fore.CYAN+'Github'+Fore.BLUE+']'+Fore.BLUE+' - '+Fore.BLUE+'['+Fore.CYAN+'github.com/rootsiir'+Fore.BLUE+']')
print()



name = input(Fore.BLUE+'['+Fore.WHITE+'Username'+Fore.BLUE+']'+Fore.WHITE+'#: ')

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(email):

    if (re.fullmatch(regex, email)):
        print(Fore.YELLOW + "[" + Fore.LIGHTWHITE_EX + email + Fore.YELLOW + "]" + Fore.WHITE + " : " + Fore.GREEN + "[VALİD]")

    else:
        print(Fore.YELLOW + "[" + Fore.LIGHTWHITE_EX + email + Fore.YELLOW + "]" + Fore.WHITE + " : " + Fore.RED + "[İNVALİD]")


print("scanning..", end = "", flush = True)



print("\r          ", end = "")

print()


#MAİL

if __name__ == '__main__':

    email = (name+"@gmail.com")
    check(email)
    sleep(0.2)
    email = (name+"@hotmail.com")
    check(email)
    sleep(0.2)
    email = (name+"@aol.com")
    check(email)
    sleep(0.2)
    email = (name+"@yahoo.com")
    check(email)
    sleep(0.2)
    email = (name+"@outlook.com")
    check(email)
    sleep(0.2)
    email = (name+"@outlook.com.tr")
    check(email)
    sleep(0.2)
    email = (name+"@zoho.com")
    check(email)
    sleep(0.2)
    email = (name+"@gmx.com")
    check(email)
    sleep(0.2)
    email = (name+"@yandex.com")
    check(email)
    sleep(0.2)
    email = (name+"@mail.com")
    check(email)
    sleep(0.2)
    email = (name+"@email.com")
    check(email)
    sleep(0.2)
    email = (name+"@icloud.com")
    check(email)
    sleep(0.2)
    email = (name+"@me.com")
    check(email)
    sleep(0.2)
    email = (name+"@games.com")
    check(email)
    sleep(0.2)
    email = (name+"@ygm.com")
    check(email)
    sleep(0.2)
    email = (name+"@love.com")
    check(email)
    sleep(0.2)
    email = (name+"@mac.com")
    check(email)
    sleep(0.2)
    email = (name+"@wow.com")
    check(email)
    sleep(0.2)
print()
os.system("pause")