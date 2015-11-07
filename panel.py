# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a skeleton
of a calculator using a QGridLayout.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QLineEdit, QLabel, QHBoxLayout,
    QVBoxLayout, QPushButton, QApplication)
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):

#-------------------------------------------------------------------------------  
#Title
#------------------------------------------------------------------------------- 
        lbl1 = QLabel('Standard Zernike Polynomials', self)
        lbl1.setStyleSheet("QLabel { font-size: 20px }")
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(lbl1)
        hbox1.addStretch(1)

#-------------------------------------------------------------------------------  
#Zernike polonomials value
#-------------------------------------------------------------------------------    
        grid = QGridLayout()
 
        qlevalue_list = []
        for i in range(40):
            qlevalue_list.append(QLineEdit())

        names = ['Z1', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6', 'Z7', 'Z8', 'Z9', 'Z10',
                'Z11', 'Z12', 'Z13', 'Z14', 'Z15', 'Z16', 'Z17', 'Z18', 'Z19', 'Z20',
                'Z21', 'Z22', 'Z23', 'Z24', 'Z25', 'Z26', 'Z27', 'Z28', 'Z29', 'Z30',
                'Z31', 'Z32', 'Z33', 'Z34', 'Z35', 'Z36', 'Z37', ' R', ' ', ' ']
        positions = [(i,j) for i in range(4) for j in range(20)]
        n = 0
        m = 0
        
        for position in positions:
            print position
            if position[1]%2 == 1:
                qlevalue_list[n].setMaximumWidth(30)
                qlevalue_list[n].setText('0')
                grid.addWidget(qlevalue_list[n], *position)
                n = n + 1
                print n
            else:
                if names[m] == ' ':
                    break
                lbl_z = QLabel(names[m])
                lbl_z.setMaximumWidth(30)
                grid.addWidget(lbl_z, *position)
                m = m + 1
                print m

#-------------------------------------------------------------------------------  
#Several Buttons
#Zernikesurface, Zernikemap, ZernikeMTF, ZernikePSF, Twyman Green Interferogram
#------------------------------------------------------------------------------- 
        surfacebutton = QPushButton("Plot 3D")
        mapbutton = QPushButton("Plot 2D")
        mtfbutton = QPushButton("MTF")
        psfbutton = QPushButton("PSF")
        tgbutton = QPushButton("Interferogram")

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(surfacebutton)
        hbox2.addWidget(mapbutton)
        hbox2.addStretch(1)
        hbox2.addWidget(mtfbutton)
        hbox2.addWidget(psfbutton)
        hbox2.addWidget(tgbutton)
        hbox2.addStretch(1)
#-------------------------------------------------------------------------------  
#Two picture layout
#one for 3D and 2D plot, one for MTF, PSF, Interferogram
#------------------------------------------------------------------------------- 

        pixmap1 = QPixmap("Default1.png")
        lbl_pixmap1 = QLabel(self)
        lbl_pixmap1.setPixmap(pixmap1)

        pixmap2 = QPixmap("Default2.png")
        lbl_pixmap2 = QLabel(self)
        lbl_pixmap2.setPixmap(pixmap2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(lbl_pixmap1)
        hbox3.addWidget(lbl_pixmap2)

#------------------------------------------------------------------------------- 


        vbox = QVBoxLayout()
        
        vbox.addLayout(hbox1)
        vbox.addLayout(grid)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)
        self.setLayout(vbox)  

        self.move(150, 50)
        self.setWindowTitle('Zernike Polynomials')
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())