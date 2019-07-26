# -*- coding: utf-8 -*-

"""
Module implementing dlg_calculator.
"""
from PyQt5.QtWidgets import QDialog, QMessageBox

from Ui_UI_calculator import Ui_Dialog
from PyQt5 import QtCore,  QtGui,  QtWidgets
import sys
import calculate as cal

class dlg_calculator(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    lcdstring = ''
    operation = ''
    tb = ''
    current_num = 0
    previous_num = 0
    result = 0
    
    check2op = False
    error = False
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(dlg_calculator, self).__init__(parent)
        self.setupUi(self)
        self.action()
        
        self.TB = self.textBrowser
        self.cursor = self.TB.textCursor()

        
    def action(self):
        # press number buttons
        self.b0.clicked.connect(self.buttonClicked)
        self.b1.clicked.connect(self.buttonClicked)
        self.b2.clicked.connect(self.buttonClicked)
        self.b3.clicked.connect(self.buttonClicked)
        self.b4.clicked.connect(self.buttonClicked)
        self.b5.clicked.connect(self.buttonClicked)
        self.b6.clicked.connect(self.buttonClicked)
        self.b7.clicked.connect(self.buttonClicked)
        self.b8.clicked.connect(self.buttonClicked)
        self.b9.clicked.connect(self.buttonClicked)
        self.point.clicked.connect(self.buttonClicked)
        
        # press operation buttons
        self.devide.clicked.connect(self.opClicked)
        self.multiply.clicked.connect(self.opClicked)
        self.minus.clicked.connect(self.opClicked)
        self.plus.clicked.connect(self.opClicked)
        
        # press MC button
        self.mc.clicked.connect(self.mcClicked)
        
        # press special button
        self.square.clicked.connect(self.spClicked)
        self.sqrt.clicked.connect(self.spClicked)
        self.exp.clicked.connect(self.spClicked)
        self.ln.clicked.connect(self.spClicked)
        self.reverse.clicked.connect(self.spClicked)
        
        # press back button
        self.back.clicked.connect(self.baClicked)
        
        # press equal button
        self.equal.clicked.connect(self.eqClicked)
        
        # press trash button
        self.trash.clicked.connect(self.trClicked)
        
    def buttonClicked(self):
        if len(self.lcdstring) < 11:
            self.lcdstring += self.sender().text()
            if self.lcdstring == '.':
                self.lcdstring = '0.'
            elif self.lcdstring.count('.')>1:
                self.lcdstring = self.lcdstring[:-1]
            elif self.lcdstring.count('.') == 1:
                self.lcd.display(self.lcdstring)
                self.current_num = float(self.lcdstring)
            else:
                self.lcd.display(self.lcdstring)
                self.current_num = int(self.lcdstring)
            self.check2op = False
            self.error = False

        else:
            pass
    
    def _get_op(self):    
        if self.operation == 'plus':
            return '+'
        if self.operation == 'minus':
            return '-'
        if self.operation == 'multiply':
            return '×'
        if self.operation == 'devide':
            return '÷'
    
    def opClicked(self):
        if self.error:
            pass
        elif self.check2op:
            self.operation = self.sender().objectName()
            self.tb = self.tb[:-1] + self._get_op()
            self.cursor.deletePreviousChar()
            self.TB.insertPlainText(self._get_op())
        else:
            self.operation = self.sender().objectName()
            if self.tb == '':
                self.TB.append(str(self.current_num)+self._get_op())
            else:
                self.TB.insertPlainText(str(self.current_num)+self._get_op())
            self.tb += str(self.current_num) + self._get_op()
            self.previous_num = self.current_num
            self.current_num = 0
            self.lcdstring = ''
            self.check2op = True
        
    def mcClicked(self):
        self.lcdstring = ''
        self.operation = ''
        self.current_num = 0
        self.previous_num = 0
        self.result = 0
        self.tb = ''
        self.TB.append(' ')
        self.lcd.display(0)
        self.check2op = False
        self.error = False
    
    def spClicked(self):
        if self.error:
            pass
        
        elif self.sender().objectName() == 'square':
            if self.check2op:
                self.current_num = cal.square(self.previous_num)
            else:
                self.current_num =cal.square(self.current_num)
            self.lcd.display(self.current_num)
        
        elif self.sender().objectName() == 'sqrt':
            if self.check2op:
                if self.previous_num >= 0:
                    self.current_num = cal.sqrt(self.previous_num)
                    self.lcd.display(self.current_num)
                else:
                    self.textBrowser.append(' ')
                    tem = 'sqrt(' + str(self.current_num) + ')'
                    self.TB.insertPlainText(tem)
                    self._Error()
            else:
                if self.current_num >= 0:
                    self.current_num = cal.sqrt(self.current_num)
                    self.lcd.display(self.current_num)
                else:
                    self.textBrowser.append(' ')
                    tem = 'sqrt(' + str(self.current_num) + ')'
                    self.TB.insertPlainText(tem)
                    self._Error()
        
        elif self.sender().objectName() == 'exp':
            if self.check2op:
                self.current_num = cal.exp(self.previous_num)
            else:
                self.current_num = cal.exp(self.current_num)
                
            self.lcd.display(self.current_num)
        
        elif self.sender().objectName() == 'ln':
            if self.check2op:
                if self.previous_num >= 0:
                    self.current_num = cal.ln(self.previous_num)
                    self.lcd.display(self.current_num)
                else:
                    self.TB.append(' ')
                    tem = 'ln(' + str(self.current_num) + ')'
                    self.TB.insertPlainText(tem)
                    self._Error()
            else:
                if self.current_num >= 0:
                    self.current_num = cal.ln(self.current_num)
                    self.lcd.display(self.current_num)
                else:
                    self.TB.append(' ')
                    tem = 'ln(' + str(self.current_num) + ')'
                    self.TB.insertPlainText(tem)
                    self._Error()
        
        elif self.sender().objectName() == 'reverse':
            if self.check2op:
                self.current_num = -self.previous_num
            else:
                self.current_num = -self.current_num
            self.lcd.display(self.current_num)
        
        self.check2op = False
        self.spe = True
        
    def baClicked(self):
        self.check2op = False
        self.error = False
        if len(self.lcdstring) > 1:
            self.lcdstring = self.lcdstring[:-1]
            self.lcd.display(self.lcdstring)
            self.current_num = float(self.lcdstring)
        else:
            self.lcdstring = ''
            self.lcd.display(0)
            self.current_num = 0
    
    def eqClicked(self):
        if self.error:
            pass
        elif self.tb == '':
            pass
        elif self.tb[-1] in ['+', '-', '*', '/'] and self.check2op:
            self.tb = self.tb[:-1]
            self._get_result()
        else:
            self.tb += str(self.current_num)
            self._get_result()
    
    def _get_result(self):
        try:
            self.result = cal.plumiu(self.tb)
        except ZeroDivisionError:
            self.TB.insertPlainText('0')
            self._Error()
        else:
            self.lcd.display(float(self.result))
            self.TB.insertPlainText(str(self.current_num) + '=' + str(self.result))
            self.TB.append(' ')
        
        self.current_num = self.result
        self.lcdstring = ''
        self.tb = ''
    
    def trClicked(self):
        self.textBrowser.clear()
    
    def _Error(self):
        self.error = True
        self.lcd.display('Error')
        self.result = 0
        self.previous_num = 0
        self.current_num = 0
        self.lcdstring = ''
        self.tb = ''
        self.TB.insertPlainText(' ' + str('Error'))
        self.TB.append('   ')
        
    def closeEvent(self,  event):
        reply = QMessageBox.question(self, 'exit','Are your sure to leave?', QMessageBox.Yes,  QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mycal = dlg_calculator()
    mycal.show()
    sys.exit(app.exec_())
