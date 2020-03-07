from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from srs import Ui_Transform
import os,re,json

ver = "version:2.0.0"
author = "made by 沈子涵"

class mywindow(QtWidgets.QWidget, Ui_Transform):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        #初始化按钮
        self.UtoC.clicked.connect(self.processUtoC)
        self.CtoU.clicked.connect(self.processCtoU)
        self.clr.clicked.connect(self.clearText)
        self.folderIn.clicked.connect(self.readF)
        self.folderOut.clicked.connect(self.writeF)
        self.trans.clicked.connect(self.transInfo)
        #显示软件信息
        self.setWindowTitle("json & txt 转换器")
        self.ver.setText(ver)
        self.author.setText(author)
        self.rst.setText("Welcome!!")
        #设置滚动条始终处于最下面
        scroll = self.textLast.verticalScrollBar()
        scroll.setValue(scroll.maximum())

    def transInfo(self):
        try:
            if self.info == "jtot":
                with open(self.pathin, 'r', encoding='utf-8') as j:
                    txt = json.load(j)
                with open(self.pathout+"/"+self.fname.replace('json', 'txt'), "w") as fp:
                    str = json.dumps(txt, indent=4, ensure_ascii=False)
                    fp.write(str)
                    self.textLast.setPlainText(str)
                self.rst.setText(r'转换成功。')
            elif self.info == "ttoj":
                self.TtoJ(self.pathin, self.pathout+"/"+self.fname.replace('txt', 'json'))
                self.rst.setText(r'转换成功。')
        except:
            self.rst.setText(r'转换失败。')

    def TtoJ(self, inpath, outpath):
        with open(inpath, "r", encoding='GBK') as fp:
            result = []
            item = {}
            for line in fp:
                if line.find('{') == 0:
                    continue
                elif line.find('}') == 0:
                    result.append(item)
                    continue
                else:
                    res = re.split(":", line.strip())
                    a = {
                        res[0]: res[1]
                    }
                    item.update(a)
        with open(outpath, 'w') as j:
            json.dump(result, j, indent=1)

    def readF(self):
        try:
            filename,filetype = QFileDialog.getOpenFileName(self, "选取文件", "C:/", "All Files(*);;Text Files(*.csv)")
            self.pathIn.setText(filename)
            self.pathin = filename
            self.fpath = os.path.split(filename)[0]
            self.fname = os.path.split(filename)[1]
            suffix = os.path.splitext(filename)[1]
            if suffix == ".json":
                self.info = "jtot"
                self.rst.setText(r'json转txt')
            elif suffix == ".txt":
                self.info = "ttoj"
                self.rst.setText(r'txt转json')
        except:
            self.rst.setText(r'打开失败。')

    def writeF(self):
        try:
            folder = QFileDialog.getExistingDirectory(self, "选取文件夹", self.fpath)
            self.pathOut.setText(folder)
            self.pathout = folder
        except:
            self.rst.setText(r'选取失败。')

    def clearText(self):
        try:
            self.textLast.setPlainText("")
            self.rst.setText(r'清除成功。')
        except:
            self.rst.setText(r'清除失败。')

    def processUtoC(self):
        try:
            str = self.textIn.toPlainText()
            txt = bytes(str, 'utf-8')
            res = txt.decode("unicode_escape")
            self.textOut.setPlainText(res)
            self.rst.setText(r'转换成功。')
            self.textLast.appendPlainText("{}\n=> {}".format(str,res))
        except:
            self.rst.setText(r'转换失败。')

    def processCtoU(self):
        try:
            txt = self.textIn.toPlainText()
            res = txt.encode("unicode_escape")
            byt = str(res, 'utf-8')
            self.textOut.setPlainText(byt)
            self.rst.setText(r'转换成功。')
            self.textLast.appendPlainText("{}\n=> {}".format(txt,byt))
        except:
            self.rst.setText(r'转换失败。')

if __name__== "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
