import os
os.system("usermod -G wheel Jasur")
os.system("usermod -G wheel Javlon")
os.system("usermod -G wheel Aziz")
os.system("usermod -g Students Jasur")
os.system("usermod -g Engineers Javlon")
os.system("usermod -g Devops Aziz")
os.popen("tail -3 /etc/passwd")