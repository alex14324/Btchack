#Mizogg 23/05/2021 mizogg.co.uk Random Scan for bitcoin cash Addresses and Balance Random
from bitcash import *
from bitcash.format import bytes_to_wif
import random
import multiprocessing

def spawn():
    while True:
        key = Key.from_int(random.randint(1,115792089237316195423570985008687907852837564279074904382605163141518161494336))
        wif = bytes_to_wif(key.to_bytes(), compressed=False)
        wif2 = bytes_to_wif(key.to_bytes(), compressed=True)
        key1 = Key(wif)
        ammount = 0
        print(key.address + ' : ' + key.to_hex() + ' : ' + key.get_balance('bch'))
        print(key1.address + ' : ' + key.to_hex() + ' : ' + key1.get_balance('bch'))
        if key.get_balance('bch') > str(ammount)  :
            print("Matching Key ==== Found!!!\n PrivateKey: " + key.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + key.to_hex())
            f.write('\nBitcoin Address: ' + key.address)
            f.write('\nPrivateKey (wif): ' + key.to_wif())
            f.write('\n==================================')
            f.close()
        if key1.get_balance('bch') > str(ammount)  :
            print("Matching Key ==== Found!!!\n PrivateKey: " + wif)
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + key.to_hex())
            f.write('\nBitcoin Address: ' + key1.address)
            f.write('\nPrivateKey (wif): ' + wif)
            f.write('\nPrivateKey (wif): ' + wif2)
            f.write('\n==================================')
            f.close()
        
if __name__ == '__main__':
  for i in range(2):
    p = multiprocessing.Process(target=spawn)
    p.start()