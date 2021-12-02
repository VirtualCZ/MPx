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

        self.centralWidget = QtWidgets.QWidget(QueueWin)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        #self.centralWidget.setSizePolicy(sizePolicy)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()

        self.openFileBtn = QPushButton("Otevrit soubor...", self.centralWidget)
        #self.openFileBtn.clicked.connect(self.open_file)

        self.playBtn = QPushButton(self.centralWidget)  # vytvori tlacitko "play"
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        #self.playBtn.clicked.connect(self.play_video)

        self.slider = QSlider(Qt.Horizontal, self.centralWidget)  # vytvori slider
        self.slider.setRange(0, 0)
        self.slider.valueChanged.connect(self.mediaPlayer.setPosition)

        self.audioSlider = QSlider(Qt.Horizontal, self.centralWidget)
        self.audioSlider.setMaximum(100)
        self.audioSlider.setProperty("value", 100)
        self.audioSlider.valueChanged.connect(self.mediaPlayer.setVolume)

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

        #self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
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
        #open = self.menuBar.addMenu('Soubor')
        #open_act = QAction('Otevřít...', self)
        #open_act.setShortcut('Ctrl+O')
        #open_act.triggered.connect(lambda: self.open_file())
        #open.addAction(open_act)

        #history = self.menuBar.addMenu('Historie')

        #history_act = QAction('Otevřít Historii', self)
        #history_act.setShortcut('Ctrl+H')
        #open_act.triggered.connect(lambda:self.open_history())
        #history.addAction(history_act)

        #historyClr_act = QAction('Promaž Historii', self)
        #historyClr_act.setShortcut('ALT+H')
        #open_act.triggered.connect(lambda:self.clr_history())
        #history.addAction(historyClr_act)

        #about = self.menuBar.addMenu('Autor')
        #about_act = QAction('O autorovi...', self)
        #about_act.setShortcut('CTRL+A')
        #about_act.triggered.connect(lambda: self.credits())
        #about.addAction(about_act)


        QtCore.QMetaObject.connectSlotsByName(QueueWin)
