import sys
import magic
#bude obsahovat menu (File, Edit, About,...), Queue, v menu bude historie
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog


class QueueWin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('MPx')  # nastavi title
        self.setWindowIcon(QIcon('media-player-5.ico'))  # nastavi ikonku
        self.setGeometry(710, 290, 500, 500) #xMistoOtevreni, yMistoOtevreni, xVelikost, yVelikost
        self.setMinimumSize(400, 400) # xMinimalniVelikost, yMinimalniVelikost

        p = self.palette()
        p.setColor(QPalette.Window, QColor(52, 51, 51))  # nastavi barvu okna
        self.setPalette(p)  # aplikuje barvu

        self._menuBar()



    #def createControls(self):

    def _menuBar(self):
        self.menuBar = self.menuBar()

        open = self.menuBar.addMenu('Soubor')
        open_act = QAction('Otevřít...', self)
        open_act.setShortcut('Ctrl+O')
        open_act.triggered.connect(lambda:self.open_file())
        open.addAction(open_act)


        history = self.menuBar.addMenu('Historie')

        history_act = QAction('Otevřít Historii', self)
        history.addAction(history_act)

        historyClr_act = QAction('Promaž Historii', self)
        history.addAction(historyClr_act)


        about = self.menuBar.addMenu('Autor')
        about_act = QAction('O autorovi...', self)

        about.addAction(about_act)

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
    #def playVideo(self):

    #def playAudio(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)

    qwin = QueueWin()
    qwin.show()

    sys.exit(app.exec_())