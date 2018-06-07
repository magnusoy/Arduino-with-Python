/**
  This program will turn a LED
  on or off, by reciving data from
  the sreial. Multiple LED's are
  made easy to add by simply
  re-using the functions.

  Can be used as a stand-alone program,
  or be used with Python for further
  development.

  Code by: Magnus Øye, Dated: 05.06-2018
  Contact: magnus.oye@gmail.com
  Website: https://github.com/magnusoy
*/

// defining global variables assigned to values
const int LEDPIN = 13;
int serialData;

// The setup() configures hardware (digital outputs) and serial comm.
void setup() {
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(LEDPIN, OUTPUT); //make the LED pin (13) as output
  digitalWrite (LEDPIN, LOW);
}

// Turns LED on
// input: led pin
// returns: none
void turnLedOn(int ledPin) {
  digitalWrite(ledPin, HIGH);
}

// Turns LED off
// input: led pin
// returns: none
void turnLedOff(int ledPin) {
  digitalWrite(ledPin, LOW);
}

// loop() will run ‘forever’:
// Reads from serial and checks if
// condition match.
void loop() {
  while (Serial.available()) {
    serialData = Serial.read();

  } if (serialData == '1') {
    turnLedOn(LEDPIN);

  } else if (serialData == '0') {
    turnLedOff(LEDPIN);
  }

}
