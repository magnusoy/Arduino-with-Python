/**
  This program will measure the distance
  and print out if anything is detected.
  Expanding the program with more
  Ultrasonic sensors are made easy
  with re-using functions. Just remember to
  define new inputs.
  Can be used as a stand-alone program,
  or be used with Python for further
  development.
  Code by: Magnus Øye, Dated: 24.07-2018
  Contact: magnus.oye@gmail.com
  Website: https://github.com/magnusoy
*/


// defining global constants assigned to values
const int trigPin = 6;
const int echoPin = 7;
char data = 0;

// The setup() configures hardware (digital outputs) and serial comm.
void setup() {
  Serial.begin(9600);   //Sets the baud for serial data transmission
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  pinMode(13, OUTPUT);  //Sets digital pin 13 as output pin
}

// loop() will run ‘forever’:
// Change delay for faster or slower readings
void loop() {
  trigEcho(trigPin);
  long duration = readInput(echoPin);
  int distance = convertToCm(duration);
  if (distance < 60) {
    Serial.println("DETECTION!");
    digitalWrite(13, HIGH);
    delay(100);
  }
  digitalWrite(13, LOW);
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
