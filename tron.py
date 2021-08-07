#Tron Wallet Generator Check against file mizogg.co.uk 18/05/21
import ecdsa
import base58
import random
import atexit
from time import time
from datetime import timedelta, datetime
from Crypto.Hash import keccak

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

def keccak256(data):
    hasher = keccak.new(digest_bits=256)
    hasher.update(data)
    return hasher.digest()

def get_signing_key(raw_priv):
    return ecdsa.SigningKey.from_string(raw_priv, curve=ecdsa.SECP256k1)

def verifying_key_to_addr(key):
    pub_key = key.to_string()
    primitive_addr = b'\x41' + keccak256(pub_key)[-20:]
    addr = base58.b58encode_check(primitive_addr)
    return addr

print("Loading TRON TXT Please Wait and Good Luck...")  
filename ='tron.txt'

with open(filename) as f:
    add = f.read().split()
add = set(add)

while True:
    raw = bytes(random.sample(range(0, 256), 32))
    key = get_signing_key(raw)
    addr = verifying_key_to_addr(key.get_verifying_key()).decode()
    addhex = base58.b58decode_check(addr.encode()).hex()
    publickey = key.get_verifying_key().to_string().hex()
    privatekey = raw.hex()
    print (colour_cyan + 'TRON Address : ' + colour_red + addr + colour_reset + " : Date&Time" + seconds_to_str()) #TRON address display
    print(colour_cyan +'PrivateKey' + ' : ' + colour_red + privatekey + colour_reset, '\n') # Running Display Output
    if addr in add:
        f=open(u"winner.txt","a")
        f.write('\nPrivateKey (hex) : ' + privatekey)
        f.write('\nPublic Key       : ' + publickey)
        f.write('\nTRON Address     : ' + addr)
        f.write('\nTRON Address(hex): ' + addhex)
        f.write('\n==================================================================================')
        f.close()
        break