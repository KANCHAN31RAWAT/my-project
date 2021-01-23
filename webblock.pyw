import time
from datetime import datetime as dt
hosts_path=r"C:\Windows\System32\drivers\etc\hosts.txt"
redirect="127.0.0.1"
websites_list=["https://www.facebook.com","facebook.com"]#user can modify the list of the websites they want to block
while True:
    #duration during which website blocker will work
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,22):
        with open(hosts_path, "r+") as file:#r+:-opens a file for reading only in binary format.
            content=file.read()
            for site in websites_list:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")#mapping hostnames to our localhost ip address
        print("Working hours")
        print("All sites are blocked")
        break
    else:
        with open(hosts_path,"r+") as file:
            content=file.readlines()
            file.seek(0)#reset the pointer to the top of the text file
            for line in content:
                #here comes the tricky line,basically we overtime the whole file
                if not any(site in line for site in websites_list):
                    file.write(line)
                    #do nothing otherwise
            file.truncate()#this line is used to delete the trailing lines (that contain DNS)
        print("Fun time")
        print("Allowed access!")
        break
