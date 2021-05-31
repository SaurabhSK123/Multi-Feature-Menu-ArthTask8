from os import system
def Ansible():
    while True:
        system("clear")
        system("tput setaf 2")
        system("tput bold")
        print("\t\t\t ************************************\n")
        print("\t\t\t    Welcome To Ansible Services\n")
        print("\t\t\t ************************************")
        system("tput sgr0")
        system("tput setaf 6")
        print("""
            Press 1: Run Ansible to configure weberver with LoadBalancer 
            Press 2: Ansible plabook to Provision AWS instances
            Press 3: Ansible Playbook to deploy web pages inside docker container
            Press 4: Ansible playbook Configure Kubernetes Cluster
            press 5: Exit to main Menu
            """)
        system("tput setaf 7")
        ch = int(input("Enter your choice :- "))
        if ch == 5:
            break
        else:
                print("Enter a valid choice")
                input("Press Enter to continue")

    
