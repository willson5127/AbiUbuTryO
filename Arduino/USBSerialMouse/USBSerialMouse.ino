#include <SoftwareSerial.h>   // 引用程式庫
#include <Mouse.h>

String st;
int xDistance = 0, yDistance = 0;
int M = 0;

void mouseMove(long x, long y) 
{
  long max = max(abs(x), abs(y));
  int count = (int) (max / 127);
  signed char stepX = x / (count + 1);
  signed char stepY = y / (count + 1);
  for (int i = 0; i < count; i++) 
  {
    Mouse.move(stepX, stepY);
  }
  signed char resX = x - (stepX * count);
  signed char resY = y - (stepY * count);
  if (resX != 0 || resY != 0) 
  {
    Mouse.move(resX, resY);
  }
}
 
void setup() 
{
  Serial.begin(9600);
  Serial.println("BT is ready!");
}
 
void loop() 
{
  if(M == 1)
  {
    //Serial.println("Please insert Xpos!");    
  }
  else if(M == 2)
  {
    //Serial.println("Please insert Ypos!");
  }
  if (Serial.available()) 
  {   
    char val = Serial.read();

    if(val == '\r')
    {
      if(M == 0)
      {
        if (st == "Move*")
        {
          M = 1;
        }
        else if (st == "ClickLeftBTN*") 
        {
          Mouse.press(MOUSE_LEFT);
          delay(10);
          Mouse.release(MOUSE_LEFT);     
        }
        else if (st == "ClickRightBTN*") 
        {
          Mouse.press(MOUSE_RIGHT);
          delay(10);
          Mouse.release(MOUSE_RIGHT);     
        }
        else if (st == "PressLeftBTN*") 
        {
          Mouse.press(MOUSE_LEFT);     
        }
        else if (st == "releaseLeftBTN*")
        {
          Mouse.release(MOUSE_LEFT);  
        }
        else if (st == "PressRightBTN*") 
        {
          Mouse.press(MOUSE_RIGHT);     
        }
        else if (st == "releaseRightBTN*")
        {
          Mouse.release(MOUSE_RIGHT);  
        }
      }
      else if(M == 1)
      {        
        xDistance = st.toInt();
        M = 2;
      }
      else if(M == 2)
      {
        yDistance = st.toInt();
        if ((xDistance != 0) || (yDistance != 0)) 
        {
          mouseMove(xDistance, yDistance);
          M = 0;
        }
      }     
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
