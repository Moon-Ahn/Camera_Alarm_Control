import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QFileDialog)
import subprocess
import os

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Enter Alarm Control')
        self.resize(400, 100)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> User Name </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your user name')
        layout.addWidget(label_name, 1, 0)
        layout.addWidget(self.lineEdit_username, 1, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 2, 0)
        layout.addWidget(self.lineEdit_password, 2, 1)

        label_servername = QLabel('<font size="4"> Server Name </font>')
        self.lineEdit_servername = QLineEdit()
        self.lineEdit_servername.setPlaceholderText('Please enter your server name')
        layout.addWidget(label_servername, 3, 0)
        layout.addWidget(self.lineEdit_servername, 3, 1)

        button_login = QPushButton('불러오기')
        button_login.clicked.connect(self.Load_Data)
        layout.addWidget(button_login, 4, 0, 1, 2)
        layout.setRowMinimumHeight(4, 40)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 5, 0, 1, 2)
        layout.setRowMinimumHeight(4, 20)

        self.setLayout(layout)
    def Load_Data(self):

        File_Data=[]
        Data = QFileDialog.getOpenFileName(self, 'Open File', './Load')
        #print(Data[0][-3:])
        if Data[0][-3:] == 'txt':
            msg = QMessageBox()
            msg.setText('Success')
            msg.exec_()
            f = open(Data[0], 'r')
            lines = f.readlines()
            for line in lines:
                line = line.replace('\n', '')
                File_Data.append(line)
            self.lineEdit_username.setText(File_Data[0])
            self.lineEdit_password.setText(File_Data[1])
            self.lineEdit_servername.setText(File_Data[2])
        else :
            msg = QMessageBox()
            msg.setText('Fail, Please open txtFile')
            msg.exec_()

        #app.quit()
        # execute_python = "Alarm_control.exe " + self.lineEdit_username.text() + " " + self.lineEdit_password.text() + " " + self.lineEdit_servername.text()
        # subprocess.Popen(execute_python, shell = True)

    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == '':
            msg.setText('Please enter Username')
            msg.exec_()
        elif self.lineEdit_password.text() == '' :
            msg.setText('Please enter Password')
            msg.exec_()
        elif self.lineEdit_servername.text() == '' :
            msg.setText('Please enter Servername')
            msg.exec_()
        else :
            msg.setText('Login')
            msg.exec_()
            app.quit()

            path = "./Load"
            if not os.path.isdir(path):
                os.mkdir(path)
            f = open("./Load/"+self.lineEdit_servername.text() + "로드파일.txt", 'w')
            f.write(self.lineEdit_username.text() + '\n')
            f.write(self.lineEdit_password.text() + '\n')
            f.write(self.lineEdit_servername.text())
            f.close()

            execute_python = "Alarm_control.exe " + self.lineEdit_username.text() + " " + self.lineEdit_password.text() + " " + self.lineEdit_servername.text()
            subprocess.Popen(execute_python, shell = True)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = LoginForm()
    form.show()

    sys.exit(app.exec_())