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
from PyQt5 import QtCore
import opticspy

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
 
        self.qlevalue_list = []
        for i in range(40):
            self.qlevalue_list.append(QLineEdit())

        names = ['Z1', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6', 'Z7', 'Z8', 'Z9', 'Z10',
                'Z11', 'Z12', 'Z13', 'Z14', 'Z15', 'Z16', 'Z17', 'Z18', 'Z19', 'Z20',
                'Z21', 'Z22', 'Z23', 'Z24', 'Z25', 'Z26', 'Z27', 'Z28', 'Z29', 'Z30',
                'Z31', 'Z32', 'Z33', 'Z34', 'Z35', 'Z36', 'Z37', ' R', 'z', ' ']
        positions = [(i,j) for i in range(4) for j in range(20)]
        n = 0
        m = 0
        
        for position in positions:
            if position[1]%2 == 1:
                self.qlevalue_list[n].setMaximumWidth(40)
                if names[n] == ' R':
                    self.qlevalue_list[n].setText('1')
                elif names[n] == 'z':
                    self.qlevalue_list[n].setText('0.1')
                else:
                    self.qlevalue_list[n].setText('0')
                grid.addWidget(self.qlevalue_list[n], *position)
                n = n + 1
            else:
                if names[m] == ' ':
                    break
                lbl_z = QLabel(names[m])
                lbl_z.setMaximumWidth(30)
                grid.addWidget(lbl_z, *position)
                m = m + 1

#-------------------------------------------------------------------------------  
#Several Buttons
#Zernikesurface, Zernikemap, ZernikeMTF, ZernikePSF, Twyman Green Interferogram
#------------------------------------------------------------------------------- 
        surfacebutton = QPushButton("Plot 3D", self)
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

        self.pixmap1 = QPixmap("surface.png")
        self.pixmap1 = self.pixmap1.scaled(524,396)
        self.lbl_pixmap1 = QLabel(self)
        self.lbl_pixmap1.setPixmap(self.pixmap1)
        self.lbl_pixmap1.setStyleSheet('border: 2px solid black; border-radius: 5px;') 

        self.pixmap2 = QPixmap("psf.png")
        self.pixmap2 = self.pixmap2.scaled(524,396)
        self.lbl_pixmap2 = QLabel(self)
        self.lbl_pixmap2.setPixmap(self.pixmap2)
        self.lbl_pixmap2.setStyleSheet('border: 2px solid black; border-radius: 5px;') 

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.lbl_pixmap1)
        hbox3.addWidget(self.lbl_pixmap2)
#-------------------------------------------------------------------------------
# Author and link at the bottom
#-------------------------------------------------------------------------------
        lbl_bottom1 = QLabel('Author: Xing Fan')
        lbl_bottom1.setStyleSheet("QLabel { font-size: 15px }")

        lbl_bottom2 = QLabel('This app based on python optical module:')
        lbl_bottom2.setStyleSheet("QLabel { font-size: 15px }")

        lbl_bottom3 = QLabel()
        lbl_bottom3.setText('''<a href='https://github.com/Sterncat/opticspy'>opticspy</a>''')
        lbl_bottom3.setOpenExternalLinks(True)
        lbl_bottom3.setStyleSheet("QLabel { font-size: 15px }")

        lbl_bottom4 = QLabel()
        lbl_bottom4.setText('''<a href='https://github.com/Sterncat/zernikeapp'>How to use and reference</a>''')
        lbl_bottom4.setOpenExternalLinks(True)
        lbl_bottom4.setStyleSheet("QLabel { font-size: 15px }")

        hbox4 = QHBoxLayout()
        hbox4.addWidget(lbl_bottom1)
        hbox4.addStretch(1)
        hbox4.addWidget(lbl_bottom2)
        hbox4.addWidget(lbl_bottom3)
        hbox4.addStretch(1)
        hbox4.addWidget(lbl_bottom4)

#-------------------------------------------------------------------------------
# Set all horizontal box to vertical box 
#-------------------------------------------------------------------------------
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(grid)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)
        self.setLayout(vbox)  
        self.move(150, 50)
        self.setWindowTitle('Zernike Polynomials')
        self.show()

#-------------------------------------------------------------------------------
# Button action
#-------------------------------------------------------------------------------  
        surfacebutton.clicked.connect(self.plotsurface)
        mapbutton.clicked.connect(self.plotmap)
        mtfbutton.clicked.connect(self.plotmtf)
        psfbutton.clicked.connect(self.plotpsf)
        tgbutton.clicked.connect(self.plottg)


    @QtCore.pyqtSlot()
    def getzernikevalue(self):

        zvalue = []
        for i in range(37):        
            tmp = self.qlevalue_list[i].text()
            zvalue.append(float(tmp))
        r = float(self.qlevalue_list[37].text())
        z = float(self.qlevalue_list[38].text())
        return [zvalue,r,z]

    @QtCore.pyqtSlot()
    def plotsurface(self):
        [zvalue,r,z] =self.getzernikevalue()
        picname = "surface.png"
        Z = opticspy.zernike.Coefficient(zvalue)
        fig = Z.zernikesurface(savefig = True)
        fig.savefig(picname, dpi=60, bbox_inches='tight')
        newsurface = QPixmap(picname)
        newsurface = newsurface.scaled(524,396)
        self.lbl_pixmap1.setPixmap(newsurface)


    @QtCore.pyqtSlot()
    def plotmap(self):
        [zvalue,r,z] =self.getzernikevalue()
        picname = "map.png"
        Z = opticspy.zernike.Coefficient(zvalue)
        fig = Z.zernikemap(savefig = True)
        fig.savefig(picname, dpi=60, bbox_inches='tight')
        newmap = QPixmap(picname)
        newmap = newmap.scaled(524,396)
        self.lbl_pixmap1.setPixmap(newmap)

    @QtCore.pyqtSlot()
    def plotmtf(self):
        [zvalue,r,z] =self.getzernikevalue()
        picname = "mtf.png"
        Z = opticspy.zernike.Coefficient(zvalue)
        fig = Z.mtf(r=r, z=z)
        fig.savefig(picname, dpi=60, bbox_inches='tight')
        newmap = QPixmap(picname)
        newmap = newmap.scaled(524,396)
        self.lbl_pixmap2.setPixmap(newmap)


    @QtCore.pyqtSlot()
    def plotpsf(self):
        [zvalue,r,z] =self.getzernikevalue()
        picname = "psf.png"
        Z = opticspy.zernike.Coefficient(zvalue)
        fig = Z.psf(r=r, z=z)
        fig.savefig(picname, dpi=60, bbox_inches='tight')
        newmap = QPixmap(picname)
        newmap = newmap.scaled(524,396)
        self.lbl_pixmap2.setPixmap(newmap)

    @QtCore.pyqtSlot()
    def plottg(self):
        [zvalue,r,z] =self.getzernikevalue()
        picname = "interferogram.png"
        Z = opticspy.zernike.Coefficient(zvalue)
        fig = Z.twyman_green()
        fig.savefig(picname, dpi=60, bbox_inches='tight')
        newmap = QPixmap(picname)
        newmap = newmap.scaled(524,396)
        self.lbl_pixmap2.setPixmap(newmap)

        	
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




