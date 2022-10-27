from PyQt5 import QtWidgets, uic, QtCore, QtGui 
import sys
import weather, download_image

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('weather.ui', self) # Load the .ui file
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Exit_Button.clicked.connect(quit)
        self.Get_Button.clicked.connect(self.set_weather_stats)
        self.show() # Show the GUI
    def enable_search(self):
        self.Get_Button.setEnabled(True)
        
    def set_weather_stats(self):
        self.Get_Button.setEnabled(False)
        stats = weather.get_weather(self.Search_LineEdit.text())
        self.Geo_Label.setText(stats[0])
        self.Temp_Label.setText(stats[1])
        self.Time_Label.setText(stats[2])
        self.Weather_Label.setText(stats[3])
        if download_image.download(stats[4]):
            pixmap = QtGui.QPixmap("out.png")
            self.Photo_Label.setPixmap(pixmap)
        QtCore.QTimer.singleShot(5000, self.enable_search)
        

        
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
