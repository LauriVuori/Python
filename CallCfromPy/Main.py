from ctypes import *
so_file ="/home/pi/Desktop/CallCfromPy/Cfunc.so"
Cfunc = CDLL(so_file)

print(Cfunc.power(5))