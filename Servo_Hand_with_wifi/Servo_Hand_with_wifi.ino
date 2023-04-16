#include <ESP32Servo.h>
#include <LiquidCrystal_I2C.h>
#include <WiFi.h>
#include <SECRET.h>

extern const std::string seccret_password;
extern const std::string seccret_ssid;
extern const std::string seccret_ip_server;

const char* ssid = seccret_ssid.c_str();
const char* password = seccret_password.c_str();
const char* server = seccret_ip_server.c_str();
// const char* server = seccret_ip_server_laptop.c_str();
const int port = 80;

const int buttonPin = 34; 
const int ledPin_green = 32;
const int ledPin_red = 13;
const int ledPin_yellow = 33;
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

  pinMode(ledPin_green, OUTPUT);
  pinMode(ledPin_red, OUTPUT);
  pinMode(ledPin_yellow, OUTPUT);
  Serial.begin(115200);
  delay(1000);

  lcd.init();                
  lcd.backlight();

  pinMode(buttonPin, INPUT);

  S_Wrist.attach(10);  // attaches the servo Wrist

  S_Thumb.attach(12);  // attaches the servo Thumb

  S_Forefinger.attach(15);  // attaches the servo Forefinger

  S_Middle_finger.attach(2); // attaches the servo Middle finger

  S_Ring_finger.attach(27); // attaches the servo Ring finger

  S_Little_finger.attach(4); // attaches the servo Little finger

  digitalWrite(ledPin_red, HIGH);
  digitalWrite(ledPin_green, HIGH);
  digitalWrite(ledPin_yellow, HIGH);
  Serial.println("Connecting to WiFi network...");
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("WiFi...");
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  digitalWrite(ledPin_red, LOW);
  digitalWrite(ledPin_green, LOW);
  digitalWrite(ledPin_yellow, LOW);

  Serial.println("Connected to WiFi");
  digitalWrite(ledPin_green, HIGH);
}

void loop() {

  WiFiClient client;
  buttonState = digitalRead(buttonPin);

  digitalWrite(ledPin_red, LOW);
  digitalWrite(ledPin_yellow, LOW);
  
  Serial.println("Connecting to server...");
  if (client.connect(server, port)) {
    digitalWrite(ledPin_yellow, HIGH);
    Serial.println("Connected to server");
    while (client.connected()) {

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Connected to");
      lcd.setCursor(0, 1);
      lcd.print("Server");

      String line = client.readStringUntil('\n');
      line.trim(); 
      Serial.println(line);
      if (line == "Thumb_Up"){
        S_Thumb.write(170);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(line);
        digitalWrite(ledPin_red, HIGH);
      }

      if (line == "Thumb_Down"){
        S_Thumb.write(0);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(line);
        digitalWrite(ledPin_red, HIGH);
      }

       if (line == "Forefinger_Up"){
        S_Forefinger.write(168);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(line);
        digitalWrite(ledPin_red, HIGH);
      }

       if (line == "Forefinger_Down"){
        S_Forefinger.write(13);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(line);
        digitalWrite(ledPin_red, HIGH);
      }
       
       if (line == "Middle_Up"){
        S_Middle_finger.write(180);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(line);
        digitalWrite(ledPin_red, HIGH);
      }

       if (line == "Middle_Down"){
        S_Middle_finger.write(0);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(line);
        digitalWrite(ledPin_red, HIGH);
      }
      
       if (line == "Ring_finger_Up"){
        // this servo working another direction :) 
        S_Ring_finger.write(0);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(line);
        digitalWrite(ledPin_red, HIGH);
      }

       if (line == "Ring_finger_Down"){
        // this servo working another direction :) 
        S_Ring_finger.write(180);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(line);
        digitalWrite(ledPin_red, HIGH);
      }

       if (line == "Little_finger_Up"){
        // this servo working another direction :) 
        S_Little_finger.write(180);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(line);
        digitalWrite(ledPin_red, HIGH);
      }

       if (line == "Little_finger_Down"){
        // this servo working another direction :) 
        S_Little_finger.write(0);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(line);
        digitalWrite(ledPin_red, HIGH);
      }
    
    }
    
    Serial.println();
    Serial.println("Disconnecting from server");
    client.stop();
  
  } else {
    Serial.println("Connection failed.");
    digitalWrite(ledPin_red, LOW);
    digitalWrite(ledPin_yellow, LOW);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Server ");
    lcd.setCursor(0, 1);
    lcd.print("Connecting ....");
  }
  delay(1000);
  digitalWrite(ledPin_red, LOW);
  digitalWrite(ledPin_yellow, LOW);

}

