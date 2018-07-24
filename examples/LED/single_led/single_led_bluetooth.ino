/**
  This program will turn a LED
  on or off, by reciving data from
  the bluetooth module. Multiple LED's are
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
char data = 0;            //Variable for storing received data
const int LED = 13;

// The setup() configures hardware (digital outputs) and serial comm
void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

// loop() will run ‘forever’:
// Reads from serial and checks if
// condition match.
void loop() {
  if (Serial.available() > 0) {
    data = Serial.read();
    Serial.println(data);
    if (data == '1') {
      turnLedOn)LED);
      Serial.println("LED: ON"); 
    }else if (data == '0') {
      turnLedOff(LED);
      Serial.println("LED: OFF"); 
    }
  }
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
