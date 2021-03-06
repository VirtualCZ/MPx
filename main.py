import sys

from PyQt5.QtCore import QUrl, Qt, QAbstractListModel
from PyQt5.QtGui import QPalette, QColor, QIcon, QFont
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel, QStyle

from ui import UI

# veci co budu asi chtit
# https://stackoverflow.com/questions/70227921/pyqt-5-i-need-to-make-a-new-window-with-video-output-qmediaplayer?noredirect=1#comment124143967_70227921
class Model(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()

class QueueWin(QMainWindow, UI):
    def __init__(self, *args, **kwargs):
        super(QueueWin, self).__init__(*args, **kwargs)
        self.ui(self)
        self.v = None
        self.playlist = QMediaPlaylist()
        self.mediaPlayer.setPlaylist(self.playlist)

        self.mediaPlayer.error.connect(self.error)

        self.setWindowTitle('MPx')  # nastavi title
        self.setWindowIcon(QIcon('media-player-5.ico'))  # nastavi ikonku

        p = self.palette()
        p.setColor(QPalette.Window, QColor(1, 97, 99))  # nastavi barvu okna
        self.setPalette(p)  # aplikuje barvu

        self.model = Model(self.playlist)
        self.playlistV.setModel(self.model)
        self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
        selection_model = self.playlistV.selectionModel()
        selection_model.selectionChanged.connect(self.playlist_selection_changed)

        self.open_file_act.triggered.connect(self.open_file)
        self.open_video_act.triggered.connect(self.videopop)
        self.credits_act.triggered.connect(self.creditsd)

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)  # men?? ikonku na tla????tku play
        self.mediaPlayer.positionChanged.connect(self.update_position)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.mediaPlayer.videoAvailableChanged.connect(self.videoAvailableChanged)

        self.slider.valueChanged.connect(self.mediaPlayer.setPosition)
        self.audioSlider.valueChanged.connect(self.mediaPlayer.setVolume)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            QueueWin.play_video(self)
            # https://doc.qt.io/qt-5/qt.html#Key-enum

    def videopop(self):
        if self.v is None:
            self.v = VideoWindow(self)
        self.v.videoui(self.v)
        self.mediaPlayer.setVideoOutput(self.v.videowidget)
        self.v.show()
        self.v.activateWindow()

    def creditsd(self):
        w = Credits(self)
        w.show()

    def open_file(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Open File")

        if filepath:
            self.playlist.addMedia(
                QMediaContent(
                    QUrl.fromLocalFile(filepath)
                )
            )

            self.model.layoutChanged.emit()

    def videoAvailableChanged(self, available):
        if available:
            print('Video')
            self.videopop()

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
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
    def playlist_selection_changed(self, ix):
        # Dostanu QItemSelection z selectionChanged.
        i = ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)
        self.mediaPlayer.play()

    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.model.index(i)
            self.playlistV.setCurrentIndex(ix)
            self.mediaPlayer.play()

    def error(self, *args):
        print(args)

class VideoWindow(QMainWindow, UI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Video')  # nastavi title
        self.setWindowIcon(QIcon('media-player-5.ico'))  # nastavi ikonku
        # http://www.iconseeker.com/search-icon/isabi/media-player-5.html   <-- odkaz na ikonku
        self.setMinimumSize(400, 400)  # xMinimalniVelikost, yMinimalniVelikost
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
        p.setColor(QPalette.Window, QColor(31, 63, 66))  # nastavi barvu okna
        self.setPalette(p)  # aplikuje barvu

        self.label = QLabel('Autor: Tom???? Gabriel, 3.B OAUH<br>Naps??no pomoc?? Pythonu a PyQt5', self)
        self.label.setOpenExternalLinks(True)
        self.label.setStyleSheet("color: #ededed")
        self.label.setFont(QFont('Times', 10))
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QueueWin()
    mainWin.show()
    sys.exit(app.exec_())