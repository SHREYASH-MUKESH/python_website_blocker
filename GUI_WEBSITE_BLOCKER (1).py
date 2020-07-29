# Run this script as root 

import time 
from datetime import datetime as dt 

import tkinter as tk
from tkinter import simpledialog

# change hosts path according to your OS 
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
# localhost's IP 
redirect = "127.0.0.1"

# websites That you want to block 
website_list = []
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
n = int(input("Enter the number of websites you want to block : "))
for i in range(0, n):
	USER_INP = simpledialog.askstring(title="Block Website",
                                  prompt="Enter website you want to block: ")
	
	website_list.append(USER_INP)

while True: 

	# time of your work 
	if dt(dt.now().year, dt.now().month, dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,23): 
		print("Working hours...") 
		with open(hosts_path, 'r+') as file: 
			content = file.read() 
			for website in website_list: 
				if website in content: 
					pass
				else: 
					# mapping hostnames to your localhost IP address 
					file.write(redirect + " " + website + "\n") 
	else: 
		with open(hosts_path, 'r+') as file: 
			content=file.readlines() 
			file.seek(0) 
			for line in content: 
				if not any(website in line for website in website_list): 
					file.write(line) 

			# removing hostnmes from host file 
			file.truncate() 

		print("Fun hours...") 
	time.sleep(5) 