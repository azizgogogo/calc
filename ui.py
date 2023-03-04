import sys

from functools import partial
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(60,40)
        self.setStyleSheet( "QPushButton::hover { background-color : lightgreen;}")

    def Value(self):
        return self.text()

class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.h_boxs=list()
        self.v_box=QVBoxLayout()
        self.setLayout(self.v_box)
        self.btn=[
            ['C','(',')','/'],
            ['7','8','9','*'],
            ['4','5','6','-'],
            ['1','2','3','+'],
            ['←','0','.','=']
        ]

        self.btn1=[
            ['C','(',')','/'],
            ['7','8','9','*'],
            ['4','5','6','-'],
            ['1','2','3','+'],
            ['←','0','.','=']
        ]
        self.s_str=''

        for i in range(len(self.btn)):
            for j in range(len(self.btn[i])):
                self.btn[i][j]=Button(self.btn[i][j])
                
        for i in range(len(self.btn)):
            h=QHBoxLayout()
            for j in range(len(self.btn[i])):
                h.addWidget(self.btn[i][j])
            self.h_boxs.append(h)

        self.btn[4][0].setStyleSheet("QPushButton::hover"
                     "{"
                     "background-color : red;"
                     "}")

        self.line=QLineEdit()
        self.lab=QLabel()

        self.line.setFixedHeight(40)
        self.line.setStyleSheet('font-size: 25px; border : 2px solid black')

        self.v_box.addWidget(self.line)
        self.v_box.addWidget(self.lab)
        for i in self.h_boxs:
            self.v_box.addLayout(i)

        for i in range(len(self.btn)):
            for j in range(len(self.btn[i])):
                if self.btn1[i][j] == 'C':
                    self.btn[i][j].clicked.connect(self.cls)
                elif self.btn1[i][j] == '=':
                    self.btn[i][j].clicked.connect(self.solve)   
                elif self.btn1[i][j] == '←':
                    self.btn[i][j].clicked.connect(self.chap)
                else :
                    self.btn[i][j].clicked.connect(partial(self.add_str,self.btn1[i][j]))

        self.show()

    def add_str(self,st):
        self.s_str+= st
        self.line.setText(self.s_str)

    def cls (self):
        self.line.clear()
        self.lab.clear()
        self.s_str=''

    def chap(self):
        self.s_str=self.s_str[:-1]
        self.line.setText(self.s_str)
    
    def solve(self):
        try:
            n=eval(self.s_str)

        except ZeroDivisionError  as err :
            n=err

        except SyntaxError  as err :
            n='you entered an error'
        
        except TypeError  as err :
            n='you entered an error'
            
        self.lab.setText(str(n))


app=QApplication(sys.argv)
win=Calc()
win.setWindowTitle('calc.py')

sys.exit(app.exec_())

# vs code