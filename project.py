# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(750, 820)
        self.image = QtWidgets.QLabel(Dialog)
        self.image.setGeometry(QtCore.QRect(10, 170, 310, 131))
        self.image.setObjectName("image")
        self.image.setFrameShape(1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 310, 111))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setStyleSheet("font-weight: bold")
        self.radioButton_WGS84 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_WGS84.setGeometry(QtCore.QRect(50, 40, 95, 20))
        self.radioButton_WGS84.setAutoRepeat(False)
        self.radioButton_WGS84.setObjectName("radioButton_WGS84")
        self.radioButton_GRS80 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_GRS80.setGeometry(QtCore.QRect(50, 70, 95, 20))
        self.radioButton_GRS80.setObjectName("radioButton_GRS80")
        self.lineEdit_F = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_F.setGeometry(QtCore.QRect(10, 400, 141, 41))
        self.lineEdit_F.setObjectName("lineEdit_F")
        self.lineEdit_F.setStyleSheet("font-weight: bold")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 320, 320, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("font-weight: bold")
        self.lineEdit_L = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_L.setGeometry(QtCore.QRect(160, 400, 141, 41))
        self.lineEdit_L.setObjectName("lineEdit_L")
        self.lineEdit_L.setStyleSheet("font-weight: bold")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 360, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font-weight: bold")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(220, 360, 55, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("font-weight: bold")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 40, 246, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setStyleSheet("font-weight: bold")
        self.radioButton_1992 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_1992.setGeometry(QtCore.QRect(10, 40, 121, 20))
        self.radioButton_1992.setObjectName("radioButton_1992")
        self.radioButton_2000 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2000.setGeometry(QtCore.QRect(10, 70, 131, 20))
        self.radioButton_2000.setObjectName("radioButton_2000")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 90, 161, 141))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setStyleSheet("font-weight: bold")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 10, 95, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 40, 95, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 70, 95, 20))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_8.setGeometry(QtCore.QRect(10, 100, 95, 20))
        self.radioButton_8.setObjectName("radioButton_8")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(340, 320, 246, 123))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setStyleSheet("font-weight: bold")
        self.radioButton_H_yes = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_H_yes.setGeometry(QtCore.QRect(10, 30, 191, 20))
        self.radioButton_H_yes.setObjectName("radioButton_H_yes")
        self.radioButton_H_no = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_H_no.setGeometry(QtCore.QRect(10, 70, 241, 20))
        self.radioButton_H_no.setObjectName("radioButton_H_no")
        self.lineEdit_H = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_H.setEnabled(False)
        self.lineEdit_H.setGeometry(QtCore.QRect(590, 400, 141, 41))
        self.lineEdit_H.setObjectName("lineEdit_H")
        self.lineEdit_H.setStyleSheet("font-weight: bold")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(595, 360, 161, 41))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("font-weight: bold")
        self.wynikXY = QtWidgets.QLabel(Dialog)
        self.wynikXY.setGeometry(QtCore.QRect(130, 550, 471, 91))
        self.wynikXY.setText("")
        self.wynikXY.setObjectName("wynikXY")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wynikXY.setFont(font)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(260, 500, 191, 41))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("font-weight: bold")
        self.wynikXYZ = QtWidgets.QLabel(Dialog)
        self.wynikXYZ.setGeometry(QtCore.QRect(110, 690, 531, 81))
        self.wynikXYZ.setText("")
        self.wynikXYZ.setObjectName("wynikXYZ")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wynikXYZ.setFont(font)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setEnabled(False)
        self.label_9.setGeometry(QtCore.QRect(230, 640, 261, 31))
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("font-weight: bold")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(280, 455, 126, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("font-weight: bold")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "1. Elipsoida"))
        self.radioButton_WGS84.setText(_translate("Dialog", "WGS 84"))
        self.radioButton_GRS80.setText(_translate("Dialog", "GRS 80"))
        self.label.setText(_translate("Dialog", "2. Wprowadz współrzędne w stopniach dziesietnych"))
        self.label_3.setText(_translate("Dialog", "φ [°]"))
        self.label_4.setText(_translate("Dialog", "λ [°]"))
        self.groupBox_2.setTitle(_translate("Dialog", "3. Współrzędne X,Y wynikowe"))
        self.radioButton_1992.setText(_translate("Dialog", "Układ PL-1992"))
        self.radioButton_2000.setText(_translate("Dialog", "Układ PL-2000"))
        self.radioButton_5.setText(_translate("Dialog", "strefa 5"))
        self.radioButton_6.setText(_translate("Dialog", "strefa 6"))
        self.radioButton_7.setText(_translate("Dialog", "strefa 7"))
        self.radioButton_8.setText(_translate("Dialog", "strefa 8"))
        self.groupBox_4.setTitle(_translate("Dialog", "4. Wybierz by obliczyć"))
        self.radioButton_H_yes.setText(_translate("Dialog", "chcę podać H elipsoidalną"))
        self.radioButton_H_no.setText(_translate("Dialog", "nie chcę podawać H elipsoidalnej"))
        self.label_5.setText(_translate("Dialog", "Podaj wartość H [m]"))
        self.label_7.setText(_translate("Dialog", "Wybrane współrzędne X,Y"))
        self.label_9.setText(_translate("Dialog", "Współrzędne ortokartezjańskie X,Y,Z"))
        self.pushButton.setText(_translate("Dialog", "Oblicz"))
       

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

