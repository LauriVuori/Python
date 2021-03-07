"""
	Kioskissa myytävät tuotteet on numeroitu väliltä 1-500.
	Tuotteiden varastossa olevat kappalemäärät on kirjoitettu tuotenumeron perusteella taulukkoon.
	Tuotenumeroa käytetään taulukon indeksinä.
	Vuosi-inventaarion yhteydessä taulukon sisältö kirjoitetaan uusiksi.
Kirjoita ohjelma, joka kysyy tuotenumeron ja varastossa olevan kappalemäärän. 
Kunkin tuotteen tietojen kysymisen jälkeen ohjelma kysyy, haluaako käyttäjä syöttää 
lisää tietoja, ja toimii käyttäjän toiveen mukaan. 
(Jos käyttäjä ei syötä jotain tuotenumeroa, tämä tarkoittaa, että tuotetta ei ole varastossa.)
"""
import random
# import string

def findItem(productList):
    itemNum = int(input("Give itemnum to find:\n"))
    Found = False
    for i in range(0, 500):
        if (itemNum == product[i][0]):
            print(product[i])
            Found = True
    if (Found == False):
        print("Didnt find product")


def setQuantity(productList):
    itemNum = int(input("Give item num:"))
    for i in range(0, 500):
        if (itemNum == productList[i][0]):
            print(productList[i])
            choice = input("Do you want change quantity(y/n)")
            if (choice == "y"):
                productList[i][1] = int(input("Give quantity:"))
                print("New quantity " , productList[i])
            else:
                print("Didnt change quantity")
    


product = [[]]
# for i in range(0,500):
#     if (i == 0):
#         product[0] = [i,random.randint(0,22)]
#     else:
#         product.append([i,random.randint(0,22)])
# f = open("shopdata.txt","r")
# data = f.read()

# text = data.split("\n")
# for i in range(500):
#     print(text[i])
s = '[51, 65]'
# result = ''.join([i for i in s if i.isdigit()])
str = "h3110 23 cat 444.4 rabbit 11 2 dog"
[int(s) for s in str.split() if s.isdigit()]
# mat = [[]]

# for line in content:
#     s = line.split('\n')
#     if s[0].isdigit() and len(s) <= 10:
#         mat.append(s)

# print(mat)






# print(product)

choice = "n"
while (choice != "q"):
    choice = input("A)Find item\nB)New quantity\nC)Save to File\nQ)Quit\n")
    while(len(choice) > 1):
        print("Input wrong\n")
        choice = input("A)Find item\nB)New quantity\nQ)Quit\n")
    choice = choice.lower()
    if (choice == "a"):
        findItem(product)
    elif (choice == "b"):
        setQuantity(product)
    elif (choice == "c"):
        test = open("shopdata.txt","w+")
        for i in range(500):
            test.write(str(product[i])+"\n")
        test.close()
    else:
        print("Wrong input")

print("Exit program")

# #     # product[i][0] = random.randint(0,22)
# # print(product[0][0])
# itemNum = int(input("Give item num:"))

# # [576, 534] ["tuote", "lmk"]
# # 500 tuotetta
# for i in range(0, 500):
#     if (itemNum == product[i][0]):
#         print(product[i])
#         choice = input("Do you want change quantity(y/n)")
#         if (choice == "y"):
#             product[i][1] = int(input("Give quantity:"))
#             print("New quantity " , product[i])
#         else:
#             print("Didnt change quantity")

# print(product[itemNum])
# print(product)