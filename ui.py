from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QPushButton, QSlider, QStyle, QHBoxLayout, QVBoxLayout, QMenuBar, QListView

class UI(object):
    def ui(self, QueueWin):
        QueueWin.setObjectName("QueueWin")
        QueueWin.resize(600, 500)

        _translate = QtCore.QCoreApplication.translate
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.centralWidget = QtWidgets.QWidget(QueueWin)

        self.playBtn = QPushButton(self.centralWidget)  # vytvori tlacitko "play"
        self.playBtn.setEnabled(True)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        self.slider = QSlider(Qt.Horizontal, self.centralWidget)  # vytvori slider
        self.slider.setRange(0, 0)

        self.audioSlider = QSlider(Qt.Horizontal, self.centralWidget)
        self.audioSlider.setMaximum(100)
        self.audioSlider.setProperty("value", 100)

        QueueWin.setCentralWidget(self.centralWidget)

        self.playlistV = QListView(self)
        self.playlistV.setAlternatingRowColors(True)
        self.playlistV.setUniformItemSizes(True)
        self.playlistV.setStyleSheet("alternate-background-color: #2f796c;background-color: #1f3f42; color: #ededed;")

        self.hbox = QHBoxLayout()  # umisti tlacitka, slidery,... do UI
        self.hbox.setContentsMargins(11, 11, 11, 11)
        self.hbox.addWidget(self.playBtn)
        self.hbox.addWidget(self.slider)
        self.hbox.addWidget(self.audioSlider)

        self.vbox = QVBoxLayout(self.centralWidget)
        self.vbox.setSpacing(6)
        self.vbox.addWidget(self.playlistV)
        self.vbox.addLayout(self.hbox)

        self.menuBar = QMenuBar(QueueWin)
        QueueWin.setMenuBar(self.menuBar)

        self.setStyleSheet("""
                QMenuBar {
                    background-color: rgb(1,97,99);
                    color: rgb(255,255,255);
                }

                QMenuBar::item {
                    background-color: rgb(1,97,99 );
                    color: rgb(255,255,255);
                }

                QMenuBar::item::selected {
                    background-color: rgb(70,133,136 );
                }

                QMenu {
                    background-color: rgb(31,63,66);
                    color: rgb(255,255,255);   
                }

                QMenu::item::selected {
                    background-color: rgb(41,73,76);
                }
            """)
        #https://stackoverflow.com/questions/54524274/how-do-i-change-the-color-of-the-text-in-a-menu-bar-item-in-pyqt5
        #https://stitchpalettes.com/palette/northern-lights-spa0226/

        self.open = QtWidgets.QMenu(self.menuBar)
        self.open_file_act = QtWidgets.QAction(QueueWin)
        self.open.addAction(self.open_file_act)
        self.open_file_act.setText(_translate("QueueWin", "Otevřít..."))
        self.menuBar.addAction(self.open.menuAction())
        self.open_file_act.setShortcut('CTRL+A')
        self.open.setTitle(_translate("QueueWin", "Soubor"))

        self.open_video_act = QtWidgets.QAction(QueueWin)
        self.open.addAction(self.open_video_act)
        self.open_video_act.setText(_translate("QueueWin", "Videopop"))
        self.open_video_act.setShortcut('CTRL+V')

        self.credits = QtWidgets.QMenu(self.menuBar)
        self.credits_act = QtWidgets.QAction(QueueWin)
        self.credits.addAction(self.credits_act)
        self.credits_act.setText(_translate("QueueWin", "O autorovi"))
        self.menuBar.addAction(self.credits.menuAction())
        self.credits.setTitle(_translate("QueueWin", "About"))
        self.credits_act.setShortcut('CTRL+O')

        QtCore.QMetaObject.connectSlotsByName(QueueWin)

    def videoui(self, VideoWindow):
        VideoWindow.resize(1280, 720)
        self.centralWidget = QtWidgets.QWidget(VideoWindow)

        self.videowidget = QVideoWidget(self.centralWidget)
        VideoWindow.setCentralWidget(self.centralWidget)

        self.hbox = QHBoxLayout()  # umisti tlacitka, slidery,... do UI
        self.hbox.setContentsMargins(11, 11, 11, 11)
        self.hbox.addWidget(self.videowidget)

        self.vbox = QVBoxLayout(self.centralWidget)
        self.vbox.addLayout(self.hbox)

        QtCore.QMetaObject.connectSlotsByName(VideoWindow)

