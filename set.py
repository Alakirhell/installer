import os, time, webbrowser

from colorama import Fore, Style

os.system('clear')

def res():
    print(Style.RESET_ALL)
    
while True:
    print('')
    print(Fore.CYAN+'', Style.BRIGHT)
    print (" ___                 _             _   _               ")
    print ("|_ _|  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print (" | |  | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print (" | |  | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print ("|___| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    print ("\n")
    print ("[Настройки]                                    [v2.7.1]")
    res()
    print (Fore.GREEN+"    [1] Запускать вместе с Termux")
    print (Fore.GREEN+"    [2] Обновить Installer")
    print (Fore.GREEN+"    [2] ")
    print (Fore.CYAN+"")
    print (Fore.YELLOW+'    [e] Назад')
    res()
    inp = input ('  Выбери пункт>>> ')
    os.system('clear')

    if inp == '1':
        print('')
        
    if inp == 'e':
        os.system('clear')
        print(Fore.WHITE+'')
        break
        
