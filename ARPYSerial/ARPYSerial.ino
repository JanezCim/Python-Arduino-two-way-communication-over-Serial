#define Button1   42 // Left bottom
#define Button2   44 // Left center bottom
#define Button3   46 // Right center bottom
#define Button4   48 // Right bottom
// Top buttons
#define ButtonZ1  38 // al pa 36    gumb se nahaja na zgornji plošči
#define ButtonZ2  36
#define ButtonZ3  34 // al pa 38    gumb se nahaja na zgornji plošči
int Button[] = {Button1, Button2, Button3, Button4, ButtonZ1, ButtonZ2, ButtonZ3};
long Bstate = 10000000;


void setup(){
  Serial.begin(9600); 
}


void loop(){
  Bstate = 10000000;
  for (int i = 0; i<=6; i++){
    if(digitalRead(Button[i])){
      Bstate = Bstate + pow(10,i);
    }
  }
  //Serial.println(Bstate);
  PyComs(Bstate);
  delay(100);
}



void PyComs(long sendData){
  Serial.println(sendData);
  //delay(50);
  boolean Done = 0;
  while (!Done) {
    if(Serial.available() > 0) {
      char data = Serial.read();
      char str[2];
      str[0] = data;
      str[1] = '\0';
      Done = 1;
    }
  }
  //delay(50);
}
