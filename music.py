import sys
from PyQt6.QtWidgets import QApplication
from player import MusicPlayer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec())