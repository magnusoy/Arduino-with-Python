from arduino_serial import ArduinoSerial

filename = "temperature.csv"

arduino = ArduinoSerial()

arduino.createFile(filename)

arduino.connect("COM4", 9600)

while arduino.isConnected():
    t = arduino.getTimeElapsed()
    y = arduino.cleanData()
    arduino.logToFile(filename, t, y)
    if arduino.getTimeElapsed > 10:
        arduino.disconnect()
