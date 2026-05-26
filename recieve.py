」#python C:\Users\81807\OneDrive\デスクトップ\物理部\これで世界\pyserial_test.py
import serial
import time


COM="COM10"
bitRate=115200

ser = serial.Serial(COM, bitRate, timeout=0.1)

with open(r"C:\Users\81807\OneDrive\デスクトップ\物理部\これで世界\termres.csv","w") as f:
        f.write("data" + "\n")

while True:
    time.sleep(0.1)
    result = ser.read_all()
    if str(result) != "b''":
        with open(r"C:\Users\81807\OneDrive\デスクトップ\物理部\これで世界\termres.csv","a") as c:
            text = str(result).lstrip("b'") 
            c.write(text.rstrip("\r\n\r\n'") + "\n")




print('program end')

ser.close()
