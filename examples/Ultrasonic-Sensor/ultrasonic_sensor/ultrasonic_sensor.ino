/**
  This program will measure the distance
  and print out the result in centimeters.
  Expanding the program with more
  Ultrasonic sensors are made easy
  with re-using functions. Just remember to
  define new inputs.

  Can be used as a stand-alone program,
  or be used with Python for further
  development.

  Code by: Magnus Øye, Dated: 05.06-2018
  Contact: magnus.oye@gmail.com
  Website: https://github.com/magnusoy
*/

// defining global constants assigned to values
const int trigPin = 6;
const int echoPin = 7;

// The setup() configures hardware (digital outputs) and serial comm.
void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600); // Starts the serial communication
}
// Calculating the distance
// input: duration between sent and recived signal
// returns: integer distance
int convertToCm(int duration) {
  int distance = duration * 0.034 / 2;
  return distance;
}

// Reads the echoPin, returns the sound wave travel time in microseconds
// input: echo
// returns: long duration between sent and recived signal
long readInput(int echoPin) {
  long duration = pulseIn(echoPin, HIGH);
  return duration;
}

// Clears the trigPin
// Sets the trigPin on HIGH state for 10 microseconds
// input: trig
// returns: none
void trigEcho(int trigPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
}

// Prints the distance on the Serial Monitor
// input: distance in centimeters
// returns: none
void printDistance(int distance) {
  Serial.println(distance);
}

// loop() will run ‘forever’:
// Change delay for faster or slower readings
void loop() {
  trigEcho(trigPin);
  long duration = readInput(echoPin);
  int distance = convertToCm(duration);
  printDistance(distance);
  delay(100); // delay in milliseconds
}
