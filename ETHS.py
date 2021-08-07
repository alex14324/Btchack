#Mizogg.co.uk 17/05/21 ETHS.py (Ethereum Sequential Scanner)
#Install all Modules
#pip3 install bit chainside-btcpy eth_keys eth-hash[pycryptodome]
import eth_keys
from eth_keys import keys
import atexit
from time import time
from datetime import timedelta, datetime

def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))

def log(txt, elapsed=None):
    colour_cyan = '\033[36m'
    colour_reset = '\033[0;0;39m'
    colour_red = '\033[31m'
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

print("Loading Address List Please Wait and Good Luck...")
with open("eth.txt","r") as m: #Your ETH List of addresses
    add = m.read().split()
add= set(add)

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
        eaddr = keys.PublicKey(public_key_bytes).to_address()			#Eth address
        if eaddr in add:
            print ("Nice One Found!!!",ran, private_key, eaddr) #Eth address
            s1 = str(ran)
            s2 = eaddr
            s3 = private_key
            f=open(u"EthWinner.txt","a") #Output File of Eth Wallet Found
            f.write(s1+":"+s2+":"+s3) 
            f.write("\n")
            f.close()
            continue #break or continue
        else:
            colour_cyan = '\033[36m'
            colour_reset = '\033[0;0;39m'
            colour_red = '\033[31m'
            print ("\n " + colour_cyan + "ETHS.py---" + colour_red + "---Good--Luck--Happy--Hunting--Mizogg.co.uk&Chad---" + colour_cyan + "---ETHS.py"  + colour_reset) # Running Display Output
            print (myhex)
            print (eaddr)
            print ("\n ")
            print(colour_cyan + seconds_to_str())