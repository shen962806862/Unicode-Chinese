# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'srs.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Transform(object):
    def setupUi(self, Transform):
        Transform.setObjectName("Transform")
        Transform.resize(861, 461)
        self.label1 = QtWidgets.QLabel(Transform)
        self.label1.setGeometry(QtCore.QRect(30, 10, 161, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.UtoC = QtWidgets.QPushButton(Transform)
        self.UtoC.setGeometry(QtCore.QRect(90, 230, 141, 31))
        self.UtoC.setObjectName("UtoC")
        self.CtoU = QtWidgets.QPushButton(Transform)
        self.CtoU.setGeometry(QtCore.QRect(360, 230, 141, 31))
        self.CtoU.setObjectName("CtoU")
        self.rst = QtWidgets.QLabel(Transform)
        self.rst.setGeometry(QtCore.QRect(450, 10, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rst.setFont(font)
        self.rst.setText("")
        self.rst.setObjectName("rst")
        self.label = QtWidgets.QLabel(Transform)
        self.label.setGeometry(QtCore.QRect(580, 10, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ver = QtWidgets.QLabel(Transform)
        self.ver.setGeometry(QtCore.QRect(710, 410, 141, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.ver.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ver.setFont(font)
        self.ver.setText("")
        self.ver.setObjectName("ver")
        self.author = QtWidgets.QLabel(Transform)
        self.author.setGeometry(QtCore.QRect(720, 430, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.author.setFont(font)
        self.author.setText("")
        self.author.setObjectName("author")
        self.textIn = QtWidgets.QPlainTextEdit(Transform)
        self.textIn.setGeometry(QtCore.QRect(20, 40, 541, 181))
        self.textIn.setObjectName("textIn")
        self.textOut = QtWidgets.QPlainTextEdit(Transform)
        self.textOut.setGeometry(QtCore.QRect(20, 270, 541, 181))
        self.textOut.setObjectName("textOut")
        self.textLast = QtWidgets.QPlainTextEdit(Transform)
        self.textLast.setGeometry(QtCore.QRect(580, 40, 261, 361))
        self.textLast.setObjectName("textLast")
        self.clr = QtWidgets.QPushButton(Transform)
        self.clr.setGeometry(QtCore.QRect(580, 410, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.clr.setFont(font)
        self.clr.setObjectName("clr")

        self.retranslateUi(Transform)
        QtCore.QMetaObject.connectSlotsByName(Transform)

    def retranslateUi(self, Transform):
        _translate = QtCore.QCoreApplication.translate
        Transform.setWindowTitle(_translate("Transform", "Dialog"))
        self.label1.setText(_translate("Transform", "填入Unicode或中文："))
        self.UtoC.setText(_translate("Transform", "Unicode转中文"))
        self.CtoU.setText(_translate("Transform", "中文转Unicode"))
        self.label.setText(_translate("Transform", "历史记录："))
        self.clr.setText(_translate("Transform", "清除记录"))