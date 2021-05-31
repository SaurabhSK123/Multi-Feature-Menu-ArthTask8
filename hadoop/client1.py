import os
def client():
    while True :
            print("""	
            1. Configure the hdfs-site.xml file
            2. Configure the core-site.xml file
            5. Previous menu
		""")
            cl=int(input("Enter your Choice.."))	
            if cl == 1:
                print("Already Configured")
    	    elif cl == 2:
                p = int(input("Enter the port no. on which hadoop services is running in namenode: "))
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
            elif cl==3 :
                break
            else :
                print(" Option not supported ")

