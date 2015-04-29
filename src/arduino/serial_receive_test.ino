/*
 The circuit:
 * RX is digital pin 10 (connect to TX of other device)
 * TX is digital pin 11 (connect to RX of other device)
*/


#include <SoftwareSerial.h>

//Receiver Code

char str[4];
byte indata[2];
unsigned int test;
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
      //str[i++] = mySerial.read();
      indata[i++] = mySerial.read();
  }
    //str[i]='\0';
  }

  if(i>0) {
    //int ut = indata[0] * 256 + indata[1];
    unsigned int ut = word(indata[0], indata[1]);
    Serial.println(ut, DEC);
  }
}
