#include <SoftwareSerial.h>   // 引用程式庫

String st;
 
void setup() 
{
  Serial.begin(9600);
  Serial.println("BT is ready!");
}
 
void loop() 
{
  if (Serial.available()) 
  {   
    char val = Serial.read();

    if(val == '\r')
    {
      Serial.println(st);
    }
    else if(val == '\n')
    {
      st = "";
    }
    else
    {
      st += val;
    }
  }
}
