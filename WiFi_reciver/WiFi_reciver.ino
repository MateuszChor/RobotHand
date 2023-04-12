#include <WiFi.h>

const char* ssid = "";
const char* password = "";

const char* server = "";
const int port = 80;

const int buttonPin = 34; 
const int ledPin_green = 32;
const int ledPin_red = 13;
const int ledPin_yellow = 33;
int buttonState = 2;

void setup() {
  pinMode(ledPin_green, OUTPUT);
  pinMode(ledPin_red, OUTPUT);
  pinMode(ledPin_yellow, OUTPUT);
  Serial.begin(115200);
  delay(1000);

  digitalWrite(ledPin_red, HIGH);
  digitalWrite(ledPin_green, HIGH);
  digitalWrite(ledPin_yellow, HIGH);

  Serial.println("Connecting to WiFi network...");
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
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

  digitalWrite(ledPin_red, LOW);
  digitalWrite(ledPin_yellow, LOW);
  
  Serial.println("Connecting to server...");
  if (client.connect(server, port)) {
    digitalWrite(ledPin_yellow, HIGH);
    Serial.println("Connected to server");
    while (client.connected()) {
      String line = client.readStringUntil('\n');
      line.trim(); 
      Serial.println(line);
      if (line == "two"){
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
  }
  delay(1000);
  digitalWrite(ledPin_red, LOW);
  digitalWrite(ledPin_yellow, LOW);
}