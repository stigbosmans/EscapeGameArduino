import serial
import time
from socketIO_client import SocketIO, LoggingNamespace

ser = serial.Serial('COM3', 9600, timeout=0)
socketIO = SocketIO('localhost', 3000, LoggingNamespace)

def process_code(code):
    if code.find(';')>-1:
        ar=code.split(";")
        if len(ar[0])==4:
            socketIO.emit("msg",ar[0])
            socketIO.wait(seconds=1)
            print(ar[0])

def print_state(code):
    if code[0]!="0":
        print(num_to_text(code[0]),"Geel")
    if code[1]!="0":
        print(num_to_text(code[1]),"Groen")
    if code[2]!="0":
        print(num_to_text(code[2]),"Oranje")
    if code[3]!="0":
        print(num_to_text(code[3]),"Grijs")
    else:
        print("CLOCK IS TICKING!")

    if code=="1234":
        print("CORRECT!")
    elif code[0]!="0" and code[1]!="0" and code[2]!="0" and code[3]!="0":
        print("EXPLODED!")

def num_to_text(num):
    if num=="1":
       return "eerste kabel verwijderd:"
    elif num=="2":
       return "tweede kabel verwijderd:"
    elif num=="3":
       return "derde kabel verwijderd:"
    elif num=="4":
       return "vierde kabel verwijderd:"
    else:
        return ""

while True:
    bytesToRead = ser.inWaiting()
    res=ser.read(bytesToRead)
    process_code(str(res, 'ascii'))
    time.sleep(.1)
