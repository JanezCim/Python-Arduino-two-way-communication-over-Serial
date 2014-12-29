#define ButtonPin A0
long Bstate = 0;
int RecievedData = 0;

void setup(){
  Serial.begin(9600); 
  pinMode(13, OUTPUT);
  pinMode(ButtonPin, INPUT);
}


void loop(){
  //Bstate = 0;
  //Bstate = analogRead(ButtonPin);
  //if(Bstate > 1000) digitalWrite(13, HIGH);
  //else digitalWrite(13, LOW);
  RecievedData = PyComs(RecievedData);
}


//returns -1 if no data was recieved
int DataNotSent = 0;
long PyComs(long sendData){
  //send data to host
  if(DataNotSent != 1) Serial.println(sendData);
  
  DataNotSent = 0;
  long RecievedData = 0;

  //recieve data from host
  if (Serial.available()){
      RecievedData = Serial.read();
    }
  else DataNotSent = 1;

  return RecievedData;
}
