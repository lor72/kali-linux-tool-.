import os
import time
import sys
from colorama import *

r = Fore.RED
b = Fore.BLUE
bl = Fore.BLACK
p = Fore.MAGENTA
res = Fore.RESET
pi = Fore.MAGENTA

def a():
    for i in range(5):
        print(f'{pi}\nlove 2bood .')

def v9j():
    for i in range(3):
        print(f'{pi}\n@v9.j')

def slowprint(s):
    for C in s + '\n':
        sys.stdout.write(C)
        sys.stdout.flush()
        time.sleep(5. / 100)

slowprint(" welcome to reailty ..")
time.sleep(1)
os.system('clear')
slowprint(f'''
{b}┌──({r}root㉿2bood{b})
└─# $wp.admin
''')
os.system('clear')
time.sleep(2)
slowprint("Loading ...")
time.sleep(1)
slowprint("\nDone ! .")

print("""
||||||||||||||
|| wp admin || 
||||||||||||||           
""")

def menu():
    print(" system. \n 1. start \n 2. else \n 3. exit")
    osption = input()

    if osption == "1":
        os.system('sudo apt-get update && apt-get upgrade')
        os.system('sudo apt-get dist-upgrade ')
        os.system('sudo apt-get insall python && apt-get install python3')
        time.sleep(2)
        slowprint("\n Done daddy dody ;")
        v9j()
    
    elif osption == "2":
        sad = os.system(input("~: "))
        a()
    
    elif osption == "3":
        os.system('exit')
        slowprint("See you 2bood ~ .")
        time.sleep(1)
        v9j()
        time.sleep(1)
menu()        
     