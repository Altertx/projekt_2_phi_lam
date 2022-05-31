# -*- coding: utf-8 -*-
from __future__ import unicode_literals # obsluga polskich znakÃ³w diaktrtycznych
from PyQt5.QtGui import *
import sys
from math import *
import time
from PyQt5.QtWidgets import QDialog, QApplication
from project import * # import kodu pythona ze schematem GUI

class MyForm(QDialog): # wiec QDialog to klasa parent,, nadrzedna
    def __init__(self):
        """
        Konstruktor klasy z parametrem self, którym można poslugiwac się dla zmiennej, funkcji
        w całej klasie. Konstruktor wywoływany jest przy każdym tworzeniu instancji, obiektu klasy.

        Returns
        -------
        None.
        """
        super().__init__()
        self.ui = Ui_Dialog() # ui = bierzemy wszystkie dane z pliku UI do PY project.py z klasy Ui_Program()
        self.ui.setupUi(self) # ustawiamy nasz user interface dla owego pliku main
        self.ui.image.setScaledContents(True)
        obraz = ('philam.jpg')
        pixmap = QPixmap(obraz)
        self.ui.image.setPixmap(pixmap)
        self.ui.image.repaint()
        self.setWindowIcon(QtGui.QIcon('philam.jpg')) # gdy uzyjemy r to convertujemy ze string na raw string
        self.setWindowTitle('PhiLam App')
        self.setStyleSheet("""
                           
                        QDialog {
                             background-color: #A2CC31;  
                            
                        }
                     
                           """)
        self.ui.radioButton_1992.toggled.connect(lambda:self.button_1992_state(self.ui.radioButton_1992))
        self.ui.radioButton_2000.toggled.connect(lambda:self.button_2000_state(self.ui.radioButton_2000))
        self.ui.radioButton_H_yes.toggled.connect(lambda:self.H_yes_choice(self.ui.radioButton_H_yes))
        
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
        Funkcja, która włącza widocznosc i umożliwia działanie groupBox_3. 

        Parameters
        ----------
        b : radioButton_2000 (QRadioButton)

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
        Funkcja, która wyłącza widocznosc i umożliwia działanie groupBox_3.

        Parameters
        ----------
        b : radioButton_1992 (QRadioButton)

        Returns
        -------
        None.

        """
        if b.isChecked():
            self.ui.groupBox_3.setEnabled(False)
        else:
            self.ui.groupBox_3.setEnabled(True)
            
    def H_yes_choice(self, b):
        """
        Funkcja, która włącza widocznosc i umożliwia działanie label_5 i lineEdit_H.

        Parameters
        ----------
        b : radioButton_H_yes (QRadioButton)
           
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
        Funkcja, która włącza widocznosc i umożliwia działanie pushButton.

        Parameters
        ----------
        wgs : radioButton_WGS84 (QRadioButton)
        grs : radioButton_GRS80 (QRadioButton)
        b92 : radioButton_1992 (QRadioButton)
        b5 : radioButton_5 (QRadioButton)
        b6 : radioButton_6 (QRadioButton)
        b7 : radioButton_7 (QRadioButton)
        b8 : radioButton_8 (QRadioButton)
        editF : lineEdit_F (QLineEdit) stopnie dziesietne
        editL : lineEdit_L (QLineEdit) stopnie dziesietne
        H_no : radioButton_H_no (QRadioButton)
        H_yes : radioButton_H_yes (QRadioButton)
        editH : lineEdit_H (QLineEdit) metry

        Returns
        -------
        None.

        """
        if ((wgs.isChecked() or grs.isChecked())and(b92.isChecked() or b5.isChecked() or b6.isChecked() or b7.isChecked() or b8.isChecked())
            and(len(editF.text())!=0 and len(editL.text())!=0 and H_no.isChecked())):
            self.ui.pushButton.setEnabled(True)
                 
             
    def H_line_choice(self,wgs,grs,b92,b5,b6,b7,b8,editF,editL,H_no,H_yes,editH):
        """
        Funkcja, która włącza widocznosc i umożliwia działanie pushButton.
        
        Parameters
        ----------
        wgs : radioButton_WGS84 (QRadioButton)
        grs : radioButton_GRS80 (QRadioButton)
        b92 : radioButton_1992 (QRadioButton)
        b5 : radioButton_5 (QRadioButton)
        b6 : radioButton_6 (QRadioButton)
        b7 : radioButton_7 (QRadioButton)
        b8 : radioButton_8 (QRadioButton)
        editF : lineEdit_F (QLineEdit) stopnie dziesietne
        editL : lineEdit_L (QLineEdit) stopnie dziesietne
        H_no : radioButton_H_no (QRadioButton)
        H_yes : radioButton_H_yes (QRadioButton)
        editH : lineEdit_H (QLineEdit) metry

        Returns
        -------
        None.

        """
        if ((wgs.isChecked() or grs.isChecked())and(b92.isChecked() or b5.isChecked() or b6.isChecked() or b7.isChecked() or b8.isChecked())
            and(len(editF.text())!=0 and len(editL.text())!=0 and H_yes.isChecked() and len(editH.text())!=0)):
            self.ui.pushButton.setEnabled(True)
    
    def Np(self,phi):
        """
        Max. promień w I wertykale w kierunku głownym.
        
        Parametres
        ----------
        phi : float - szerokosc geodezyjna [radians]
        
        Returns
        -------
        N : float - promien w I wertykale [m]
        """
        N = self.a/sqrt(1-self.e2*sin(phi)**2)
        return N
    
    def sigma(self,phi):
        """
        Wartosc sigmy.
        
        Paramtetres:
        -----------
        phi - float - szerokosc elipsoidalna [radians]
        
        Returns:
        --------
        si - float - sigma
        """
        A0 = 1-(self.e2/4)-((3*(self.e2**2))/64)-((5*(self.e2**3))/256);
        A2 = (3/8)*(self.e2+(self.e2**2/4)+((15*(self.e2**3))/128));
        A4 = (15/256)*((self.e2**2)+((3*(self.e2**3))/4));
        A6 = (35*(self.e2**3))/3072;
        si= self.a*(A0*phi-A2*sin(2*phi)+A4*sin(4*phi)-A6*sin(6*phi));
        return si
    
    def pl2xy_gk(self,phi,l,L0):
        """
        Transformacja wspolrzednych geodezyjnych na wspolrzedne w układzie Gaussa-Krugera
        Parametres:
        pji,l - float - szerokosc oraz dlugosc geodezyjna [stopnie dziesietne]
        L0 - float - poludnik osiowy [radians]
        
        Returns:
        xgk,ygk - float - wspolrzedne w ukladzie Gaussa-Krugera [m]
        
        """
        phi = phi*pi/180
        l = l*pi/180
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
        Transformacja współrzędnych w układzie Gaussa-Krugera do układu PL-1992
        Parametres:
        -----------
        xgk,ygk - float - współrzędne w układzie Gaussa-Krugera [m]
        
        Returns:
        --------
        x,y - float - współrzędne w układzie PL-1992 [m]
        """
        x = xgk * 0.9993 - 5300000
        y = ygk * 0.9993 + 500000
        return x,y
    
    def u2000(self,xgk,ygk,L0):
        """
        Transformacja współrzędnych w układzie Gaussa-Krugera do układu PL-2000
        Parametres:
        -----------
        xgk,ygk - float - współrzędne w układzie Gaussa-Krugera [m]
        L0 - float - poludnik osiowy [radians]
        
        Returns:
        --------
        x,y - float - współrzędne w układzie PL-2000 [m]
        """
        x = xgk * 0.999923
        y = ygk * 0.999923 + (L0*180/pi/3) * 1000000 + 500000
        return x,y
    
    def plh2xyz(self,P,L,H):
        """
        Transformacja odwrotna do algorytmu Hirvonena- transformacja współrzędnych geodezyjnych:
        szerokosc, dlugosc i wysokosc elipsoidalna na współrzędne ortokartezjańskie X,Y,Z
        
        Parametres:
        ----------
        P,L,H - float - szerokosc, dlugosc oraz wysokosc elipsoidalna [stopnie dziesietne i metry]
        
        Returns:
        --------
        X,Y,Z - float - wspolrzedne ortokartezjańskie [m]
        
        """
        P = P*pi/180
        L = L*pi/180
        N = self.Np(P)
        X = (N+H)*cos(P)*cos(L)
        Y = (N+H)*cos(P)*sin(L)
        Z = (N*(1 -self.e2 )+H)*sin(P)
        return X,Y,Z
     
     
    def isFloat(self,string):
        """
        Funkcja sprawdzająca czy podany ciąg znaków jest liczbą (float).
        
        Parameters
        ----------
        string : string
        na przykład "AlaMaKota" lub "15.78"
        
        Returns
        -------
        bool (True or False)

        """
    
        try:
            float(string)
            return True
        except:
            return False
            
    def pushButton_choice(self,wgs,grs,b92,b5,b6,b7,b8,editF,editL,H_no,H_yes,editH,wynikXY,wynikXYZ,b00):
        """
        Główna funkcja programu pozwalająca użytkownikowi na obliczenie współrzędnych ((I) na podstawie wyboru elipsoidy, (II) wprowadzonych współrzędnych
        fi, lambda, (III) wyboru układu dla współrzędnych wynikowych oraz (IV) potencjalnego wyboru wprowadzenia wysokosci elipsoidalnej) 
        w układzie PL-2000, PL-1992 lub w układzie współrzędnych ortokartezjańskich XYZ [m].
        
        Parameters
        ----------
        wgs : radioButton_WGS84 (QRadioButton)
        grs : radioButton_GRS80 (QRadioButton)
        b92 : radioButton_1992 (QRadioButton)
        b5 : radioButton_5 (QRadioButton)
        b6 : radioButton_6 (QRadioButton)
        b7 : radioButton_7 (QRadioButton)
        b8 : radioButton_8 (QRadioButton)
        editF : lineEdit_F (QLineEdit) stopnie dziesietne
        editL : lineEdit_L (QLineEdit) stopnie dziesietne
        H_no : radioButton_H_no (QRadioButton)
        H_yes : radioButton_H_yes (QRadioButton)
        editH : lineEdit_H (QLineEdit) metry
        wynikXY : wynikXY (QLabel)
        wynikXYZ : wynikXYZ (QLabel)
        b00 : radioButton_2000 (QRadioButton)

        Raises
        ------
        TypeError
            Błąd wyswietlający się po niewprowadzeniu współrzędnych, wprowadzeniu ciągu znaków lub niewprowadzeniu wysokosci elipsoidalnej.
        ValueError
            Błąd wyswietlający się po wprowadzeniu współrzędnych punktu nieznajdującego się w Polsce lub wybraniu błędnej strefy dla wprowadzonej
            wartosci lambdy.

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
            
        if H_yes.isChecked():
            self.ui.label_7.setEnabled(False)
            self.ui.label_9.setEnabled(True)
            if len(editH.text())!= 0:
                if self.isFloat(editH.text()):
                    self.H = float(editH.text())
                    self.X_or, self.Y_or, self.Z_or = self.plh2xyz(self.F_deg, self.L_deg, self.H)
                    wynikXYZ.setText(f'X: {self.X_or:.3f} m, Y: {self.Y_or:.3f} m, Z: {self.Z_or:.3f} m')
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
                wynikXY.setText(f'X 1992: {self.X:.3f} m, Y 1992: {self.Y:.3f} m')
                wynikXYZ.setText(f'')
            if b00.isChecked():
                self.dx = self.L_deg - self.L0*180/pi
                if self.dx > 1.5 or self.dx < -1.5:
                    wynikXY.setText(f'Dla podanej lambda wybrano błędną strefę')
                    raise ValueError(f'Dla podanej lambda wybrano błędną strefę')
                else:
                    self.X, self.Y = self.u2000(self.X_gk, self.Y_gk, self.L0)
                    wynikXY.setText(f'X 2000: {self.X:.3f} m, Y 2000: {self.Y:.3f} m')
                    wynikXYZ.setText(f'')
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
    
