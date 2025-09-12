import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QListWidget, QPushButton, QVBoxLayout, QWidget
)
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl

MUSIC_DIR = "bgm"  # 曲ファイルを保存するフォルダ

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("複数曲プレイヤー")
        self.setGeometry(100, 100, 540, 380)

        # 曲リスト
        self.list_widget = QListWidget()
        self.load_music_files()

        # 再生・一時停止ボタン
        self.play_btn = QPushButton("再生")
        self.pause_btn = QPushButton("一時停止")
        self.pause_btn.setEnabled(False)

        # プレイヤー
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(0.5)

        # レイアウト
        layout = QVBoxLayout()
        layout.addWidget(QLabel("曲リスト:"))
        layout.addWidget(self.list_widget)
        layout.addWidget(self.play_btn)
        layout.addWidget(self.pause_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # イベント
        self.play_btn.clicked.connect(self.play_music)
        self.pause_btn.clicked.connect(self.pause_music)
        self.list_widget.itemDoubleClicked.connect(self.select_and_play_music)

        # 最初の曲を自動再生
        if self.list_widget.count() > 0:
            self.list_widget.setCurrentRow(0)
            self.set_music_source(self.list_widget.currentItem().text())
            self.player.play()
            self.play_btn.setEnabled(False)
            self.pause_btn.setEnabled(True)

    def load_music_files(self):
        """bgmフォルダ内の音楽ファイルをリスト表示"""
        if not os.path.exists(MUSIC_DIR):
            os.makedirs(MUSIC_DIR)
        files = [f for f in os.listdir(MUSIC_DIR) if f.lower().endswith(('.mp3', '.wav'))]
        self.list_widget.addItems(files)

    def set_music_source(self, filename):
        """曲ファイルをプレイヤーにセット"""
        music_path = os.path.join(MUSIC_DIR, filename)
        self.player.setSource(QUrl.fromLocalFile(music_path))

    def play_music(self):
        """再生ボタンで再生"""
        selected = self.list_widget.currentItem()
        if selected:
            current_source = self.player.source().toLocalFile()
            new_source = os.path.join(MUSIC_DIR, selected.text())
            # 曲が切り替わった時だけsetSource
            if current_source != new_source:
                self.set_music_source(selected.text())
                self.player.play()
            else:
                # 同じ曲なら再生だけ
                self.player.play()
            self.play_btn.setEnabled(False)
            self.pause_btn.setEnabled(True)

    def select_and_play_music(self):
        """リストダブルクリックで曲切り替え＆再生"""
        selected = self.list_widget.currentItem()
        if selected:
            current_source = self.player.source().toLocalFile()
            new_source = os.path.join(MUSIC_DIR, selected.text())
            if current_source != new_source:
                self.set_music_source(selected.text())
            self.player.play()
            self.play_btn.setEnabled(False)
            self.pause_btn.setEnabled(True)

    def pause_music(self):
        """一時停止（再開時は続きから）"""
        self.player.pause()
        self.play_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())