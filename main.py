import sys
import magic
# pip install python-magic
# pip install python-magic-bin
            #na kontrolu zda je soubor video
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MPx') #nastavi title
        self.setWindowIcon(QIcon('media-player-5.ico')) #nastavi ikonku
        # http://www.iconseeker.com/search-icon/isabi/media-player-5.html   <-- odkaz na ikonku
        # https://doc.qt.io/qt-5/multimediaoverview.html        <-- dokumentace PyQt5
        self.setGeometry(710, 290, 500, 500) #xMistoOtevreni, yMistoOtevreni, xVelikost, yVelikost
        self.setMinimumSize(400, 400) # xMinimalniVelikost,

        p = self.palette()
        p.setColor(QPalette.Window, Qt.lightGray) #nastavi barvu okna
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

        self.audioSlider = QSlider(Qt.Horizontal)
        self.audioSlider.setRange(0,0)

        self.volumeDownBtn = QPushButton('-',clicked=self.volumeDown)
        self.volumeUpBtn = QPushButton('+', clicked=self.volumeUp)


        hbox =  QHBoxLayout() #umisti tlacitka, slidery,... do UI
        hbox.setContentsMargins(0,0,0,0)
        hbox.addWidget(self.openFileBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)

        hbox.addWidget(self.audioSlider)
        hbox.addWidget(self.volumeDownBtn)
        hbox.addWidget(self.volumeUpBtn)

        vbox = QVBoxLayout()
        vbox.addWidget(videowidget)
        vbox.addLayout(hbox)
        self.mediaPlayer.setVideoOutput(videowidget)
        self.setLayout(vbox)

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def volumeDown(self):
        currentVolume = self.mediaPlayer.volume()
        print(currentVolume)
        self.mediaPlayer.setVolume(currentVolume - 5)

    def volumeUp(self):
            currentVolume = self.mediaPlayer.volume()
            print(currentVolume)
            self.mediaPlayer.setVolume(currentVolume + 5)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
            self.showMaximized()
            self.mediaPlayer.play()

        mime = magic.Magic(mime=True)
        filenamecheck = mime.from_file(filename)
        if filenamecheck.find('video') != -1:
            print('it is video')

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

app = QApplication(sys.argv) #vytvori PyQt5 aplikaci
window = Window()  #vytvori okno
window.show()
sys.exit(app.exec()) #nastartuje aplikaci
#28 31
#https://www.youtube.com/watch?v=45sPjuPJ3vs&list=WL&index=5&t=1053s