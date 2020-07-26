from time import sleep
import requests
import time
import os
import ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

print("\n\n")
print("             ===============================================================")
print("             =                                                             =")
print("             =   Coded By :-                                               =")
print("             =                .^. HACKZEX .^.                              =")
print("             =                                                             =")
print("             =   GITHUB =>   github.com/07RaHuL07                          =")
print("             =   LINKEDIN => www.linkedin.com/in/rahul-deokate-42257b14b   =")
print("             =                                                             =")
print("             ===============================================================")


iplist = input("[+] Enter List IP => ")
openlist = open(iplist, 'r')
readme = openlist.readlines()
print("[+] IP's You Have => "+str(len(readme)))

for ips in readme:
    exploit = "http://api.hackertarget.com/reverseiplookup/?q="+str(ips)
    conn = requests.get(exploit)
    sleep(3)
    result = conn.content
    file_name = "sites.txt"
    file_mod = "a+"
    site = open(file_name, file_mod)
    site.write(str(result, 'utf-8'))
    print("[+] Grabbing From : "+str(ips))
    print("[+] Save IN ["+file_name+"]\n")
    print(str(result, 'utf-8'))
    site.close()
