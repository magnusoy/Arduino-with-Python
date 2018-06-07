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


class ArduinoSerial():
    """ArduinoSerial is a simple library for
        doing operations with Arduino."""

    def __init__(self):
        super(ArduinoSerial, self).__init__()
        self.connection = None
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
        self.connection = serial.Serial(port, baudrate)
        time.sleep(2)
        print(f"Connection with {port} at {baudrate} braudrate made.")

    def readLine(self):
        """Reads from the serial port.
            Will wait for result before
            proceeding to next step.
            Returns
            -------
            byte
                Returns a byte of string."""
        print(self.connection.readline())
        return self.connection.readline()

    def continuousReadLine(self):
        if self.connection.inWaiting() > 0:
            self.readLine()

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

    def turnLedOn(self):
        """Sends 1 to Arduino board"""
        self.connection.write("1".encode())

    def turnLedOff(self):
        """Sends 0 to Arduino board"""
        self.connection.write("0".encode())

    def cleanData(self):
        """Remove unnecessary text from
            readLine. Leaving only the
            recived text or number.
            Returns
            -------
            str
            cleaned string"""
        rawData = self.connection.readline()
        cleanedData = str(rawData)[2:-5]
        return cleanedData

    def logToFile(self, filename, x, y):
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
        with open(filename, 'a') as file:
            file.write(f"{x},{y}\n")

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
