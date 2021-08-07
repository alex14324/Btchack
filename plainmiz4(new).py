#plainmiz4.py Random Scan for Bitcoin\ETH\Addresses Total Received Ammount mizogg.co.uk
from bit import *
from bit.format import bytes_to_wif
import eth_keys
from eth_keys import keys
import random
import urllib.request
import requests
api = input('ethplorer.io API KEY Paste here (Create free account to get API key) :  ')
x=1
y=115792089237316195423570985008687907852837564279074904382605163141518161494336
count=0
total=0
while True:
    count+=1
    total+=4
    ran= random.randint(x,y)
    key = Key.from_int(ran)
    seed=str(ran)
    wif = bytes_to_wif(key.to_bytes(), compressed=False)
    wif1 = bytes_to_wif(key.to_bytes(), compressed=True)
    key1 = Key(wif)
    caddr = key.address
    uaddr = key1.address
    saddr = key.segwit_address
    myhex = '%064x' % ran
    private_key = myhex[:64]
    private_key_bytes = bytes.fromhex(private_key)
    public_key_hex = keys.PrivateKey(private_key_bytes).public_key
    public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
    ethadd = keys.PublicKey(public_key_bytes).to_address()
    contents1 = urllib.request.urlopen('https://blockchain.info/q/getreceivedbyaddress/' + caddr).read()
    contents2 = urllib.request.urlopen('https://blockchain.info/q/getreceivedbyaddress/' + uaddr).read()
    contents3 = urllib.request.urlopen('https://blockchain.info/q/getreceivedbyaddress/' + saddr).read()
    blocs = requests.get('https://api.ethplorer.io/getAddressInfo/' + ethadd + '?apiKey='+ api)
    ress = blocs.json()
    balances = dict(ress)['countTxs']
    print ('Scan Number : ', str (count), ' : Total Wallets Checked : ', str (total), 'CurrentSeed : ', seed, end='\r')
    if int(contents1) > 0 or int(contents2) > 0 or int(contents3) > 0:
        print (' <================================= WINNER Total Received Ammount WINNER =================================>' + '\n')
        print ('Congraz you have found wallet with a balance : ', caddr, ' : Balance : ', str(contents1.decode('UTF8')))
        print ('Congraz you have found wallet with a balance : ', uaddr, ' : Balance : ', str(contents2.decode('UTF8')))
        print ('Congraz you have found wallet with a balance : ', saddr, ' : Balance : ', str(contents3.decode('UTF8')))
        print(' PrivateKey (wif) Compressed : ', wif1)
        print(' PrivateKey (wif) UnCompressed : ', wif)
        print('\nMatching Key ==== Found!!!\n PrivateKey  (hex): ', key.to_hex())
        print('\nMatching Key ==== Found!!!\n PrivateKey  (dec): ', seed)
        print (' <================================= WINNER Total Received Ammount WINNER =================================>' + '\n')
        f=open(u'btcwinner.txt','a')
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
        print (' <================================= WINNER Ethereum Address With Transactions WINNER =================================>' + '\n')
        print ('Congraz you have found wallet with a balance : ', ethadd, 'Transactions = ',  str(balances))
        print('\nMatching Key ==== Found!!!\n PrivateKey  (hex): ', key.to_hex())
        print('\nMatching Key ==== Found!!!\n PrivateKey  (dec): ', seed)
        print (' <================================= WINNER Ethereum Address With Transactions WINNER =================================>' + '\n')
        f=open(u'ethwinner.txt','a')
        f.write('\n=============Ethereum Address With Transactions=====================')
        f.write('\nPrivateKey (hex): ' + key.to_hex())
        f.write('\nPrivateKey (dec): ' + seed)
        f.write('\n Eth Address: ' + ethadd)
        f.write('\n=============Ethereum Address With Transactions=====================')
        f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' + '\n')
        f.close()