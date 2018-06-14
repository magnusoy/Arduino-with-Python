from arduino_serial import Arduino

arduino = Arduino()
arduino.connect("COM4", 9600)
while arduino.isConnected():
    arduino.getData()
