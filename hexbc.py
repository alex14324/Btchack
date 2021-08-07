#bitcoin HEX address balance checker. Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
from bit import *
from bit.format import bytes_to_wif
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

print('HEX List loading please wait..................................:')

with open("hex.txt", "r") as file:
    line_count = 0
    for line in file:
        line != "\n"
        line_count += 1

mylist = []

with open('hex.txt', newline='', encoding='utf-8') as f:
    for line in f:
        mylist.append(line.strip())

ammount = 0
count=0
total=0
for i in range(0,len(mylist)):
    myhex = mylist[i]
    priv = myhex.split()[0]
    key = Key.from_hex(priv)
    wif = bytes_to_wif(key.to_bytes(), compressed=False)
    wif2 = bytes_to_wif(key.to_bytes(), compressed=True)
    key1 = Key(wif)
    caddr = key.address
    uaddr = key1.address
    bal = key.get_balance('btc')
    bal1 = key1.get_balance('btc')
    count+=1
    total+=2
    print(colour_cyan + "\hexbc.py---" + colour_red + "HEX address balance checker---------mizogg.co.uk---------HEX address balance checker" + colour_cyan + "---hexbc.py"  + colour_reset + seconds_to_str())
    print('Total HEX addresses Loaded:', line_count)
    print (priv + colour_yellow, wif + colour_cyan, caddr + colour_red,bal + colour_reset)
    print (priv + colour_yellow, wif2 + colour_cyan, uaddr + colour_red,bal1 + colour_reset)
    print ( "Scan Number" + ' : ' + str (count) + ' : ' + "Total Wallets Checked" + ' : ' + str (total))
    if float (bal) or float (bal1) > float(ammount):
        print ( 'Congraz you have found wallet with a balance : ' + colour_cyan + caddr + colour_green + ' : Balance : ' + bal + ' : ' + colour_cyan + seconds_to_str() + colour_reset)
        print ( 'Congraz you have found wallet with a balance : ' + colour_cyan + uaddr + colour_green + ' : Balance : ' + bal1 + ' : ' + colour_cyan + seconds_to_str() + colour_reset)
        print(colour_purple + "Matching Key ==== Found!!!\n PrivateKey: " + priv + colour_reset)
        f=open(u"winner.txt","a")
        f.write('\nPrivateKey (hex): ' + priv)
        f.write('\nBitcoin Address Compressed : ' + caddr)
        f.write('\nBitcoin Address UnCompressed :' + uaddr)
        f.write('\nPrivateKey (wif) Compressed : ' + wif2)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wif)
        f.write('\n==================================')
        f.close()