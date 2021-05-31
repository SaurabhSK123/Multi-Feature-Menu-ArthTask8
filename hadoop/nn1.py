import os
import subprocess as sp
def namenode():
	while True :
         print("""  
        what do you want to configue in Namenode 
        1. Configure the hdfs-site.xml file
        2. Configure the core-site.xml file
        3. Format the Namenode
        4. Check the Namenode status
        5. main menu
            """)
        ch = int(input("Enter the choice..."))
            
        if ch==1 : 
            conf_hdfs_nn()
        elif ch==2 :
            conf_core_nn()
        elif ch==3 : 
            os.system("hadoop namenode format")
        elif ch==4 :
            os.system("jps")
        elif ch==5 :
            break
        else:
            print("Option not Supported")		
def conf_hdfs_nn():
    ans = input('''For configuring Namenode we have to create a folder 
                   select bleow option...
				1. folder already created in this we will format the existing folder
				2. to create a new folder
				Enter here: ''')
	d_name = input("Give the name of the folder want to create or already exist: ")
	if int(ans) == 2:
		os.system("mkdir /{}".format(d_name))
	os.system('hadoop namenode -format ')

	with open("/etc/hadoop/hdfs-site.xml",'w+') as f:
		f.write("<?xml version='1.0'?>\n")
		f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n")
		f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
		f.write("<configuration>\n")
		f.write("<property>\n")
		f.write("<name>dfs.name.dir</name>\n")
		f.write("<value>/{}</value>\n".format(d_name))
		f.write("</property>\n")
		f.write("</configuration>\n")
def conf_core_nn():
    p_no = input("Enter the port no. on which hadoop services is running in namenode: ")
	ip= input("Enter the ip of namenode")
	with open("/etc/hadoop/core-site.xml",'w+') as f:
		f.write("<?xml version='1.0'?>\n")
		f.write("<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n")
		f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
		f.write("<configuration>\n")
		f.write("<property>\n")
		f.write("<name>fs.default.name</name>\n")
		f.write("<value>hdfs://{}:{}</value>\n".format(ip,int(p_no)))
		f.write("</property>\n")
		f.write("</configuration>\n")
