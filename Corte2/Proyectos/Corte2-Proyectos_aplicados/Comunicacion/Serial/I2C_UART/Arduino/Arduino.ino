#include <Wire.h>

#define SLAVE_ADDR 0x08

String buffer = "";
bool nuevoMensaje = false;

void setup() {
  Wire.begin(SLAVE_ADDR);
  Wire.onReceive(receiveEvent);

  Serial.begin(115200);
}

void loop() {
  if (nuevoMensaje) {
    Serial.print("Recibido por I2C: ");
    Serial.println(buffer);

    buffer = "";
    nuevoMensaje = false;
  }
}

// SOLO leer datos aquí (sin Serial)
void receiveEvent(int bytes) {
  while (Wire.available()) {
    char c = Wire.read();
    buffer += c;
  }

  nuevoMensaje = true;
}