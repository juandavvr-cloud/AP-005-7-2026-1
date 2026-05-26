#include <SPI.h>

void setup() {
  pinMode(10, OUTPUT);
  digitalWrite(10, LOW);

  pinMode(MISO, OUTPUT);

  SPCR = _BV(SPE);         // SPI enable slave simple
  SPDR = 0x37;             // dato fijo
}

void loop() {
  if (SPSR & _BV(SPIF)) {
    SPDR = 0x37;
  }
}