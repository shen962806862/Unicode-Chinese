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
        Transform.resize(852, 651)
        self.gridLayout_3 = QtWidgets.QGridLayout(Transform)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(Transform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(491, 520))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.textIn = QtWidgets.QPlainTextEdit(self.widget)
        self.textIn.setMinimumSize(QtCore.QSize(470, 0))
        self.textIn.setObjectName("textIn")
        self.gridLayout.addWidget(self.textIn, 2, 0, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(470, 28))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.UtoC = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UtoC.sizePolicy().hasHeightForWidth())
        self.UtoC.setSizePolicy(sizePolicy)
        self.UtoC.setMinimumSize(QtCore.QSize(200, 0))
        self.UtoC.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(True)
        font.setWeight(75)
        self.UtoC.setFont(font)
        self.UtoC.setObjectName("UtoC")
        self.horizontalLayout.addWidget(self.UtoC)
        self.CtoU = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CtoU.sizePolicy().hasHeightForWidth())
        self.CtoU.setSizePolicy(sizePolicy)
        self.CtoU.setMinimumSize(QtCore.QSize(200, 0))
        self.CtoU.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(True)
        font.setWeight(75)
        self.CtoU.setFont(font)
        self.CtoU.setObjectName("CtoU")
        self.horizontalLayout.addWidget(self.CtoU)
        self.gridLayout.addWidget(self.widget_5, 3, 0, 1, 2)
        self.textOut = QtWidgets.QPlainTextEdit(self.widget)
        self.textOut.setMinimumSize(QtCore.QSize(470, 0))
        self.textOut.setObjectName("textOut")
        self.gridLayout.addWidget(self.textOut, 5, 0, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(470, 28))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label1 = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy)
        self.label1.setMinimumSize(QtCore.QSize(0, 0))
        self.label1.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.horizontalLayout_2.addWidget(self.label1)
        self.rst = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rst.sizePolicy().hasHeightForWidth())
        self.rst.setSizePolicy(sizePolicy)
        self.rst.setMinimumSize(QtCore.QSize(0, 0))
        self.rst.setMaximumSize(QtCore.QSize(320, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rst.setFont(font)
        self.rst.setText("")
        self.rst.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rst.setObjectName("rst")
        self.horizontalLayout_2.addWidget(self.rst)
        self.gridLayout.addWidget(self.widget_6, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(Transform)
        self.widget_2.setMinimumSize(QtCore.QSize(331, 520))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textLast = QtWidgets.QPlainTextEdit(self.widget_2)
        self.textLast.setMinimumSize(QtCore.QSize(0, 0))
        self.textLast.setObjectName("textLast")
        self.gridLayout_5.addWidget(self.textLast, 1, 0, 1, 1)
        self.clr = QtWidgets.QPushButton(self.widget_2)
        self.clr.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.clr.setFont(font)
        self.clr.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clr.setAutoFillBackground(True)
        self.clr.setObjectName("clr")
        self.gridLayout_5.addWidget(self.clr, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMinimumSize(QtCore.QSize(0, 37))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_2, 0, 1, 1, 2)
        self.widget_4 = QtWidgets.QWidget(Transform)
        self.widget_4.setMinimumSize(QtCore.QSize(661, 102))
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.pathIn = QtWidgets.QLineEdit(self.widget_4)
        self.pathIn.setMinimumSize(QtCore.QSize(348, 28))
        self.pathIn.setObjectName("pathIn")
        self.gridLayout_4.addWidget(self.pathIn, 0, 1, 1, 1)
        self.folderIn = QtWidgets.QPushButton(self.widget_4)
        self.folderIn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.folderIn.setFont(font)
        self.folderIn.setObjectName("folderIn")
        self.gridLayout_4.addWidget(self.folderIn, 0, 2, 1, 1)
        self.trans = QtWidgets.QPushButton(self.widget_4)
        self.trans.setMinimumSize(QtCore.QSize(66, 66))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.trans.setFont(font)
        self.trans.setMouseTracking(True)
        self.trans.setObjectName("trans")
        self.gridLayout_4.addWidget(self.trans, 0, 3, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.pathOut = QtWidgets.QLineEdit(self.widget_4)
        self.pathOut.setMinimumSize(QtCore.QSize(348, 28))
        self.pathOut.setObjectName("pathOut")
        self.gridLayout_4.addWidget(self.pathOut, 1, 1, 1, 1)
        self.folderOut = QtWidgets.QPushButton(self.widget_4)
        self.folderOut.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.folderOut.setFont(font)
        self.folderOut.setObjectName("folderOut")
        self.gridLayout_4.addWidget(self.folderOut, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.widget_4, 1, 0, 1, 2)
        self.widget_3 = QtWidgets.QWidget(Transform)
        self.widget_3.setMinimumSize(QtCore.QSize(161, 102))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ver = QtWidgets.QLabel(self.widget_3)
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
        self.gridLayout_2.addWidget(self.ver, 2, 0, 1, 1)
        self.author = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.author.setFont(font)
        self.author.setText("")
        self.author.setObjectName("author")
        self.gridLayout_2.addWidget(self.author, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_3, 1, 2, 1, 1)

        self.retranslateUi(Transform)
        QtCore.QMetaObject.connectSlotsByName(Transform)

    def retranslateUi(self, Transform):
        _translate = QtCore.QCoreApplication.translate
        Transform.setWindowTitle(_translate("Transform", "Dialog"))
        self.UtoC.setText(_translate("Transform", "Unicode转中文"))
        self.CtoU.setText(_translate("Transform", "中文转Unicode"))
        self.label1.setText(_translate("Transform", "填入Unicode或中文："))
        self.clr.setText(_translate("Transform", "清除记录"))
        self.label.setText(_translate("Transform", "历史记录："))
        self.label_2.setText(_translate("Transform", "输入文件路径："))
        self.folderIn.setText(_translate("Transform", "添加文件"))
        self.trans.setText(_translate("Transform", "转换"))
        self.label_3.setText(_translate("Transform", "输出路径："))
        self.folderOut.setText(_translate("Transform", "添加文件夹"))
