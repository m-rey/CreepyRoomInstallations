#include <Servo.h>

Servo myservo;
int pos = 0;

void setup() {
  myservo.attach(0);
}

void loop() {
  int times = random(20);
  while(times) {
    for (pos = 0; pos <= 180; pos += 1) {
      myservo.write(pos);
      delay(5);
    }
    for (pos = 180; pos >= 0; pos -= 1) {
      myservo.write(pos);
      delay(5);
    }
    times = times - 1;
  }
  delay(random(6000, 8640000));
}

