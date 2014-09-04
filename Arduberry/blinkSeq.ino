/* blinkSeq.ino 
 
 A variation on "Hello World" for the Arduberry
 (C) 2014 Dougie Lawson, Creative Commons v4.0 BY-NC-SA
 
 Wire four LEDs with 560ohm resistors to pins 6, 7, 8 & 9
 
 */

void setup() {

  for (int i=6; i<=9; i++) {
    pinMode(i, OUTPUT);
  }

}

void loop() {

  for (int i=6; i<=9; i++) {
    digitalWrite(i,LOW);
    delay(999);
    digitalWrite(i,HIGH);
    delay(999);
  }

}

