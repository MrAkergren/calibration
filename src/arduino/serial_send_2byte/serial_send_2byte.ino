int analogPin = 0;     // analog pin to connect to the lux meter


unsigned int val = 0;     // variable to store the value read
byte buf[2];


void setup()

{

  Serial.begin(300);          //  setup serial

}

void loop()

{

//  val = analogRead(analogPin);    // read the input pin
    for(int i=300; i<311; i++){
        buf[0] = highByte(i);
        buf[1] = lowByte(i);
        Serial.write(buf, 2);             // debug value 1
        delay(1000);
  }
    
 // Serial.println(val);              // debug value 2
  
}
