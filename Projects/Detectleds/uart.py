import serial
import serial.tools.list_ports as ls 
print([p.device for p in ls.comports()])

ser = serial.Serial('COM4', 115200)  # open serial port


test = "{111}"
sendbytes = test.encode()
ser.write(sendbytes)
print("string sent:",test)