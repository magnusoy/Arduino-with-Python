from arduino_serial import Arduino

arduino = Arduino()
arduino.connect("COM4", 9600)
print("Turn LED On or Off.\n")
while arduino.isConnected():
	switch = input("Turn light:")

	if switch == "On":
		arduino.setHigh()
	elif switch == "Off":
		arduino.setLow()
	if switch == "q":
		arduino.disconnect()
