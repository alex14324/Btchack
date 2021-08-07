#Mizogg 06/07/2021 mizogg.co.uk Random Scan for bitcoin Addresses and Balance Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
from bit import *
from bit.format import bytes_to_wif
import random
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
count=0
total=0
while True:
    ran= random.randint(18446744073709551615,115792089237316195423570985008687907852837564279074904382605163141518161494336)
    key = Key.from_int(ran)
    seed=str(ran)
    wif = bytes_to_wif(key.to_bytes(), compressed=False)
    wif2 = bytes_to_wif(key.to_bytes(), compressed=True)
    key1 = Key(wif)
    caddr = key.address
    uaddr = key1.address
    bal = key.get_balance('btc')
    bal1 = key1.get_balance('btc')
    count+=1
    total+=2
    print(colour_red + '<== Current PrivateKey (dec) ==> ' + colour_yellow + seed + colour_reset)
    print (colour_green +  ' <================================= Bitcoin Addresses Checked for Balance =================================>' + '\n' +  colour_reset)
    print(caddr + ' : ' + colour_cyan + key.to_hex() + ' : ' + colour_yellow + wif2 + ' : ' + colour_red + bal + colour_reset)
    print(uaddr + ' : ' + colour_cyan + key1.to_hex() + ' : ' + colour_yellow + wif + ' : ' + colour_red + bal1 + colour_reset)
    print (colour_green + "Scan Number" + ' : ' + colour_reset + str (count) + ' : ' + colour_green + "Total Wallets Checked" + ' : ' + colour_reset + str (total))
    print(colour_cyan + "---r2.py---" + colour_red + "Random Scan for Bitcoin Addresses and Check Balance---------mizogg.co.uk" + colour_cyan + "---r2.py--- "  + colour_reset + seconds_to_str())
    if float (bal) or float (bal1) > 0:
        print (colour_purple +  ' <================================= WINNER WINNER WINNER WINNER =================================>' + '\n' +  colour_reset)
        print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + caddr + colour_green + ' : Balance : ' + bal + colour_reset)
        print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + uaddr +  colour_green +' : Balance : ' + bal1 + colour_reset)
        print(colour_red + ' PrivateKey (wif) Compressed : ' + colour_yellow + wif2 + colour_reset)
        print(colour_red + ' PrivateKey (wif) UnCompressed : ' + colour_yellow + wif + colour_reset)
        print(colour_green + "\nMatching Key ==== Found!!!\n PrivateKey  (hex): " + colour_yellow + key.to_hex() + colour_reset)
        print(colour_green + "\nMatching Key ==== Found!!!\n PrivateKey  (dec): " + colour_yellow + seed + colour_reset)
        print('\n Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD ' ) 
        print (colour_purple +  ' <================================= WINNER WINNER WINNER WINNER =================================>' + '\n' +  colour_reset)
        f=open(u"winner.txt","a")
        f.write('\n=============Bitcoin Address with Total Received Ammount=====================')
        f.write('\nPrivateKey (hex): ' + key.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr)
        f.write('\nBitcoin Address UnCompressed :' + uaddr)
        f.write('\nPrivateKey (wif) Compressed : ' + wif2)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wif)
        f.write('\n=============Bitcoin Address with Total Received Ammount=====================')
        f.write('\n Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD ' ) 
        f.close()
        break