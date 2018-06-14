from arduino import Arduino

filename = "temperature.csv"

arduino = Arduino()

arduino.createFile(filename)

arduino.connect("COM4", 9600)

while arduino.isConnected():
    data = arduino.getData()
    arduino.logDataWithTime(filename, data)
    if arduino.getTimeElapsed > 10:
        arduino.disconnect()
