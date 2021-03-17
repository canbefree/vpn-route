import ctypes
import optparse
import os
import re
import socket
import sys
import tempfile
import typing

import psutil
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QDesktopWidget,
                             QFileDialog, QGridLayout, QHBoxLayout, QLabel,
                             QLineEdit, QMainWindow, QMessageBox, QPushButton,
                             QTextEdit, QToolTip, QVBoxLayout, QWidget, qApp)


class VpnUi(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUi()

    def initUi(self):

        self.setGeometry(300,300,300,220)
        
        enable_btn = QPushButton("开启VPN",self)
        enable_btn.move(10,10)
        enable_btn.clicked.connect(self.enable_vpn)

        disable_btn = QPushButton("关闭VPN",self)
        disable_btn.move(200,10)
        disable_btn.clicked.connect(self.disable_vpn)


        choose_file_btn = QPushButton("打开文件",self)
        choose_file_btn.move(150,50)
        choose_file_btn.resize(50,20)

        choose_file_btn.clicked.connect(self.open_file_dialog)

        self.vpnfile = QLineEdit("选择文件",self)
        self.vpnfile.setFocus()
        self.vpnfile.move(10,50)

        switch_btn = QPushButton("更新metric",self)
        switch_btn.move(220,50)

        self.show()


    def enable_vpn(self):
        ## 启动VPN
        result = os.popen("rasdial vpn")
        print(result.read())
        ## 获取当前路由
        vpn = self.get_vpn_gateway("vpn")
        print(vpn)

        ## 加大vpn权重
        cmd = "route change 0.0.0.0 mask 0.0.0.0 {} metric 1".format(vpn)
        result = os.popen(cmd)
        print(result.read())

    def disable_vpn(self):
        result = os.popen("rasdial vpn /disconnect")
        print(result.read())

        cmd = "powershell netsh interface set interface '以太网' {}"
        print(cmd.format("disabled"))
        result = os.popen(cmd.format("disabled"))
        print(result.read())

        cmd = "powershell netsh interface set interface '以太网' {}"
        print(cmd.format("enable"))
        result = os.popen(cmd.format("enable"))
        print(result.read())


    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        default_path = "{}{}config".format(os.path.dirname(__file__),os.sep)
        data_path = QFileDialog.getOpenFileName(self,'Open File',default_path,'*.txt',options=options)
        self.vpnfile.setText(data_path[0])

    def get_vpn_gateway(self,net_name:str):
        '''
        获取vpn访问地址
        @param net_name net名称
        '''
        addrs = psutil.net_if_addrs()
        if net_name in addrs:
            addr_family = addrs[net_name]
            for addr in addr_family:
                if addr[0] == socket.AddressFamily.AF_INET:
                    return addr[1]
        return None


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    app = QApplication(sys.argv)
    ex = VpnUi()
    sys.exit(app.exec_())
else:
    if sys.version_info[0] == 3:
    	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable,__file__, None, 1)