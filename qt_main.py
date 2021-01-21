import sys
import os
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtCore import QFile, QIODevice
# from mainwindow_ui import Ui_MainWindow

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


# Instance class
if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.path.join(os.path.dirname(__file__), "qml/login.qml"))
    # check exit app
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())