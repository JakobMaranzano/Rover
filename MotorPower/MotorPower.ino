#include <Servo.h>

Servo servoFL;
Servo servoBL;
Servo servoFR;
Servo servoBR;
void setup() 
{
  servoFL.attach(7);
  servoBL.attach(9);
  servoFR.attach(13);
  servoBR.attach(11);
  Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
}

void loop()
{
  //initilizing variable
  int incomingByte = 1;
  int previousByte = 1;
  
  incomingByte = Serial.read();
  //Serial.print(incomingByte);

  while(incomingByte != previousByte) // && incomingByte != 0)
  {

    if (incomingByte == 49) 
    {
      servoFL.writeMicroseconds(1900);
      servoBL.writeMicroseconds(1900);
      servoFR.writeMicroseconds(1100);
      servoBR.writeMicroseconds(1100); 
      Serial.print("Moving Foward\n");
    }

    if (incomingByte == 50) 
    {
      servoFL.writeMicroseconds(1100);
      servoBL.writeMicroseconds(1100);
      servoFR.writeMicroseconds(1900);
      servoBR.writeMicroseconds(1900);
      Serial.print("Moving Back\n");
    }
    
    if (incomingByte == 51) 
    {
      servoFL.writeMicroseconds(1900);
      servoBL.writeMicroseconds(1900);
      servoFR.writeMicroseconds(1900);
      servoBR.writeMicroseconds(1900);
      Serial.print("Turning Right\n");
    }
    
    if (incomingByte == 52) 
    {
      servoFL.writeMicroseconds(1100);
      servoBL.writeMicroseconds(1100);
      servoFR.writeMicroseconds(1100);
      servoBR.writeMicroseconds(1100);
      Serial.print("Turning Left\n");
    }

    if (incomingByte == 48) 
    {
      servoFL.writeMicroseconds(1500);
      servoBL.writeMicroseconds(1500);
      servoFR.writeMicroseconds(1500);
      servoBR.writeMicroseconds(1500);
      Serial.print("Stoped\n");
    }
    previousByte = incomingByte;
  }
}
