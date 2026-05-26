#include <Wire.h>

#define DIRECCION 0x08

char buffer[32];

void setup() {
  Wire.begin(DIRECCION);
  Wire.onReceive(recibir);
  Wire.onRequest(responder);

  Serial.begin(115200);
  Serial.println("Arduino listo");
}

void loop() {}

void recibir(int bytes) {
  int i = 0;

  while (Wire.available() && i < 31) {
    buffer[i++] = Wire.read();
  }

  buffer[i] = '\0';

  Serial.print("ESP32 dice: ");
  Serial.println(buffer);
}

void responder() {
  Wire.write("Hola ESP32, recibido");
}