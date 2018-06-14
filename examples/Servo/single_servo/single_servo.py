from arduino_serial import Arduino

arduino = Arduino()
arduino.connect("COM4", 9600)
while arduino.isConnected():
    pos = input("Servo position: ")
    arduino.sendCommand(pos)
    if pos == "q":
        arduino.disconnect()
