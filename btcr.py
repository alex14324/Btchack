# btcr.py Random Bitcoin Legacy compressed/uncompresses address and Segwit address P2SH. 25/06/2021
# Good Luck and Happy Hunting. Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
from bit import *
from bit.format import bytes_to_wif
import atexit
from time import time
from datetime import timedelta, datetime
import random
import multiprocessing

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

print("btcr.py Random Bitcoin Legacy compressed/uncompresses address and Segwit address P2SH. List loading Good Luck...")
filename ='btc.txt'

with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
        
with open(filename) as file:
    add = file.read().split()
add = set(add)

print(colour_cyan + "\bctr.py---" + colour_red + "---------mizogg.co.uk---------" + colour_cyan + "---btcr.py"  + colour_reset)
print(colour_purple +'Total Addresses  Loaded and Checking : ',str (line_count) + colour_reset)
print(colour_yellow+ "Start search... Pick Range"+ colour_reset)
x=int(input("'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))


def spawn():
    count=1
    totalkey=0
    total=0
    while True: 
        C=Key.from_int(random.randint(x,y)) 
        C1=Key.from_int(random.randint(x+1,y))
        C2=Key.from_int(random.randint(x+2,y))  
        C3=Key.from_int(random.randint(x+3,y))
        C4=Key.from_int(random.randint(x+4,y))
        C5=Key.from_int(random.randint(x+5,y))
        C6=Key.from_int(random.randint(x+6,y))  
        C7=Key.from_int(random.randint(x+7,y))
        C8=Key.from_int(random.randint(x+8,y))
        C9=Key.from_int(random.randint(x+9,y))
        C10=Key.from_int(random.randint(x+10,y))  
        C11=Key.from_int(random.randint(x+11,y))
        C12=Key.from_int(random.randint(x+12,y))
        C13=Key.from_int(random.randint(x+13,y))
        C14=Key.from_int(random.randint(x+14,y))  
        C15=Key.from_int(random.randint(x+15,y))
        C16=Key.from_int(random.randint(x+16,y))
        C17=Key.from_int(random.randint(x+17,y))
        C18=Key.from_int(random.randint(x+18,y))  
        C19=Key.from_int(random.randint(x+19,y))
        C20=Key.from_int(random.randint(x+20,y))
        C21=Key.from_int(random.randint(x+21,y))
        C22=Key.from_int(random.randint(x+22,y))  
        C23=Key.from_int(random.randint(x+23,y))
        C24=Key.from_int(random.randint(x+24,y)) 
        C25=Key.from_int(random.randint(x+25,y))
        C26=Key.from_int(random.randint(x+26,y))  
        C27=Key.from_int(random.randint(x+27,y))
        C28=Key.from_int(random.randint(x+28,y))
        C29=Key.from_int(random.randint(x+29,y))
        C30=Key.from_int(random.randint(x+30,y))  
        C31=Key.from_int(random.randint(x+31,y))
        C32=Key.from_int(random.randint(x+32,y))
        C33=Key.from_int(random.randint(x+33,y))
        C34=Key.from_int(random.randint(x+34,y))  
        C35=Key.from_int(random.randint(x+35,y))
        C36=Key.from_int(random.randint(x+36,y))
        C37=Key.from_int(random.randint(x+37,y))
        C38=Key.from_int(random.randint(x+38,y))  
        C39=Key.from_int(random.randint(x+39,y))
        C40=Key.from_int(random.randint(x+40,y))
        C41=Key.from_int(random.randint(x+41,y))
        C42=Key.from_int(random.randint(x+42,y))  
        C43=Key.from_int(random.randint(x+43,y))
        C44=Key.from_int(random.randint(x+44,y))
        C45=Key.from_int(random.randint(x+45,y))
        C46=Key.from_int(random.randint(x+46,y))  
        C47=Key.from_int(random.randint(x+47,y))
        C48=Key.from_int(random.randint(x+48,y))
        C49=Key.from_int(random.randint(x+49,y))
        C50=Key.from_int(random.randint(x+50,y))
        C51=Key.from_int(random.randint(x+51,y))
        C52=Key.from_int(random.randint(x+52,y))
        C53=Key.from_int(random.randint(x+53,y))
        C54=Key.from_int(random.randint(x+54,y))
        C55=Key.from_int(random.randint(x+55,y))
        C56=Key.from_int(random.randint(x+56,y))
        C57=Key.from_int(random.randint(x+57,y))
        C58=Key.from_int(random.randint(x+58,y))
        C59=Key.from_int(random.randint(x+59,y))
        C60=Key.from_int(random.randint(x+60,y))
        C61=Key.from_int(random.randint(x+61,y))
        C62=Key.from_int(random.randint(x+62,y))
        C63=Key.from_int(random.randint(x+63,y))
        C64=Key.from_int(random.randint(x+64,y)) 
        wif=bytes_to_wif(C.to_bytes(),compressed=False) 
        wif1=bytes_to_wif(C1.to_bytes(),compressed=False)
        wif2=bytes_to_wif(C2.to_bytes(),compressed=False)
        wif3=bytes_to_wif(C3.to_bytes(),compressed=False)
        wif4=bytes_to_wif(C4.to_bytes(),compressed=False)
        wif5=bytes_to_wif(C5.to_bytes(),compressed=False)
        wif6=bytes_to_wif(C6.to_bytes(),compressed=False)
        wif7=bytes_to_wif(C7.to_bytes(),compressed=False)
        wif8=bytes_to_wif(C8.to_bytes(),compressed=False)
        wif9=bytes_to_wif(C9.to_bytes(),compressed=False)
        wif10=bytes_to_wif(C10.to_bytes(),compressed=False) 
        wif11=bytes_to_wif(C11.to_bytes(),compressed=False)
        wif12=bytes_to_wif(C12.to_bytes(),compressed=False)
        wif13=bytes_to_wif(C13.to_bytes(),compressed=False)
        wif14=bytes_to_wif(C14.to_bytes(),compressed=False)
        wif15=bytes_to_wif(C15.to_bytes(),compressed=False)
        wif16=bytes_to_wif(C16.to_bytes(),compressed=False)
        wif17=bytes_to_wif(C17.to_bytes(),compressed=False)
        wif18=bytes_to_wif(C18.to_bytes(),compressed=False)
        wif19=bytes_to_wif(C19.to_bytes(),compressed=False)
        wif20=bytes_to_wif(C20.to_bytes(),compressed=False)
        wif21=bytes_to_wif(C21.to_bytes(),compressed=False)
        wif22=bytes_to_wif(C22.to_bytes(),compressed=False)
        wif23=bytes_to_wif(C23.to_bytes(),compressed=False)
        wif24=bytes_to_wif(C24.to_bytes(),compressed=False)
        wif25=bytes_to_wif(C25.to_bytes(),compressed=False)
        wif26=bytes_to_wif(C26.to_bytes(),compressed=False)
        wif27=bytes_to_wif(C27.to_bytes(),compressed=False)
        wif28=bytes_to_wif(C28.to_bytes(),compressed=False)
        wif29=bytes_to_wif(C29.to_bytes(),compressed=False)
        wif30=bytes_to_wif(C30.to_bytes(),compressed=False)
        wif31=bytes_to_wif(C31.to_bytes(),compressed=False)
        wif32=bytes_to_wif(C32.to_bytes(),compressed=False)
        wif33=bytes_to_wif(C33.to_bytes(),compressed=False)
        wif34=bytes_to_wif(C34.to_bytes(),compressed=False)
        wif35=bytes_to_wif(C35.to_bytes(),compressed=False)
        wif36=bytes_to_wif(C36.to_bytes(),compressed=False)
        wif37=bytes_to_wif(C37.to_bytes(),compressed=False)
        wif38=bytes_to_wif(C38.to_bytes(),compressed=False)
        wif39=bytes_to_wif(C39.to_bytes(),compressed=False)
        wif40=bytes_to_wif(C40.to_bytes(),compressed=False)
        wif41=bytes_to_wif(C41.to_bytes(),compressed=False)
        wif42=bytes_to_wif(C42.to_bytes(),compressed=False)
        wif43=bytes_to_wif(C43.to_bytes(),compressed=False)
        wif44=bytes_to_wif(C44.to_bytes(),compressed=False)
        wif45=bytes_to_wif(C45.to_bytes(),compressed=False)
        wif46=bytes_to_wif(C46.to_bytes(),compressed=False)
        wif47=bytes_to_wif(C47.to_bytes(),compressed=False)
        wif48=bytes_to_wif(C48.to_bytes(),compressed=False)
        wif49=bytes_to_wif(C49.to_bytes(),compressed=False)
        wif50=bytes_to_wif(C50.to_bytes(),compressed=False)
        wif51=bytes_to_wif(C51.to_bytes(),compressed=False)
        wif52=bytes_to_wif(C52.to_bytes(),compressed=False)
        wif53=bytes_to_wif(C53.to_bytes(),compressed=False)
        wif54=bytes_to_wif(C54.to_bytes(),compressed=False)
        wif55=bytes_to_wif(C55.to_bytes(),compressed=False)
        wif56=bytes_to_wif(C56.to_bytes(),compressed=False)
        wif57=bytes_to_wif(C57.to_bytes(),compressed=False)
        wif58=bytes_to_wif(C58.to_bytes(),compressed=False)
        wif59=bytes_to_wif(C59.to_bytes(),compressed=False)
        wif60=bytes_to_wif(C60.to_bytes(),compressed=False)
        wif61=bytes_to_wif(C61.to_bytes(),compressed=False)
        wif62=bytes_to_wif(C62.to_bytes(),compressed=False) 
        wif63=bytes_to_wif(C63.to_bytes(),compressed=False)
        wif64=bytes_to_wif(C64.to_bytes(),compressed=False)
        WIF=bytes_to_wif(C.to_bytes(),compressed=True)        
        WIF1=bytes_to_wif(C1.to_bytes(),compressed=True)
        WIF2=bytes_to_wif(C2.to_bytes(),compressed=True)
        WIF3=bytes_to_wif(C3.to_bytes(),compressed=True)
        WIF4=bytes_to_wif(C4.to_bytes(),compressed=True)
        WIF5=bytes_to_wif(C5.to_bytes(),compressed=True)
        WIF6=bytes_to_wif(C6.to_bytes(),compressed=True)
        WIF7=bytes_to_wif(C7.to_bytes(),compressed=True)
        WIF8=bytes_to_wif(C8.to_bytes(),compressed=True)
        WIF9=bytes_to_wif(C9.to_bytes(),compressed=True)
        WIF10=bytes_to_wif(C10.to_bytes(),compressed=True)
        WIF11=bytes_to_wif(C11.to_bytes(),compressed=True)
        WIF12=bytes_to_wif(C12.to_bytes(),compressed=True)
        WIF13=bytes_to_wif(C13.to_bytes(),compressed=True)
        WIF14=bytes_to_wif(C14.to_bytes(),compressed=True)
        WIF15=bytes_to_wif(C15.to_bytes(),compressed=True)
        WIF16=bytes_to_wif(C16.to_bytes(),compressed=True)
        WIF17=bytes_to_wif(C17.to_bytes(),compressed=True)
        WIF18=bytes_to_wif(C18.to_bytes(),compressed=True)
        WIF19=bytes_to_wif(C19.to_bytes(),compressed=True)
        WIF20=bytes_to_wif(C20.to_bytes(),compressed=True)
        WIF21=bytes_to_wif(C21.to_bytes(),compressed=True)
        WIF22=bytes_to_wif(C22.to_bytes(),compressed=True)
        WIF23=bytes_to_wif(C23.to_bytes(),compressed=True)
        WIF24=bytes_to_wif(C24.to_bytes(),compressed=True)
        WIF25=bytes_to_wif(C25.to_bytes(),compressed=True)
        WIF26=bytes_to_wif(C26.to_bytes(),compressed=True)
        WIF27=bytes_to_wif(C27.to_bytes(),compressed=True)
        WIF28=bytes_to_wif(C28.to_bytes(),compressed=True)
        WIF29=bytes_to_wif(C29.to_bytes(),compressed=True)
        WIF30=bytes_to_wif(C30.to_bytes(),compressed=True)
        WIF31=bytes_to_wif(C31.to_bytes(),compressed=True)
        WIF32=bytes_to_wif(C32.to_bytes(),compressed=True)
        WIF33=bytes_to_wif(C33.to_bytes(),compressed=True)
        WIF34=bytes_to_wif(C34.to_bytes(),compressed=True)
        WIF35=bytes_to_wif(C35.to_bytes(),compressed=True)
        WIF36=bytes_to_wif(C36.to_bytes(),compressed=True)
        WIF37=bytes_to_wif(C37.to_bytes(),compressed=True)
        WIF38=bytes_to_wif(C38.to_bytes(),compressed=True)
        WIF39=bytes_to_wif(C39.to_bytes(),compressed=True)
        WIF40=bytes_to_wif(C40.to_bytes(),compressed=True)
        WIF41=bytes_to_wif(C41.to_bytes(),compressed=True)
        WIF42=bytes_to_wif(C42.to_bytes(),compressed=True)
        WIF43=bytes_to_wif(C43.to_bytes(),compressed=True)
        WIF44=bytes_to_wif(C44.to_bytes(),compressed=True)
        WIF45=bytes_to_wif(C45.to_bytes(),compressed=True)
        WIF46=bytes_to_wif(C46.to_bytes(),compressed=True)
        WIF47=bytes_to_wif(C47.to_bytes(),compressed=True)
        WIF48=bytes_to_wif(C48.to_bytes(),compressed=True)
        WIF49=bytes_to_wif(C49.to_bytes(),compressed=True)
        WIF50=bytes_to_wif(C50.to_bytes(),compressed=True)
        WIF51=bytes_to_wif(C51.to_bytes(),compressed=True)
        WIF52=bytes_to_wif(C52.to_bytes(),compressed=True)
        WIF53=bytes_to_wif(C53.to_bytes(),compressed=True)
        WIF54=bytes_to_wif(C54.to_bytes(),compressed=True)
        WIF55=bytes_to_wif(C55.to_bytes(),compressed=True)
        WIF56=bytes_to_wif(C56.to_bytes(),compressed=True)
        WIF57=bytes_to_wif(C57.to_bytes(),compressed=True)
        WIF58=bytes_to_wif(C58.to_bytes(),compressed=True)
        WIF59=bytes_to_wif(C59.to_bytes(),compressed=True)
        WIF60=bytes_to_wif(C60.to_bytes(),compressed=True)
        WIF61=bytes_to_wif(C61.to_bytes(),compressed=True)
        WIF62=bytes_to_wif(C62.to_bytes(),compressed=True)
        WIF63=bytes_to_wif(C63.to_bytes(),compressed=True)
        WIF64=bytes_to_wif(C64.to_bytes(),compressed=True) 
        U=Key(wif)        
        U1=Key(wif1)
        U2=Key(wif2)
        U3=Key(wif3)
        U4=Key(wif4)
        U5=Key(wif5)
        U6=Key(wif6)
        U7=Key(wif7)
        U8=Key(wif8)
        U9=Key(wif9)
        U10=Key(wif10)
        U11=Key(wif11)
        U12=Key(wif12)
        U13=Key(wif13)
        U14=Key(wif14)
        U15=Key(wif15)
        U16=Key(wif16)
        U17=Key(wif17)
        U18=Key(wif18)
        U19=Key(wif19)
        U20=Key(wif20)
        U21=Key(wif21)
        U22=Key(wif22)
        U23=Key(wif23)
        U24=Key(wif24)
        U25=Key(wif25)
        U26=Key(wif26)
        U27=Key(wif27)
        U28=Key(wif28)
        U29=Key(wif29)
        U30=Key(wif30)
        U31=Key(wif31)
        U32=Key(wif32)
        U33=Key(wif33)
        U34=Key(wif34)
        U35=Key(wif35)
        U36=Key(wif36)
        U37=Key(wif37)
        U38=Key(wif38)
        U39=Key(wif39)
        U40=Key(wif40)
        U41=Key(wif41)
        U42=Key(wif42)
        U43=Key(wif43)
        U44=Key(wif44)
        U45=Key(wif45)
        U46=Key(wif46)
        U47=Key(wif47)
        U48=Key(wif48)
        U49=Key(wif49)
        U50=Key(wif50)
        U51=Key(wif51)
        U52=Key(wif52)
        U53=Key(wif53)
        U54=Key(wif54)
        U55=Key(wif55)
        U56=Key(wif56)
        U57=Key(wif57)
        U58=Key(wif58)
        U59=Key(wif59)
        U60=Key(wif60)
        U61=Key(wif61)
        U62=Key(wif62)
        U63=Key(wif63)
        U64=Key(wif64)
        uaddr = U.address
        uaddr1 = U1.address
        uaddr2 = U2.address
        uaddr3 = U3.address
        uaddr4 = U4.address
        uaddr5 = U5.address
        uaddr6 = U6.address
        uaddr7 = U7.address
        uaddr8 = U8.address
        uaddr9 = U9.address
        uaddr10 = U10.address
        uaddr11 = U11.address
        uaddr12 = U12.address
        uaddr13 = U13.address
        uaddr14 = U14.address
        uaddr15 = U15.address
        uaddr16 = U16.address
        uaddr17 = U17.address
        uaddr18 = U18.address
        uaddr19 = U19.address
        uaddr20 = U20.address
        uaddr21 = U21.address
        uaddr22 = U22.address
        uaddr23 = U23.address
        uaddr24 = U24.address
        uaddr25 = U25.address
        uaddr26 = U26.address
        uaddr27 = U27.address
        uaddr28 = U28.address
        uaddr29 = U29.address
        uaddr30 = U30.address
        uaddr31 = U31.address
        uaddr32 = U32.address
        uaddr33 = U33.address
        uaddr34 = U34.address
        uaddr35 = U35.address
        uaddr36 = U36.address
        uaddr37 = U37.address
        uaddr38 = U38.address
        uaddr39 = U39.address
        uaddr40 = U40.address
        uaddr41 = U41.address
        uaddr42 = U42.address
        uaddr43 = U43.address
        uaddr44 = U44.address
        uaddr45 = U45.address
        uaddr46 = U46.address
        uaddr47 = U47.address
        uaddr48 = U48.address
        uaddr49 = U49.address
        uaddr50 = U50.address
        uaddr51 = U51.address
        uaddr52 = U52.address
        uaddr53 = U53.address
        uaddr54 = U54.address
        uaddr55 = U55.address
        uaddr56 = U56.address
        uaddr57 = U57.address
        uaddr58 = U58.address
        uaddr59 = U59.address
        uaddr60 = U60.address
        uaddr61 = U61.address
        uaddr62 = U62.address
        uaddr63 = U63.address
        uaddr64 = U64.address
        caddr = C.address
        caddr1 = C1.address
        caddr2 = C2.address
        caddr3 = C3.address
        caddr4 = C4.address
        caddr5 = C5.address
        caddr6 = C6.address
        caddr7 = C7.address
        caddr8 = C8.address
        caddr9 = C9.address
        caddr10 = C10.address
        caddr11 = C11.address
        caddr12 = C12.address
        caddr13 = C13.address
        caddr14 = C14.address
        caddr15 = C15.address
        caddr16 = C16.address
        caddr17 = C17.address
        caddr18 = C18.address
        caddr19 = C19.address
        caddr20 = C20.address
        caddr21 = C21.address
        caddr22 = C22.address
        caddr23 = C23.address
        caddr24 = C24.address
        caddr25 = C25.address
        caddr26 = C26.address
        caddr27 = C27.address
        caddr28 = C28.address
        caddr29 = C29.address
        caddr30 = C30.address
        caddr31 = C31.address
        caddr32 = C32.address
        caddr33 = C33.address
        caddr34 = C34.address
        caddr35 = C35.address
        caddr36 = C36.address
        caddr37 = C37.address
        caddr38 = C38.address
        caddr39 = C39.address
        caddr40 = C40.address
        caddr41 = C41.address
        caddr42 = C42.address
        caddr43 = C43.address
        caddr44 = C44.address
        caddr45 = C45.address
        caddr46 = C46.address
        caddr47 = C47.address
        caddr48 = C48.address
        caddr49 = C49.address
        caddr50 = C50.address
        caddr51 = C51.address
        caddr52 = C52.address
        caddr53 = C53.address
        caddr54 = C54.address
        caddr55 = C55.address
        caddr56 = C56.address
        caddr57 = C57.address
        caddr58 = C58.address
        caddr59 = C59.address
        caddr60 = C60.address
        caddr61 = C61.address
        caddr62 = C62.address
        caddr63 = C63.address
        caddr64 = C64.address
        saddr = C.segwit_address
        saddr1 = C1.segwit_address
        saddr2 = C2.segwit_address
        saddr3 = C3.segwit_address
        saddr4 = C4.segwit_address
        saddr5 = C5.segwit_address
        saddr6 = C6.segwit_address
        saddr7 = C7.segwit_address
        saddr8 = C8.segwit_address
        saddr9 = C9.segwit_address
        saddr10 = C10.segwit_address
        saddr11 = C11.segwit_address
        saddr12 = C12.segwit_address
        saddr13 = C13.segwit_address
        saddr14 = C14.segwit_address
        saddr15 = C15.segwit_address
        saddr16 = C16.segwit_address
        saddr17 = C17.segwit_address
        saddr18 = C18.segwit_address
        saddr19 = C19.segwit_address
        saddr20 = C20.segwit_address
        saddr21 = C21.segwit_address
        saddr22 = C22.segwit_address
        saddr23 = C23.segwit_address
        saddr24 = C24.segwit_address
        saddr25 = C25.segwit_address
        saddr26 = C26.segwit_address
        saddr27 = C27.segwit_address
        saddr28 = C28.segwit_address
        saddr29 = C29.segwit_address
        saddr30 = C30.segwit_address
        saddr31 = C31.segwit_address
        saddr32 = C32.segwit_address
        saddr33 = C33.segwit_address
        saddr34 = C34.segwit_address
        saddr35 = C35.segwit_address
        saddr36 = C36.segwit_address
        saddr37 = C37.segwit_address
        saddr38 = C38.segwit_address
        saddr39 = C39.segwit_address
        saddr40 = C40.segwit_address
        saddr41 = C41.segwit_address
        saddr42 = C42.segwit_address
        saddr43 = C43.segwit_address
        saddr44 = C44.segwit_address
        saddr45 = C45.segwit_address
        saddr46 = C46.segwit_address
        saddr47 = C47.segwit_address
        saddr48 = C48.segwit_address
        saddr49 = C49.segwit_address
        saddr50 = C50.segwit_address
        saddr51 = C51.segwit_address
        saddr52 = C52.segwit_address
        saddr53 = C53.segwit_address
        saddr54 = C54.segwit_address
        saddr55 = C55.segwit_address
        saddr56 = C56.segwit_address
        saddr57 = C57.segwit_address
        saddr58 = C58.segwit_address
        saddr59 = C59.segwit_address
        saddr60 = C60.segwit_address
        saddr61 = C61.segwit_address
        saddr62 = C62.segwit_address
        saddr63 = C63.segwit_address
        saddr64 = C64.segwit_address
        count+=1
        totalkey+=65
        total+=195        
        if caddr in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C.to_hex())
            f.write('\nBitcoin Address: ' + C.address)
            f.write('\nPrivateKey (wif): ' + C.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U.to_hex())
            f.write('\nBitcoin Address: ' + U.address)
            f.write('\nPrivateKey (wif): ' + U.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C.to_hex())
            f.write('\nBitcoin Address: ' + C.segwit_address)
            f.write('\nPrivateKey (wif): ' + C.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr1 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C1.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C1.to_hex())
            f.write('\nBitcoin Address: ' + C1.address)
            f.write('\nPrivateKey (wif): ' + C1.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr1 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U1.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U1.to_hex())
            f.write('\nBitcoin Address: ' + U1.address)
            f.write('\nPrivateKey (wif): ' + U1.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr1 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C1.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C1.to_hex())
            f.write('\nBitcoin Address: ' + C1.segwit_address)
            f.write('\nPrivateKey (wif): ' + C1.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr2 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C2.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C2.to_hex())
            f.write('\nBitcoin Address: ' + C2.address)
            f.write('\nPrivateKey (wif): ' + C2.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr2 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U2.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U2.to_hex())
            f.write('\nBitcoin Address: ' + U2.address)
            f.write('\nPrivateKey (wif): ' + U2.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr2 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C2.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C2.to_hex())
            f.write('\nBitcoin Address: ' + C2.segwit_address)
            f.write('\nPrivateKey (wif): ' + C2.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr3 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C3.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C3.to_hex())
            f.write('\nBitcoin Address: ' + C3.address)
            f.write('\nPrivateKey (wif): ' + C3.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr3 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U3.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U3.to_hex())
            f.write('\nBitcoin Address: ' + U3.address)
            f.write('\nPrivateKey (wif): ' + U3.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr3 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C3.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C3.to_hex())
            f.write('\nBitcoin Address: ' + C3.segwit_address)
            f.write('\nPrivateKey (wif): ' + C3.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr4 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C4.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C4.to_hex())
            f.write('\nBitcoin Address: ' + C4.address)
            f.write('\nPrivateKey (wif): ' + C4.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr4 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U4.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U4.to_hex())
            f.write('\nBitcoin Address: ' + U4.address)
            f.write('\nPrivateKey (wif): ' + U4.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr4 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C4.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C4.to_hex())
            f.write('\nBitcoin Address: ' + C4.segwit_address)
            f.write('\nPrivateKey (wif): ' + C4.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr5 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C5.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C5.to_hex())
            f.write('\nBitcoin Address: ' + C5.address)
            f.write('\nPrivateKey (wif): ' + C5.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr5 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U5.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U5.to_hex())
            f.write('\nBitcoin Address: ' + U5.address)
            f.write('\nPrivateKey (wif): ' + U5.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr5 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C5.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C5.to_hex())
            f.write('\nBitcoin Address: ' + C5.segwit_address)
            f.write('\nPrivateKey (wif): ' + C5.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr6 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C6.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C6.to_hex())
            f.write('\nBitcoin Address: ' + C6.address)
            f.write('\nPrivateKey (wif): ' + C6.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr6 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U6.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U6.to_hex())
            f.write('\nBitcoin Address: ' + U6.address)
            f.write('\nPrivateKey (wif): ' + U6.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr6 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C6.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C6.to_hex())
            f.write('\nBitcoin Address: ' + C6.segwit_address)
            f.write('\nPrivateKey (wif): ' + C6.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr7 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C7.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C7.to_hex())
            f.write('\nBitcoin Address: ' + C7.address)
            f.write('\nPrivateKey (wif): ' + C7.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr7 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U7.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U7.to_hex())
            f.write('\nBitcoin Address: ' + U7.address)
            f.write('\nPrivateKey (wif): ' + U7.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr7 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C7.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C7.to_hex())
            f.write('\nBitcoin Address: ' + C7.segwit_address)
            f.write('\nPrivateKey (wif): ' + C7.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr8 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C8.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C8.to_hex())
            f.write('\nBitcoin Address: ' + C8.address)
            f.write('\nPrivateKey (wif): ' + C8.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr8 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U8.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U8.to_hex())
            f.write('\nBitcoin Address: ' + U8.address)
            f.write('\nPrivateKey (wif): ' + U8.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr8 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C8.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C8.to_hex())
            f.write('\nBitcoin Address: ' + C8.segwit_address)
            f.write('\nPrivateKey (wif): ' + C8.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr9 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C9.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C9.to_hex())
            f.write('\nBitcoin Address: ' + C9.address)
            f.write('\nPrivateKey (wif): ' + C9.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr9 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U9.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U9.to_hex())
            f.write('\nBitcoin Address: ' + U9.address)
            f.write('\nPrivateKey (wif): ' + U9.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr9 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C9.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C9.to_hex())
            f.write('\nBitcoin Address: ' + C9.segwit_address)
            f.write('\nPrivateKey (wif): ' + C9.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr10 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C10.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C10.to_hex())
            f.write('\nBitcoin Address: ' + C10.address)
            f.write('\nPrivateKey (wif): ' + C10.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr10 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U10.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U10.to_hex())
            f.write('\nBitcoin Address: ' + U10.address)
            f.write('\nPrivateKey (wif): ' + U10.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr10 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C10.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C10.to_hex())
            f.write('\nBitcoin Address: ' + C10.segwit_address)
            f.write('\nPrivateKey (wif): ' + C10.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr11 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C11.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C11.to_hex())
            f.write('\nBitcoin Address: ' + C11.address)
            f.write('\nPrivateKey (wif): ' + C11.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr11 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U11.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U11.to_hex())
            f.write('\nBitcoin Address: ' + U11.address)
            f.write('\nPrivateKey (wif): ' + U11.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr11 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C11.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C11.to_hex())
            f.write('\nBitcoin Address: ' + C11.segwit_address)
            f.write('\nPrivateKey (wif): ' + C11.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr12 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C12.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C12.to_hex())
            f.write('\nBitcoin Address: ' + C12.address)
            f.write('\nPrivateKey (wif): ' + C12.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr12 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U12.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U12.to_hex())
            f.write('\nBitcoin Address: ' + U12.address)
            f.write('\nPrivateKey (wif): ' + U12.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr12 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C12.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C12.to_hex())
            f.write('\nBitcoin Address: ' + C12.segwit_address)
            f.write('\nPrivateKey (wif): ' + C12.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr13 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C13.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C13.to_hex())
            f.write('\nBitcoin Address: ' + C13.address)
            f.write('\nPrivateKey (wif): ' + C13.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr13 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U13.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U13.to_hex())
            f.write('\nBitcoin Address: ' + U13.address)
            f.write('\nPrivateKey (wif): ' + U13.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr13 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C13.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C13.to_hex())
            f.write('\nBitcoin Address: ' + C13.segwit_address)
            f.write('\nPrivateKey (wif): ' + C13.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr14 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C14.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C14.to_hex())
            f.write('\nBitcoin Address: ' + C14.address)
            f.write('\nPrivateKey (wif): ' + C14.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr14 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U14.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U14.to_hex())
            f.write('\nBitcoin Address: ' + U14.address)
            f.write('\nPrivateKey (wif): ' + U14.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr14 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C14.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C14.to_hex())
            f.write('\nBitcoin Address: ' + C14.segwit_address)
            f.write('\nPrivateKey (wif): ' + C14.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr15 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C15.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C15.to_hex())
            f.write('\nBitcoin Address: ' + C15.address)
            f.write('\nPrivateKey (wif): ' + C15.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr15 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U15.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U15.to_hex())
            f.write('\nBitcoin Address: ' + U15.address)
            f.write('\nPrivateKey (wif): ' + U15.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr15 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C15.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C15.to_hex())
            f.write('\nBitcoin Address: ' + C15.segwit_address)
            f.write('\nPrivateKey (wif): ' + C15.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr16 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C16.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C16.to_hex())
            f.write('\nBitcoin Address: ' + C16.address)
            f.write('\nPrivateKey (wif): ' + C16.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr16 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U16.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U16.to_hex())
            f.write('\nBitcoin Address: ' + U16.address)
            f.write('\nPrivateKey (wif): ' + U16.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr16 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C16.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C16.to_hex())
            f.write('\nBitcoin Address: ' + C16.segwit_address)
            f.write('\nPrivateKey (wif): ' + C16.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr17 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C17.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C17.to_hex())
            f.write('\nBitcoin Address: ' + C17.address)
            f.write('\nPrivateKey (wif): ' + C17.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr17 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U17.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U17.to_hex())
            f.write('\nBitcoin Address: ' + U17.address)
            f.write('\nPrivateKey (wif): ' + U17.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr17 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C17.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C17.to_hex())
            f.write('\nBitcoin Address: ' + C17.segwit_address)
            f.write('\nPrivateKey (wif): ' + C17.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr18 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C18.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C18.to_hex())
            f.write('\nBitcoin Address: ' + C18.address)
            f.write('\nPrivateKey (wif): ' + C18.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr18 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U18.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U18.to_hex())
            f.write('\nBitcoin Address: ' + U18.address)
            f.write('\nPrivateKey (wif): ' + U18.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr18 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C18.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C18.to_hex())
            f.write('\nBitcoin Address: ' + C18.segwit_address)
            f.write('\nPrivateKey (wif): ' + C8.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr19 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C19.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C19.to_hex())
            f.write('\nBitcoin Address: ' + C19.address)
            f.write('\nPrivateKey (wif): ' + C19.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr19 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U19.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U19.to_hex())
            f.write('\nBitcoin Address: ' + U19.address)
            f.write('\nPrivateKey (wif): ' + U19.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr19 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C19.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C19.to_hex())
            f.write('\nBitcoin Address: ' + C19.segwit_address)
            f.write('\nPrivateKey (wif): ' + C9.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr20 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C20.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C20.to_hex())
            f.write('\nBitcoin Address: ' + C20.address)
            f.write('\nPrivateKey (wif): ' + C20.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr20 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U20.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U20.to_hex())
            f.write('\nBitcoin Address: ' + U20.address)
            f.write('\nPrivateKey (wif): ' + U20.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr20 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C20.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C20.to_hex())
            f.write('\nBitcoin Address: ' + C20.segwit_address)
            f.write('\nPrivateKey (wif): ' + C20.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr21 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C21.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C21.to_hex())
            f.write('\nBitcoin Address: ' + C21.address)
            f.write('\nPrivateKey (wif): ' + C21.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr21 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U21.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U21.to_hex())
            f.write('\nBitcoin Address: ' + U21.address)
            f.write('\nPrivateKey (wif): ' + U21.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr21 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C21.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C21.to_hex())
            f.write('\nBitcoin Address: ' + C21.segwit_address)
            f.write('\nPrivateKey (wif): ' + C1.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr22 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C22.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C22.to_hex())
            f.write('\nBitcoin Address: ' + C22.address)
            f.write('\nPrivateKey (wif): ' + C22.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr22 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U22.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U22.to_hex())
            f.write('\nBitcoin Address: ' + U22.address)
            f.write('\nPrivateKey (wif): ' + U22.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr22 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C22.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C22.to_hex())
            f.write('\nBitcoin Address: ' + C22.segwit_address)
            f.write('\nPrivateKey (wif): ' + C22.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr23 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C23.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C23.to_hex())
            f.write('\nBitcoin Address: ' + C23.address)
            f.write('\nPrivateKey (wif): ' + C23.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr23 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U23.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U23.to_hex())
            f.write('\nBitcoin Address: ' + U23.address)
            f.write('\nPrivateKey (wif): ' + U23.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr23 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C23.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C23.to_hex())
            f.write('\nBitcoin Address: ' + C23.segwit_address)
            f.write('\nPrivateKey (wif): ' + C23.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr24 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C24.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C24.to_hex())
            f.write('\nBitcoin Address: ' + C24.address)
            f.write('\nPrivateKey (wif): ' + C24.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr24 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U24.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U24.to_hex())
            f.write('\nBitcoin Address: ' + U24.address)
            f.write('\nPrivateKey (wif): ' + U24.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr24 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C24.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C24.to_hex())
            f.write('\nBitcoin Address: ' + C24.segwit_address)
            f.write('\nPrivateKey (wif): ' + C4.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr25 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C25.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C25.to_hex())
            f.write('\nBitcoin Address: ' + C25.address)
            f.write('\nPrivateKey (wif): ' + C25.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr25 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U25.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U25.to_hex())
            f.write('\nBitcoin Address: ' + U25.address)
            f.write('\nPrivateKey (wif): ' + U25.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr25 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C25.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C25.to_hex())
            f.write('\nBitcoin Address: ' + C25.segwit_address)
            f.write('\nPrivateKey (wif): ' + C25.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr26 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C26.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C26.to_hex())
            f.write('\nBitcoin Address: ' + C26.address)
            f.write('\nPrivateKey (wif): ' + C26.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr26 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U26.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U26.to_hex())
            f.write('\nBitcoin Address: ' + U26.address)
            f.write('\nPrivateKey (wif): ' + U26.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr26 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C26.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C26.to_hex())
            f.write('\nBitcoin Address: ' + C26.segwit_address)
            f.write('\nPrivateKey (wif): ' + C26.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr27 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C27.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C27.to_hex())
            f.write('\nBitcoin Address: ' + C27.address)
            f.write('\nPrivateKey (wif): ' + C27.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr27 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U27.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U27.to_hex())
            f.write('\nBitcoin Address: ' + U27.address)
            f.write('\nPrivateKey (wif): ' + U27.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr27 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C27.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C27.to_hex())
            f.write('\nBitcoin Address: ' + C27.segwit_address)
            f.write('\nPrivateKey (wif): ' + C27.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr28 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C28.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C28.to_hex())
            f.write('\nBitcoin Address: ' + C28.address)
            f.write('\nPrivateKey (wif): ' + C28.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr28 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U28.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U28.to_hex())
            f.write('\nBitcoin Address: ' + U28.address)
            f.write('\nPrivateKey (wif): ' + U28.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr28 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C28.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C28.to_hex())
            f.write('\nBitcoin Address: ' + C28.segwit_address)
            f.write('\nPrivateKey (wif): ' + C28.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr29 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C29.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C29.to_hex())
            f.write('\nBitcoin Address: ' + C29.address)
            f.write('\nPrivateKey (wif): ' + C29.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr29 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U29.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U29.to_hex())
            f.write('\nBitcoin Address: ' + U29.address)
            f.write('\nPrivateKey (wif): ' + U29.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr29 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C29.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C29.to_hex())
            f.write('\nBitcoin Address: ' + C29.segwit_address)
            f.write('\nPrivateKey (wif): ' + C29.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr30 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C30.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C30.to_hex())
            f.write('\nBitcoin Address: ' + C30.address)
            f.write('\nPrivateKey (wif): ' + C30.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr30 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U30.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U30.to_hex())
            f.write('\nBitcoin Address: ' + U30.address)
            f.write('\nPrivateKey (wif): ' + U30.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr30 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C30.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C30.to_hex())
            f.write('\nBitcoin Address: ' + C30.segwit_address)
            f.write('\nPrivateKey (wif): ' + C0.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr31 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C31.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C31.to_hex())
            f.write('\nBitcoin Address: ' + C31.address)
            f.write('\nPrivateKey (wif): ' + C31.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr31 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U31.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U31.to_hex())
            f.write('\nBitcoin Address: ' + U31.address)
            f.write('\nPrivateKey (wif): ' + U31.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr31 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C31.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C31.to_hex())
            f.write('\nBitcoin Address: ' + C31.segwit_address)
            f.write('\nPrivateKey (wif): ' + C31.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr32 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C32.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C32.to_hex())
            f.write('\nBitcoin Address: ' + C32.address)
            f.write('\nPrivateKey (wif): ' + C32.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr32 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U32.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U32.to_hex())
            f.write('\nBitcoin Address: ' + U32.address)
            f.write('\nPrivateKey (wif): ' + U32.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr32 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C32.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C32.to_hex())
            f.write('\nBitcoin Address: ' + C32.segwit_address)
            f.write('\nPrivateKey (wif): ' + C32.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr33 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C33.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C33.to_hex())
            f.write('\nBitcoin Address: ' + C33.address)
            f.write('\nPrivateKey (wif): ' + C33.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr33 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U33.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U33.to_hex())
            f.write('\nBitcoin Address: ' + U33.address)
            f.write('\nPrivateKey (wif): ' + U33.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr33 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C33.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C33.to_hex())
            f.write('\nBitcoin Address: ' + C33.segwit_address)
            f.write('\nPrivateKey (wif): ' + C33.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr34 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C34.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C34.to_hex())
            f.write('\nBitcoin Address: ' + C34.address)
            f.write('\nPrivateKey (wif): ' + C34.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr34 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U34.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U34.to_hex())
            f.write('\nBitcoin Address: ' + U34.address)
            f.write('\nPrivateKey (wif): ' + U34.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr34 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C34.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C34.to_hex())
            f.write('\nBitcoin Address: ' + C34.segwit_address)
            f.write('\nPrivateKey (wif): ' + C34.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr35 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C35.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C35.to_hex())
            f.write('\nBitcoin Address: ' + C35.address)
            f.write('\nPrivateKey (wif): ' + C35.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr35 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U35.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U35.to_hex())
            f.write('\nBitcoin Address: ' + U35.address)
            f.write('\nPrivateKey (wif): ' + U35.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr35 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C35.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C35.to_hex())
            f.write('\nBitcoin Address: ' + C35.segwit_address)
            f.write('\nPrivateKey (wif): ' + C35.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr36 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C36.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C36.to_hex())
            f.write('\nBitcoin Address: ' + C36.address)
            f.write('\nPrivateKey (wif): ' + C36.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr36 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U36.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U36.to_hex())
            f.write('\nBitcoin Address: ' + U36.address)
            f.write('\nPrivateKey (wif): ' + U36.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr36 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C36.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C36.to_hex())
            f.write('\nBitcoin Address: ' + C36.segwit_address)
            f.write('\nPrivateKey (wif): ' + C36.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr37 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C37.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C37.to_hex())
            f.write('\nBitcoin Address: ' + C37.address)
            f.write('\nPrivateKey (wif): ' + C37.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr37 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U37.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U37.to_hex())
            f.write('\nBitcoin Address: ' + U37.address)
            f.write('\nPrivateKey (wif): ' + U37.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr37 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C37.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C37.to_hex())
            f.write('\nBitcoin Address: ' + C37.segwit_address)
            f.write('\nPrivateKey (wif): ' + C37.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr38 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C38.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C38.to_hex())
            f.write('\nBitcoin Address: ' + C38.address)
            f.write('\nPrivateKey (wif): ' + C38.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr38 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U38.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U38.to_hex())
            f.write('\nBitcoin Address: ' + U38.address)
            f.write('\nPrivateKey (wif): ' + U38.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr38 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C38.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C38.to_hex())
            f.write('\nBitcoin Address: ' + C38.segwit_address)
            f.write('\nPrivateKey (wif): ' + C38.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr39 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C39.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C39.to_hex())
            f.write('\nBitcoin Address: ' + C39.address)
            f.write('\nPrivateKey (wif): ' + C39.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr39 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U39.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U39.to_hex())
            f.write('\nBitcoin Address: ' + U39.address)
            f.write('\nPrivateKey (wif): ' + U39.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr39 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C39.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C39.to_hex())
            f.write('\nBitcoin Address: ' + C39.segwit_address)
            f.write('\nPrivateKey (wif): ' + C39.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr40 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C40.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C40.to_hex())
            f.write('\nBitcoin Address: ' + C40.address)
            f.write('\nPrivateKey (wif): ' + C40.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr40 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U40.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U40.to_hex())
            f.write('\nBitcoin Address: ' + U40.address)
            f.write('\nPrivateKey (wif): ' + U40.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr40 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C40.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C40.to_hex())
            f.write('\nBitcoin Address: ' + C40.segwit_address)
            f.write('\nPrivateKey (wif): ' + C40.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr41 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C41.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C41.to_hex())
            f.write('\nBitcoin Address: ' + C41.address)
            f.write('\nPrivateKey (wif): ' + C41.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr41 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U41.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U41.to_hex())
            f.write('\nBitcoin Address: ' + U41.address)
            f.write('\nPrivateKey (wif): ' + U41.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr41 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C41.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C41.to_hex())
            f.write('\nBitcoin Address: ' + C41.segwit_address)
            f.write('\nPrivateKey (wif): ' + C41.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr42 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C42.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C42.to_hex())
            f.write('\nBitcoin Address: ' + C42.address)
            f.write('\nPrivateKey (wif): ' + C42.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr42 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U42.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U42.to_hex())
            f.write('\nBitcoin Address: ' + U42.address)
            f.write('\nPrivateKey (wif): ' + U42.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr42 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C42.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C42.to_hex())
            f.write('\nBitcoin Address: ' + C42.segwit_address)
            f.write('\nPrivateKey (wif): ' + C42.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr43 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C43.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C43.to_hex())
            f.write('\nBitcoin Address: ' + C43.address)
            f.write('\nPrivateKey (wif): ' + C43.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr43 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U43.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U43.to_hex())
            f.write('\nBitcoin Address: ' + U43.address)
            f.write('\nPrivateKey (wif): ' + U43.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr43 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C43.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C43.to_hex())
            f.write('\nBitcoin Address: ' + C43.segwit_address)
            f.write('\nPrivateKey (wif): ' + C43.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr44 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C44.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C44.to_hex())
            f.write('\nBitcoin Address: ' + C44.address)
            f.write('\nPrivateKey (wif): ' + C44.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr44 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U44.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U44.to_hex())
            f.write('\nBitcoin Address: ' + U44.address)
            f.write('\nPrivateKey (wif): ' + U44.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr44 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C44.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C44.to_hex())
            f.write('\nBitcoin Address: ' + C44.segwit_address)
            f.write('\nPrivateKey (wif): ' + C44.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr45 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C45.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C45.to_hex())
            f.write('\nBitcoin Address: ' + C45.address)
            f.write('\nPrivateKey (wif): ' + C45.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr45 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U45.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U45.to_hex())
            f.write('\nBitcoin Address: ' + U45.address)
            f.write('\nPrivateKey (wif): ' + U45.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr45 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C45.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C45.to_hex())
            f.write('\nBitcoin Address: ' + C45.segwit_address)
            f.write('\nPrivateKey (wif): ' + C45.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr46 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C46.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C46.to_hex())
            f.write('\nBitcoin Address: ' + C46.address)
            f.write('\nPrivateKey (wif): ' + C46.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr46 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U46.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U46.to_hex())
            f.write('\nBitcoin Address: ' + U46.address)
            f.write('\nPrivateKey (wif): ' + U46.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr46 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C46.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C46.to_hex())
            f.write('\nBitcoin Address: ' + C46.segwit_address)
            f.write('\nPrivateKey (wif): ' + C46.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr47 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C47.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C47.to_hex())
            f.write('\nBitcoin Address: ' + C47.address)
            f.write('\nPrivateKey (wif): ' + C47.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr47 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U47.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U47.to_hex())
            f.write('\nBitcoin Address: ' + U47.address)
            f.write('\nPrivateKey (wif): ' + U47.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr47 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C47.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C47.to_hex())
            f.write('\nBitcoin Address: ' + C47.segwit_address)
            f.write('\nPrivateKey (wif): ' + C47.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr48 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C48.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C48.to_hex())
            f.write('\nBitcoin Address: ' + C48.address)
            f.write('\nPrivateKey (wif): ' + C48.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr48 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U48.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U48.to_hex())
            f.write('\nBitcoin Address: ' + U48.address)
            f.write('\nPrivateKey (wif): ' + U48.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr48 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C48.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C48.to_hex())
            f.write('\nBitcoin Address: ' + C48.segwit_address)
            f.write('\nPrivateKey (wif): ' + C48.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr49 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C49.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C49.to_hex())
            f.write('\nBitcoin Address: ' + C49.address)
            f.write('\nPrivateKey (wif): ' + C49.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr49 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U49.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U49.to_hex())
            f.write('\nBitcoin Address: ' + U49.address)
            f.write('\nPrivateKey (wif): ' + U49.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr49 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C49.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C49.to_hex())
            f.write('\nBitcoin Address: ' + C49.segwit_address)
            f.write('\nPrivateKey (wif): ' + C49.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr50 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C50.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C50.to_hex())
            f.write('\nBitcoin Address: ' + C50.address)
            f.write('\nPrivateKey (wif): ' + C50.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr50 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U50.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U50.to_hex())
            f.write('\nBitcoin Address: ' + U50.address)
            f.write('\nPrivateKey (wif): ' + U50.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr50 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C50.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C50.to_hex())
            f.write('\nBitcoin Address: ' + C50.segwit_address)
            f.write('\nPrivateKey (wif): ' + C50.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr51 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C51.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C51.to_hex())
            f.write('\nBitcoin Address: ' + C51.address)
            f.write('\nPrivateKey (wif): ' + C51.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr51 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U51.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U51.to_hex())
            f.write('\nBitcoin Address: ' + U51.address)
            f.write('\nPrivateKey (wif): ' + U51.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr51 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C51.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C51.to_hex())
            f.write('\nBitcoin Address: ' + C51.segwit_address)
            f.write('\nPrivateKey (wif): ' + C51.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr52 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C52.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C52.to_hex())
            f.write('\nBitcoin Address: ' + C52.address)
            f.write('\nPrivateKey (wif): ' + C52.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr52 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U52.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U52.to_hex())
            f.write('\nBitcoin Address: ' + U52.address)
            f.write('\nPrivateKey (wif): ' + U52.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr52 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C52.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C52.to_hex())
            f.write('\nBitcoin Address: ' + C52.segwit_address)
            f.write('\nPrivateKey (wif): ' + C52.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr53 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C53.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C53.to_hex())
            f.write('\nBitcoin Address: ' + C53.address)
            f.write('\nPrivateKey (wif): ' + C53.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr53 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U53.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U53.to_hex())
            f.write('\nBitcoin Address: ' + U53.address)
            f.write('\nPrivateKey (wif): ' + U53.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr53 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C53.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C53.to_hex())
            f.write('\nBitcoin Address: ' + C53.segwit_address)
            f.write('\nPrivateKey (wif): ' + C53.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr54 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C54.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C54.to_hex())
            f.write('\nBitcoin Address: ' + C54.address)
            f.write('\nPrivateKey (wif): ' + C54.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr54 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U54.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U54.to_hex())
            f.write('\nBitcoin Address: ' + U54.address)
            f.write('\nPrivateKey (wif): ' + U54.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr54 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C54.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C54.to_hex())
            f.write('\nBitcoin Address: ' + C54.segwit_address)
            f.write('\nPrivateKey (wif): ' + C54.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr55 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C55.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C55.to_hex())
            f.write('\nBitcoin Address: ' + C55.address)
            f.write('\nPrivateKey (wif): ' + C55.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr55 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U55.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U55.to_hex())
            f.write('\nBitcoin Address: ' + U55.address)
            f.write('\nPrivateKey (wif): ' + U55.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr55 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C55.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C55.to_hex())
            f.write('\nBitcoin Address: ' + C55.segwit_address)
            f.write('\nPrivateKey (wif): ' + C55.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr56 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C56.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C56.to_hex())
            f.write('\nBitcoin Address: ' + C56.address)
            f.write('\nPrivateKey (wif): ' + C56.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr56 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U56.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U56.to_hex())
            f.write('\nBitcoin Address: ' + U56.address)
            f.write('\nPrivateKey (wif): ' + U56.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr56 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C56.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C56.to_hex())
            f.write('\nBitcoin Address: ' + C56.segwit_address)
            f.write('\nPrivateKey (wif): ' + C56.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr57 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C57.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C57.to_hex())
            f.write('\nBitcoin Address: ' + C57.address)
            f.write('\nPrivateKey (wif): ' + C57.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr57 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U57.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U57.to_hex())
            f.write('\nBitcoin Address: ' + U57.address)
            f.write('\nPrivateKey (wif): ' + U57.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr57 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C57.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C57.to_hex())
            f.write('\nBitcoin Address: ' + C57.segwit_address)
            f.write('\nPrivateKey (wif): ' + C57.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr58 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C58.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C58.to_hex())
            f.write('\nBitcoin Address: ' + C58.address)
            f.write('\nPrivateKey (wif): ' + C58.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr58 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U58.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U58.to_hex())
            f.write('\nBitcoin Address: ' + U58.address)
            f.write('\nPrivateKey (wif): ' + U58.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr58 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C58.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C58.to_hex())
            f.write('\nBitcoin Address: ' + C58.segwit_address)
            f.write('\nPrivateKey (wif): ' + C58.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr59 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C59.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C59.to_hex())
            f.write('\nBitcoin Address: ' + C59.address)
            f.write('\nPrivateKey (wif): ' + C59.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr59 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U59.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U59.to_hex())
            f.write('\nBitcoin Address: ' + U59.address)
            f.write('\nPrivateKey (wif): ' + U59.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr59 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C59.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C59.to_hex())
            f.write('\nBitcoin Address: ' + C59.segwit_address)
            f.write('\nPrivateKey (wif): ' + C59.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr60 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C60.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C60.to_hex())
            f.write('\nBitcoin Address: ' + C60.address)
            f.write('\nPrivateKey (wif): ' + C60.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr60 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U60.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U60.to_hex())
            f.write('\nBitcoin Address: ' + U60.address)
            f.write('\nPrivateKey (wif): ' + U60.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr60 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C60.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C60.to_hex())
            f.write('\nBitcoin Address: ' + C60.segwit_address)
            f.write('\nPrivateKey (wif): ' + C60.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr61 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C61.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C61.to_hex())
            f.write('\nBitcoin Address: ' + C61.address)
            f.write('\nPrivateKey (wif): ' + C61.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr61 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U61.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U61.to_hex())
            f.write('\nBitcoin Address: ' + U61.address)
            f.write('\nPrivateKey (wif): ' + U61.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr61 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C61.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C61.to_hex())
            f.write('\nBitcoin Address: ' + C61.segwit_address)
            f.write('\nPrivateKey (wif): ' + C61.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr62 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C62.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C62.to_hex())
            f.write('\nBitcoin Address: ' + C62.address)
            f.write('\nPrivateKey (wif): ' + C62.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr62 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U62.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U62.to_hex())
            f.write('\nBitcoin Address: ' + U62.address)
            f.write('\nPrivateKey (wif): ' + U62.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr62 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C62.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C62.to_hex())
            f.write('\nBitcoin Address: ' + C62.segwit_address)
            f.write('\nPrivateKey (wif): ' + C62.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr63 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C63.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C63.to_hex())
            f.write('\nBitcoin Address: ' + C63.address)
            f.write('\nPrivateKey (wif): ' + C63.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr63 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U63.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U63.to_hex())
            f.write('\nBitcoin Address: ' + U63.address)
            f.write('\nPrivateKey (wif): ' + U63.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr63 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C63.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C63.to_hex())
            f.write('\nBitcoin Address: ' + C63.segwit_address)
            f.write('\nPrivateKey (wif): ' + C63.to_wif())
            f.write('\n==================================')
            f.close()
        if caddr64 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C64.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C64.to_hex())
            f.write('\nBitcoin Address: ' + C64.address)
            f.write('\nPrivateKey (wif): ' + C64.to_wif())
            f.write('\n==================================')
            f.close()
        if uaddr64 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + U64.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + U64.to_hex())
            f.write('\nBitcoin Address: ' + U64.address)
            f.write('\nPrivateKey (wif): ' + U64.to_wif())
            f.write('\n==================================')
            f.close()
        if saddr64 in add:
            print("\nMatching Key ==== Found!! PrivateKey: " + C64.to_wif())
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + C64.to_hex())
            f.write('\nBitcoin Address: ' + C64.segwit_address)
            f.write('\nPrivateKey (wif): ' + C64.to_wif())
            f.write('\n==================================')
            f.close()
        else:
            print ('-- btcr.py -- ' + colour_green +  'Running Scan : ' + str (count) + '  :  ' + colour_cyan + 'Total Private Keys : ' + str(totalkey) + '  :  ' + colour_red + 'Total Bitcoin Addresses : ' + str (total) + ' : ' + colour_yellow + seconds_to_str(), end='\r' + colour_reset)


if __name__ == '__main__':
  for i in range(1):
    p = multiprocessing.Process(target=spawn)
    p.start()

