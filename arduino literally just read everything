/*
 * This ESP32 code is created by esp32io.com
 *
 * This ESP32 code is released in the public domain
 *
 * For more detail (instruction and wiring diagram), visit https://esp32io.com/tutorials/esp32-joystick
 */


#define VRY_PIN  0 // ESP32 pin GPIO39 (ADC0) connected to VRY pin
#define VRX_PIN  4
#define SWITCH   2
#define BUTTON   5

int valueY = 0; // to store the Y-axis value
int valueX = 0
int valueSwitch = 0
int valueButton = 0

void setup() {
  Serial.begin(9600) ;
}

void loop() {
  valueY = analogRead(VRY_PIN);
  valueX = analogRead(VRX_PIN);
  valueSwitch = digitalRead(SWITCH);
  valueButton = digitalRead(BUTTON);

  // print data to Serial Monitor on Arduino IDE
  Serial.print("Y value is");
  Serial.print(valueY);
  Serial.print("X value is");
  Serial.print(valueX);
  Serial.print("Switch is");
  Serial.print(valueSwitch);
  Serial.print("Button is");
  Serial.println(buttonSwitch)
}
