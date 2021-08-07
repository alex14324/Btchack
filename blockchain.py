#bitcoin address balance checker Using blockchain API. Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
import itertools
import random
import urllib.request
import threading
import atexit
from time import time
from datetime import timedelta, datetime

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'
colour_green='\033[0;32m'
colour_yellow='\033[0;33m'
colour_purple='\033[0;35m'

def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))


def log(txt, elapsed=None):
    print('\n ' + colour_cyan + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' + colour_reset)
    if elapsed:
        print("\n " + colour_red + " [TIMING]> Elapsed time ==> " + elapsed + "\n" + colour_reset)


def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))


start = time()
atexit.register(end_log)
log("Start Program")

print('addresses loading please wait..................................:')

with open("btc.txt", "r") as file:
    line_count = 0
    for line in file:
        line != "\n"
        line_count += 1
print(colour_cyan + "\blockchain.py---" + colour_red + "address balance checker---------mizogg.co.uk---------address balance checker" + colour_cyan + "---blockchain.py"  + colour_reset)
print('Total Addresses Loaded:', line_count)

mylist = []

with open('btc.txt', newline='', encoding='utf-8') as f:
    for line in f:
        mylist.append(line.strip())


count=0
total=0
for i in range(0,len(mylist)):
    count+=1
    total+=1
    add = mylist[i]
    contents = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + str (add)).read()
    print(colour_cyan + "\blockchain.py---" + colour_red + "blockchain address balance checker---------mizogg.co.uk---------address balance checker" + colour_cyan + "---blockchain.py"  + colour_reset + seconds_to_str())
    print('Total addresses Loaded:', line_count)
    print ('Biction address Checked : ' + str(add) + ' : Total Balance = ' + str(contents.decode('UTF8')))
    print ( "Scan Number" + ' : ' + str (count) + ' : ' + "Total Wallets Checked" + ' : ' + str (total))
    if int(contents) > 0:
        print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + str (add) + colour_green + ' : Balance : ' + str(contents.decode('UTF8')) + colour_reset)
        f=open(u"balance.txt","a")
        f.write('\nBitcoin Address Compressed : ' + str (add) + 'Balance : ' +  str(contents.decode('UTF8')))
        f.write('\n==================================')
        f.close()
