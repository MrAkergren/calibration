byte buf[2];

void setup(){
  Serial.begin(300);          //  setup serial
}

void loop(){
    for(int i=300; i<311; i++){
        buf[0] = highByte(i);
        buf[1] = lowByte(i);
        Serial.write(buf, 2);             // debug value 1
        delay(1000);
    }
}
