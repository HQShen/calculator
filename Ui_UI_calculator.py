# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\Desktop\calculator\.eric6project\UI_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(783, 435)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Calculator.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.lcd = QtWidgets.QLCDNumber(Dialog)
        self.lcd.setGeometry(QtCore.QRect(40, 20, 401, 121))
        self.lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd.setDigitCount(12)
        self.lcd.setObjectName("lcd")
        self.square = QtWidgets.QPushButton(Dialog)
        self.square.setGeometry(QtCore.QRect(40, 160, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        font.setItalic(True)
        self.square.setFont(font)
        self.square.setAutoDefault(False)
        self.square.setObjectName("square")
        self.sqrt = QtWidgets.QPushButton(Dialog)
        self.sqrt.setGeometry(QtCore.QRect(40, 220, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.sqrt.setFont(font)
        self.sqrt.setAutoDefault(False)
        self.sqrt.setObjectName("sqrt")
        self.exp = QtWidgets.QPushButton(Dialog)
        self.exp.setGeometry(QtCore.QRect(40, 280, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.exp.setFont(font)
        self.exp.setAutoDefault(False)
        self.exp.setObjectName("exp")
        self.equal = QtWidgets.QPushButton(Dialog)
        self.equal.setGeometry(QtCore.QRect(390, 280, 50, 111))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.equal.setFont(font)
        self.equal.setAutoDefault(False)
        self.equal.setObjectName("equal")
        self.b7 = QtWidgets.QPushButton(Dialog)
        self.b7.setGeometry(QtCore.QRect(110, 160, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.b7.setFont(font)
        self.b7.setAutoDefault(False)
        self.b7.setObjectName("b7")
        self.b8 = QtWidgets.QPushButton(Dialog)
        self.b8.setGeometry(QtCore.QRect(180, 160, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.b8.setFont(font)
        self.b8.setAutoDefault(False)
        self.b8.setObjectName("b8")
        self.b9 = QtWidgets.QPushButton(Dialog)
        self.b9.setGeometry(QtCore.QRect(250, 160, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.b9.setFont(font)
        self.b9.setAutoDefault(False)
        self.b9.setObjectName("b9")
        self.devide = QtWidgets.QPushButton(Dialog)
        self.devide.setGeometry(QtCore.QRect(320, 160, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.devide.setFont(font)
        self.devide.setAutoDefault(False)
        self.devide.setObjectName("devide")
        self.b4 = QtWidgets.QPushButton(Dialog)
        self.b4.setGeometry(QtCore.QRect(110, 220, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.b4.setFont(font)
        self.b4.setAutoDefault(False)
        self.b4.setObjectName("b4")
        self.b5 = QtWidgets.QPushButton(Dialog)
        self.b5.setGeometry(QtCore.QRect(180, 220, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.b5.setFont(font)
        self.b5.setAutoDefault(False)
        self.b5.setObjectName("b5")
        self.b6 = QtWidgets.QPushButton(Dialog)
        self.b6.setGeometry(QtCore.QRect(250, 220, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.b6.setFont(font)
        self.b6.setAutoDefault(False)
        self.b6.setObjectName("b6")
        self.multiply = QtWidgets.QPushButton(Dialog)
        self.multiply.setGeometry(QtCore.QRect(320, 220, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.multiply.setFont(font)
        self.multiply.setAutoDefault(False)
        self.multiply.setObjectName("multiply")
        self.b1 = QtWidgets.QPushButton(Dialog)
        self.b1.setGeometry(QtCore.QRect(110, 280, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.b1.setFont(font)
        self.b1.setAutoDefault(False)
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(Dialog)
        self.b2.setGeometry(QtCore.QRect(180, 280, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.b2.setFont(font)
        self.b2.setAutoDefault(False)
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(Dialog)
        self.b3.setGeometry(QtCore.QRect(250, 280, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.b3.setFont(font)
        self.b3.setAutoDefault(False)
        self.b3.setObjectName("b3")
        self.minus = QtWidgets.QPushButton(Dialog)
        self.minus.setGeometry(QtCore.QRect(320, 280, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.minus.setFont(font)
        self.minus.setAutoDefault(False)
        self.minus.setObjectName("minus")
        self.mc = QtWidgets.QPushButton(Dialog)
        self.mc.setGeometry(QtCore.QRect(390, 160, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.mc.setFont(font)
        self.mc.setAutoDefault(False)
        self.mc.setObjectName("mc")
        self.b0 = QtWidgets.QPushButton(Dialog)
        self.b0.setGeometry(QtCore.QRect(180, 340, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.b0.setFont(font)
        self.b0.setAutoDefault(False)
        self.b0.setObjectName("b0")
        self.point = QtWidgets.QPushButton(Dialog)
        self.point.setGeometry(QtCore.QRect(250, 340, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.point.setFont(font)
        self.point.setAutoDefault(False)
        self.point.setObjectName("point")
        self.plus = QtWidgets.QPushButton(Dialog)
        self.plus.setGeometry(QtCore.QRect(320, 340, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.plus.setFont(font)
        self.plus.setAutoDefault(False)
        self.plus.setObjectName("plus")
        self.reverse = QtWidgets.QPushButton(Dialog)
        self.reverse.setGeometry(QtCore.QRect(110, 340, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.reverse.setFont(font)
        self.reverse.setAutoDefault(False)
        self.reverse.setObjectName("reverse")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(390, 220, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setAutoDefault(False)
        self.back.setObjectName("back")
        self.ln = QtWidgets.QPushButton(Dialog)
        self.ln.setGeometry(QtCore.QRect(40, 340, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.ln.setFont(font)
        self.ln.setAutoDefault(False)
        self.ln.setObjectName("ln")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(470, 21, 271, 371))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Panel)
        self.textBrowser.setObjectName("textBrowser")
        self.trash = QtWidgets.QPushButton(Dialog)
        self.trash.setGeometry(QtCore.QRect(702, 352, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        self.trash.setFont(font)
        self.trash.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d18.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trash.setIcon(icon1)
        self.trash.setAutoDefault(False)
        self.trash.setObjectName("trash")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        Dialog.setWhatsThis(_translate("Dialog", "Calculator"))
        self.square.setText(_translate("Dialog", "x²"))
        self.sqrt.setText(_translate("Dialog", "√"))
        self.exp.setText(_translate("Dialog", "exp"))
        self.equal.setText(_translate("Dialog", "="))
        self.equal.setShortcut(_translate("Dialog", "Return"))
        self.b7.setText(_translate("Dialog", "7"))
        self.b7.setShortcut(_translate("Dialog", "7"))
        self.b8.setText(_translate("Dialog", "8"))
        self.b8.setShortcut(_translate("Dialog", "8"))
        self.b9.setText(_translate("Dialog", "9"))
        self.b9.setShortcut(_translate("Dialog", "9"))
        self.devide.setText(_translate("Dialog", "÷"))
        self.devide.setShortcut(_translate("Dialog", "/"))
        self.b4.setText(_translate("Dialog", "4"))
        self.b4.setShortcut(_translate("Dialog", "4"))
        self.b5.setText(_translate("Dialog", "5"))
        self.b5.setShortcut(_translate("Dialog", "5"))
        self.b6.setText(_translate("Dialog", "6"))
        self.b6.setShortcut(_translate("Dialog", "6"))
        self.multiply.setText(_translate("Dialog", "×"))
        self.multiply.setShortcut(_translate("Dialog", "*"))
        self.b1.setText(_translate("Dialog", "1"))
        self.b1.setShortcut(_translate("Dialog", "1"))
        self.b2.setText(_translate("Dialog", "2"))
        self.b2.setShortcut(_translate("Dialog", "2"))
        self.b3.setText(_translate("Dialog", "3"))
        self.b3.setShortcut(_translate("Dialog", "3"))
        self.minus.setText(_translate("Dialog", "-"))
        self.minus.setShortcut(_translate("Dialog", "-"))
        self.mc.setText(_translate("Dialog", "C"))
        self.b0.setText(_translate("Dialog", "0"))
        self.b0.setShortcut(_translate("Dialog", "0"))
        self.point.setText(_translate("Dialog", "."))
        self.point.setShortcut(_translate("Dialog", "."))
        self.plus.setText(_translate("Dialog", "+"))
        self.plus.setShortcut(_translate("Dialog", "+"))
        self.reverse.setText(_translate("Dialog", "±"))
        self.reverse.setShortcut(_translate("Dialog", "Return"))
        self.back.setText(_translate("Dialog", "←"))
        self.back.setShortcut(_translate("Dialog", "Return"))
        self.ln.setText(_translate("Dialog", "ln"))
        self.ln.setShortcut(_translate("Dialog", "Return"))
        self.trash.setWhatsThis(_translate("Dialog", "Delete"))
        self.trash.setShortcut(_translate("Dialog", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
