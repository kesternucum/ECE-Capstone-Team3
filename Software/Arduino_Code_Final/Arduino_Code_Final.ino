const int onesDigitPins[] = {2, 3, 4, 5, 6, 7, 8};
const int tensDigitPins[] = {9, 10, 11, 12, 13, 14, 15};

// Seven segment binary codes for 0 through 9
const int digitCodes[] = {
  0b00111111, // 0
  0b00000110, // 1
  0b01011011, // 2
  0b01001111, // 3
  0b01100110, // 4
  0b01101101, // 5
  0b01111101, // 6
  0b00000111, // 7
  0b01111111, // 8
  0b01101111  // 9
};

int data; // Stores number to display to sign

void setup() {
  // Set digit pins as outputs
  for (int i = 2; i <= 15; i++) {
    pinMode(i, OUTPUT);
  }
  
  // Setup serial connection
  Serial.begin(9600);
  //Serial.setTimeout(3);
}

// Main loop
void loop() {
  // Constantly update sign with number coming from computer
  while (!Serial.available());
  data = Serial.readString().toInt(); 
  displayNumber(data);
}

// Separate parking lot number into two separate values
void displayNumber(int number) {
  // If number is outside of range, return
  if (number < 0 || number > 99) {
    return;
  }
  
  int onesDigit = number % 10;
  int tensDigit = number / 10;
  displayDigit(onesDigit, onesDigitPins);
  displayDigit(tensDigit, tensDigitPins);
}

// Write to correct pins to output to correct LED strips based off digit value
void displayDigit(int digit, const int* digitPins) {
  // If digit is outside of range, return
  if (digit < 0 || digit > 9) {
    return;
  }

  digitalWrite(digitPins[0], digitCodes[digit] & 0b00000001);
  digitalWrite(digitPins[1], digitCodes[digit] & 0b00000010);
  digitalWrite(digitPins[2], digitCodes[digit] & 0b00000100);
  digitalWrite(digitPins[3], digitCodes[digit] & 0b00001000);
  digitalWrite(digitPins[4], digitCodes[digit] & 0b00010000);
  digitalWrite(digitPins[5], digitCodes[digit] & 0b00100000);
  digitalWrite(digitPins[6], digitCodes[digit] & 0b01000000);
} 