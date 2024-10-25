int pulsePin = A0;  // پین آنالوگ متصل به سنسور ضربان قلب
int threshold = 512;  // آستانه تشخیص ضربان
unsigned long lastBeatTime = 0;  // زمان آخرین ضربان
unsigned long interval = 0;  // فاصله بین ضربان‌ها
int bpm = 0;  // ضربان در دقیقه

void setup() {
  Serial.begin(9600);  // شروع ارتباط سریال
}

void loop() {
  int pulseValue = analogRead(pulsePin);  // خواندن مقدار آنالوگ

  if (pulseValue > threshold) {  // بررسی اینکه آیا ضربان قلب شناسایی شده است
    unsigned long currentTime = millis();
    if (currentTime - lastBeatTime > 600) {  // جلوگیری از تشخیص چند ضربه به سرعت
      interval = currentTime - lastBeatTime;
      lastBeatTime = currentTime;
      bpm = 60000 / interval;  // محاسبه BPM
      Serial.println(bpm);  // ارسال BPM به کامپیوتر
    }
  }
  
  delay(10);  // تاخیر برای جلوگیری از ارسال بیش از حد داده‌ها
}
