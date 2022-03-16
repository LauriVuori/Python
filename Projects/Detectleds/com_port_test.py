import serial.tools.list_ports as ls 
from time import sleep

print([p.device for p in ls.comports()])
sleep(2)