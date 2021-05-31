from os import system
import hadoop 

def Hadoop():
    while True:
        system("clear")
        system("tput setaf 2 ")
        system("tput bold")
        print("\t\t\t *************************************\n")
        print("\t\t\t     Welcome to Hadoop-Config Menu\n")
        print("\t\t\t *************************************")
        system("tput sgr0")
        system("tput setaf 6")
        print("""
                Press 1:  Install Hadoop configuration	
                Press 2:  Start the Namenode
                Press 3:  Start the Datanode
                Press 4:  To configure Namenode
                Press 5:  To configure Datanode
                Press 6:  To configure Client
                Press 7:  Hadoop cluster Report
                Press 8:  To upload the data from client 
                Press 9:  List all the Uploaded files
                Press 10: Exit to  Main menu
              """)
        system("tput setaf 5")
        ch = int(input('Enter your choice : '))
        system("tput setaf 7")
        if ch == 1:	       
            system("rpm -ivh jdk-8u171-linux-x64.rpm")
            system("yum install 'hadoop-1.2.1-1.x86_64 (1).rpm' ")
            print("\n Installed Sucessfully ")
        elif ch == 2:
            system("hadoop-daemon.sh start namenode")
            input("Enter to continue: ")
        elif ch == 3:
            system("hadoop-daemon.sh start datanode")
            input("Enter to continue: ")
        elif ch == 4:
            print("\n Configuring MasterNode....\n")
            namenode()
            input("Enter to continue: ")
        elif ch == 5:
            print("\n Configuring SlaveNode.....\n")
            datanode()
            input("Enter to continue: ")
        elif ch == 6:
            print("\n Configuring ClientNode....\n")
            client()
        elif ch == 7:
            system("clear")
            r = os.system('hadoop dfsadmin -report')
            print(r)
            input("Enter to continue: ")
        elif ch == 8:
            upload_f_client()
            input("Enter to continue: ")
        elif ch == 9:
            list_file()
            input("Enter to continue: ")
        elif ch == 10:
            break
        else:
            print("Incorrect input please try again")
            input("Enter to continue")


	
def upload_f_client():
	os.system('clear')
	f_name = input("Enter the name of file with location : ")
	system('hadoop fs -put {} /'.format(f_name))

def list_file():
	system('clear')
	print(system('hadoop fs -ls /'))
	input("Enter to continue")
