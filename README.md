# Arduino with Python

This project is supposed to give anyone who wants to control their Arduino with Python an easy process setting up. The project provide a Python class that contains useful functions to get started. More functionality and classes will be implimented in later versions.

### Prerequisites

You will need Python 3.4=< and Arduino IDE for using the provided files.
Furthermore you will also have to install some dependencies.

```
python pip install -r /path/to/requirements.txt

or

python pip install serial==3.4
python pip install matplotlib==2.2.2
python pip install pandas==0.23.0
```

### Installing

Simply clone or download project as Zip.
Create a new python script within the project,
import the provided class and start programming.

### Examples

In /example you will find some example scripts,
for both Arduino and Python.

```
from arduino import Arduino

arduino = Arduino()
arduino.connect("COM4", 9600)
arduino.readLine()
```

or

```
from arduino import Arduino

filename = "distance.csv"

arduino = Arduino()

arduino.createFile(filename)

arduino.connect("COM4", 9600)

while arduino.isConnected():
	data = arduino.getData()
	arduino.logToFile(filename, data)
	if arduino.getTimeElapsed > 10:
		arduino.disconnect()
```


## Built With

* [Python](https://www.python.org/) - Python
* [Arduino](https://www.arduino.cc/) - Arduino IDE

## Contributing

If you want to contribute or find anything wrong, please create a Pull request, or issue adressing the change, or issue.


## Author

* **Magnus Øye** - [magnusoy](https://github.com/magnusoy)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/magnusoy/Arduino-with-Python/blob/master/LICENSE) file for details


## Libraries

[pySerial](http://pyserial.readthedocs.io/en/latest/index.html)

[Matplotlib](https://matplotlib.org/index.html)

[pandas](https://pandas.pydata.org/)
