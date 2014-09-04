/* TL.ino 
 
 Traffic lights on the Arduino
 (C) 2014 Dougie Lawson, Creative Commons v4.0 BY-NC-SA
 
 */

/* Use compiler directives to control the sequence */

// RED, RED+AMBER, GREEN, AMBER RED ...
#define UK
#undef US

// We're going to skip RED+AMBER
// RED, GREEN, AMBER, RED ...
// #define US
// #undef UK

int redLED = 9;
int yellLED = 8;
int grnLED = 7;

void setup() {

  pinMode(redLED, OUTPUT);
  pinMode(yellLED, OUTPUT);
  pinMode(grnLED, OUTPUT);

}

void loop() {

  digitalWrite(redLED, HIGH);
  delay(1500);

#ifdef UK
  digitalWrite(yellLED, HIGH);
  delay(750);
#endif

  digitalWrite(redLED, LOW);
  digitalWrite(yellLED, LOW);
  digitalWrite(grnLED, HIGH);
  delay(1500);
  digitalWrite(grnLED, LOW);
  digitalWrite(yellLED, HIGH);
  delay(750);
  digitalWrite(yellLED, LOW);

}







