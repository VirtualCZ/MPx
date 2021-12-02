import sys

import magic
# bude obsahovat menu (File, Edit, About,...), Queue, v menu bude historie
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog, QWidget, QLabel, QVBoxLayout, QHBoxLayout, \
    QPushButton, QStyle, QSlider
from ui import UI

class QueueWin(QMainWindow, UI):
    def __init__(self, *args, **kwargs):
        super(QueueWin, self).__init__(*args, **kwargs)
        self.ui(self)

        self.setWindowTitle('MPx')  # nastavi title
        self.setWindowIcon(QIcon('media-player-5.ico'))  # nastavi ikonku

        p = self.palette()
        p.setColor(QPalette.Window, QColor(52, 51, 51))  # nastavi barvu okna
        self.setPalette(p)  # aplikuje barvu

        self.open_file_act.triggered.connect(self.open_file)


        self.show()


    #def createControls(self):

    #def _menuBar(self):


    def credits(self):
        w = Credits(self)
        w.show()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
            self.mediaPlayer.play()
            mime = magic.Magic(mime=True)  # check zda je soubor video
            videocheck = mime.from_file(filename)

            if videocheck.find('video') != -1:
                print('it is video')
                self.showMaximized()


class VideoWindow(QWidget):
    def __init__(self, parent=None):
        super(VideoWindow, self).__init__(parent)
        self.setWindowTitle('Video') #nastavi title
        self.setWindowIcon(QIcon('media-player-5.ico')) #nastavi ikonku
        # http://www.iconseeker.com/search-icon/isabi/media-player-5.html   <-- odkaz na ikonku
        self.setGeometry(710, 290, 500, 500) #xMistoOtevreni, yMistoOtevreni, xVelikost, yVelikost
        self.setMinimumSize(400, 400) # xMinimalniVelikost, yMinimalniVelikost

        p = self.palette()
        p.setColor(QPalette.Window, QColor(52, 51, 51)) #nastavi barvu okna
        self.setPalette(p) #aplikuje barvu
        self.prehravac()
        self.show()

    def prehravac(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()

#class History

class Credits(QMainWindow):
    def __init__(self, parent=None):
        super(Credits, self).__init__(parent)
        self.setWindowTitle('Credits')  # nastavi title
        self.setWindowIcon(QIcon('media-player-5.ico'))  # nastavi ikonku
        # http://www.iconseeker.com/search-icon/isabi/media-player-5.html   <-- odkaz na ikonku
        self.setGeometry(710, 290, 500, 200)  # xMistoOtevreni, yMistoOtevreni, xVelikost, yVelikost
        self.setMinimumSize(200, 200)  # xMinimalniVelikost, yMinimalniVelikost

        p = self.palette()
        p.setColor(QPalette.Window, QColor(52, 51, 51))  # nastavi barvu okna
        self.setPalette(p)  # aplikuje barvu

        self.label = QLabel('Autor: Tomáš Gabriel, 3.B OAUH<br>Napsáno pomocí Pythonu a PyQt5', self)
        self.label.setStyleSheet("color: yellow")
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QueueWin()
    mainWin.show()
    sys.exit(app.exec_())