from arduino import Arduino

arduino = Arduino()
arduino.connect("COM4", 9600)
while arduino.isConnected():
    print(arduino.getData())
