#hex.py 13/06/2021 Bitcoin Legacy compressed/uncompresses address and Segwit address P2SH. Made by Mizogg.co.uk Donations:3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD 
import random
from bit import *
from bit.format import bytes_to_wif
import atexit
from time import time
from datetime import timedelta, datetime
import multiprocessing

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'

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

print("hex.py Bitcoin Legacy compressed/uncompresses address and Segwit address P2SH. List loading Good Luck...")
filename ='btc.txt'
with open(filename) as f:
    add = f.read().split()
add = set(add)


def spawn():
    count=0
    total=0
    while True:
        c1 = str (random.choice("0123456789abcdef"))
        c2 = str (random.choice("0123456789abcdef"))
        c3 = str (random.choice("0123456789abcdef"))
        c4 = str (random.choice("0123456789abcdef"))
        c5 = str (random.choice("0123456789abcdef"))
        c6 = str (random.choice("0123456789abcdef"))
        c7 = str (random.choice("0123456789abcdef"))
        c8 = str (random.choice("0123456789abcdef"))      
        c9 = str (random.choice("0123456789abcdef"))
        c10 = str (random.choice("0123456789abcdef"))
        c11 = str (random.choice("0123456789abcdef"))
        c12 = str (random.choice("0123456789abcdef"))
        c13 = str (random.choice("0123456789abcdef"))
        c14 = str (random.choice("0123456789abcdef"))
        c15 = str (random.choice("0123456789abcdef"))
        c16 = str (random.choice("0123456789abcdef"))
        c17 = str (random.choice("0123456789abcdef"))
        c18 = str (random.choice("0123456789abcdef"))
        c19 = str (random.choice("0123456789abcdef"))
        c20 = str (random.choice("0123456789abcdef"))
        c21 = str (random.choice("0123456789abcdef"))
        c22 = str (random.choice("0123456789abcdef"))
        c23 = str (random.choice("0123456789abcdef"))
        c24 = str (random.choice("0123456789abcdef"))
        c25 = str (random.choice("0123456789abcdef"))
        c26 = str (random.choice("0123456789abcdef"))
        c27 = str (random.choice("0123456789abcdef"))
        c28 = str (random.choice("0123456789abcdef"))
        c29 = str (random.choice("0123456789abcdef"))
        c30 = str (random.choice("0123456789abcdef"))
        c31 = str (random.choice("0123456789abcdef"))
        c32 = str (random.choice("0123456789abcdef"))
        c33 = str (random.choice("0123456789abcdef"))
        c34 = str (random.choice("0123456789abcdef"))
        c35 = str (random.choice("0123456789abcdef"))
        c36 = str (random.choice("0123456789abcdef"))
        c37 = str (random.choice("0123456789abcdef"))
        c38 = str (random.choice("0123456789abcdef"))
        c39 = str (random.choice("0123456789abcdef"))
        c40 = str (random.choice("0123456789abcdef"))
        c41 = str (random.choice("0123456789abcdef"))
        c42 = str (random.choice("0123456789abcdef"))
        c43 = str (random.choice("0123456789abcdef"))
        c44 = str (random.choice("0123456789abcdef"))
        c45 = str (random.choice("0123456789abcdef"))
        c46 = str (random.choice("0123456789abcdef"))
        c47 = str (random.choice("0123456789abcdef"))
        c48 = str (random.choice("0123456789abcdef"))
        c49 = str (random.choice("0123456789abcdef"))
        c50 = str (random.choice("0123456789abcdef"))
        c51 = str (random.choice("0123456789abcdef"))
        c52 = str (random.choice("0123456789abcdef"))
        c53 = str (random.choice("0123456789abcdef"))
        c54 = str (random.choice("0123456789abcdef"))
        c55 = str (random.choice("0123456789abcdef"))
        c56 = str (random.choice("0123456789abcdef"))
        c57 = str (random.choice("0123456789abcdef"))
        c58 = str (random.choice("0123456789abcdef"))
        c59 = str (random.choice("0123456789abcdef"))
        c60 = str (random.choice("0123456789abcdef"))
        c61 = str (random.choice("0123456789abcdef"))
        c62 = str (random.choice("0123456789abcdef"))
        c63 = str (random.choice("0123456789abcdef"))
        c64 = str (random.choice("0123456789abcdef"))
        magic = (c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32+c33+c34+c35+c36+c37+c38+c39+c40+c41+c42+c43+c44+c45+c46+c47+c48+c49+c50
		+c51+c52+c53+c54+c55+c56+c57+c58+c59+c60+c61+c62+c63+c64)
        key = Key.from_hex(magic)
        wif=bytes_to_wif(key.to_bytes(),compressed=False)
        WIF=bytes_to_wif(key.to_bytes(),compressed=True)
        key1=Key(wif)
        caddr = key.address
        uaddr = key1.address
        saddr = key.segwit_address
        count+=1
        total+=3
        if caddr in add:
            print("Matching Key ==== Found!!!\n PrivateKey: " + str(key))
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + magic)
            f.write('\nBitcoin Address: ' + caddr)
            f.write('\nPrivateKey (wif): ' + WIF)
            f.write('\n==================================')
            f.close()
        if uaddr in add:
            print("Matching Key ==== Found!!!\n PrivateKey: " + str(key))
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + magic)
            f.write('\nBitcoin Address: ' + uaddr)
            f.write('\nPrivateKey (wif): ' + wif)
            f.write('\n==================================')
            f.close()
        if saddr in add:
            print("Matching Key ==== Found!!!\n PrivateKey: " + str(key))
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + magic)
            f.write('\nBitcoin Address: ' + saddr)
            f.write('\nPrivateKey (wif): ' + WIF)
            f.write('\nPrivateKey (wif): ' + wif)
            f.write('\n==================================')
            f.close()
        else:
         #print ( 'hex.py Running Scan : ' + str (count) + '  :  ' + colour_cyan + 'PrivateKey : ' + magic + '  :  ' + colour_red + 'Total Bitcoin Addresses : ' + str (total) + ' : ' + colour_cyan + seconds_to_str(), end='\r' + colour_reset)
         print ( 'hex.py Running Scan : ' + str (count) + '  :  ' + colour_red + 'Total Bitcoin Addresses : ' + str (total) + ' : ' + colour_cyan + seconds_to_str(), end='\r' + colour_reset)

if __name__ == '__main__':
  for i in range(1):
    p = multiprocessing.Process(target=spawn)
    p.start()
