# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dial.ui'
#
# Created: Fri May  6 12:01:21 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_about_dial(object):
    def setupUi(self, about_dial):
        about_dial.setObjectName(_fromUtf8("about_dial"))
        about_dial.resize(320, 240)
        about_dial.setMinimumSize(QtCore.QSize(320, 240))
        about_dial.setMaximumSize(QtCore.QSize(320, 240))
        self.textBrowser_about = QtGui.QTextBrowser(about_dial)
        self.textBrowser_about.setEnabled(False)
        self.textBrowser_about.setGeometry(QtCore.QRect(10, 10, 301, 221))
        self.textBrowser_about.setObjectName(_fromUtf8("textBrowser_about"))

        self.retranslateUi(about_dial)
        QtCore.QMetaObject.connectSlotsByName(about_dial)

    def retranslateUi(self, about_dial):
        about_dial.setWindowTitle(_translate("about_dial", "About_AutoCar_Application_V1_0", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    about_dial = QtGui.QWidget()
    ui = Ui_about_dial()
    ui.setupUi(about_dial)
    about_dial.show()
    sys.exit(app.exec_())

