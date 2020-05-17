import os
from time import sleep
import sys
def logo():
	os.system("cat banner.txt")
def get_ip_info(ip):
	url = "http://ip-api.com/"+ip
	response = requests.get(url)
	result = response.text
	with open("x.txt","w") as res:
		res.write(result)
	os.system("cat x.txt | tr -d '{}\",' > ne.txt")
	r = open("ne.txt","r")
	for i in r:
		i.strip("\n")
		sleep(0.5)
		print ("[+] "+i)
os.system("clear")
print ("\033[1;31m")
logo()
print ("\033[1;36m\t=================================================")
try :
        import requests
except ImportError :
#	print ("An Error")
        print ("[!] => An Error \n[!] => pip install requests")
try :
	ip = sys.argv[2]
	get_ip_info(ip)
	os.system("rm -rf x.txt ne.txt")
except IndexError :
	print ("Use python3 ip.py --ip [ip_address & target_domain]")
except Exception :
	os.system("rm -rf x.txt ne.txt")
except KeyboardInterrupt :
	os.system("rm -rf x.txt ne.txt")
	print ("Exiting..")
	sleep(0.5)
