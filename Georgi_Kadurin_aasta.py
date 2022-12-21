from math import*
from pickle import TRUE 
from random import * 
from time import*
#3
while True:
    try:
       p=int(input("Pikkus:  "))
       if p>0: break
    except: 
        print("On Numbreid kirjutada, mis on suurem kui 0")
while True:
    try:
       l=int(input("Laius: "))
       if l>0: break
    except: 
        print("On Numbreid kirjutada, mis on suurem kui 0")
while True:
    v=input("Kas tahad remonti teha")
    if v.upper()=="JAH" or v.upper()=="EI": break
if v.upper()=="JAH":
    while True:
        try:
            hind=float(input("Kui palju maksam m^2 "))
            break
        except TypeError:
            print()
    hind=l*p*hind
    print(f"Remonti hind on {hind}")
else:
    print("omg")









#üL2
while True:
    nimi1=input("Mis sinu nimi on?")
    if nimi1.isalpha(): break
while True:
    nimi2=input("Mis sinu nimi on?")
    if nimi2.isalpha(): break
if nimi1=="anna" and "Naan": print("Neid on täna pinginaabrid")
    




#Ül1
while True:
    nimi=input("Mis on sinu nimi")
    if nimi.isalpha(): break


if nimi.upper()=="JUKU":
    while True:
        try:
            vanus=int(input("Kui vana sa oled? "))
            break
        except: 
            print("On vaja arvude tüüp kasutada")

    if vanus<=0 or vanus>=100:
        print("Viga andmetega")
    elif vanus<6:
        print("Tasuta")
    elif vanus>=6 and vanus<=14:
        print("Lapse pilet")
    elif vanus>=65:
        print("Sooduspilet")
    elif vanus<=0 and vanus>=100:
        print("Viga andmetega")
else:
    print("Ma otsin Juku!")

