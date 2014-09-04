/* blink.ino 

  The "Hello World" for the Arduino
  (C) 2014 Dougie Lawson, Creative Commons v4.0 BY-NC-SA

*/

int pin13LED = 13;

void setup() {

  pinMode(pin13LED, OUTPUT);

}

void loop() {

  digitalWrite(pin13LED,LOW);
  delay(999);
  digitalWrite(pin13LED,HIGH);
  delay(999);

}

