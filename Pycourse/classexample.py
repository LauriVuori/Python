
class asiakas:
    """Luokka määrittelee toimitettavat esineet"""
    
    kori = []
    def lisaa(self):
        esine = input("Mitä laitetaan koriin?: ")
        self.kori.append(esine)

    def kassalle(self):
        print("Korissa oli seuraavat esineet:")
        for i in range(0,len(self.kori)):
            print(self.kori[i], end = " ")

def main():
    henkilo = asiakas()
    while True:
        valinta = input("Lisätäänkö tuote vai mennäänkö kassalle?: ")
        if valinta == "kassalle":
            henkilo.kassalle()
            break
        else:
            henkilo.lisaa()
if __name__ == "__main__":
    main()