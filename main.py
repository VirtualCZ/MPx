import sys
# bude obsahovat menu (File, Edit, About,...), Queue, v menu bude historie
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog, QWidget, QLabel, QVBoxLayout, QHBoxLayout, \
    QPushButton, QStyle, QSlider
from ui import UI
# do dokumentace:
#kontrola videa https://python.hotexamples.com/examples/PyQt5.QtMultimedia/QMediaPlayer/state/python-qmediaplayer-state-method-examples.html

#veci co budu asi chtit
#https://stackoverflow.com/questions/70227921/pyqt-5-i-need-to-make-a-new-window-with-video-output-qmediaplayer?noredirect=1#comment124143967_70227921
#https://www.pythonguis.com/tutorials/creating-multiple-windows/
class QueueWin(QMainWindow, UI):
    def __init__(self, *args, **kwargs):
        super(QueueWin, self).__init__(*args, **kwargs)
        self.ui(self)
        self.playlist = QMediaPlaylist()
        self.mediaPlayer.setPlaylist(self.playlist)

        self.setWindowTitle('MPx')  # nastavi title
        self.setWindowIcon(QIcon('media-player-5.ico'))  # nastavi ikonku

        p = self.palette()
        p.setColor(QPalette.Window, QColor(52, 51, 51))  # nastavi barvu okna
        self.setPalette(p)  # aplikuje barvu

        self.open_file_act.triggered.connect(self.open_file)
        #self.history_act.triggered.connect(self.open_history)
        self.history_act.triggered.connect(self.videopop)
        #self.open_act.triggered.connect(self.clr_history)

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed) #mení ikonku na tlačítku play
        self.mediaPlayer.positionChanged.connect(self.update_position)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.mediaPlayer.videoAvailableChanged.connect(self.videoAvailableChanged)

        self.slider.valueChanged.connect(self.mediaPlayer.setPosition)
        self.audioSlider.valueChanged.connect(self.mediaPlayer.setVolume)

    def open_history (self):
        h = History(self)
        h.show()

    def videopop(self):
        v = VideoWindow(self)
        v.show()

    def credits(self):
        w = Credits(self)
        w.show()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
            self.mediaPlayer.play()

    def videoAvailableChanged(self, available):
        videoWindow = VideoWindow(self)
        if available:
            print('Video')
            self.mediaPlayer.setVideoOutput(videoWindow.videowidget)
            videoWindow.show()
#bylo by fajn to okno pak zavrit

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self,duration):
        self.slider.setRange(0, duration)

    def update_position(self, position):
        self.slider.blockSignals(True)
        self.slider.setValue(position)
        self.slider.blockSignals(False)

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

class VideoWindow(QMainWindow, UI):
    def __init__(self, *args, **kwargs):
        super(VideoWindow, self).__init__(*args, **kwargs)
        self.videoui(self)
        self.setWindowTitle('Video') #nastavi title
        self.setWindowIcon(QIcon('media-player-5.ico')) #nastavi ikonku
        # http://www.iconseeker.com/search-icon/isabi/media-player-5.html   <-- odkaz na ikonku
        self.setGeometry(710, 290, 500, 500) #xMistoOtevreni, yMistoOtevreni, xVelikost, yVelikost
        self.setMinimumSize(400, 400) # xMinimalniVelikost, yMinimalniVelikost
        p = self.palette()
        p.setColor(QPalette.Window, QColor(52, 51, 51)) #nastavi barvu okna
        self.setPalette(p) #aplikuje barvu

class History(QMainWindow):
    def __init__(self, parent=None):
        super(History, self).__init__(parent)
        self.setWindowTitle('Historie')  # nastavi title
        self.setWindowIcon(QIcon('media-player-5.ico'))  # nastavi ikonku
        # http://www.iconseeker.com/search-icon/isabi/media-player-5.html   <-- odkaz na ikonku
        self.setGeometry(710, 290, 500, 200)  # xMistoOtevreni, yMistoOtevreni, xVelikost, yVelikost
        self.setMinimumSize(200, 200)  # xMinimalniVelikost, yMinimalniVelikost

        p = self.palette()
        p.setColor(QPalette.Window, QColor(52, 51, 51))  # nastavi barvu okna
        self.setPalette(p)  # aplikuje barvu

class Credits(QMainWindow):
    def __init__(self, parent=None):
        super(Credits, self).__init__(parent)
        self.setWindowTitle('O programu')  # nastavi title
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