import sys
import magic
# pip install python-magic
# pip install python-magic-bin
                                #nedokaze prehrat háčky, kroužky ů ú ěščřžýáíé
                                #fix: replace 214 řádek na              return s.decode('utf-8', errors='replace')      v C:\Users\Virtual\AppData\Local\Programs\Python\Python39\Lib\site-packages\magic\magic.py
            #doc - https://pypi.org/project/python-magic/
            #na kontrolu zda je soubor video
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
            #doc - https://doc.qt.io/qt-5/multimediaoverview.html
# pip install PyQt5

#opencv mega cool

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MPx') #nastavi title
        self.setWindowIcon(QIcon('media-player-5.ico')) #nastavi ikonku
        # http://www.iconseeker.com/search-icon/isabi/media-player-5.html   <-- odkaz na ikonku
        self.setGeometry(710, 290, 500, 500) #xMistoOtevreni, yMistoOtevreni, xVelikost, yVelikost
        self.setMinimumSize(400, 400) # xMinimalniVelikost, yMinimalniVelikost

        p = self.palette()
        p.setColor(QPalette.Window, QColor(52, 51, 51)) #nastavi barvu okna
        self.setPalette(p) #aplikuje barvu

        self.create_player()

        self.show()

    def create_player(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()

        self.openFileBtn = QPushButton("Otevrit soubor...")
        self.openFileBtn.clicked.connect(self.open_file)

        self.playBtn = QPushButton() #vytvori tlacitko "play"
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        self.slider = QSlider(Qt.Horizontal) #vytvori slider
        self.slider.setRange(0,0)
        self.slider.valueChanged.connect(self.mediaPlayer.setPosition)

        self.audioSlider = QSlider(Qt.Horizontal)
        self.audioSlider.setMaximum(100)
        self.audioSlider.setProperty("value", 100)
        self.audioSlider.valueChanged.connect(self.mediaPlayer.setVolume)

        hbox =  QHBoxLayout() #umisti tlacitka, slidery,... do UI
        hbox.setContentsMargins(0,0,0,0)
        hbox.addWidget(self.openFileBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)

        hbox.addWidget(self.audioSlider)

        vbox = QVBoxLayout()
        vbox.addWidget(videowidget)
        vbox.addLayout(hbox)
        self.mediaPlayer.setVideoOutput(videowidget)
        self.setLayout(vbox)

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.update_position)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
            self.mediaPlayer.play()

        mime = magic.Magic(mime=True) #check zda je soubor video
        videocheck = mime.from_file(filename)

        if videocheck.find('video') != -1:
            print('it is video')
            self.showMaximized()

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

        else:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self,duration):
        self.slider.setRange(0, duration)

    def update_position(self, position):
        self.slider.blockSignals(True)
        self.slider.setValue(position)
        self.slider.blockSignals(False)

app = QApplication(sys.argv) #vytvori PyQt5 aplikaci
window = Window()  #vytvori okno
window.show()
sys.exit(app.exec()) #nastartuje aplikaci
#28 31
#https://www.youtube.com/watch?v=45sPjuPJ3vs&list=WL&index=5&t=1053s