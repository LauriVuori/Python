class kilpailija:
    "Kilpailija: sisältää pisteet ja värin"
    pisteet = 0
    vari1 = "sininen"
    vari2 = "sininen"

    
    def tilanne1(self):
        print("Olen ",self.vari1," ja minulla on ",self.pisteet," pistettä!")
    def tilanne2(self):
        print("Olen ",self.vari1," ja minulla on ",self.pisteet," pistettä!")
    def vari(self):
        self.vari1 = input("Anna minulle väri: ")
        self.vari2 = input("Anna minulle väri: ")
    def maali(self):
        self.pisteet += 1
        return self

def main():
    test = kilpailija()
    test.vari()
    test.tilanne1()
    test.tilanne2()
    print(test.__doc__)


if __name__ == "__main__":
    main()