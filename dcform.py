# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dcform.ui'
#
# Created by: PyQt4 UI code generator 4.9.6
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
        Dialog.resize(1028, 698)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(91, 91, 91);"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, -1, 1021, 91))
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgb(153, 204, 204);"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textEdit = QtGui.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(140, 26, 651, 27))
        self.textEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(140, 60, 83, 20))
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 192, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 60, 83, 20))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 220, 168);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(4, 20, 131, 61))
        self.groupBox_3.setStyleSheet(_fromUtf8("background-color: rgb(51, 153, 204);"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.comboBox = QtGui.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(10, 21, 111, 24))
        self.comboBox.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 220);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(320, 60, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(952, 20, 51, 25))
        self.pushButton_6.setStyleSheet(_fromUtf8("background-color: rgb(192, 192, 0);"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(430, 60, 81, 21))
        self.comboBox_2.setStyleSheet(_fromUtf8("background-color: rgb(192, 192, 255);"))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 100, 1021, 571))
        self.groupBox_2.setStyleSheet(_fromUtf8("color: rgb(204, 255, 102);"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.textEdit_2 = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit_2.setGeometry(QtCore.QRect(6, 20, 1009, 511))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet(_fromUtf8("background-color: rgb(248, 255, 238);\n"
"color: rgb(7, 7, 7);"))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(920, 540, 83, 20))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 46, 10);\n"
"color: rgb(255, 255, 255);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(830, 540, 83, 20))
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color: rgb(0, 128, 128);\n"
"color: rgb(255, 255, 255);"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 540, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(7, 675, 641, 16))
        self.label.setStyleSheet(_fromUtf8("color: rgb(102, 204, 51);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 90, 431, 16))
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 204);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(584, 90, 91, 17))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 220, 168);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "qqTop -  Dictionary Interface", None))
        self.pushButton.setText(_translate("Dialog", "Go", None))
        self.pushButton_4.setText(_translate("Dialog", "Clear", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Dictionaries", None))
        self.label_2.setText(_translate("Dialog", "Language Pairs  for Glosbe", None))
        self.pushButton_6.setText(_translate("Dialog", "Help", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", "eng/id", None))
        self.comboBox_2.setItemText(1, _translate("Dialog", "eng/jpn", None))
        self.comboBox_2.setItemText(2, _translate("Dialog", "eng/de", None))
        self.comboBox_2.setItemText(3, _translate("Dialog", "eng/fr", None))
        self.comboBox_2.setItemText(4, _translate("Dialog", "eng/zh", None))
        self.comboBox_2.setItemText(5, _translate("Dialog", "eng/rus", None))
        self.comboBox_2.setItemText(6, _translate("Dialog", "id/eng", None))
        self.comboBox_2.setItemText(7, _translate("Dialog", "id/jpn", None))
        self.comboBox_2.setItemText(8, _translate("Dialog", "id/de", None))
        self.comboBox_2.setItemText(9, _translate("Dialog", "jpn/id", None))
        self.comboBox_2.setItemText(10, _translate("Dialog", "jpn/eng", None))
        self.comboBox_2.setItemText(11, _translate("Dialog", "de/eng", None))
        self.comboBox_2.setItemText(12, _translate("Dialog", "de/jpn", None))
        self.comboBox_2.setItemText(13, _translate("Dialog", "zh/de", None))
        self.comboBox_2.setItemText(14, _translate("Dialog", "zh/eng", None))
        self.comboBox_2.setItemText(15, _translate("Dialog", "zh/id", None))
        self.comboBox_2.setItemText(16, _translate("Dialog", "zh/jpn", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Results", None))
        self.pushButton_3.setText(_translate("Dialog", "Quit", None))
        self.pushButton_5.setText(_translate("Dialog", "About", None))
        self.label_4.setText(_translate("Dialog", "TextLabel", None))
        self.label.setText(_translate("Dialog", "TextLabel", None))
        self.label_3.setText(_translate("Dialog", "TextLabel", None))
        self.pushButton_2.setText(_translate("Dialog", "Clear Results", None))
