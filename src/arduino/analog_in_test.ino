int analogPin = 0;     // potentiometer wiper (middle terminal) connected to analog pin 3

                       // outside leads to ground and +5V

unsigned int val = 0;     // variable to store the value read
byte buf[2];


void setup()

{

  Serial.begin(300);          //  setup serial

}

void loop()

{

  val = analogRead(analogPin);    // read the input pin
  buf[0] = highByte(val);
  buf[1] = lowByte(val);
  
  Serial.write(buf, 2);             // debug value 1
 // Serial.println(val);              // debug value 2
  delay(1000);
}
