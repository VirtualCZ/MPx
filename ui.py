from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QPushButton, QSlider, QStyle, QHBoxLayout, QVBoxLayout, QMenuBar


class UI(object):
    def ui(self, QueueWin):
        QueueWin.setObjectName("QueueWin")
        QueueWin.resize(600, 500)
        _translate = QtCore.QCoreApplication.translate
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.centralWidget = QtWidgets.QWidget(QueueWin)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        #self.centralWidget.setSizePolicy(sizePolicy)



        self.openFileBtn = QPushButton("Otevrit soubor...", self.centralWidget)
        self.openFileBtn.clicked.connect(self.open_file)

        self.playBtn = QPushButton(self.centralWidget)  # vytvori tlacitko "play"
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        self.slider = QSlider(Qt.Horizontal, self.centralWidget)  # vytvori slider
        self.slider.setRange(0, 0)

        self.audioSlider = QSlider(Qt.Horizontal, self.centralWidget)
        self.audioSlider.setMaximum(100)
        self.audioSlider.setProperty("value", 100)

        QueueWin.setCentralWidget(self.centralWidget)

        # self.queue = QListView(self)
        # self.queue.setAcceptDrops(True)
        # self.queue.setAlternatingRowColors(True)

        self.hbox = QHBoxLayout(self.centralWidget)  # umisti tlacitka, slidery,... do UI
        self.hbox.setContentsMargins(11, 11, 11, 11)
        self.hbox.addWidget(self.openFileBtn)
        self.hbox.addWidget(self.playBtn)
        self.hbox.addWidget(self.slider)
        self.hbox.addWidget(self.audioSlider)

        self.vbox = QVBoxLayout(self.centralWidget)
        #self.vbox.addWidget(videowidget)
        # vbox.addWidget(self.queue)
        self.vbox.addLayout(self.hbox)
        #self.mediaPlayer.setVideoOutput(videowidget)

        #self.mediaPlayer.positionChanged.connect(self.update_position)
        #self.mediaPlayer.durationChanged.connect(self.duration_changed)


        self.menuBar = QMenuBar(QueueWin)
        QueueWin.setMenuBar(self.menuBar)

        self.open = QtWidgets.QMenu(self.menuBar)
        self.open_file_act = QtWidgets.QAction(QueueWin)
        self.open.addAction(self.open_file_act)
        self.open_file_act.setText(_translate("QueueWin", "Otevřít..."))
        self.menuBar.addAction(self.open.menuAction())
        self.open.setTitle(_translate("QueueWin", "Soubor"))

        self.history = QtWidgets.QMenu(self.menuBar)
        self.history_act = QtWidgets.QAction(QueueWin)
        self.history.addAction(self.history_act)
        self.history_act.setText(_translate("QueueWin", "Otevřít historii"))
        self.menuBar.addAction(self.history.menuAction())
        self.history.setTitle(_translate("QueueWin", "Historie"))

        self.historyClr_act = QtWidgets.QAction(QueueWin)
        self.history.addAction(self.historyClr_act)
        self.historyClr_act.setText(_translate("QueueWin", "Vymazat historii"))
        self.historyClr_act.setShortcut('ALT+H')

        #about = self.menuBar.addMenu('Autor')
        #about_act = QAction('O autorovi...', self)
        #about_act.setShortcut('CTRL+A')
        #about_act.triggered.connect(lambda: self.credits())
        #about.addAction(about_act)

        QtCore.QMetaObject.connectSlotsByName(QueueWin)

    def videoui(self, VideoWindow):
        VideoWindow.setObjectName("QueueWin")
        VideoWindow.resize(600, 500)
        self.centralWidget = QtWidgets.QWidget(VideoWindow)
        self.videowidget = QVideoWidget(self.centralWidget)
        VideoWindow.setCentralWidget(self.centralWidget)
        self.hbox = QHBoxLayout(self.centralWidget)  # umisti tlacitka, slidery,... do UI
        self.hbox.setContentsMargins(11, 11, 11, 11)
        self.hbox.addWidget(self.videowidget)
        self.vbox = QVBoxLayout(self.centralWidget)
        self.vbox.addLayout(self.hbox)

        QtCore.QMetaObject.connectSlotsByName(VideoWindow)