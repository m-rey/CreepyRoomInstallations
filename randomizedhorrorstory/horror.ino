
#include "Charliplexing.h"
#include "Myfont.h"

#include "Arduino.h"
const int l = 7;
unsigned char a2[] = "Don't be scared of the monsters. Look to your left, to your right, under your bed, behind your dresser, in your closet but never look up, she hates being seen. \0";
unsigned char a3[] = "I woke up to hear knocking on glass. At first, I though it was the window until I heard it come from the mirror again. \0";
unsigned char a5[] = "The grinning face stared at me from the darkness beyond my bedroom window. I live on the 14th floor. \0";
unsigned char a6[] = "Working the night shift alone tonight. There is a face in the cellar staring at the security camera. \0";
unsigned char a7[] = "They delivered the mannequins in bubble wrap. From the main room I begin to hear popping. \0";
unsigned char a15[] = "Nurse's Note: Born 7 pounds 10 ounces, 18 inches long, 32 fully formed teeth. Silent, always smiling. \0";
unsigned char a17[] = "I looked out my window. The stars had gone away. \0";
unsigned char* all_data[l] = {a2, a3, a5, a6, a7, a15, a17};

void setup() {
  LedSign::Init();
}

void loop() {
  int i = random(0, l-1);
  int leng;
  for(int j=0; ; j++) {
    if(all_data[i][j]==0){
      leng=j;
      break;
    }
  }
  Myfont::Banner(leng + 5,all_data[i]);
  delay(random(6000, 8640000));
}
