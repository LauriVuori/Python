import webbrowser
import pickle
import os
import time
import datetime

    
# using now() to get current time  
current_time = datetime.datetime.now()  
    
# Printing attributes of now().  
print ("The attributes of now() are : ")  
    
print ("Year : ", end = "")  
print (current_time.year)  
    
print ("Month : ", end = "")  
print (current_time.month)  
    
print ("Day : ", end = "")  
print (current_time.day) 

if (current_time.day == 16 and current_time.month == 12):
    print(current_time.hour)

# url = "https://www.youtube.com/watch?v=JBRGjlF8tGY&feature=youtu.be"
# tiedosto = open("tallenne.dat","wb")
# # webbrowser.open(url)
# pickle.dump(url, tiedosto)
# tiedosto.close()
    


# tiedosto = open("tallenne.dat","rb")
# luettu = pickle.load(tiedosto)
# print("Luettiin tallenne: ",luettu)
# webbrowser.open(luettu)
# tiedosto.close()
