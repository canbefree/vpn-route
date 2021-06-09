
'''
 VPN tools
'''
import ctypes
import sys

from common.get_domain_ip import getIP
from src import ui

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QDesktopWidget,
                             QFileDialog, QGridLayout, QHBoxLayout, QLabel,
                             QLineEdit, QMainWindow, QMessageBox, QPushButton,
                             QTextEdit, QToolTip, QVBoxLayout, QWidget, qApp)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ =="__main__":
    if is_admin():
        app = QApplication(sys.argv)
        ex = ui.VpnUi()
        sys.exit(app.exec_())
    else:
        if sys.version_info[0] == 3:
    	    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:#in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable,__file__, None, 1)
