from arduino_serial import ArduinoSerial

arduino = ArduinoSerial()
arduino.connect("COM4", 9600)
while arduino.isConnected():
    arduino.readLine()
