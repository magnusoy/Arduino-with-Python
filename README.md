# Arduino with Python

This project is supposed to give anyone who wants to control their Arduino with Python an easy process setting up. The project provide a Python class that contains useful functions to get started. It also contains a visualizer class for showcasing stored data acquired from the Arduino. More functionality and classes will be implimented in later versions.

### Prerequisites

You will need [Python 3](https://www.python.org/) and [Arduino IDE](https://www.arduino.cc/) for using the provided files.
Also you will need to install dependencies listed below.

```bash
pip install -r /path/to/requirements.txt

or

pip install pyserial==3.4
pip install matplotlib==2.2.2
pip install pandas==0.23.0
```

### Installing

Clone or download project as zip in any directory.
Create a new python script within the directory,
import the provided classes and start programming.

### Examples

In [/example](https://github.com/magnusoy/Arduino-with-Python/tree/master/examples) you will find some example scripts,
for both Arduino and Python.

- Reading data
```python
from arduino import Arduino

arduino = Arduino()
arduino.connect("COM4", 9600)
arduino.getData()

```

- Storing data in file

```python
from arduino import Arduino

filename = "measurements.csv"
arduino = Arduino()
arduino.createLogfile(filename, ("A", "B", "C"))
arduino.connect("COM4", 9600)

while arduino.isConnected():
	data = arduino.getData()
	arduino.logToFile(filename, data)
	if arduino.getTimeElapsed() > 10:
		arduino.disconnect()
		
```
- Storing data in file and
presenting it in a line graph
```python
from arduino import Arduino
from visualize import Visualize

arduino = Arduino()
filename = "ultrasonic_readings.csv"
arduino.createLogfile(
    filename, ("Time", "Value"))
arduino.connect("COM4", 115200)

while arduino.isConnected():
    data = arduino.getData()
    arduino.logDataWithTime(filename, data)
    arduino.delay(0.1)
    
    # Ending measurement sampling after 10 sec
    if arduino.getTimeElapsed() > 10:
        arduino.disconnect()

data_presenter = Visualize()
dataset = data_presenter.collectData(filename)
figure = data_presenter.plot(dataset["Time"], dataset["Value"])
data_presenter.savePlot(figure, "Output.png")

```
![Output](https://github.com/magnusoy/Arduino-with-Python/blob/master/img/Output.png)


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
