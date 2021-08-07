#Mizogg 23/05/2021 mizogg.co.uk Sequential Scan for bitcoin cash Addresses and Balance
from bitcash import *
from bitcash.format import bytes_to_wif
x=int(input("'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
F = []
P = x
while P<y:
        P+=1
        ran = P
        ammount = 0
        key = Key.from_int(ran)
        wif = bytes_to_wif(key.to_bytes(), compressed=False)
        key1 = Key(wif)
        print(key.address + ' : ' + key.to_hex() + ' : ' + key.get_balance('usd'))
        print(key1.address + ' : ' + key.to_hex() + ' : ' + key1.get_balance('bch'))
        if key.get_balance('usd') > str(ammount)  :
            print("Matching Key ==== Found!!!\n PrivateKey: " + key.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + key.to_hex())
            f.write('\nBitcoin Address: ' + key.address)
            f.write('\nPrivateKey (wif): ' + key.to_wif())
            f.write('\n==================================')
            f.close()
        if key1.get_balance('bch') > str(ammount)  :
            print("Matching Key ==== Found!!!\n PrivateKey: " + key.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + key.to_hex())
            f.write('\nBitcoin Address: ' + key1.address)
            f.write('\nPrivateKey (wif): ' + key.to_wif())
            f.write('\n==================================')
            f.close()