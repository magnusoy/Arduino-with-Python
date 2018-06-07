from arduino_serial import ArduinoSerial

arduino = ArduinoSerial()
arduino.connect("COM4", 9600)
print("Turn LED On or Off.\n")
while arduino.isConnected():
	switch = input("Turn light:")

	if switch == "On":
		arduino.turnLedOn()
	elif switch == "Off":
		arduino.turnLedOff()
	if switch == "q":
		arduino.disconnect()
