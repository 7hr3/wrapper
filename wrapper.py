#!/usr/bin/python
import os, sys, re

#Ensure first argument exists with a try/except
try:
    ip = sys.argv[1]
except:
    print "[X] IP Argument required!!"
    exit(0)

#Ensure argument matches IP format using regular expressions (Regex)
if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip):
    print "[X] Argument is not a valid IP Adress."
    exit(0)

#Here we check if -full is provided
try:
     runfull = sys.argv[2]
     os.system('nmap -p- -A %s' % ip)
except:
     os.system('nmap %s' % ip)
