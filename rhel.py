from os import system 
import subprocess 
def RemoteLogin():
	pass

def Locally():
    while True:
        system("clear")
        system("tput setaf 2")
        system("tput bold")
        print("\t\t\t ************************************\n")
        print("\t\t\t    Welcome To RHEL Linux Services\n")
        print("\t\t\t ************************************")
        system("tput sgr0")
        system("tput setaf 6")
        print("""
            Press 1: To Check IP Address
            Press 2: Date
            Press 3: Calendar
            Press 4: Create a directory
            Press 5: Create a file
            Press 6: Configure Web Server
            Press 7: Launch Firefox
            Press 8: To add a new user
            Press 9: To delete a new user
            Press 10: To ping an IP address
            Press 11: Install a package/software using yum
            Press 12: Uninstall a package/software using yum
            Press 13: Exit
            """)
        system("tput setaf 7")
        ch = int(input("Enter your Choice: "))

        if ch == 1:
                r = system("ifconfig enp0s3")
                print(r)
                input("Press Enter to continue")
        elif ch == 2:
                r = system("date")
                print(r)
                input("Press Enter to continue")
        elif ch == 3:
                system("cal")
                print(r)
                input("Press Enter to continue")
        elif ch == 4:
                dir_nm = input("Enter the name of directory ")
                system("mkdir {}".format(dir_nm))
                print("Directory Successfully Created...\n\n")
                input("Press Enter to continue")
        elif ch == 5:
                File_nm = input("Enter the name of file ")
                system("touch {}".format(File_nm))
                print("File Successfully Created...\n\n")
                input("Press Enter to continue")
        elif ch == 6:
                system("yum install httpd -y")
                system("cp index.html /var/www/html/index.html") 
                system("systemctl start httpd")
                system("systemctl status httpd")
                print("Apache Httpd Successfully installed and configured\n\n")
                input("Press Enter to continue")
        elif ch == 7:
                sys("firefox")
        elif ch == 8:
                username = input("Enter a new username ")
                system(f"useradd {user_name};id {user_name}")
                input("\n Press Enter to continue")
        elif ch == 9:
                user_name=input("Enter the username To Delete : ")
                input("\nPress Enter to continue")
        elif ch == 10:
                ip = input("Enter IP or Hostname you want to ping : ")
                print("\nPress CTRL + C to stop pinging...")
                system("ping {}".format(ip))
                input("\nPress Enter to continue")
        elif ch == 11:
                software = input("Enter package you want to install ")
                system(f"yum install {software}")
                print("{} Softwate install Sucessfully".format(software))
                input("\nPress Enter to continue")
        elif ch == 12:
                soft = input("Enter package you want to uninstall ")
                system(f"yum remove {soft}")
                input("\nPress Enter to continue")
        elif ch == 13:
                break
        else:
                print("Enter a valid choice")
                input("Press Enter to continue")


def Linux():
    while True:
            print()
            system("tput setaf 3")
            login = input("In which system you want to login : locally/remotely : ")
            print(login)
            print()
            system("tput setaf 7")
            if login.lower() == "remotely":
                    RemoteLogin()
                    break
            elif login.lower() == "locally":
                    Locally()
                    break
            else:
                    print("Enter a valid choice ")
                    input("Press Enter to Continue ")
