import pickle

my_list = ["Sub1","Sub2","Sub3","Sub4"]

Binfile = open("Binarytest.dat", "wb")

#print(my_list)

pickle.dump(my_list, Binfile)


Binfile = open("Binarytest.dat", "rb")

FromFile = pickle.load(Binfile)

print(FromFile)

Binfile.close()