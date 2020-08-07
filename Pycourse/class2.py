class Nimike:
    """Uusi luokka"""
    nimi = "Eemeli"
    suku = "Jaava"
    def nimi(self):
	    print(self.nimi, self.suku)

def main():
    test = Nimike()
    print(test.nimi)



if __name__ == "__main__":
    main()
