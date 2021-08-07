#miz6.py Random Scan for Bitcoin\ETH\DOGEAddresses Total Received Ammount mizogg.co.uk
import random
import bit
from bit import *
from bit.format import bytes_to_wif
import hashlib
from bitcoinlib.encoding import pubkeyhash_to_addr_bech32, addr_bech32_to_pubkeyhash, change_base
from eth_hash.auto import keccak
import atexit
from time import time
from datetime import timedelta, datetime
import urllib.request
import requests
import json
import threading

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'
colour_green='\033[0;32m'
colour_yellow='\033[0;33m'
colour_purple='\033[0;35m'
colour_blue='\033[0;34m'

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
 
def ETH_Address(un_pubk_bytes):
    return '0x' + keccak(un_pubk_bytes[1:])[-20:].hex()

def HASH160(pubk_bytes):
    return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()

def hash160_to_addrbech32(hash160):
 	return pubkeyhash_to_addr_bech32(hash160, prefix='bc', witver=0, separator='1')
  
print(colour_cyan + "miz6.py---" + colour_red + "Random Scan for BTC\ETH\DOGE Addresses Transactions/Balance/Total Received Ammount-------mizogg.co.uk" + colour_cyan + "---miz6.py"  + colour_reset + seconds_to_str())
threadCount = input('Best Run on 1 thread to not block API but you can try more : How many threads to run?:  ')
api = input('ethplorer.io API KEY Paste here (Create free account to get API key) :  ')
print(colour_yellow+ "Start search... Pick Range to start (Example Puzzle 64 starting Range 18446744073709551615 ):"+ colour_reset)
x=int(input("'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
print(colour_purple +"Happy Hunting and Good Luck, Starting search... Please Wait "+ colour_reset)
print("===============================================================================")

def seek():
    count=0
    total=0
    while True:
        ran= random.randint(x,y)
        pk = Key.from_int(ran)
        key = Key.from_int(ran)
        seed=str(ran)
        wif = bytes_to_wif(key.to_bytes(), compressed=False)                            # Uncompressed WIF
        wif1 = bytes_to_wif(key.to_bytes(), compressed=True)                            # Compressed WIF
        key1 = Key(wif)
        upub = pk._pk.public_key.format(compressed=False)                               # Uncompressed publickey
        cpub = pk._pk.public_key.format(compressed=True)                                # Compressed publickey
        crmd = HASH160(cpub)                                                            # compressed HASH160
        urmd = HASH160(upub)                                                            # uncompressed HASH160
        caddr = key.address                                                             #Legacy compressed address
        uaddr = key1.address                                                            #Legacy uncompressed address
        saddr = key.segwit_address                                                      #Segwit address P2SH
        dogecaddr = bit.base58.b58encode_check(b'\x1e' + crmd)                          #Dogecoin compressed
        dogeuaddr = bit.base58.b58encode_check(b'\x1e' + urmd)                          #Dogecoin uncompressed
        ethadd = ETH_Address(upub)                                                      #Ethereum address

        count+=1*int(threadCount)
        total+=6*int(threadCount)
        pagenumber= int(seed)//128
    #API Request Weblist
        contents1 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + caddr).read()
        contents2 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + uaddr).read()
        contents3 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + saddr).read()
        blocs = requests.get("https://api.ethplorer.io/getAddressInfo/" + ethadd + "?apiKey="+ api) #Ethereum address API
        ress = blocs.json()
        balances = dict(ress)["countTxs"] 
        Dogecoin = requests.get("https://dogechain.info/api/v1/address/received/"+ str (dogecaddr)) #received or balance
        resedoge = Dogecoin.json()
        balanceDoge = dict(resedoge)['received'] #received or balance
        Dogecoin1 = requests.get("https://dogechain.info/api/v1/address/received/"+ str (dogeuaddr)) #received or balance
        resedoge1 = Dogecoin1.json()
        balanceDoge1 = dict(resedoge1)['received'] #received or balance 
        
    # Running Display Output
        #print(colour_green + "Scan Number" + ' : ' + colour_reset + str (count) + ' : ' + colour_green + "Total Wallets Checked Transactions/Balance/Total Received Ammount " + ' : ' + colour_reset + str (total)+ ' : ' + colour_green +'Current Seed' + ' : ' + colour_reset + seed, end='\r') # Running Display Output
        print(colour_cyan + "miz6.py---" + colour_reset + "Random Scan for BTC\ETH\DOGE Addresses Transactions/Balance/Total Received Ammount---" + '\n' + colour_yellow + "---Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD" + colour_cyan + "---miz6.py--- TIMING ---->    "  + colour_reset + seconds_to_str())
        print (colour_green + "Scan Number" + ' : ' + colour_reset + str (count) + ' : ' + colour_green + "Total Wallets Checked" + ' : ' + colour_reset + str (total))
        print (colour_red + ' PrivateKey (hex) : ' + colour_yellow + key.to_hex() + colour_reset)
        print (colour_red + ' PrivateKey (dec) : ' + colour_yellow + seed + colour_reset)
        print (colour_red + ' PrivateKey (wif) Compressed : ' + colour_yellow + wif1 + colour_reset)
        print (colour_red + ' PrivateKey (wif) UnCompressed : ' + colour_yellow + wif + colour_reset)
        print(colour_green +  '<------------Page Number ' , colour_yellow , pagenumber , colour_green , ' on Keys------------> '+ colour_reset)
        print (colour_red + ' <=============================='+ colour_reset + 'Addresses Checked for Transactions/Balance/Total Received Ammount' + colour_red + '==============================>' + '\n' +  colour_reset)
        print (colour_green + 'COMPRESSED   BTC     :  ' + caddr + '            : ' + colour_reset + 'Transactions/Balance/Total Received Ammount = ' + colour_red + str(contents1.decode('UTF8')) + colour_reset)
        print (colour_green + 'UNCOMPRESSED BTC     :  ' + uaddr + '            : ' + colour_reset + 'Transactions/Balance/Total Received Ammount = ' + colour_red + str(contents2.decode('UTF8')) + colour_reset)
        print (colour_green + 'Segwit Address BTC   :  ' + saddr + '            : ' + colour_reset + 'Transactions/Balance/Total Received Ammount = ' + colour_red + str(contents3.decode('UTF8')) + colour_reset)
        print (colour_green + 'Ethereum Address     :  ' + ethadd + '    : ' + colour_reset + 'Transactions/Balance/Total Received Ammount = ' + colour_red +  str(balances)) #Ethereum address display
        print (colour_green + 'Dogecoin Compressed  :  ' + str(dogecaddr) + '            : ' + colour_reset + 'Transactions/Balance/Total Received Ammount = ' + colour_red +  str(balanceDoge)) #Dogecoin Compressed address display
        print (colour_green + 'Dogecoin UnCompressed:  ' + str(dogeuaddr) + '            : ' + colour_reset + 'Transactions/Balance/Total Received Ammount = ' + colour_red +  str(balanceDoge1)) #Dogecoin  UnCompressed address display
        print (colour_red + ' <=============================='+ colour_reset + 'Addresses Checked for Transactions/Balance/Total Received Ammount' + colour_red + '==============================>' + '\n' +  colour_reset)
    #Results Winner TEXT
        if int(contents1) > 0 or int(contents2) > 0 or int(contents3) > 0:
            print (colour_purple +  ' <================================= WINNER Total Received Ammount WINNER =================================>' + '\n' +  colour_reset) #bitcoin winner
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + caddr + colour_green + ' : Balance : ' + str(contents1.decode('UTF8')) + colour_reset)
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + uaddr + colour_green + ' : Balance : ' + str(contents2.decode('UTF8')) + colour_reset)
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + saddr + colour_green + ' : Balance : ' + str(contents3.decode('UTF8')) + colour_reset)
            print(colour_red + ' PrivateKey (wif) Compressed : ' + colour_yellow + wif1 + colour_reset)
            print(colour_red + ' PrivateKey (wif) UnCompressed : ' + colour_yellow + wif + colour_reset)
            print(colour_green + "\nMatching Key ==== Found!!!\n PrivateKey  (hex): " + colour_yellow + key.to_hex() + colour_reset)
            print(colour_green + "\nMatching Key ==== Found!!!\n PrivateKey  (dec): " + colour_yellow + seed + colour_reset)
            print(colour_green +  '<------------Page Number ' , colour_yellow , pagenumber , colour_green , ' on Keys------------> '+ colour_reset)
            print (colour_purple +  ' <================================= WINNER Total Received Ammount WINNER =================================>' + '\n' +  colour_reset)
            f=open(u"btcwinner.txt","a")
            f.write('\n=============Bitcoin Address with Total Received Ammount=====================')
            f.write('\nPrivateKey (hex): ' + key.to_hex())
            f.write('\nPrivateKey (dec): ' + seed)
            f.write('\nBitcoin Address Compressed : ' + caddr)
            f.write('\nBitcoin Address UnCompressed :' + uaddr)
            f.write('\nBitcoin Segwit Address :' + saddr)
            f.write('\nPrivateKey (wif) Compressed : ' + wif1)
            f.write('\nPrivateKey (wif) UnCompressed : ' + wif)
            f.write('\n=============Bitcoin Address with Total Received Ammount=====================')
            f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' ) 
            f.close()
        if int(balances) > 0:
            print (colour_purple +  ' <================================= WINNER Ethereum Address With Transactions WINNER =================================>' + '\n' +  colour_reset)
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + ethadd + colour_green + 'Transactions = ' +  str(balances)) #Ethereum winner
            print(colour_green + "\nMatching Key ==== Found!!!\n PrivateKey  (hex): " + colour_yellow + key.to_hex() + colour_reset)
            print(colour_green + "\nMatching Key ==== Found!!!\n PrivateKey  (dec): " + colour_yellow + seed + colour_reset)
            print(colour_green +  '<------------Page Number ' , colour_yellow , pagenumber , colour_green , ' on Keys------------> '+ colour_reset)
            print (colour_purple +  ' <================================= WINNER Ethereum Address With Transactions WINNER =================================>' + '\n' +  colour_reset)
            f=open(u"ethwinner.txt","a")
            f.write('\n=============Ethereum Address With Transactions=====================')
            f.write('\nPrivateKey (hex): ' + key.to_hex())
            f.write('\nPrivateKey (dec): ' + seed)
            f.write('\n Eth Address: ' + ethadd)
            f.write('\n=============Ethereum Address With Transactions=====================')
            f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' + '\n')
            f.close()
        if float(balanceDoge) > 0 or float(balanceDoge1) > 0:
            print (colour_purple +  '\n <================================= WINNER DOGE Coin Total Received Ammount WINNER =================================>' +  colour_reset)
            print (colour_green + "Matching Key ==== Found!!!\n PrivateKey  (hex): " + colour_yellow + key.to_hex() + colour_reset) #Dogecoin Compressed address winner
            print (colour_green + "Matching Key ==== Found!!!\n PrivateKey  (dec): " + colour_yellow + seed + colour_reset)
            print (colour_yellow + 'Congraz you have found wallet with a Total Received Ammount : ' + colour_reset + dogecaddr + colour_green + ' : Total Received Ammount : ' + str(balanceDoge) + colour_reset)
            print (colour_yellow + 'Congraz you have found wallet with a Total Received Ammount : ' + colour_reset + dogeuaddr + colour_green + ' : Total Received Ammount : ' + str(balanceDoge1) + colour_reset)
            print (colour_purple +  '\n <================================= WINNER DOGE Coin Total Received Ammount WINNER =================================>' +  colour_reset)
            f=open(u"dogewinner.txt","a")
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