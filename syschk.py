#!/usr/bin/python3

#The first part will import the modules needed for the script to run
import os
import platform

#This will display as much information as possible about the system it is run on.
OSType = platform.platform()
print(f"Your OS and Version is {OSType}")

#Further commands will be run depending on the system running the script.
#This is determined by the output of the OS details in the previous command.

#This part shows the commands triggered to run on a Linux system.
#They are mostly linux commands with text manipulation run by os.system.
if "Linux" in OSType:
	print("Your private IP is:")
	os.system("ifconfig | grep broadcast | awk '{print$2}'")
	print("Your default gateway is:")
	os.system("route | grep UG | awk '{print $2}'")
	print("Your public IP is:")
	os.system('curl -s ifconfig.co')
	print("Your storage details are as follows:")
	os.system("df -h | grep -E 'File|sda'")
	print("Your 5 largest directories are:")
	os.system("du -h ~ | sort -nr | head -5")
	print("Your CPU usage is displayed below. It is refreshed every 10 seconds.")
	#Since the command for CPU usage will be run indefinitely, the user is reminded to manually end it with CTRL+C.
	#Coloured text is used to draw the user's attention 
	class col:
		red = '\033[31m'
		yellow = '\033[93m'	
	print(col.yellow,"!!!", col.red, "PRESS CTRL+C TO END", col.yellow,"!!!")
	os.system('top -d 10')

#The next part will show the commands used on a Windows system
if "Windows" in OSType:
	#This part deals with the IP address requirements. 
	#The output from iponfid is first stored, then the details of the private ip address and default gateway are displayed by
	# 1) searching for the appropriate text in each line that contains the required information
	# 2) Using positioning based on windows ipconfig output to display only the IP address of that line
	data = os.popen(ipconfig).readlines()
	for eachline in data:
		if "IPv4" in eachline:
			print("Your private IP is:")
			print(eachline[39:55])
		if "Default Gateway" in eachline:
			print("Your default gateway is:")
			print(eachline[39:55])
	#For public IP, no differece from the Linux method. Just executing a command using os.system
	print("Your public IP is:")
	os.system('curl ifconfig.co')
	#The storage details are taken from the output of the dir command.
	#The last two lines will show the storage used by the contents displayed in that current directory and the remaining free space.
	#Due to the nature of the dir command, only the remaining free space is accurate.
	#The used space will only show the space used by the contents of the current directory.
	print("Your used and free storage is:")
	rawdir=os.popen('dir C:\ /A').readlines()
	for eachline in rawdir:
		if "bytes" in eachline:
			print(eachline)
	#For the largest 5 directories, only the names are displayed. 
	#I was not able to use dir to display the size of each one like in the Linux section.
	#Searches online suggested downloading additional programs that can mimic du from Linux.
	print("Your largest 5 directories are:")
	rawdir=os.popen('dir C:\ /B /O:-S').readlines()
	big5=rawdir[0:5]
	for eachdir in big5:
		print(eachdir)
	#For CPU usage, the command will only show the usage at that time, unlike the Linux version 
	#which will run until the user terminates it.
	print("Your CPU usage is:")
	os.system('wmic cpu get loadpercentage')


#General Comments:
#As I was not able to run the python script in windows, the windows commands were written using the following process:
#1) running the windows commands in windows
#2) copying the output into a Linux file using nano
#3) python commands were fine tuned and run on the Linux file instead of a direct output from a windows file.
#Examples:
# ~ data=open("windir").readlines()
# ~ big5=data[0:5]
# ~ for eachline in big5:
	# ~ print(eachline)
# ~ for eachline in data:
	# ~ if "bytes" in eachline:
		# ~ print(eachline)
# ~ workfile = open('wintestip')
# ~ data = workfile.readlines()
	
