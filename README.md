# Arduino with Python

This project is supposed to give anyone who wants to control their Arduino with Python an easy process setting up. The project provide a Python class that contains useful functions to get started. It also contains a visualizer class for showcasing stored data acquired from the Arduino. More functionality and classes will be implimented in later versions.

### Prerequisites

You will need [Python 3.4](https://www.python.org/) and [Arduino IDE](https://www.arduino.cc/) for using the provided files.
Also you will need to install dependencies listed below.

```
python pip install -r /path/to/requirements.txt

or

python pip install serial==3.4
python pip install matplotlib==2.2.2
python pip install pandas==0.23.0
```

### Installing

Clone or download project as zip in any directory.
Create a new python script within the directory,
import the provided classes and start programming.

### Examples

In [/example](https://github.com/magnusoy/Arduino-with-Python/tree/master/examples) you will find some example scripts,
for both Arduino and Python.

Reading data example
```
from arduino import Arduino

arduino = Arduino()
arduino.connect("COM4", 9600)
arduino.getData()
```

Storing data in file

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
