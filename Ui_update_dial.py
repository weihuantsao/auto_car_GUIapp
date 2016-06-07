# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_form.ui'
#
# Created: Fri May 20 09:49:03 2016
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(320, 240)
        self.label_update_state = QtGui.QLabel(Dialog)
        self.label_update_state.setGeometry(QtCore.QRect(60, 110, 181, 20))
        self.label_update_state.setText(_fromUtf8(""))
        self.label_update_state.setObjectName(_fromUtf8("label_update_state"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 180, 85, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_goupdate = QtGui.QPushButton(Dialog)
        self.pushButton_goupdate.setGeometry(QtCore.QRect(60, 180, 85, 41))
        self.pushButton_goupdate.setObjectName(_fromUtf8("pushButton_goupdate"))
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 70, 181, 21))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_current_version = QtGui.QLabel(self.formLayoutWidget)
        self.label_current_version.setText(_fromUtf8(""))
        self.label_current_version.setObjectName(_fromUtf8("label_current_version"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_current_version)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_2.setText(_translate("Dialog", "取消", None))
        self.pushButton_goupdate.setText(_translate("Dialog", "更新", None))
        self.label.setText(_translate("Dialog", "目前版本 ：", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

