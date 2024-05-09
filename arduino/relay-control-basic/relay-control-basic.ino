// basic relay control using arduino

void setup()
{
  pinMode(3, OUTPUT);
}

void loop()
{
  digitalWrite(3, HIGH);
  delay(3000); // Wait for 3000 milliseconds
  digitalWrite(3, LOW);
  delay(3000); // Wait for 3000 milliseconds
}
