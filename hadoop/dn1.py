import os
def datanode():
    while True :
        os.system("clear")
        print("""

            1. Configure the hdfs-site.xml file
            2. Configure the core-site.xml file
            3. Check the Datanode status
            4. main menu
            """)
        choice=int(input("Enter your choice ..."))
        if n==1 :
            hdfs_conf_dn()
        elif n==2 :
            core_conf_dn
        elif n==3 :
            os.system("jps")
        elif n==4 :
            break
        else :
                print("not supported")
def hdfs_conf_dn():
    ans = input('''For configuring we have to create a folder
                select option from below....
				1. folder already created in this we will delete the existing folder and create new folder
				2. to create a new folder
				Enter here: ''')
	dir_name = input("Give the name of the folder want to create or already exist : ")
	if int(answer) == 2:
		os.system("mkdir /{}".format(dir_name))
	elif int(answer)==1:
		os.system("rm -rf /{}".format(dir_name))
		os.system("mkdir /{}".format(dir_name))

	with open("/etc/hadoop/hdfs-site.xml",'w+') as f:
		f.write("<?xml version='1.0'?>\n")
		f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n")
		f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
		f.write("<configuration>\n")
		f.write("<property>\n")
		f.write("<name>dfs.data.dir</name>\n")
		f.write("<value>/{}</value>".format(dir_name))
		f.write("</property>\n")
		f.write("</configuration>\n")
def core_conf_dn():
    port = int(input("Enter the port no. on which hadoop services is running in namenode: "))
	ip = input("Enter the ip of namenode")
	with open("/etc/hadoop/core-site.xml",'w+') as f:
		f.write("<?xml version='1.0'?>\n")
		f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n")
		f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
		f.write("<configuration>\n")
		f.write("<property>\n")
		f.write("<name>fs.default.name</name>\n")
		f.write("<value>hdfs://{}:{}</value>\n".format(ip,port))
		f.write("</property>\n")
		f.write("</configuration>\n")
