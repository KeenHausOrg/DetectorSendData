const int AirValue = 484;   
const int WaterValue = 217;  //you need to replace this value with Value_2
int intervals = (AirValue - WaterValue)/3;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // open serial port, set the baud rate as 9600 bps
}

void loop() {
  int val;
  val = analogRead(A0); //connect sensor to Analog 0

  int pcnt = 0;
  if(val < WaterValue){pcnt = 100;}
  else if(val > AirValue){pcnt = 0;}
  else{
      pcnt = 100 - ((val - WaterValue)*100 /(AirValue - WaterValue));
  }

  // 100% is very wet
  String statusText = "";
  if(pcnt > 75){
    statusText = "Very Wet";
  }
  else if(pcnt > 50)
  {
    statusText = "Wet";
  }
  else if(pcnt > 25)
  {
    statusText = "Damp";
  }
  else{
    statusText = "Dry";
  }
  
  Serial.print("moisture:");
  Serial.print(val); 
  Serial.print('\r');Serial.print('\n');
  Serial.print("Percent:");
  Serial.print(pcnt); 
  Serial.print('\r');Serial.print('\n');
  Serial.print("Status:");
  Serial.print(statusText); 
  Serial.print('\r');Serial.print('\n');
  delay(2000);
}
