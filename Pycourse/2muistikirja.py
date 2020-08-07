# coding=utf-8

import time		
kello = time.strftime("%X %x\n")

valinta = 2
muisti = ""

nimi = "muistio.txt"

try:
    fo = open(nimi, "r+")
    fo.close()

except FileNotFoundError:
    fo = open(nimi, "w+")
    print("Oletusmuistioa ei löydy, luodaan tiedosto.")
    fo.write("")
    fo.close()

while True:
    print("Käytetään muistiota: ",nimi)
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Vaihda muistiota\n(5) Lopeta\n")
    valinta = int(input("Mitä haluat tehdä?: "))
    try:
        fo = open(nimi, "r+")
        fo.close()

    except FileNotFoundError:
        fo = open(nimi, "w+")
        print("Oletusmuistioa ei löydy, luodaan tiedosto.")
        fo.write("")
        fo.close()

    finally:
        if valinta == 1:
            fo = open(nimi, "r+")
            txt = fo.read()
            print(txt)
            fo.close()
        
        elif valinta == 2:
            fo =  open(nimi, "a+")
            muisti=input("Kirjoita uusi merkintä: ")
            fo.write(muisti+":::"+kello)
            fo.close()

        elif valinta == 3:  
            fo = open(nimi,"r+")
            fo. truncate(0)
            print("Muistio tyhjennetty.")
            fo. close()

        elif valinta == 4:
            nimi = input("Anna tiedoston nimi: ")
            try:
                fo = open(nimi, "r+")
                fo.close()

            except FileNotFoundError:
                fo = open(nimi, "w+")
                print("Tiedostoa ei löydy, luodaan tiedosto.")
                fo.write("")
                fo.close()
        elif valinta == 5:
            print("Lopetetaan.")
            fo.close() 
            exit()