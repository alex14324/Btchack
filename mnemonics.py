#mnemonics.py Bitcoin Legacy compressed/uncompresses address. 04/07/2021
# Search for mnemonics
# Good Luck and Happy Hunting. Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
import bitcoinlib
import random,os,hashlib
import atexit
from time import time
from datetime import timedelta, datetime

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'
colour_green='\033[0;32m'
colour_yellow='\033[0;33m'
colour_purple='\033[0;35m'

const = "m/44'/0'/0'/0/"

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

print("mnemonics.py. List loading Good Luck...")
filename ='btc.txt'

with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
        
with open(filename) as file:
    add = file.read().split()
add = set(add)

print(colour_cyan + "\mnemonics.py---" + colour_red + "---------mizogg.co.uk---------" + colour_cyan + "---mnemonics.py"  + colour_reset)
print('Total Addresses  Loaded and Checking for matching mnemonics : ', line_count)

filename ='wordlist.txt'
with open(filename) as file:
    wordlist = file.read().split()


def create_valid_mnemonics(strength=128):
    rbytes = os.urandom(strength // 8)
    h = hashlib.sha256(rbytes).hexdigest()
    b = ( bin(int.from_bytes(rbytes, byteorder="big"))[2:].zfill(len(rbytes) * 8) \
         + bin(int(h, 16))[2:].zfill(256)[: len(rbytes) * 8 // 32] )
    result = []
    for i in range(len(b) // 11):
        idx = int(b[i * 11 : (i + 1) * 11], 2)
        result.append(wordlist[idx])
    return " ".join(result)

def mnem_to_seed(words):
 salt = 'mnemonic'
 seed = hashlib.pbkdf2_hmac("sha512",words.encode("utf-8"), salt.encode("utf-8"), 2048)
 return seed
 
def seed_to_privatekey(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b0=b.subkey_for_path(const + "0")
    return b0.address()
def seed_to_privatekey1(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b1=b.subkey_for_path(const + "1")
    return b1.address()
def seed_to_privatekey2(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b2=b.subkey_for_path(const + "2")
    return b2.address()
def seed_to_privatekey3(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b3=b.subkey_for_path(const + "3")
    return b3.address()
def seed_to_privatekey4(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b4=b.subkey_for_path(const + "4")
    return b4.address()
def seed_to_privatekey5(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b5=b.subkey_for_path(const + "5")
    return b5.address()
def seed_to_privatekey6(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b6=b.subkey_for_path(const + "6")
    return b6.address()
def seed_to_privatekey7(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b7=b.subkey_for_path(const + "7")
    return b7.address()
def seed_to_privatekey8(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b8=b.subkey_for_path(const + "8")
    return b8.address()
def seed_to_privatekey9(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b9=b.subkey_for_path(const + "9")
    return b9.address()
def seed_to_privatekey10(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b10=b.subkey_for_path(const + "10")
    return b10.address()
def seed_to_privatekey11(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b11=b.subkey_for_path(const + "11")
    return b11.address()
def seed_to_privatekey12(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b12=b.subkey_for_path(const + "12")
    return b12.address()
def seed_to_privatekey13(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b13=b.subkey_for_path(const + "13")
    return b13.address()
def seed_to_privatekey14(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b14=b.subkey_for_path(const + "14")
    return b14.address()
def seed_to_privatekey15(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b15=b.subkey_for_path(const + "15")
    return b15.address()
def seed_to_privatekey16(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b16=b.subkey_for_path(const + "16")
    return b16.address()
def seed_to_privatekey17(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b17=b.subkey_for_path(const + "17")
    return b17.address()
def seed_to_privatekey18(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b18=b.subkey_for_path(const + "18")
    return b18.address()
def seed_to_privatekey19(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b19=b.subkey_for_path(const + "19")
    return b19.address()
count=0
total=0
while True:
    line = create_valid_mnemonics()
    seed = mnem_to_seed(line)
    addr = seed_to_privatekey(seed)
    addr1 = seed_to_privatekey1(seed)
    addr2 = seed_to_privatekey2(seed)
    addr3 = seed_to_privatekey3(seed)
    addr4 = seed_to_privatekey4(seed)
    addr5 = seed_to_privatekey5(seed)
    addr6 = seed_to_privatekey6(seed)
    addr7 = seed_to_privatekey7(seed)
    addr8 = seed_to_privatekey8(seed)
    addr9 = seed_to_privatekey9(seed)
    addr10 = seed_to_privatekey10(seed)
    addr11 = seed_to_privatekey11(seed)
    addr12 = seed_to_privatekey12(seed)
    addr13 = seed_to_privatekey13(seed)
    addr14 = seed_to_privatekey14(seed)
    addr15 = seed_to_privatekey15(seed)
    addr16 = seed_to_privatekey16(seed)
    addr17 = seed_to_privatekey17(seed)
    addr18 = seed_to_privatekey18(seed)
    addr19 = seed_to_privatekey19(seed)
    count+=1
    total+=20
    print(colour_cyan + "\mnemonics.py---" + colour_red + "---------mizogg.co.uk---------" + colour_cyan + "---mnemonics.py"  + colour_reset + seconds_to_str())
    print(colour_green + 'Words for Wallet import : ' + '\n' + colour_yellow + line + colour_reset)
    print('Path : ' + colour_cyan + const + "0" + " : " + colour_red + addr + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "1" + " : " + colour_red + addr1 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "2" + " : " + colour_red + addr2 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "3" + " : " + colour_red + addr3 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "4" + " : " + colour_red + addr4 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "5" + " : " + colour_red + addr5 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "6" + " : " + colour_red + addr6 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "7" + " : " + colour_red + addr7 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "8" + " : " + colour_red + addr8 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "9" + " : " + colour_red + addr9 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "10" + " : " + colour_red + addr10 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "11" + " : " + colour_red + addr11 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "12" + " : " + colour_red + addr12 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "13" + " : " + colour_red + addr13 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "14" + " : " + colour_red + addr14 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "15" + " : " + colour_red + addr15 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "16" + " : " + colour_red + addr16 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "17" + " : " + colour_red + addr17 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "18" + " : " + colour_red + addr18 + " : " + colour_reset)
    print('Path : ' + colour_cyan + const + "19" + " : " + colour_red + addr19 + " : " + colour_reset)
    print (colour_green + "Scan Number" + ' : ' + colour_reset + str (count) + ' : ' + colour_green + "Total Wallets Checked" + ' : ' + colour_reset + str (total))
    print(colour_purple + 'Total Addresses  Loaded and Checking : ', str (line_count) + colour_reset)
    print('\n ' + colour_cyan + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + colour_reset)
    if str(addr) in add or str(addr1) in add or str(addr2) in add or str(addr3) in add or str(addr4) in add or str(addr5) in add or str(addr6) in add or str(addr7) in add or str(addr8) in add or str(addr9) in add or str(addr10) in add  or str(addr11) in add or str(addr12) in add or str(addr13) in add or str(addr14) in add or str(addr15) in add or str(addr16) in add or str(addr17) in add or str(addr18) in add or str(addr19) in add:
        print("\nMatching mnemonics Found!!  " + line)
        f=open(u"winner.txt","a")
        f.write('\n mnemonics: ' + line)
        f.write('\nBitcoin Address: ' + addr)
        f.write('\nBitcoin Address: ' + addr1)
        f.write('\nBitcoin Address: ' + addr2)
        f.write('\nBitcoin Address: ' + addr3)
        f.write('\nBitcoin Address: ' + addr4)
        f.write('\nBitcoin Address: ' + addr5)
        f.write('\nBitcoin Address: ' + addr6)
        f.write('\nBitcoin Address: ' + addr7)
        f.write('\nBitcoin Address: ' + addr8)
        f.write('\nBitcoin Address: ' + addr9)
        f.write('\nBitcoin Address: ' + addr10)
        f.write('\nBitcoin Address: ' + addr11)
        f.write('\nBitcoin Address: ' + addr12)
        f.write('\nBitcoin Address: ' + addr13)
        f.write('\nBitcoin Address: ' + addr14)
        f.write('\nBitcoin Address: ' + addr15)
        f.write('\nBitcoin Address: ' + addr16)
        f.write('\nBitcoin Address: ' + addr17)
        f.write('\nBitcoin Address: ' + addr18)
        f.write('\nBitcoin Address: ' + addr19)
        f.write('\n==================================')
        f.close()