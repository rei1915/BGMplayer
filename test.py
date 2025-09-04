import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("サンプルプログラム")  # ウィンドウのタイトルを設定
        self.setGeometry(
            100, 100, 540, 380
        )  # ウィンドウの表示位置(x,y)と大きさ(w,h)を設定

        self.label1 = QLabel(self)  # ラベルを配置
        self.label1.setText("Hello World!")  # ラベルのテキストを設定
        self.label1.adjustSize()  # テキストに合わせてラベルサイズを変更
        self.label1.move(50, 40)  # ラベルの表示位置を変更

        self.label2 = QLabel(self)
        self.label2.setText("これはサンプルです。")
        self.label2.adjustSize()
        self.label2.move(50, 80)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())