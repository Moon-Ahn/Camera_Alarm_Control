#-*- encoding: utf-8 -*-
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QButtonGroup, QMessageBox
from PyQt5.QtCore import Qt
import requests
import os
import webbrowser
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from threading import  Thread
import threading

# if len(sys.argv) != 4:
#     print("Insufficient Argument")
#     sys.exit()

# ID = sys.argv[1]
# PAS = sys.argv[2]
# SeN = sys.argv[3]

ID = 'root'
PAS = 'root'
SeN = 'Load'
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        ############## LINE ###############

        NM = ['NM0', 'NM1', 'NM2', 'NM3', 'NM4', 'NM5', 'NM6', 'NM7', 'NM8', 'NM9', 'NM10', 'NM11', 'NM12', 'NM13',
              'NM14','NM15']
        LE = ['LE0','LE1','LE2','LE3','LE4','LE5','LE6','LE7','LE8','LE9','LE10','LE11','LE12','LE13','LE14','LE15']
        ON = ['ON0','ON1', 'ON2', 'ON3', 'ON4', 'ON5', 'ON6', 'ON7', 'ON8', 'ON9', 'ON10', 'ON11', 'ON12', 'ON13',
              'ON14','ON15']
        OFF = ['OFF0','OFF1', 'OFF2', 'OFF3', 'OFF4', 'OFF5', 'OFF6', 'OFF7', 'OFF8', 'OFF9', 'OFF10', 'OFF11', 'OFF12',
               'OFF13', 'OFF14','OFF15']
        AW = ['AW0','AW1', 'AW2', 'AW3', 'AW4', 'AW5', 'AW6', 'AW7', 'AW8', 'AW9', 'AW10', 'AW11', 'AW12',
               'AW13', 'AW14', 'AW15']
        GP = ['GP0','GP1', 'GP2', 'GP3', 'GP4', 'GP5', 'GP6', 'GP7', 'GP8', 'GP9', 'GP10', 'GP11', 'GP12',
              'GP13', 'GP14', 'GP15']

        ##############NAME Text Load###############
        NAME_Read = []
        try:
            self.Read_file(NAME_Read, 'NAME')
        except:
            pass
        ###############################################
        ##############IP Text Load###############
        IP_Read=[]
        try: self.Read_file(IP_Read,'IP')
        except: pass
        ###############################################

        myFont = QtGui.QFont("consolas",14)
        myFont.setBold(True)
        Explain1 = QLabel('Name   Ip Address', self)
        Explain1.setFont(myFont)
        Explain1.move(40,20)

        Explain2 = QLabel('Alarm ON/OFF', self)
        Explain2.setFont(myFont)
        Explain2.move(222, 20)

        Button_Font = QtGui.QFont("Arial", 10)
        Button_Font.setBold(True)


        for i in range (0,16) :

            try: NM[i] = QLineEdit(NAME_Read[i], self)
            except: NM[i] = QLineEdit('', self)
            NM[i].setAlignment(Qt.AlignCenter)
            NM[i].resize(80, 20)
            NM[i].move(20, 65 + 25 * i)
            try : LE[i] = QLineEdit(IP_Read[i], self)
            except : LE[i] = QLineEdit('', self)
            LE[i].setAlignment(Qt.AlignCenter)
            LE[i].resize(100, 20)
            LE[i].move(110, 65+25*i)

            ON[i] = QPushButton('ON', self)
            ON[i].resize(55, 21)
            ON[i].move(220, 64+25*i)
            ON[i].setCheckable(True)
            ON[i].toggle()
            ON[i].setFont(Button_Font)

            OFF[i] = QPushButton('OFF', self)
            OFF[i].resize(55, 21)
            OFF[i].move(285, 64+25*i)
            OFF[i].setCheckable(True)
            OFF[i].setFont(Button_Font)

            AW[i] = QPushButton('Access Website', self)
            AW[i].resize(120, 21)
            AW[i].move(350, 64+25*i)
            AW[i].setFont(Button_Font)

            GP[i] = QButtonGroup(self)
            GP[i].addButton(ON[i])
            GP[i].addButton(OFF[i])
            # try: ON[i].clicked.connect(self.Alarm_command_on(LE[i].text()))
            # except: print('y')
            # try: OFF[i].clicked.connect(self.Alarm_command_off(LE[i].text()))
            # except: print('t')

        Save = QPushButton('SAVE',self)
        Save.resize(450, 42)
        Save.move(20,475)
        Save.setFont(myFont)
        Save.setStyleSheet('background-color: rgb(196,221,253)')
        Save.clicked.connect(lambda: self.Save_text(NM,LE))

        ALL_ON = QPushButton('ALL ON', self)
        ALL_ON.resize(100, 20)
        ALL_ON.move(360, 8)
        ALL_ON.setFont(myFont)
        ALL_ON.setStyleSheet('background-color: rgb(193,211,253)')
        ALL_ON.clicked.connect(lambda: self.ALL_on(ON, LE))

        ALL_OFF = QPushButton('ALL OFF', self)
        ALL_OFF.resize(100, 20)
        ALL_OFF.move(360, 32)
        ALL_OFF.setFont(myFont)
        ALL_OFF.setStyleSheet('background-color: rgb(253,193,211)')
        ALL_OFF.clicked.connect(lambda: self.ALL_off(OFF,LE))

        ########################    ON CONTROL    #################################

        ON[0].clicked.connect(lambda: self.Alarm_command_on(LE[0].text()))
        ON[1].clicked.connect(lambda: self.Alarm_command_on(LE[1].text()))
        ON[2].clicked.connect(lambda: self.Alarm_command_on(LE[2].text()))
        ON[3].clicked.connect(lambda: self.Alarm_command_on(LE[3].text()))
        ON[4].clicked.connect(lambda: self.Alarm_command_on(LE[4].text()))
        ON[5].clicked.connect(lambda: self.Alarm_command_on(LE[5].text()))
        ON[6].clicked.connect(lambda: self.Alarm_command_on(LE[6].text()))
        ON[7].clicked.connect(lambda: self.Alarm_command_on(LE[7].text()))
        ON[8].clicked.connect(lambda: self.Alarm_command_on(LE[8].text()))
        ON[9].clicked.connect(lambda: self.Alarm_command_on(LE[9].text()))
        ON[10].clicked.connect(lambda: self.Alarm_command_on(LE[10].text()))
        ON[11].clicked.connect(lambda: self.Alarm_command_on(LE[11].text()))
        ON[12].clicked.connect(lambda: self.Alarm_command_on(LE[12].text()))
        ON[13].clicked.connect(lambda: self.Alarm_command_on(LE[13].text()))
        ON[14].clicked.connect(lambda: self.Alarm_command_on(LE[14].text()))
        ON[15].clicked.connect(lambda: self.Alarm_command_on(LE[15].text()))

        ############################################################################
        ########################    OFF CONTROL    #################################

        OFF[0].clicked.connect(lambda: self.Alarm_command_off(LE[0].text()))
        OFF[1].clicked.connect(lambda: self.Alarm_command_off(LE[1].text()))
        OFF[2].clicked.connect(lambda: self.Alarm_command_off(LE[2].text()))
        OFF[3].clicked.connect(lambda: self.Alarm_command_off(LE[3].text()))
        OFF[4].clicked.connect(lambda: self.Alarm_command_off(LE[4].text()))
        OFF[5].clicked.connect(lambda: self.Alarm_command_off(LE[5].text()))
        OFF[6].clicked.connect(lambda: self.Alarm_command_off(LE[6].text()))
        OFF[7].clicked.connect(lambda: self.Alarm_command_off(LE[7].text()))
        OFF[8].clicked.connect(lambda: self.Alarm_command_off(LE[8].text()))
        OFF[9].clicked.connect(lambda: self.Alarm_command_off(LE[9].text()))
        OFF[10].clicked.connect(lambda: self.Alarm_command_off(LE[10].text()))
        OFF[11].clicked.connect(lambda: self.Alarm_command_off(LE[11].text()))
        OFF[12].clicked.connect(lambda: self.Alarm_command_off(LE[12].text()))
        OFF[13].clicked.connect(lambda: self.Alarm_command_off(LE[13].text()))
        OFF[14].clicked.connect(lambda: self.Alarm_command_off(LE[14].text()))
        OFF[15].clicked.connect(lambda: self.Alarm_command_off(LE[15].text()))

        ############################################################################
        ########################    ACC CONTROL    #################################

        AW[0].clicked.connect(lambda: self.Access_IP(LE[0].text()))
        AW[1].clicked.connect(lambda: self.Access_IP(LE[1].text()))
        AW[2].clicked.connect(lambda: self.Access_IP(LE[2].text()))
        AW[3].clicked.connect(lambda: self.Access_IP(LE[3].text()))
        AW[4].clicked.connect(lambda: self.Access_IP(LE[4].text()))
        AW[5].clicked.connect(lambda: self.Access_IP(LE[5].text()))
        AW[6].clicked.connect(lambda: self.Access_IP(LE[6].text()))
        AW[7].clicked.connect(lambda: self.Access_IP(LE[7].text()))
        AW[8].clicked.connect(lambda: self.Access_IP(LE[8].text()))
        AW[9].clicked.connect(lambda: self.Access_IP(LE[9].text()))
        AW[10].clicked.connect(lambda: self.Access_IP(LE[10].text()))
        AW[11].clicked.connect(lambda: self.Access_IP(LE[11].text()))
        AW[12].clicked.connect(lambda: self.Access_IP(LE[12].text()))
        AW[13].clicked.connect(lambda: self.Access_IP(LE[13].text()))
        AW[14].clicked.connect(lambda: self.Access_IP(LE[14].text()))
        AW[15].clicked.connect(lambda: self.Access_IP(LE[15].text()))

        ############################################################################

        self.setWindowTitle(SeN+' Alarm Control')
        self.resize(500, 530)
        self.show()

    def Alarm_command_on(self, IP):
        # on
        if IP == '':
            pass
        else:
            try : requests.get('http://'+ IP +'/cgi-bin/admin/fwvamispecific.cgi?AlarmDisable=0&FwCgiVer=0x0001',
                         auth=HTTPDigestAuth(ID, PAS), timeout=3)
            except:
                msg = QMessageBox()
                msg.setText(IP + '_Wrong IP')
                msg.exec_()

    def Alarm_command_off(self, IP):
        # off

        self.thread = Thread(target=self.Thread_OFF_FUNCTION(IP))
        self.thread.start()

    def Thread_OFF_FUNCTION(self,IP):
        if IP == '':
            pass
        else :
            try :requests.get('http://'+ IP +'/cgi-bin/admin/fwvamispecific.cgi?AlarmDisable=1&FwCgiVer=0x0001',
                         auth=HTTPDigestAuth(ID, PAS), timeout=3)
            except :
                msg = QMessageBox()
                msg.setText(IP + '_Wrong IP')
                msg.exec_()

    def Access_IP(self, IP_Add):
        # access
        ie = webbrowser.get('c:\\program files\\internet explorer\\iexplore.exe')

        try: ie.open(IP_Add+'/admin/video_analytics2.asp')#os.system('explorer http:'+IP_Add)
        except:
            msg = QMessageBox()
            msg.setText(IP_Add + '_Wrong IP')
            msg.exec_()

    def Save_text(self,NAME,IP):
        f = open(SeN+"_NAME_Save.txt", 'w')
        for i in range(0, 15):
            data = NAME[i].text()
            f.write(data + '\n')
        f.close()

        f = open(SeN+"_IP_Save.txt", 'w')
        for i in range(0,15) :
            data = IP[i].text()
            f.write(data+'\n')
        f.close()
    def ALL_on(self, ON, Text):
        for i in range(0, 16):
            ON[i].toggle()
            self.Alarm_command_on(Text[i].text())

    def ALL_off(self, OFF, Text):
        for i in range(0, 16):
            OFF[i].toggle()
            self.Alarm_command_off(Text[i].text())

    def Read_file(self,FILE,Case):
        if Case == 'NAME' :
            f = open(SeN+"_NAME_Save.txt", 'r')
            lines = f.readlines()
            for line in lines:
                line = line.replace('\n', '')
                FILE.append(line)
            #print(FILE)
            f.close()
        elif Case == 'IP' :
            f = open(SeN+"_IP_Save.txt", 'r')
            lines = f.readlines()
            for line in lines:
                line = line.replace('\n', '')
                FILE.append(line)
            #print(FILE)
            f.close()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())