#!/usr/bin/python
"""
Class to send and recive data from
Serial connection with an Arduino.

Code by: Magnus Øye, Dated: 05.06-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy
"""

# importing nessary libraries
import serial
import time


class Arduino():
    """ArduinoSerial is a simple library for
        doing operations with Arduino."""

    def __init__(self):
        self.connection = None
        self.port = None
        self.baudrate = None
        self.startTime = time.time()

    def connect(self, port, baudrate):
        """Creates a connection with the
            Arduino board.
            Parameters
            ----------
            port : str
                USB-port where Arduino
                is connected.
            baudrate : int
                Assign working baudrate, check
                your Arduino IDE. Normally it
                is 9600, 14400, 19200, 28800,
                 38400, 57600, or 115200."""
        self.port = port
        self.baudrate = baudrate
        self.connection = serial.Serial(port, baudrate)
        time.sleep(2)
    
    def __str__(self):
        if self.port is None:
            return "Arduino is not connected"
        else:
            return f"Arduino is on port {self.port} at {self.baudrate} baudrate"

    def getData(self):
        """Reads from the serial port.
            will wait for result before
            proceeding to next step.
            Returns
            -------
            str
                Output as a string."""
        raw = self.connection.readline()
        cleaned = raw.decode('latin-1')
        return cleaned.rstrip('\n')

    def sendCommand(self, command):
        """Sends the following command to
            Arduino board.
            Parameters
            ----------
            command: str
                    Command to be sent"""
        self.connection.write(command.encode())
        # print(f"{command} is sent to Arduino")

    def sendMultipleCommands(self, commands, delay):
        """Sends the following commands to
            Arduino board.
            Parameters
            ----------
            commands: list
                Commands to be sent
            delay: int
                Delay between each command,
                time is in seconds."""
        for command in commands:
            self.sendCommand(command)
            self.delay(delay)

    def setHigh(self):
        """Sends 1 out to Arduino board"""
        self.connection.write("1".encode())

    def setLow(self):
        """Sends 0 out to Arduino board"""
        self.connection.write("0".encode())

    def logToFile(self, filename, data):
        """Logs data to a already
            existing file.
            Parameters
            ----------
            filename: str
                filepath
            x: str
                first varibale.
            y: str
                second variable"""
        #lst = [', '.join(map(str, x)) for x in args]
        #data = ''.join(lst)
        lst = data.split(',')
        data = ','.join(lst)
        with open(filename, 'a') as file:
            file.write(f"{data}")

    def createFile(self, filename):
        """Creates a new file.
            Parameters
            ----------
            filename: str
                filepath"""
        with open(filename, 'w') as file:
            file.write("time,distance\n")

    def getTimeElapsed(self):
        """Get time since object was
            made.
            Returns
            -------
            float
                time since start
            """
        timeElapsed = time.time() - self.startTime
        return timeElapsed - 2

    def delay(self, delay):
        """Delays prosess, program
            will pause.
            Parameters
            ----------
            delay: int
                time to be delayed"""
        time.sleep(delay)

    def isConnected(self):
        """Checks if connection with
            Arduino board is true.
            Returns
            -------
            boolean
                True or False, depends
                if it is connected or not"""
        if self.connection.is_open == False:
            self.connection = None
        elif self.connection.is_open == True:
            return self.connection.is_open

    def disconnect(self):
        """Closes the connection
            with the Arduino."""
        self.connection.close()
        print("Arduino disconnected.")
        return True
