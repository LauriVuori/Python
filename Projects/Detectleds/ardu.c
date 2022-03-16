// pinMode(pin, INPUT);           // set pin to input
// digitalWrite(pin, HIGH);       // turn on pullup resistors
// pinMode()
// digitalWrite()
// digitalRead()
#define INPUT_D2 2
#define GREED_D3 3
#define BLUE_D4 4
#define RED_D5 5
void setup() {
    pinMode(INPUT_D2, INPUT);
    pinMode(GREED_D3, OUTPUT);
    pinMode(BLUE_D4, OUTPUT);
    pinMode(RED_D5, OUTPUT);
    // Serial.begin(9600);
}

void loop() {
    uint8_t button_state = 0, random_num = 0;
    button_state = digitalRead(INPUT_D2);
    // Serial.write(button_state);
    if (button_state == 1) {
        delay(100);
        random_num = random(2);
        if (random_num == 1) {
            digitalWrite(RED_D5, 1);
        }
        else {
            digitalWrite(RED_D5, 0);
        }
        random_num = random(2);
        if (random_num == 1) {
            digitalWrite(GREED_D3, 1);
        }
        else {
            digitalWrite(GREED_D3, 0);
        }
        random_num = random(2);
        if (random_num == 1) {
            digitalWrite(BLUE_D4, 1);
        }
        else {
            digitalWrite(BLUE_D4, 0);
        }
    }
}
