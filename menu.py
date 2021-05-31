import os
from rhel import *
from docker import *
from hadoop import *
from aws import *
from ansible import *

while True:
    os.system("clear")
    os.system("tput setaf 2")
    os.system("tput bold")
    print("\t\t\t ******************************************\n")
    print("\t\t\t    Welcome To Muti-Feature Menu Program\n")
    print("\t\t\t ******************************************")
    os.system("tput sgr0")
    os.system("tput setaf 6")
    print("""
            Press 1:  RHEL8 - OS (Linux) related services
            Press 2:  Hadoop Services
            Press 3:  Docker Services
            Press 4:  Amazon Web Services (AWS) 
            Press 5:  Ansible Services 
            Press 6:  Exit
            """)
    print("\n")
    os.system("tput setaf 5")
    ch = int(input("Enter your choice:- "))
    os.system("tput setaf 7")
    if ch == 1:
        Linux()
    elif ch == 2:
        Hadoop()
    elif ch == 3:
        Docker()
    elif ch == 4:
        AWS()
    elif ch == 5:
        Ansible()
    elif ch == 6:
        os.system('clear')
        print("\n")
        os.system("tput setaf 2")
        print("\t\t\t ################################")
        print("\t\t\t    Thank you Good Bye... !!!! ")
        print("\t\t\t ################################")
        os.system('tput setaf 7')
        exit()
