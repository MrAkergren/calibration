/*
 The circuit:
 * RX is digital pin 10 (connect to TX of other device)
 * TX is digital pin 11 (connect to RX of other device)
*/


#include <SoftwareSerial.h>

//Receiver Code
byte indata[2];
SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {
  Serial.begin(9600);
  
  // set the data rate for the SoftwareSerial port
  mySerial.begin(300);
}

void loop() {
  int i=0;

  if (mySerial.available()) {
    delay(500); //allows all serial sent to be received together
    while(mySerial.available() && i<2) {
      indata[i++] = mySerial.read();
    }
  }

  if(i>0) {
    unsigned int ut = word(indata[0], indata[1]);
    Serial.println(ut, DEC);
  }
}
