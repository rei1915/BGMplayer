from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl
import os
from bgm_data import extract_bgm_to_tempfile

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BGMプレイヤー")
        self.setGeometry(200, 200, 300, 120)

        self.play_btn = QPushButton("再生", self)
        self.pause_btn = QPushButton("一時停止", self)
        self.play_btn.setEnabled(False)
        self.pause_btn.setEnabled(True)

        layout = QVBoxLayout()
        layout.addWidget(self.play_btn)
        layout.addWidget(self.pause_btn)
        self.setLayout(layout)

        self.bgm_path = extract_bgm_to_tempfile()
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(self.bgm_path))
        self.audio_output.setVolume(0.5)
        self.player.play()

        self.play_btn.clicked.connect(self.play_music)
        self.pause_btn.clicked.connect(self.pause_music)

    def play_music(self):
        self.player.play()
        self.play_btn.setEnabled(False)
        self.pause_btn.setEnabled(True)

    def pause_music(self):
        self.player.pause()
        self.play_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)

    def closeEvent(self, event):
        if hasattr(self, "bgm_path") and os.path.exists(self.bgm_path):
            os.remove(self.bgm_path)
        event.accept()