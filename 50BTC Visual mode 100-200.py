from bitcoin import *
import random

while True:
    ran = random.randrange(7237005577332262213973186563042994240829374041602535252466099000494570602496,14474011154664524427946373126085988481658748083205070504932198000989141204992)
    # 1000000000000000000000000000000000000000000000000000000000000000
    # 2000000000000000000000000000000000000000000000000000000000000000
    myhex = "%064x" % ran
    myhex = myhex[:64]
    priv = myhex
    pub = privtopub(priv)
    pubkey1 = encode_pubkey(privtopub(priv), "bin")
    addr = pubtoaddr(pubkey1)
    n = addr
        print ("found!!!",addr,myhex)
        s1 = myhex
        s2 = addr

        f=open(u"50BTC Private key.txt","a")
        f.write(s1)
        f.write(s2)       
        f.close()
#       break
    else:
        print (addr,myhex)