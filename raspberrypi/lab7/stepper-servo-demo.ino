#include <Stepper.h>
#include <Servo.h>

const int stepsPerRevolution = 2048;
const int stepperSpeed = 20;

#define IN1 26
#define IN2 25
#define IN3 33
#define IN4 32
#define SERVO_PIN 27

Stepper myStepper(stepsPerRevolution, IN1, IN3, IN2, IN4);
Servo myservo;

int servoPos = 0;

void setup() {
  myStepper.setSpeed(stepperSpeed);
  myservo.attach(SERVO_PIN);

  Serial.begin(115200);
  myservo.write(servoPos); 
}

void loop() {
  servoPos = servoPos + 10 > 180 ? 0 : servoPos + 10;
  myStepper.step(stepsPerRevolution);
  myservo.write(servoPos);   
}
