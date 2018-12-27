import time
from datetime import datetime as dt


#host_path="C:\Windows\System32\drivers\etc\hosts"
host_path="hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com"]

while True:
    if  dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        with open(host_path, 'r+') as fi:
            content = fi.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    fi.write("\n" + redirect + " " + website)
    else:
        with open(host_path, 'r+') as fi:
            content = fi.readlines()
            fi.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    fi.write(line)
            fi.truncate()
    time.sleep(5)