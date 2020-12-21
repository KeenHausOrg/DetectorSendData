void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // open serial port, set the baud rate as 9600 bps
}

void loop() {
  int val;
  val = analogRead(0); //connect sensor to Analog 0
  Serial.print("moisture:");
  Serial.print(val); //print the value to serial port
  Serial.print('\r');Serial.print('\n');
  delay(2000);
}
