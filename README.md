# Arduino with Python

This project is supposed to give anyone who wants to control their Arduino with Python an easy process setting up. The project provide a Python class that contains useful functions to get started. More functionality and classes will be implimented in later versions.

### Prerequisites

You will need Python 3.4=< and Arduino IDE for using the provided files.
Furthermore you will also have to install pySerial.

```
python -m pip install pyserial

or

conda install -c conda-forge pyserial
```

### Installing

Simply clone or download project as Zip.
Create a new python script within the project,
import the provided class and start programming.

### Examples

In /example you will find some example scripts,
for both Arduino and Python.

```
from arduino_serial import ArduinoSerial

arduino = ArduinoSerial()
arduino.connect("COM4", 9600)
arduino.readLine()
```

or

```
from arduino_serial import ArduinoSerial

filename = "distance.csv"

arduino = ArduinoSerial()

arduino.createFile(filename)

arduino.connect("COM4", 9600)

while arduino.isConnected():
	t = arduino.getTimeElapsed()
	y = arduino.cleanData()
	arduino.logToFile(filename, t, y)
	if arduino.getTimeElapsed > 10:
		arduino.disconnect()
```


## Built With

* [Python](https://www.python.org/) - Python
* [Arduino](https://www.arduino.cc/) - Arduino IDE

## Contributing

If you want to contribute or find anything wrong, please create a Pull request, or issue adressing the change, or issue.


## Author

* **Magnus Øye** - *Initial work* - [magnusoy](https://github.com/magnusoy)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/magnusoy/Arduino-with-Python/blob/master/LICENSE) file for details


## Acknowledgments

[pySerial](http://pyserial.readthedocs.io/en/latest/index.html)
