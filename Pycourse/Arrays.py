"""
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 2
Listalla on 0 alkiota.
Monesko niistä poistetaan?: 1231
Virheellinen valinta.
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 6
Virheellinen valinta.
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 3
Listalla oli tuotteet:
"""
array = []

while True:
    valinta = int(input("(1)Lisätä listaan\n(2)Poistaa listalta vai \n(3)Lopettaa?: "))
    num = len(array)
    print("Listalla on ", num, "alktiota.")
    if valinta == 1:
        txt = input("Kirjoita: ")
        array.append(txt)
    elif valinta == 2:
        num = input("Monesko niistä poistetaan?: ")
        array.remove(num)
    elif valinta == 3:
        i=0
        
        maks = len(array)
        print("Listalla oli tuotteet: ")
        while i < maks:
            print(array[i])
            i+=1  
            exit()