from os import system
def AWS():
    while True:
        system("clear")
        system("tput setaf 2")
        system("tput bold")
        print("\t\t\t *****************************\n")    
        print("\t\t\t    Welcome To AWS Services\n")
        print("\t\t\t *****************************")
        system("tput sgr0")
        system("tput setaf 6")
        print("""
            Press 1: To Configure AWS Into CLI
            Press 2: To Create a Key Pair
            Press 3: To Create a Security Group 
            Press 4: To Launch an EC2 Instance
            Press 5: To Stop an EC2 Instance
            Press 6: To Create an EBS Volume
            Press 7: To Attach EBS volume to EC2 Instance
            Press 8: To Create an S3 Bucket
            Press 9: To Delete an S3 Bucket
            Press 10: Exit
            """)
        print("\n")
        system("tput setaf 5")
        ch = int(input("Enter your choice: "))
        system("tput setaf 7")
        if ch == 1:
            print()
            system("aws configure")
            system("tput setaf 2")
            input("Press enter to Continue...")
            system("tput setaf 7")
        elif ch == 2:
            system("tput setaf 5")
            key = input("Enter key-pair name: ")
            system("tput setaf 7")
            system("aws ec2 create-key-pair --keyname {}".format(key))
            system("tput setaf 2")
            input("Press enter to Continue")
            system("tput setaf 7")
        elif ch == 3:
            print()
            system("tput setaf 5")
            sg_name = input("Enter Security Group Name: ")
            sg_desc = input("Enter the description: ")
            os.system("aws ec2 create-security-group --group-name {0} --description {1} ".format(sg_name,sg_desc))
            print("Add rule to the security group")
            protocol = input("Enter the protocol: ")
            port = input("Enter the port number: ")
            cidr = input("Enter the CIDR: ")
            system("aws ec2 authorize-security-group-ingress --group-name {0} --protocol {1} --port {2} --cidr {3}".format(sg_name,protocol,port,cidr))
            input("Press enter to continue")
        elif ch == 4:
            print()
            ami = input('Enter AMI id to Launch Instance : ')
            itype = input("Enter Instance type : ")
            count = input('Enter Number of Instances to launch : ')
            sg_id = input('Enter Security Group Id to attach to the Instance : ')
            key_name = input('Enter Key to attach to ec2 Instance : ')
            system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --security-group-ids {} --key-name {} --region us-east-1 '.format(ami , itype , count , sg_id , key_name))
            print()
            print('Instance Successfully Launched ')
            print()
        elif ch == 5:
            print()
            ec2_id = input("Enter Instance Id to stop Instance")
            system('aws ec2 stop-instances --instance-ids {}  --region us-east-1'.format(ec2_id))
            print()
            print('Instance Successfully Stopped ')
            print()
        elif ch == 6:
            print()
            az = input('Enter the Availablity Zone to Create EBS Volume : ')
            size = input('Enter the Size of EBS Volume : ')
            system('aws ec2 create-volume --availability-zone {} --size {} --region us-east-1'.format(az , size))
            print()
            print('EBS Volume Created. Keep the volume ID for future references ')
            print()
        elif ch == 7:
            print()
            ebs_id = input('Enter EBS Volume ID to Attach to EC2 Instance : ')
            instance_id = input('Enter EC2 Instance ID to attach EBS Volume : ')
            system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf --region us-east-1'.format(ebs_id , instance_id))
            print()
            print('EBS Volume Attached ')
            print()
        elif ch == 8:
            print()
            s3_bucket_name = input("Enter S3 bucket name : ")
            system('aws s3api create-bucket --bucket {} --region us-east-1 '.format(s3_bucket_name))
            print()
            print('S3 Bucket Created Successfully ')
            print()
        elif ch == 9:
            print()
            s3_bucket_name = input("Enter S3 bucket name to delete : ")
            system('aws s3 rm --recursive s3://{}'.format(s3_bucket_name))
            system('aws s3api delete-bucket --bucket {} --region us-east-1'.format(s3_bucket_name))
            print()
            print('Bucket Deleted Successfully ')
            print()
        elif ch == 10:
            break
        else:
            print("Invalid Choice")
            input("Press Enter to continue ")
