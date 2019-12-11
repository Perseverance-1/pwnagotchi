#needs A TON of work....

#import logging
import subprocess
import string
import re
import socket
import time
#import pwnagotchi.plugins as plugins

#Logs into cracked network and start info gathering.

#class nmap(plugins.Plugin):
#    __author__ = 'Perseverance'
#    __version__ = '1.0.0'
#    __license__ = 'GPL3'
#    __name__ = 'nmap'
#    __description__ = 'changes mac for anonyimity and/or filter evasion, logs in, and starts nmap'

#    def __init__(self):
#        self.text_to)set = ""

#    def on_loaded(self):
#        logging.info("[login] plugin loaded")

def interface()
    int(re.search(r'\d+', eth).group(0)) # finds eth in string 
    eth = "eth0"
    wlan0 = "wlan0"


#maybe use mac from ap association altogether?
print('Current MAC') # find code to pull current vs changed
cmac = subprocess.run(('/usr/bin/macchanger `echo -s eth0`'),shell=True,stdout=subprocess.PIPE)
print(cmac)
print("changing mac")
down = subprocess.run(('/sbin/ifconfig `echo eth0 down`'),shell=True,stdout=subprocess.PIPE)
print("link down")
macchange = subprocess.run(('/usr/bin/macchanger `echo -m (mac from assoc.) eth0`'),shell=True,stdout=subprocess.PIPE)
up = subprocess.run(('/sbin/ifconfig `echo eth0 up`'),shell=True,stdout=subprocess.PIPE)
rmac = subprocess.run(('/usr/bin/macchanger `echo -s eth0`'),shell=True,stdout=subprocess.PIPE)
print("link up")
print("mac address changed to" + cmac)

#print("Changing network") #changes wpa_supplicant.
#if macchange == true
#do; .....
#elif ip == false
something something

#nano /etc/wpa_supplicant.conf
#network={
#ssid="{current.ap}"
#psk="{use.key}"
#}
#wpa_supplicant -B -i {interface} -c /etc/wpa_supplicant.conf
#if output==true
#do; {port.scan}
#else {recrack.cap}

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

#if ip == true
#do; os.system("gnome-terminal -e 'bash -c \"ping -w 3 1.1.1.1; exec bash\"'"),shell=True,stdout=subprocess.PIPE)
print("link is up")
#else ip == false
print("link down")
something something

print("we're in, start nmap")

#Port scan
#if {allgood}==true do;
#need arguments
#else {allgood}=false 
something something
