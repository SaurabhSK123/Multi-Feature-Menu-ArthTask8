from os import system 

def config_docker():
    system('yum install docker-ce --nobest -y')
    system('systemctl start docker')
    system('systemctl status docker')
   
def config_web():
    system('docker run -dit --name doc_web -p 8080:80 centos')
    system('docker exec doc_web yum install httpd -y')
    system('docker cp index.html doc_web:/var/www/html/')
    system('docker exec doc_web /usr/sbin/httpd')
    
  
def docker_GUI():
    os.system('docker un -it gui --env="DISPLAY" -net=host firefox:v1')
    input()
 
def Docker():
    while True:
        system("clear")
        system("tput setaf 2")
        system("tput bold")
        print("\t\t\t **************************************\n")
        print("\t\t\t     Welcome To Our Docker Services\n")
        print("\t\t\t **************************************")
        system("tput sgr0")
        system("tput setaf 6")
        print("""
            Press 1: To Configure Docker
            Press 2: To List All Images
            Press 3: To Pull the Image form Dockerhub
            Press 4: To List all the Containers
            Press 5: To Remove All Containers
            Press 6: To Launch a Container
            Press 7: To Configure Web Server on Docker
            Press 8: To Launch GUI Program (Firefox) in Docker
            Press 9: To go back to the Main Menu
            """)
        print("\n")
        system('tput setaf 5')
        ch = int(input("Enter your choice:- "))
        system("tput setaf 7")
        if ch == 1:
            config_docker()
            input("Press Enter to continue")
        elif ch == 2:
            system("docker images")
            input("Press Enter to continue")
        elif ch == 3:
            system("tput setaf 5")
            img = input("Enter the name of image:- ")
            system('tput setaf 7')
            system('docker pull {0}'.format(img))
            input("Press Enter to continue")
        elif ch == 4:
            system('docker ps -a')
            input("Press Enter to continue")
        elif ch == 5:
            system("docker rm -f $(docker ps -aq)")
            input("Press Enter to continue")
        elif ch == 6:
            system("tput setaf 5")
            image = input("Enter the Image to pull ")
            con_name = input("Enter the name of container ")
            system("tput setaf 7")
            cmd = 'docker run -it --name {} {}'.format(con_name,image)
            print("Launching the container successfully")
            input("Press Enter to continue")
            system(cmd)
        elif ch == 7:
            config_web()
            input("Press Enter to continue")
        elif ch == 8:
            docker_GUI()
            input("Press Enter to continue")
        elif ch == 9:
            break
        else:
            print('Enter a valid choice')
            input("Press Enter to Continue")
