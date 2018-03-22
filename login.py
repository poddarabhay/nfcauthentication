# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import NFCAuth

class Ui_Form(object):
    
    def createTag(self):
        uname=self.lineEdit.text()
        passw=self.lineEdit_2.text()
        obj=NFCAuth.NFCAuth(0)
        conf=obj.write(username=uname,password=passw)
        if conf==0:
            self.showSuccessBox("Tag created: ",obj.get())
            #print("Tag created: ",obj.get())
        elif conf==-1:
            self.showMessageBox('Error in file op')
            #print("Error in file op")
        elif conf==-2:
            self.showMessageBox('Error in Database Operation')
            #print("Error in Database Operation")
    
    def showMessageBox(self,message):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(message)
        error_dialog.exec_()
        
    def showSuccessBox(self,title,message):
        msg=QtWidgets.QMessageBox()
        msg.setText(str(message))
        msg.setWindowTitle(title)
        #error_dialog = QtWidgets.QErrorMessage()
        #error_dialog.showMessage(str(message))
        msg.exec_()
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(454, 349)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 50, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 260, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.createTag)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 130, 161, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 190, 161, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "WELCOME"))
        self.label_2.setText(_translate("Form", "Username"))
        self.label_3.setText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Create tag"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

