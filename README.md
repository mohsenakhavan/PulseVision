# 💓 PulseVision - Real-time Heart Rate Monitoring System

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Arduino](https://img.shields.io/badge/Arduino-Compatible-green)

**[English](#english)** | **[فارسی](#persian)**

# English

## 🌟 Overview
PulseVision is an advanced real-time heart rate monitoring system that combines Arduino hardware with a sophisticated Python-based graphical interface. This system provides accurate, real-time heart rate measurements with visual feedback, making it ideal for health monitoring, sports training, medical research, and educational purposes.

The project integrates hardware and software components to create a reliable and user-friendly heart rate monitoring solution. Using an Arduino-based sensor for data acquisition and a PyQt5 graphical interface for visualization, PulseVision offers professional-grade heart rate monitoring capabilities in an accessible package.

## 📸 Project Screenshots

[//]: # "Replace these placeholder links with your actual project screenshots"

| Real-time Monitoring | Interface View | Interface View |
|---------------|---------------------|----------------|
| ![Interface][screenshot1] | ![Monitoring][screenshot2] | ![Analysis][screenshot3] |

[screenshot1]: https://cdn.discordapp.com/attachments/1047503812111372424/1299261848880939072/image.png?ex=671c8f63&is=671b3de3&hm=7e8d8682e9c7347a63449484afd0b9fd6cb01d44794a15199d03086685c74b1a&
[screenshot2]: https://cdn.discordapp.com/attachments/1047503812111372424/1299262138774327346/20241025_100745.jpg?ex=671c8fa9&is=671b3e29&hm=be0e973f2d51e5af830e8de0e27c441b906bd707d977dead26a82c0ca2b30114&
[screenshot3]: https://cdn.discordapp.com/attachments/1047503812111372424/1299262139218788362/20241025_100653.jpg?ex=671c8fa9&is=671b3e29&hm=d7a675c106da9b73d402bd4adbe5a031dfa6ed27a1d81814012ea0c775836275&

## ✨ Key Features

- 📊 Real-time heart rate visualization with professional-grade graphics
- 🔢 Precise BPM (Beats Per Minute) calculation and display
- 📱 Modern, intuitive user interface built with PyQt5
- ⚡ High-performance data processing and display updates
- 📈 Dynamic graphing showing the last 100 samples for trend analysis
- 🔍 Built-in signal filtering for accurate readings
- 💾 Real-time data processing capabilities

## 🛠️ Technical Requirements

### Hardware
- Arduino board (Uno, Nano, or compatible)
- Pulse sensor module
- USB cable for Arduino connection
- Proper wiring components

### Software
- Python 3.6 or higher
- Arduino IDE (latest version recommended)
- Required Python libraries:
  ```
  PyQt5==5.15.9
  pyqtgraph==0.13.3
  pyserial==3.5
  ```

## 📥 Installation & Setup

### 1. Hardware Setup
```
1. Connect the pulse sensor to Arduino:
   - RED wire → 3.3V/5V
   - BLACK wire → GND
   - PURPLE wire → A0
```

### 2. Software Installation
```bash
# Clone the repository
git clone https://github.com/mohsenakhavan/PulseVision.git
cd PulseVision

```

### 3. Arduino Configuration
```
1. Open Arduino IDE
2. Load test.ino
3. Select correct board and port
4. Upload the code
```

### 4. Running the Application
```bash
python main.py
```

## 💻 Usage Guide

1. **Initial Setup**
   - Ensure all connections are secure
   - Verify Arduino port in main.py
   - Start the application

2. **Sensor Placement**
   - Place the sensor correctly on fingertip/earlobe
   - Maintain steady pressure for best results

3. **Monitoring**
   - Watch real-time BPM display
   - Monitor heart rate graph
   - Check for stable readings

## 🔧 Troubleshooting

Common issues and solutions:
- No serial connection: Check COM port settings
- Noisy readings: Ensure proper sensor contact
- Display issues: Verify PyQt5 installation

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact & Support

- Create an Issue for bug reports
- Submit Pull Requests for contributions
- Contact maintainers for further questions

---

<div dir="rtl">

# فارسی

## 🌟 نمای کلی
PulseVision یک سیستم پیشرفته مانیتورینگ ضربان قلب در زمان واقعی است که سخت‌افزار Arduino را با یک رابط گرافیکی پیشرفته مبتنی بر Python ترکیب می‌کند. این سیستم اندازه‌گیری‌های دقیق ضربان قلب را با بازخورد تصویری ارائه می‌دهد که آن را برای نظارت بر سلامت، تمرینات ورزشی، تحقیقات پزشکی و اهداف آموزشی ایده‌آل می‌سازد.

این پروژه با یکپارچه‌سازی اجزای سخت‌افزاری و نرم‌افزاری، یک راه‌حل قابل اعتماد و کاربرپسند برای نظارت بر ضربان قلب ایجاد می‌کند. با استفاده از سنسور مبتنی بر Arduino برای جمع‌آوری داده‌ها و رابط گرافیکی PyQt5 برای تجسم‌سازی، PulseVision قابلیت‌های نظارت بر ضربان قلب در سطح حرفه‌ای را در یک بسته قابل دسترس ارائه می‌دهد.

## 📸 تصاویر پروژه

| نمای تحلیل | مانیتورینگ زنده | رابط کاربری |
|------------|-----------------|-------------|
| ![تحلیل][screenshot3] | ![مانیتورینگ][screenshot2] | ![رابط][screenshot1] |

## ✨ ویژگی‌های کلیدی

- 📊 نمایش گرافیکی ضربان قلب در زمان واقعی با گرافیک حرفه‌ای
- 🔢 محاسبه و نمایش دقیق BPM (ضربان در دقیقه)
- 📱 رابط کاربری مدرن و بصری با PyQt5
- ⚡ پردازش داده و به‌روزرسانی نمایش با کارایی بالا
- 📈 نمودار پویا با نمایش 100 نمونه آخر برای تحلیل روند
- 🔍 فیلترینگ داخلی سیگنال برای قرائت‌های دقیق
- 💾 قابلیت پردازش داده در زمان واقعی

## 🛠️ نیازمندی‌های فنی

### سخت‌افزار
- برد Arduino (Uno، Nano یا سازگار)
- ماژول سنسور ضربان
- کابل USB برای اتصال Arduino
- قطعات سیم‌کشی مناسب

### نرم‌افزار
- Python 3.6 یا بالاتر
- Arduino IDE (آخرین نسخه توصیه می‌شود)
- کتابخانه‌های Python مورد نیاز:
  ```
  PyQt5==5.15.9
  pyqtgraph==0.13.3
  pyserial==3.5
  ```

## 📥 نصب و راه‌اندازی

### 1. راه‌اندازی سخت‌افزار
```
1. اتصال سنسور ضربان به Arduino:
   - سیم قرمز → 3.3V/5V
   - سیم مشکی → GND
   - سیم بنفش → A0
```

### 2. نصب نرم‌افزار
```bash
# کلون کردن مخزن
git clone https://github.com/mohsenakhavan/PulseVision.git
cd PulseVision

```

### 3. پیکربندی Arduino

1. باز کردن Arduino IDE
2. بارگذاری test.ino
3. انتخاب برد و پورت صحیح
4. آپلود کد
```

### 4. اجرای برنامه
python main.py
```

## 💻 راهنمای استفاده

1. **راه‌اندازی اولیه**
   - از محکم بودن همه اتصالات اطمینان حاصل کنید
   - پورت Arduino را در main.py تأیید کنید
   - برنامه را اجرا کنید

2. **قرارگیری سنسور**
   - سنسور را به درستی روی نوک انگشت/لاله گوش قرار دهید
   - برای بهترین نتایج، فشار ثابتی را حفظ کنید

3. **نظارت**
   - نمایش BPM در زمان واقعی را مشاهده کنید
   - نمودار ضربان قلب را نظارت کنید
   - قرائت‌های پایدار را بررسی کنید

## 🔧 عیب‌یابی

مشکلات رایج و راه‌حل‌ها:
- عدم اتصال سریال: تنظیمات پورت COM را بررسی کنید
- قرائت‌های نویزدار: از تماس مناسب سنسور اطمینان حاصل کنید
- مشکلات نمایش: نصب PyQt5 را تأیید کنید

## 🤝 مشارکت

از مشارکت شما استقبال می‌کنیم! لطفاً این مراحل را دنبال کنید:

1. پروژه را Fork کنید
2. یک شاخه ویژگی ایجاد کنید
3. تغییرات خود را Commit کنید
4. به شاخه Push کنید
5. یک Pull Request ایجاد کنید

## 📝 مجوز

این پروژه تحت مجوز MIT منتشر شده است - برای جزئیات فایل [LICENSE](LICENSE) را ببینید.

## 📞 تماس و پشتیبانی

- برای گزارش اشکالات یک Issue ایجاد کنید
- برای مشارکت‌ها Pull Request ارسال کنید
- برای سؤالات بیشتر با نگهدارندگان تماس بگیرید

</div>

---
⭐ از ستاره دادن به این پروژه خودداری نکنید!
