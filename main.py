import sys
import serial
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg

# تنظیمات سریال برای Arduino
ser = serial.Serial('COM3', 9600)  # پورت سریال Arduino را بر اساس سیستم خود تنظیم کنید

# کلاس اصلی پنجره گرافیکی
class HeartRateMonitor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(100)  # هر 100 میلی‌ثانیه داده‌ها را به‌روز کند

        self.x_data = []
        self.y_data = []

    def initUI(self):
        # تنظیمات پنجره اصلی
        self.setWindowTitle('Heartbeat Monitor')
        self.setGeometry(100, 100, 800, 600)

        # ویجت مرکزی
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        
        # طرح‌بندی اصلی
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
        
        # نمودار ضربان قلب
        self.plot_widget = pg.PlotWidget()
        self.layout.addWidget(self.plot_widget)
        self.plot = self.plot_widget.plot(pen=pg.mkPen(color='r', width=2))  # تنظیم رنگ و ضخامت نمودار
        
        # فیلد نمایش BPM
        self.bpm_label = QtWidgets.QLabel('BPM: -')
        self.bpm_label.setStyleSheet("font-size: 20px; color: blue;")
        self.layout.addWidget(self.bpm_label)

    def update_data(self):
        if ser.in_waiting > 0:
            try:
                data = ser.readline().decode('utf-8').strip()  # خواندن داده از سریال
                bpm_value = int(data)  # تبدیل داده به عدد
                self.x_data.append(len(self.x_data))  # محور x، تعداد نمونه‌ها
                self.y_data.append(bpm_value)  # محور y، مقدار BPM
                self.plot.setData(self.x_data[-100:], self.y_data[-100:])  # فقط 100 نقطه اخیر را نمایش دهد
                
                # به‌روز کردن نمایش BPM
                self.bpm_label.setText(f'BPM: {bpm_value}')
            except ValueError:
                pass

# راه‌اندازی برنامه
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    monitor = HeartRateMonitor()
    monitor.show()
    sys.exit(app.exec_())
