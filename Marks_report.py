from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(736, 491)
        Dialog.setWindowOpacity(1.0)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(630, 410, 81, 71))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Telugu = QtWidgets.QLabel(Dialog)
        self.Telugu.setGeometry(QtCore.QRect(80, 140, 55, 16))
        self.Telugu.setObjectName("Telugu")
        self.Hindi = QtWidgets.QLabel(Dialog)
        self.Hindi.setGeometry(QtCore.QRect(80, 180, 55, 21))
        self.Hindi.setObjectName("Hindi")
        self.English = QtWidgets.QLabel(Dialog)
        self.English.setGeometry(QtCore.QRect(80, 230, 55, 16))
        self.English.setObjectName("English")
        self.Result = QtWidgets.QLabel(Dialog)
        self.Result.setGeometry(QtCore.QRect(280, 450, 104, 31))
        self.Result.setObjectName("Result")
        self.Status = QtWidgets.QLabel(Dialog)
        self.Status.setGeometry(QtCore.QRect(280, 410, 93, 28))
        self.Status.setObjectName("Status")
        self.Total = QtWidgets.QLabel(Dialog)
        self.Total.setGeometry(QtCore.QRect(450, 170, 93, 28))
        self.Total.setObjectName("Total")
        self.Average = QtWidgets.QLabel(Dialog)
        self.Average.setGeometry(QtCore.QRect(450, 210, 93, 28))
        self.Average.setObjectName("Average")
        self.Percentage = QtWidgets.QLabel(Dialog)
        self.Percentage.setGeometry(QtCore.QRect(450, 250, 93, 28))
        self.Percentage.setObjectName("Average")
        self.Maths = QtWidgets.QLabel(Dialog)
        self.Maths.setGeometry(QtCore.QRect(80, 270, 81, 16))
        self.Maths.setObjectName("Maths")
        self.Science = QtWidgets.QLabel(Dialog)
        self.Science.setGeometry(QtCore.QRect(80, 310, 55, 16))
        self.Science.setObjectName("Science")
        self.Social = QtWidgets.QLabel(Dialog)
        self.Social.setGeometry(QtCore.QRect(80, 350, 55, 16))
        self.Social.setObjectName("Social")
        self.textEdit_Telugu = QtWidgets.QTextEdit(Dialog)
        self.textEdit_Telugu.setGeometry(QtCore.QRect(160, 130, 104, 31))
        self.textEdit_Telugu.setObjectName("textEdit_Telugu")
        self.textEdit_Hindi = QtWidgets.QTextEdit(Dialog)
        self.textEdit_Hindi.setGeometry(QtCore.QRect(160, 180, 104, 31))
        self.textEdit_Hindi.setObjectName("textEdit_Hindi")
        self.textEdit_Maths = QtWidgets.QTextEdit(Dialog)
        self.textEdit_Maths.setGeometry(QtCore.QRect(160, 260, 104, 31))
        self.textEdit_Maths.setObjectName("textEdit_Maths")
        self.textEdit_Science = QtWidgets.QTextEdit(Dialog)
        self.textEdit_Science.setGeometry(QtCore.QRect(160, 300, 104, 31))
        self.textEdit_Science.setObjectName("textEdit_Science")
        self.textEdit_Social = QtWidgets.QTextEdit(Dialog)
        self.textEdit_Social.setGeometry(QtCore.QRect(160, 340, 104, 31))
        self.textEdit_Social.setObjectName("textEdit_Social")
        self.textEdit_English = QtWidgets.QTextEdit(Dialog)
        self.textEdit_English.setGeometry(QtCore.QRect(160, 220, 104, 31))
        self.textEdit_English.setObjectName("textEdit_English")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(540, 170, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(540, 210, 104, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(540, 250, 104, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_Result = QtWidgets.QTextEdit(Dialog)
        self.textEdit_Result.setGeometry(QtCore.QRect(360, 450, 104, 31))
        self.textEdit_Result.setObjectName("textEdit_Result")
        self.textEdit__Status = QtWidgets.QTextEdit(Dialog)
        self.textEdit__Status.setGeometry(QtCore.QRect(360, 410, 141, 31))
        self.textEdit__Status.setObjectName("textEdit__Status")
        #####  Creating Calculate button  ######
        self.pushButton_Get_Result = QtWidgets.QPushButton(Dialog)
        self.pushButton_Get_Result.setGeometry(QtCore.QRect(450, 120, 93, 28))
        self.pushButton_Get_Result.setObjectName("pushButton_Get_Result")

        #####  Creating Reset button  ######
        self.pushButton_Reset = QtWidgets.QPushButton(Dialog)
        self.pushButton_Reset.setGeometry(QtCore.QRect(560, 120, 93, 28))
        self.pushButton_Reset.setObjectName("pushButton_Reset")


        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(250, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Student_name = QtWidgets.QLabel(Dialog)
        self.Student_name.setGeometry(QtCore.QRect(20, 50, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Student_name.setFont(font)
        self.Student_name.setObjectName("Student_name")
        self.lineEdit_student_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_student_name.setGeometry(QtCore.QRect(130, 50, 511, 22))
        self.lineEdit_student_name.setObjectName("lineEdit_student_name")
        self.Class = QtWidgets.QLabel(Dialog)
        self.Class.setGeometry(QtCore.QRect(80, 80, 61, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Class.setFont(font)
        self.Class.setObjectName("Class")
        self.comboBox_class = QtWidgets.QComboBox(Dialog)
        self.comboBox_class.setGeometry(QtCore.QRect(130, 80, 73, 22))
        self.comboBox_class.setEditable(True)
        self.comboBox_class.setObjectName("comboBox_class")
        self.comboBox_class.addItem("")
        self.comboBox_class.addItem("")
        self.comboBox_class.addItem("")
        self.comboBox_class.addItem("")
        self.comboBox_class.addItem("")
        self.comboBox_class.addItem("")
        self.comboBox_class.addItem("")
        self.comboBox_class.addItem("")
        self.comboBox_class.addItem("")
        self.comboBox_class.addItem("")

        ###### Creating Frame #########

        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(250, 390, 281, 98))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(530, 160, 131, 131))
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.Percent = 0

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_Get_Result.clicked.connect(self.Total_marks)
        self.pushButton_Get_Result.clicked.connect(self.Res)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Student Report"))
        self.Telugu.setText(_translate("Dialog", "Tekugu"))
        self.Hindi.setText(_translate("Dialog", "Hindi"))
        self.English.setText(_translate("Dialog", "English"))
        self.Maths.setText(_translate("Dialog", "Maths"))
        self.Science.setText(_translate("Dialog", "Science"))
        self.Social.setText(_translate("Dialog", "Social"))
        self.Result.setText(_translate("Dialog", "Result"))
        self.Total.setText(_translate("Dialog","Total"))
        self.Average.setText(_translate("Dialog","Average"))
        self.Percentage.setText(_translate("Dialog","Percentage"))
        self.Status.setText(_translate("Dialog","Status"))


        ###### Creating Label for Buttons #########

        self.pushButton_Get_Result.setText(_translate("Dialog", "Get_Result"))
        self.pushButton_Reset.setText(_translate("Dialog", "Reset"))

        #######      LABELS ##########

        self.label_4.setText(_translate("Dialog", "...Student Report..."))
        self.Student_name.setText(_translate("Dialog", "Student Name :"))
        self.Class.setText(_translate("Dialog", "Class :"))
        self.comboBox_class.setItemText(0, _translate("Dialog", "1"))
        self.comboBox_class.setItemText(1, _translate("Dialog", "2"))
        self.comboBox_class.setItemText(2, _translate("Dialog", "3"))
        self.comboBox_class.setItemText(3, _translate("Dialog", "4"))
        self.comboBox_class.setItemText(4, _translate("Dialog", "5"))
        self.comboBox_class.setItemText(5, _translate("Dialog", "6"))
        self.comboBox_class.setItemText(6, _translate("Dialog", "7"))
        self.comboBox_class.setItemText(7, _translate("Dialog", "8"))
        self.comboBox_class.setItemText(8, _translate("Dialog", "9"))
        self.comboBox_class.setItemText(9, _translate("Dialog", "10"))


    def Total_marks(self):
        totalsum = float(self.textEdit_Telugu.toPlainText()) + float(self.textEdit_Hindi.toPlainText()) + float(self.textEdit_English.toPlainText()) + float(self.textEdit_Maths.toPlainText()) + float(self.textEdit_Science.toPlainText()) + float(self.textEdit_Social.toPlainText())
        self.textEdit.setText(str("{:.2f}".format(totalsum)))
        Avg = (float(self.textEdit_Telugu.toPlainText()) + float(self.textEdit_Hindi.toPlainText()) + float(
            self.textEdit_English.toPlainText()) + float(self.textEdit_Maths.toPlainText()) + float(
            self.textEdit_Science.toPlainText()) + float(self.textEdit_Social.toPlainText())) / 6
        self.textEdit_2.setText(str("{:.2f}".format(Avg)))
        self.Percent = ((float(self.textEdit_Telugu.toPlainText()) + float(self.textEdit_Hindi.toPlainText()) + float(
            self.textEdit_English.toPlainText()) + float(self.textEdit_Maths.toPlainText()) + float(
            self.textEdit_Science.toPlainText()) + float(self.textEdit_Social.toPlainText())) / 600) * 100
        self.textEdit_3.setText(str("{:.1f} %".format(self.Percent)))
        if self.Percent > 90:
            self.textEdit__Status.setText("Distinction")
        elif self.Percent > 80:
            self.textEdit__Status.setText("First Class")
        elif self.Percent > 60:
            self.textEdit__Status.setText("Second Class")
        else:
            self.textEdit_Result.setText("Passed")
            self.textEdit__Status.setText(" ")




    def Res(self):
        if self.Percent > 40:
            self.textEdit_Result.setText("Passed")

        else:
            self.textEdit_Result.setText("Failed")
            self.textEdit__Status.setText(" ")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())