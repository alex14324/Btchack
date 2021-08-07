#Mizogg.co.uk 17/05/21 ETHS.py (Ethereum Sequential Scanner With Transaction Checking)
#Install all Modules
#pip3 install bit chainside-btcpy eth_keys eth-hash[pycryptodome]
import eth_keys
from eth_keys import keys
import requests
import json
import atexit
from time import time
from datetime import timedelta, datetime

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

x=int(input("'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
F = []
P = x

while P<y:
        P+=1
        ran = P
        myhex = "%064x" % ran
        private_key = myhex[:64]
        private_key_bytes = bytes.fromhex(private_key)
        public_key_hex = keys.PrivateKey(private_key_bytes).public_key
        public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
        ethadd = keys.PublicKey(public_key_bytes).to_address()			#Eth address
        blocs = requests.get("https://api.ethplorer.io/getAddressInfo/" + ethadd + "?apiKey=freekey") #Ethereum API Must create account to be better API
        ress = blocs.json()
        balance = dict(ress)["countTxs"]
        print ("\n " + colour_cyan + "Ethereum Random Scan" + colour_red + "---Good--Luck--Happy--Hunting--Mizogg.co.uk&Chad---" + colour_cyan + "With Balance Checker" + colour_reset) # Running Display Output
        print (colour_cyan + 'Ethereum Address                    ' + '  : '  + colour_red + ethadd + '     : ' + colour_reset + 'Transactions = ' +  str(balance)) #Ethereum address display
        print(colour_cyan +'PrivateKey' + ' : ' + colour_red + myhex + colour_reset + " : Date&Time" + seconds_to_str(), '\n') # Running Display Output
        if int(balance) > 0:
            print("Matching Key ==== Ethereum Address Found!!!\n PrivateKey: " + myhex) #Ethereum winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + myhex)
            f.write('\n Eth Address: ' + ethadd)
            f.write('\n==================================')
            f.close()