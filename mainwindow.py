# Embedded file name: C:\Users\USER\Desktop\auto_test\serial_app\mainwindow.py
"""
Module implementing MainWindow.
"""
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtNetwork import QTcpSocket
from Ui_mainwindow import Ui_MainWindow
from Ui_help_dial import Ui_about_dial
from Ui_update_dial import Ui_Dialog
import time
import serial
import platform
import glob
import serialportcontext
import threading
import time
import subprocess
import os

class UpdateQDialog(QDialog, Ui_Dialog):

    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_goupdate.clicked.connect(self.ChooseDirectory)

    def ChooseDirectory(self):
        file_path = os.getcwd() + '/upgrade.bat'
        output = subprocess.Popen([file_path], stdout=subprocess.PIPE).communicate()[0]


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    _receive_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.about_Dialog = QtGui.QDialog()
        self.about_ui = Ui_about_dial()
        self.about_ui.setupUi(self.about_Dialog)
        self.update_dialog = UpdateQDialog(self)
        self._port = ''
        self._baud = ''
        self._currentcmd = ''
        self._last_received = ''
        self._gopath = 'D001' + self.ui.comboBox_d001_value.currentText()
        self.on_pushButton_serialrefresh_clicked()
        self._serial_context_ = serialportcontext.SerialPortContext(port=self._port, baud=self._port)
        self._receive_signal.connect(self.__display_recv_data__)

    def list_serial_ports(self):
        system_name = platform.system()
        if system_name == 'Windows':
            available = []
            for i in range(256):
                try:
                    s = serial.Serial(i)
                    available.append(s.portstr)
                    s.close()
                except serial.SerialException:
                    pass

            return available
        elif system_name == 'Darwin':
            return glob.glob('/dev/cu*')
        else:
            return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')

    def __open_serial_port__(self):
        if self._serial_context_.isRunning():
            self._serial_context_.close()
        else:
            try:
                port = str(self.ui.comboBox_serialport.currentText())
                baud = int('%s' % self.ui.comboBox_serialbauds.currentText(), 10)
                self._serial_context_ = serialportcontext.SerialPortContext(port=port, baud=baud)
                self._serial_context_.registerReceivedCallback(self.__data_received__)
                self._serial_context_.setDTR(True)
                self._serial_context_.setRTS(True)
                self._serial_context_.open()
            except Exception as e:
                self.print_debug(str(e))
                QtGui.QMessageBox.critical(self, u'\x08\u958b\u8d77\u7aef\u53e3', u'\u958b\u8d77\u7aef\u53e3\u5931\u6557,\u8acb\u6aa2\u67e5!')

    def __data_received__(self, data):
        self._receive_signal.emit(data)

    def __display_recv_data__(self, data):
        self.print_recive(str(data))

    def __send_data__(self, msg):
        data = str(msg)
        if self._serial_context_.isRunning():
            if len(data) > 0:
                self._serial_context_.send(data, False)
                self.print_send(data)
        else:
            self.print_debug("Can't send cmd", 'ERROR')

    def __closeEvent__(self):
        if self._serial_context_.isRunning():
            self._serial_context_.close()
            self.print_debug('SERIAL PORT CLOSE', 'INFO')

    def showDial(self):
        with open('help/about_app') as f:
            content = f.read()
        self.about_ui.textBrowser_about.setText(content)
        self.about_Dialog.exec_()

    def showDial_update(self):
        with open('current_version.ini') as f:
            content = f.read().rstrip('\n')
        self.update_dialog.ui.label_current_version.setText(content)
        file_path = os.getcwd() + '/checkupdate.bat'
        output = subprocess.Popen([file_path], stdout=subprocess.PIPE, shell=True).communicate()[0]
        output = output.rstrip('\n')
        self.update_dialog.ui.label_update_state.setText(output)
        self.update_dialog.exec_()

    def currentcmd_update(self):
        self._gopath = self._gopath[:4] + self.ui.comboBox_d001_value.currentText() + self._gopath[5:]
        _cmd = 'QQQ' + self._gopath + 'XXX'
        self._currentcmd = _cmd
        self.ui.textEdit_currentcmd.setText(self._currentcmd)
        return True

    def print_debug(self, mes, stat = 'LOG'):
        st = {'NOTIFY': 'blue',
         'INFO': 'green',
         'ERROR': 'red',
         'LOG': 'gray'}
        text_format = '<span style="color:%s;" >' % st.get(stat)
        text_format = text_format + mes
        text_format = text_format + '</span>'
        self.ui.textEdit_debugmessage.append(text_format)

    def print_send(self, mes, stat = 'NOTIFY'):
        st = {'NOTIFY': 'blue',
         'INFO': 'green',
         'ERROR': 'red',
         'LOG': 'gray'}
        text_format = '<span style="color:%s;" >' % st.get(stat)
        text_format = text_format + mes
        text_format = text_format + '</span>'
        self.ui.textEdit_sendmessage.append(text_format)

    def print_recive(self, mes, stat = 'INFO'):
        st = {'NOTIFY': 'blue',
         'INFO': 'green',
         'ERROR': 'red',
         'LOG': 'gray'}
        text_format = '<span style="color:%s;" >' % st.get(stat)
        text_format = text_format + mes
        text_format = text_format + '</span>'
        self.ui.textEdit_recivemessage.insertPlainText(mes)

    @pyqtSignature('')
    def on_commandLinkButton_serailopen_clicked(self):
        self._port = self.ui.comboBox_serialport.currentText()
        self._baud = self.ui.comboBox_serialbauds.currentText()
        self.print_debug('SERIAL PORT OPEN--port : %s  baud : %s' % (self._port, self._baud), 'INFO')
        self.__open_serial_port__()
        self.ui.commandLinkButton_serailopen.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(True)

    @pyqtSignature('')
    def on_pushButton_stop_clicked(self):
        self.__closeEvent__()
        self.ui.commandLinkButton_serailopen.setEnabled(True)
        self.ui.pushButton_stop.setEnabled(False)

    @pyqtSignature('')
    def on_pushButton_send_rawcmd_clicked(self):
        cmd = self.ui.textEdit_sendcmd.toPlainText()
        if cmd == '':
            self.__send_data__('empty cmd')
        else:
            self.__send_data__(cmd)

    @pyqtSignature('')
    def on_pushButton_send_currentcmd_clicked(self):
        cmd = self.ui.textEdit_currentcmd.toPlainText()
        if cmd == '':
            self.__send_data__('empty cmd')
        else:
            self.__send_data__(cmd)

    @pyqtSignature('')
    def on_pushButton_serialrefresh_clicked(self):
        self.ui.comboBox_serialport.clear()
        self.ui.comboBox_serialport.addItems(self.list_serial_ports())

    @pyqtSignature('')
    def on_pushButton_reset_funbtn_clicked(self):
        self._gopath = 'D001' + self.ui.comboBox_d001_value.currentText()
        self.print_debug('>>clear cmd')
        self.ui.textEdit_currentcmd.setText('')

    @pyqtSignature('')
    def on_pushButton_addpath_clicked(self):
        choosepath = self.ui.comboBox_choosepath.currentText()
        path2stop = self.ui.comboBox_path2stop.currentIndex()
        self._gopath = self._gopath + str(choosepath) + str(path2stop)
        self.print_debug('>>add new station : %s%s' % (choosepath, path2stop))
        self.currentcmd_update()

    @pyqtSignature('')
    def on_pushButton_batterystate_clicked(self):
        cmd = 'QQQJ0040XXX'
        self.__send_data__(cmd)

    @pyqtSignature('')
    def on_pushButton_lastcardstate_clicked(self):
        cmd = 'QQQJ0120XXX'
        self.__send_data__(cmd)

    @pyqtSignature('')
    def on_pushButton_runstate_clicked(self):
        cmd = 'QQQJ0020XXX'
        self.__send_data__(cmd)

    @pyqtSignature('')
    def on_pushButton_addrotation_clicked(self):
        cmd = 'Z00'
        if self.ui.comboBox_rotation.currentIndex() == 0:
            cmd = cmd + '21'
        else:
            cmd = cmd + '31'
        self._gopath = self._gopath + str(cmd)
        self.print_debug('>>add rotation : %s' % cmd)
        self.currentcmd_update()

    @pyqtSignature('')
    def on_actionAbout_AutoCar_triggered(self):
        self.showDial()

    @pyqtSignature('')
    def on_action_checkupdate_triggered(self):
        self.showDial_update()

    @pyqtSignature('QString')
    def on_comboBox_d001_value_currentIndexChanged(self):
        self.print_debug('>>change speed : %s' % self.ui.comboBox_d001_value.currentText())
        self.currentcmd_update()