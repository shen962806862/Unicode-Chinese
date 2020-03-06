from PyQt5 import QtWidgets
from srs import Ui_Transform

ver = "version:1.1.0"
author = "made by 沈子涵"

class mywindow(QtWidgets.QWidget, Ui_Transform):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        #初始化按钮
        self.UtoC.clicked.connect(self.processUtoC)
        self.CtoU.clicked.connect(self.processCtoU)
        self.clr.clicked.connect(self.clearText)
        #显示软件信息
        self.ver.setText(ver)
        self.author.setText(author)
        self.rst.setText("Welcome!!")
        #设置滚动条始终处于最下面
        scroll = self.textLast.verticalScrollBar()
        scroll.setValue(scroll.maximum())

    def clearText(self):
        try:
            self.textLast.setPlainText("")
            failTxt = r'清除成功。'
            self.rst.setText(failTxt)
        except:
            failTxt = r'清除失败。'
            self.rst.setText(failTxt)

    def processUtoC(self):
        try:
            str = self.textIn.toPlainText()
            txt = bytes(str, 'utf-8')
            res = txt.decode("unicode_escape")
            self.textOut.setPlainText(res)
            successTxt = r'转换成功。'
            self.rst.setText(successTxt)
            self.textLast.appendPlainText("{}\n=> {}".format(str,res))
        except:
            failTxt = r'转换失败。'
            self.rst.setText(failTxt)

    def processCtoU(self):
        try:
            txt = self.textIn.toPlainText()
            res = txt.encode("unicode_escape")
            byt = str(res, 'utf-8')
            self.textOut.setPlainText(byt)
            successTxt = r'转换成功。'
            self.rst.setText(successTxt)
            self.textLast.appendPlainText("{}\n=> {}".format(txt,byt))
        except:
            failTxt = r'转换失败。'
            self.rst.setText(failTxt)

if __name__== "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
