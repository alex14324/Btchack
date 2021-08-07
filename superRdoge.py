#DOGE & Balance/Received checker 14/05/2021 Mizogg&Chad mizogg.co.uk Random
import random
import bit
from bit import *
from bit.format import bytes_to_wif
import hashlib
from bitcoinlib.encoding import pubkeyhash_to_addr_bech32, addr_bech32_to_pubkeyhash, change_base
import atexit
from time import time
from datetime import timedelta, datetime
import requests
import json
import threading


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

def HASH160(pubk_bytes):
    return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()

print(colour_cyan + "superdoge.py---" + colour_red + "Random Scan for bitcoin Addresses Total Received Ammount---------mizogg.co.uk" + colour_cyan + "---superdoge.py"  + colour_reset + seconds_to_str())
threadCount = input('Best Run on 1 thread to not block API but you can try more : How many threads to run?:  ')
print(colour_yellow+ "Start search... Pick Range to start (Example Puzzle 64 starting Range 18446744073709551615 ):"+ colour_reset)
x=int(input("'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
print(colour_purple +"Starting search... Please Wait "+ colour_reset)
print("==========================================================")

def seek():
    count=0
    total=0
    while True:
        ran= random.randint(x,y)
        pk = Key.from_int(ran)
        key = Key.from_int(ran)
        seed=str(ran)
        upub = pk._pk.public_key.format(compressed=False)                               # Uncompressed publickey
        cpub = pk._pk.public_key.format(compressed=True)                                # Compressed publickey
        crmd = HASH160(cpub)                                                            # compressed HASH160
        urmd = HASH160(upub)                                                            # uncompressed HASH160
        dogecaddr = bit.base58.b58encode_check(b'\x1e' + crmd)                          #Dogecoin compressed
        dogeuaddr = bit.base58.b58encode_check(b'\x1e' + urmd)                          #Dogecoin uncompressed
        count+=1*int(threadCount)
        total+=2*int(threadCount)
        Dogecoin = requests.get("https://dogechain.info/api/v1/address/received/"+ str (dogecaddr)) #received or balance
        resedoge = Dogecoin.json()
        balanceDoge = dict(resedoge)['received'] #received or balance
        Dogecoin1 = requests.get("https://dogechain.info/api/v1/address/received/"+ str (dogeuaddr)) #received or balance
        resedoge1 = Dogecoin1.json()
        balanceDoge1 = dict(resedoge1)['received'] #received or balance
        print(colour_cyan + "\nSuperdoge.py---" + colour_red + "Random Scan for DOGE Coin Addresses Total Received Ammount")
        print (colour_green + "Scan Number" + ' : ' + colour_reset + str (count) + ' : ' + colour_green + "Total Wallets Checked" + ' : ' + colour_reset + str (total))
        print(colour_red + ' PrivateKey (hex) : ' + colour_yellow + key.to_hex() + colour_reset)
        print(colour_red + ' PrivateKey (dec) : ' + colour_yellow + seed + colour_reset)
        print ('Dogecoin Compressed Address' + ' : '  + colour_cyan + dogecaddr + ' : ' + colour_red +  str(balanceDoge) + colour_reset) #Dogecoin Compressed address display
        print ('Dogecoin UnCompressed Address : '  + colour_cyan + dogeuaddr + ' : ' + colour_red +  str(balanceDoge1) + colour_reset) #Dogecoin  UnCompressed address display
        print ("------Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD" + colour_cyan + "---Superdoge.py"  + colour_reset + seconds_to_str())
        
        
        if float(balanceDoge) > 0 or float(balanceDoge1) > 0:
            print (colour_purple +  '\n <================================= WINNER Total Received Ammount WINNER =================================>' +  colour_reset)
            print (colour_green + "Matching Key ==== Found!!!\n PrivateKey  (hex): " + colour_yellow + key.to_hex() + colour_reset) #Dogecoin Compressed address winner
            print (colour_green + "Matching Key ==== Found!!!\n PrivateKey  (dec): " + colour_yellow + seed + colour_reset)
            print (colour_yellow + 'Congraz you have found wallet with a Total Received Ammount : ' + colour_reset + dogecaddr + colour_green + ' : Total Received Ammount : ' + str(balanceDoge) + colour_reset)
            print (colour_yellow + 'Congraz you have found wallet with a Total Received Ammount : ' + colour_reset + dogeuaddr + colour_green + ' : Total Received Ammount : ' + str(balanceDoge1) + colour_reset)
            print (colour_purple +  '\n <================================= WINNER Total Received Ammount WINNER =================================>' +  colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n=============DOGE Coin Address with Total Received Ammount=====================')
            f.write('\nPrivateKey (hex): ' + key.to_hex())
            f.write('\nPrivateKey (dec): ' + seed)
            f.write('\nDogecoin Compressed address: ' + dogecaddr)
            f.write('\nDogecoin  UnCompressed address: ' + dogeuaddr)
            f.write('\n=============DOGE COIN Address with Total Received Ammount=====================')
            f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' ) 
            f.close()

threads = []


for i in range(int(threadCount)):
    t = threading.Thread(target=seek)
    threads.append(t)
    t.start()