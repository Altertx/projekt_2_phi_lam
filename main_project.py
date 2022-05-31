from __future__ import unicode_literals # obsluga polskich znakÃ³w diaktrtycznych
from PyQt5.QtGui import *
import sys
from math import *
import time
from PyQt5.QtWidgets import QDialog, QApplication
from project import * # import kodu pythona ze schematem GUI

class MyForm(QDialog): # wiec QDialog to klasa parent,, nadrzedna
    def __init__(self): # self- czyli dla calej klasy
        super().__init__()
        self.ui = Ui_Dialog() # ui = bierzemy wszystkie dane z pliku UI do PY project.py z klasy Ui_Program()
        self.ui.setupUi(self) # ustawiamy nasz user interface dla owego pliku main
        self.ui.image.setScaledContents(True)
        obraz = (r'C:\Users\BRONX\OneDrive\Obrazy\philam.jpg')
        pixmap = QPixmap(obraz)
        self.ui.image.setPixmap(pixmap)
        self.ui.image.repaint()
        self.setWindowIcon(QtGui.QIcon(r'C:\Users\BRONX\OneDrive\Obrazy\philam.jpg')) # gdy uzyjemy r to convertujemy ze string na raw string
        self.setWindowTitle('PhiLam App')
        self.setStyleSheet("""
                           
                        QDialog {
                             background-color: #A2CC31;  
                            
                        }
                     
                           """)
        self.ui.radioButton_1992.toggled.connect(lambda:self.button_1992_state(self.ui.radioButton_1992))
        self.ui.radioButton_2000.toggled.connect(lambda:self.button_2000_state(self.ui.radioButton_2000))
        self.ui.radioButton_H_yes.toggled.connect(lambda:self.button_H_state(self.ui.radioButton_H_yes))
        
        self.ui.radioButton_H_no.clicked.connect(lambda:self.H_no_choice(self.ui.radioButton_WGS84,self.ui.radioButton_GRS80,
                                                                            self.ui.radioButton_1992,self.ui.radioButton_5,self.ui.radioButton_6,self.ui.radioButton_7,self.ui.radioButton_8,
                                                                            self.ui.lineEdit_F,self.ui.lineEdit_L,self.ui.radioButton_H_no,self.ui.radioButton_H_yes,self.ui.lineEdit_H))
        self.ui.lineEdit_H.textChanged.connect(lambda:self.H_line_choice(self.ui.radioButton_WGS84,self.ui.radioButton_GRS80,
                                                                            self.ui.radioButton_1992,self.ui.radioButton_5,self.ui.radioButton_6,self.ui.radioButton_7,self.ui.radioButton_8,
                                                                            self.ui.lineEdit_F,self.ui.lineEdit_L,self.ui.radioButton_H_no,self.ui.radioButton_H_yes,self.ui.lineEdit_H))
        self.ui.pushButton.clicked.connect(lambda:self.pushButton_choice(self.ui.radioButton_WGS84,self.ui.radioButton_GRS80,
                                                                            self.ui.radioButton_1992,self.ui.radioButton_5,self.ui.radioButton_6,self.ui.radioButton_7,self.ui.radioButton_8,
                                                                            self.ui.lineEdit_F,self.ui.lineEdit_L,self.ui.radioButton_H_no,self.ui.radioButton_H_yes,self.ui.lineEdit_H,
                                                                            self.ui.wynikXY,self.ui.wynikXYZ,self.ui.radioButton_2000))
        
        self.show()
  
    def button_2000_state(self, b):
        """
        

        Parameters
        ----------
        b : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if b.isChecked():
            self.ui.groupBox_3.setEnabled(True)
        else:
            self.ui.groupBox_3.setEnabled(False)
            
    def button_1992_state(self, b):
        """
        

        Parameters
        ----------
        b : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if b.isChecked():
            self.ui.groupBox_3.setEnabled(False)
        else:
            self.ui.groupBox_3.setEnabled(True)
            
    def button_H_state(self, b):
        """
        

        Parameters
        ----------
        b : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if b.isChecked():
            self.ui.label_5.setEnabled(True)
            self.ui.lineEdit_H.setEnabled(True)
        else:
            self.ui.label_5.setEnabled(False)
            self.ui.lineEdit_H.setEnabled(False)
            
    def H_no_choice(self,wgs,grs,b92,b5,b6,b7,b8,editF,editL,H_no,H_yes,editH):
        """
        

        Parameters
        ----------
        wgs : TYPE
            DESCRIPTION.
        grs : TYPE
            DESCRIPTION.
        b92 : TYPE
            DESCRIPTION.
        b5 : TYPE
            DESCRIPTION.
        b6 : TYPE
            DESCRIPTION.
        b7 : TYPE
            DESCRIPTION.
        b8 : TYPE
            DESCRIPTION.
        editF : TYPE
            DESCRIPTION.
        editL : TYPE
            DESCRIPTION.
        H_no : TYPE
            DESCRIPTION.
        H_yes : TYPE
            DESCRIPTION.
        editH : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if ((wgs.isChecked() or grs.isChecked())and(b92.isChecked() or b5.isChecked() or b6.isChecked() or b7.isChecked() or b8.isChecked())
            and(len(editF.text())!=0 and len(editL.text())!=0 and H_no.isChecked())):
            self.ui.pushButton.setEnabled(True)
                 # or (len(editF.text())!=0 and len(editL.text())!=0 and H_yes.isChecked() and len(editH.text())!=0)):
             
    def H_line_choice(self,wgs,grs,b92,b5,b6,b7,b8,editF,editL,H_no,H_yes,editH):
        """
        

        Parameters
        ----------
        wgs : TYPE
            DESCRIPTION.
        grs : TYPE
            DESCRIPTION.
        b92 : TYPE
            DESCRIPTION.
        b5 : TYPE
            DESCRIPTION.
        b6 : TYPE
            DESCRIPTION.
        b7 : TYPE
            DESCRIPTION.
        b8 : TYPE
            DESCRIPTION.
        editF : TYPE
            DESCRIPTION.
        editL : TYPE
            DESCRIPTION.
        H_no : TYPE
            DESCRIPTION.
        H_yes : TYPE
            DESCRIPTION.
        editH : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if ((wgs.isChecked() or grs.isChecked())and(b92.isChecked() or b5.isChecked() or b6.isChecked() or b7.isChecked() or b8.isChecked())
            and(len(editF.text())!=0 and len(editL.text())!=0 and H_yes.isChecked() and len(editH.text())!=0)):
            self.ui.pushButton.setEnabled(True)
    
    def Np(self,phi):
        """
        

        Parameters
        ----------
        phi : TYPE
            DESCRIPTION.

        Returns
        -------
        N : TYPE
            DESCRIPTION.

        """
        N = self.a/sqrt(1-self.e2*sin(phi)**2)
        return N
    
    def sigma(self,phi):
        """
        

        Parameters
        ----------
        phi : TYPE
            DESCRIPTION.

        Returns
        -------
        si : TYPE
            DESCRIPTION.

        """
        A0 = 1-(self.e2/4)-((3*(self.e2**2))/64)-((5*(self.e2**3))/256);
        A2 = (3/8)*(self.e2+(self.e2**2/4)+((15*(self.e2**3))/128));
        A4 = (15/256)*((self.e2**2)+((3*(self.e2**3))/4));
        A6 = (35*(self.e2**3))/3072;
        si= self.a*(A0*phi-A2*sin(2*phi)+A4*sin(4*phi)-A6*sin(6*phi));
        return si
    
    def pl2xy_gk(self,phi,l,L0):
        """
        

        Parameters
        ----------
        phi : TYPE
            DESCRIPTION.
        l : TYPE
            DESCRIPTION.
        L0 : TYPE
            DESCRIPTION.

        Returns
        -------
        xgk : TYPE
            DESCRIPTION.
        ygk : TYPE
            DESCRIPTION.

        """
        phi=phi*pi/180
        l=l*pi/180
        b2 = (self.a**2)*(1-self.e2);
        epr2 = ((self.a**2)-(b2))/(b2);
        t = tan(phi);
        n2 = epr2*((cos(phi))**2);
            
        N = self.Np(phi)
        si = self.sigma(phi)
        dl = l - L0
            
        xgk = si+ ((dl**2)/2)*N*sin(phi)*cos(phi)*(1+((dl**2)/12)*((cos(phi))**2)*(5-t**2+9*n2+4*(n2**2))+((dl**4)/360)*((cos(phi))**4)*(61-58*(t**2)+t**4+270*n2-330*n2*(t**2)))
        ygk = dl*N*cos(phi)*(1+((dl**2)/6)*((cos(phi))**2)*(1-t**2+n2)+((dl**4)/120)*((cos(phi))**4)*(5-18*(t**2)+t**4+14*n2-58*n2*(t**2)))
            
        return xgk,ygk
    
    def u1992(self,xgk,ygk):
        """
        

        Parameters
        ----------
        xgk : TYPE
            DESCRIPTION.
        ygk : TYPE
            DESCRIPTION.

        Returns
        -------
        x : TYPE
            DESCRIPTION.
        y : TYPE
            DESCRIPTION.

        """
        x = xgk * 0.9993 - 5300000
        y = ygk * 0.9993 + 500000
        return x,y
    
    def u2000(self,xgk,ygk,L0):
        """
        

        Parameters
        ----------
        xgk : TYPE
            DESCRIPTION.
        ygk : TYPE
            DESCRIPTION.
        L0 : TYPE
            DESCRIPTION.

        Returns
        -------
        x : TYPE
            DESCRIPTION.
        y : TYPE
            DESCRIPTION.

        """
        x = xgk * 0.999923
        y = ygk * 0.999923 + (L0*180/pi/3) * 1000000 + 500000
        return x,y
    
    def plh2xyz(self,P,L,H):
        """
        

        Parameters
        ----------
        P : TYPE
            DESCRIPTION.
        L : TYPE
            DESCRIPTION.
        H : TYPE
            DESCRIPTION.

        Returns
        -------
        X : TYPE
            DESCRIPTION.
        Y : TYPE
            DESCRIPTION.
        Z : TYPE
            DESCRIPTION.

        """
         P = P*pi/180
         L = L*pi/180
         N = self.Np(P)
         X = (N+H)*cos(P)*cos(L)
         Y = (N+H)*cos(P)*sin(L)
         Z = (N*(1 -self.e2 )+H)*sin(P)
         return X,Y,Z
    # glowna ostatnia funkcja
    def isFloat(self,string):
        """
        

        Parameters
        ----------
        string : TYPE
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
    
        try:
            float(string)
            return True
        except:
            return False
            
    def pushButton_choice(self,wgs,grs,b92,b5,b6,b7,b8,editF,editL,H_no,H_yes,editH,wynikXY,wynikXYZ,b00):
        """
        

        Parameters
        ----------
        wgs : TYPE
            DESCRIPTION.
        grs : TYPE
            DESCRIPTION.
        b92 : TYPE
            DESCRIPTION.
        b5 : TYPE
            DESCRIPTION.
        b6 : TYPE
            DESCRIPTION.
        b7 : TYPE
            DESCRIPTION.
        b8 : TYPE
            DESCRIPTION.
        editF : TYPE
            DESCRIPTION.
        editL : TYPE
            DESCRIPTION.
        H_no : TYPE
            DESCRIPTION.
        H_yes : TYPE
            DESCRIPTION.
        editH : TYPE
            DESCRIPTION.
        wynikXY : TYPE
            DESCRIPTION.
        wynikXYZ : TYPE
            DESCRIPTION.
        b00 : TYPE
            DESCRIPTION.

        Raises
        ------
        TypeError
            DESCRIPTION.
        ValueError
            DESCRIPTION.
        SystemError
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if grs.isChecked():
            self.a = 6378137 
            self.e2 = 0.00669438002290
        elif wgs.isChecked():
            self.a = 6378137
            self.b = 6356752.31424518
            self.flat = (self.a - self.b) / self.a 
            self.e2 = (2 * self.flat - self.flat ** 2)
        
        if len(editF.text()) == 0 and len(editL.text()) == 0:
            wynikXY.setText(f'Nie wprowadzono obu współrzędnych')
            raise TypeError(f'Nie wprowadzono obu współrzędnych')    
        
        if len(editF.text())!= 0:
            if self.isFloat(editF.text()):
                if float(editF.text()) >= 49 and float(editF.text()) <= 54 + 50/60:
                    self.F_deg = float(editF.text())
                else:
                    wynikXY.setText(f'Wybrano punkt nieznajdujący się w Polsce')
                    raise ValueError(f'Wybrano punkt nieznajdujący się w Polsce')
            else:
                wynikXY.setText(f'Wprowadzono ciąg znaków zamiast fi')
                raise TypeError('Wprowadzono ciąg znaków zamiast fi')   
        else:
            wynikXY.setText(f'Nie wprowadzono współrzędnej fi')
            raise TypeError('Nie wprowadzono współrzędnej fi')
            
        if len(editL.text())!= 0:
            if self.isFloat(editL.text()):
                if float(editL.text()) >= 14 + 7/60 and float(editL.text()) <= 24 + 9/60:
                    self.L_deg = float(editL.text())
                else:
                    wynikXY.setText(f'Wybrano punkt nieznajdujący się w Polsce')
                    raise ValueError(f'Wybrano punkt nieznajdujący się w Polsce')
            else:
                wynikXY.setText(f'Wprowadzono ciąg znaków zamiast lambda')
                raise TypeError(f'Wprowadzono ciąg znaków zamiast lambda')
        else:
            wynikXY.setText(f'Nie wprowadzono wpółrzędnej lambda')
            raise TypeError('Nie wprowadzono współrzędnej lambda')
        
        if b92.isChecked():
            self.L0 = 19*pi/180
        elif b5.isChecked():
            self.L0 = 15*pi/180
        elif b6.isChecked():
            self.L0 = 18*pi/180
        elif b7.isChecked():
            self.L0 = 21*pi/180
        elif b8.isChecked():
            self.L0 = 24*pi/180
        elif b92.isChecked(False) and self.ui.radioButton_2000.isChecked(False):
            wynikXY.setText(f'Nie wybrano układu dla współrzędnych wynikowych')
            raise SystemError(f'Nie wybrano układu dla współrzędnych wynikowych')
            
            
        if H_yes.isChecked():
            self.ui.label_7.setEnabled(False)
            self.ui.label_9.setEnabled(True)
            if len(editH.text())!= 0:
                if self.isFloat(editH.text()):
                    self.H = float(editH.text())
                    self.X_or, self.Y_or, self.Z_or = self.plh2xyz(self.F_deg, self.L_deg, self.H)
                    wynikXYZ.setText(f'X: {self.X_or:.3f}, Y: {self.Y_or:.3f}, Z: {self.Z_or:.3f}')
                    wynikXY.setText(f'')
                else:
                    wynikXYZ.setText('Wprowadzono ciąg znaków zamiast H')
                    raise TypeError('Wprowadzono ciąg znaków zamiast H')
            else:
                wynikXYZ.setText(f'Nie wprowadzono wysokosci elipsoidalnej')
                raise TypeError('Nie wprowadzono wysokosci elipsoidalnej')
        elif H_no.isChecked():
            self.ui.label_7.setEnabled(True)
            self.ui.label_9.setEnabled(False)
            self.X_gk, self.Y_gk = self.pl2xy_gk(self.F_deg, self.L_deg, self.L0)
            if b92.isChecked():
                self.X, self.Y = self.u1992(self.X_gk, self.Y_gk)
                wynikXY.setText(f'X 1992: {self.X:.3f}, Y 1992: {self.Y:.3f}')
                wynikXYZ.setText(f'')
            if b00.isChecked():
                self.X, self.Y = self.u2000(self.X_gk, self.Y_gk, self.L0)
                wynikXY.setText(f'X 2000: {self.X:.3f}, Y 2000: {self.Y:.3f}')
                wynikXYZ.setText(f'')
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
    
