/**
This program will measure the
temperature from a temperature-sensor.
Converts input to Celsius and sends
it over Serial for Python to prosess
the data.

Can be used as a stand-alone program,
or be used with Python for further
development.

Code by: Magnus Øye, Dated: 05.06-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy
*/

// defining global constant assigned to value
const int TMP_SENSOR = A0;

// The setup() configures serial comm.
void setup() {
  Serial.begin(9600);
}

// Calculating the temperature
// input: voltage output from sensor
// returns: integer temperature
float getTemperatureInC(int sensorPin){
  float measuredTempInC = 0;
  float measuredVoltage = 0;
  int sensorInput = analogRead( sensorPin );
  measuredVoltage = 5.0 / 1023 * sensorInput;
  measuredTempInC = 25 + (measuredVoltage - 0.750) * 100;
  return measuredTempInC;
}

// Converts from Celcius to Fahrenheit
// input: temperature in Celcius
// returns: temperature in Fahrenheit
float celsiusToFahrenheit(float tempC){
  return tempC * 9.0 / 5.0 + 32;
}

// Prints the temperature on the Serial Monitor
// input: temperature in Celcius
// returns: none
void printTemperature(int temperature) {
  Serial.println(temperature);
}

// loop() will run ‘forever’:
// Read temperature from sensor, return as degrees C
// Change delay for faster or slower readings
void loop() {
float tempInC = getTemperatureInC(TMP_SENSOR);
printTemperature(tempInC);
delay(100); // delay in milliseconds
}
