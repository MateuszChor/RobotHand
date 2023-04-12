#include <ESP32Servo.h>
#include <LiquidCrystal_I2C.h>

const int buttonPin = 34; 
const int ledPin = 13;
int buttonState = 2;

int lcdColumns = 16;
int lcdRows = 2;
LiquidCrystal_I2C lcd(0x27, lcdColumns, lcdRows);  

Servo S_Wrist;  // Serwo Wrist
Servo S_Thumb;  // Serwo Thumb
Servo S_Forefinger; // Serwo Forefinger
Servo S_Middle_finger; // Middle finger
Servo S_Ring_finger;  // Ring finger
Servo S_Little_finger; // Little finger

int pos = 0;
int pos_Ring_finger = 180;    

void setup() {

  lcd.init();                
  lcd.backlight();

  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);

  S_Wrist.attach(10);  // attaches the servo Wrist

  S_Thumb.attach(12);  // attaches the servo Thumb

  S_Forefinger.attach(15);  // attaches the servo Forefinger

  S_Middle_finger.attach(2); // attaches the servo Middle finger

  S_Ring_finger.attach(27); // attaches the servo Ring finger

  S_Little_finger.attach(4); // attaches the servo Little finger

  Serial.begin(115200);
}

void loop() {

  buttonState = digitalRead(buttonPin);

   if (buttonState == HIGH) {
    digitalWrite(ledPin, HIGH);
    pos = 180;
    pos_Ring_finger = 0;
    S_Wrist.write(0);
    S_Thumb.write(pos);
    S_Forefinger.write(pos);
    S_Middle_finger.write(pos);
    S_Ring_finger.write(pos_Ring_finger);
    S_Little_finger.write(pos);
    lcd.setCursor(0, 0);
    lcd.print(buttonState);
  
  } else {
    digitalWrite(ledPin, LOW);
    pos = 0;  
    pos_Ring_finger = 180;    
    S_Wrist.write(0);
    S_Thumb.write(pos);
    S_Forefinger.write(pos);
    S_Middle_finger.write(pos);
    S_Ring_finger.write(pos_Ring_finger);
    S_Little_finger.write(pos);
    
    lcd.setCursor(0, 0);
    lcd.print(buttonState);
  }



 
}