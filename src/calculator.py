# Project: IVS - Calculator
# File: calculator.py

# Description: This file contains the GUI of the calculator application. The GUI
# takes inserted values as who string and evaluates them using the eval_expr(), 
# which is a function from the mathematical_library.py file.


#===============================START-OF-FILE===================================

## Form generated from reading UI file 'CalculatorfKhcss.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QWidget, QTextBrowser)
from mathematical_library import eval_expr # Function for evaluating the expressions

##  @class Ui_MainWindow
#   @brief This class represents the main window of the application.

class Ui_MainWindow(object):

##  @fn setupUi
#   @brief Sets up the UI for the main window.
#   @param MainWindow The main window for which to set up the UI.

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(400, 500)
        MainWindow.setStyleSheet(u"background-color:black")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # FONTS
        # For buttons
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(20)
        font.setBold(False)

        # For display
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(36)
        font1.setBold(True)

        # For help center
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(12)
        font2.setBold(False)
        # END OF FONTS

        # Buttons
        self.Btn_No_1 = QPushButton(self.centralwidget, clicked = lambda: self.press_it('1'))
        self.Btn_No_1.setObjectName(u"Btn_No_1")
        self.Btn_No_1.setGeometry(QRect(30, 210, 60, 60))
        self.Btn_No_1.setFont(font)
        self.Btn_No_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_No_1.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_No_1.setAutoDefault(False)
        self.Btn_No_1.setFlat(False)
        self.Btn_No_2 = QPushButton(self.centralwidget, clicked = lambda: self.press_it('2'))
        self.Btn_No_2.setObjectName(u"Btn_No_2")
        self.Btn_No_2.setGeometry(QRect(100, 210, 60, 60))
        self.Btn_No_2.setFont(font)
        self.Btn_No_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_No_2.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_No_2.setAutoDefault(False)
        self.Btn_No_2.setFlat(False)
        self.Btn_No_3 = QPushButton(self.centralwidget, clicked = lambda: self.press_it('3'))
        self.Btn_No_3.setObjectName(u"Btn_No_3")
        self.Btn_No_3.setGeometry(QRect(170, 210, 60, 60))
        self.Btn_No_3.setFont(font)
        self.Btn_No_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_No_3.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_No_3.setAutoDefault(False)
        self.Btn_No_3.setFlat(False)
        self.Btn_No_4 = QPushButton(self.centralwidget, clicked = lambda: self.press_it('4'))
        self.Btn_No_4.setObjectName(u"Btn_No_4")
        self.Btn_No_4.setGeometry(QRect(30, 280, 60, 60))
        self.Btn_No_4.setFont(font)
        self.Btn_No_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_No_4.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_No_4.setAutoDefault(False)
        self.Btn_No_4.setFlat(False)
        self.Btn_No_5 = QPushButton(self.centralwidget, clicked = lambda: self.press_it('5'))
        self.Btn_No_5.setObjectName(u"Btn_No_5")
        self.Btn_No_5.setGeometry(QRect(100, 280, 60, 60))
        self.Btn_No_5.setFont(font)
        self.Btn_No_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_No_5.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_No_5.setAutoDefault(False)
        self.Btn_No_5.setFlat(False)
        self.Btn_No_6 = QPushButton(self.centralwidget, clicked = lambda: self.press_it('6'))
        self.Btn_No_6.setObjectName(u"Btn_No_6")
        self.Btn_No_6.setGeometry(QRect(170, 280, 60, 60))
        self.Btn_No_6.setFont(font)
        self.Btn_No_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_No_6.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_No_6.setAutoDefault(False)
        self.Btn_No_6.setFlat(False)
        self.Btn_No_7 = QPushButton(self.centralwidget, clicked = lambda: self.press_it('7'))
        self.Btn_No_7.setObjectName(u"Btn_No_7")
        self.Btn_No_7.setGeometry(QRect(30, 350, 60, 60))
        self.Btn_No_7.setFont(font)
        self.Btn_No_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_No_7.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_No_7.setAutoDefault(False)
        self.Btn_No_7.setFlat(False)
        self.Btn_No_8 = QPushButton(self.centralwidget, clicked = lambda: self.press_it('8'))
        self.Btn_No_8.setObjectName(u"Btn_No_8")
        self.Btn_No_8.setGeometry(QRect(100, 350, 60, 60))
        self.Btn_No_8.setFont(font)
        self.Btn_No_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_No_8.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_No_8.setAutoDefault(False)
        self.Btn_No_8.setFlat(False)
        self.Btn_No_9 = QPushButton(self.centralwidget, clicked = lambda: self.press_it('9'))
        self.Btn_No_9.setObjectName(u"Btn_No_9")
        self.Btn_No_9.setGeometry(QRect(170, 350, 60, 60))
        self.Btn_No_9.setFont(font)
        self.Btn_No_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_No_9.setStyleSheet(u"color: white; background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_No_9.setAutoDefault(False)
        self.Btn_No_9.setFlat(False)
        self.Btn_No_0 = QPushButton(self.centralwidget, clicked = lambda: self.press_it('0'))
        self.Btn_No_0.setObjectName(u"Btn_No_0")
        self.Btn_No_0.setGeometry(QRect(30, 420, 60, 60))
        self.Btn_No_0.setFont(font)
        self.Btn_No_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_No_0.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_No_0.setAutoDefault(False)
        self.Btn_No_0.setFlat(False)
        self.Btn_Equal = QPushButton(self.centralwidget, clicked = lambda: self.press_it('='))
        self.Btn_Equal.setObjectName(u"Btn_Equal")
        self.Btn_Equal.setGeometry(QRect(310, 420, 60, 60))
        self.Btn_Equal.setFont(font)
        self.Btn_Equal.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Equal.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_Equal.setAutoDefault(False)
        self.Btn_Equal.setFlat(False)
        self.Btn_AC = QPushButton(self.centralwidget, clicked = lambda: self.press_it('AC'))
        self.Btn_AC.setObjectName(u"Btn_AC")
        self.Btn_AC.setGeometry(QRect(310, 210, 60, 60))
        self.Btn_AC.setFont(font)
        self.Btn_AC.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_AC.setStyleSheet(u"color: white;background-color: rgb(255, 157, 9);border-radius: 10px;")
        self.Btn_AC.setAutoDefault(False)
        self.Btn_AC.setFlat(False)
        self.Btn_Plus = QPushButton(self.centralwidget, clicked = lambda: self.press_it('+'))
        self.Btn_Plus.setObjectName(u"Btn_Plus")
        self.Btn_Plus.setGeometry(QRect(240, 350, 60, 60))
        self.Btn_Plus.setFont(font)
        self.Btn_Plus.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Plus.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_Plus.setAutoDefault(False)
        self.Btn_Plus.setFlat(False)
        self.Btn_Minus = QPushButton(self.centralwidget, clicked = lambda: self.press_it('-'))
        self.Btn_Minus.setObjectName(u"Btn_Minus")
        self.Btn_Minus.setGeometry(QRect(310, 350, 60, 60))
        self.Btn_Minus.setFont(font)
        self.Btn_Minus.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Minus.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_Minus.setAutoDefault(False)
        self.Btn_Minus.setFlat(False)
        self.Btn_Multiply = QPushButton(self.centralwidget, clicked = lambda: self.press_it('*'))
        self.Btn_Multiply.setObjectName(u"Btn_Multiply")
        self.Btn_Multiply.setGeometry(QRect(240, 280, 60, 60))
        self.Btn_Multiply.setFont(font)
        self.Btn_Multiply.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Multiply.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_Multiply.setAutoDefault(False)
        self.Btn_Multiply.setFlat(False)
        self.Btn_Devide = QPushButton(self.centralwidget, clicked = lambda: self.press_it('/'))
        self.Btn_Devide.setObjectName(u"Btn_Devide")
        self.Btn_Devide.setGeometry(QRect(310, 280, 60, 60))
        self.Btn_Devide.setFont(font)
        self.Btn_Devide.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Devide.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_Devide.setAutoDefault(False)
        self.Btn_Devide.setFlat(False)
        self.Btn_Del = QPushButton(self.centralwidget, self.centralwidget, clicked = lambda: self.press_it('Del'))
        self.Btn_Del.setObjectName(u"Btn_Del")
        self.Btn_Del.setGeometry(QRect(240, 210, 60, 60))
        self.Btn_Del.setFont(font)
        self.Btn_Del.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Del.setStyleSheet(u"color: white;background-color: rgb(0, 140, 255);border-radius: 10px;")
        self.Btn_Del.setAutoDefault(False)
        self.Btn_Del.setFlat(False)
        self.Btn_Fact = QPushButton(self.centralwidget, clicked = lambda: self.press_it('!'))
        self.Btn_Fact.setObjectName(u"Btn_Fact")
        self.Btn_Fact.setGeometry(QRect(240, 420, 60, 60))
        self.Btn_Fact.setFont(font)
        self.Btn_Fact.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Fact.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_Fact.setAutoDefault(False)
        self.Btn_Fact.setFlat(False)
        self.Btn_Power = QPushButton(self.centralwidget, clicked = lambda: self.press_it('^'))
        self.Btn_Power.setObjectName(u"Btn_Power")
        self.Btn_Power.setGeometry(QRect(30, 140, 60, 60))
        self.Btn_Power.setFont(font)
        self.Btn_Power.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Power.setStyleSheet(u"color: white; background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_Power.setAutoDefault(False)
        self.Btn_Power.setFlat(False)
        self.Btn_Root = QPushButton(self.centralwidget, clicked = lambda: self.press_it('\u221a'))
        self.Btn_Root.setObjectName(u"Btn_Root")
        self.Btn_Root.setGeometry(QRect(100, 140, 60, 60))
        self.Btn_Root.setFont(font)
        self.Btn_Root.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Root.setStyleSheet(u"color: white ;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_Root.setAutoDefault(False)
        self.Btn_Root.setFlat(False)
        self.Btn_Pi = QPushButton(self.centralwidget, clicked = lambda: self.press_it('\u03c0'))
        self.Btn_Pi.setObjectName(u"Btn_Pi")
        self.Btn_Pi.setGeometry(QRect(170, 420, 60, 60))
        self.Btn_Pi.setFont(font)
        self.Btn_Pi.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Pi.setAutoDefault(False)
        self.Btn_Pi.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_Pi.setFlat(False)
        self.Btn_Sin = QPushButton(self.centralwidget, clicked = lambda: self.press_it('sin'))
        self.Btn_Sin.setObjectName(u"Btn_Sin")
        self.Btn_Sin.setGeometry(QRect(170, 140, 60, 60))
        self.Btn_Sin.setFont(font)
        self.Btn_Sin.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Sin.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_Sin.setAutoDefault(False)
        self.Btn_Sin.setFlat(False)
        self.Btn_Cos = QPushButton(self.centralwidget, clicked = lambda: self.press_it('cos'))
        self.Btn_Cos.setObjectName(u"Btn_Cos")
        self.Btn_Cos.setGeometry(QRect(240, 140, 60, 60))
        self.Btn_Cos.setFont(font)
        self.Btn_Cos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Cos.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_Cos.setAutoDefault(False)
        self.Btn_Cos.setFlat(False)
        self.Btn_Tan = QPushButton(self.centralwidget, clicked = lambda: self.press_it('tan'))
        self.Btn_Tan.setObjectName(u"Btn_Tan")
        self.Btn_Tan.setGeometry(QRect(310, 140, 60, 60))
        self.Btn_Tan.setFont(font)
        self.Btn_Tan.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Tan.setAutoDefault(False)
        self.Btn_Tan.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_Tan.setFlat(False)
        self.Btn_Point = QPushButton(self.centralwidget, clicked = lambda: self.press_it('.'))
        self.Btn_Point.setObjectName(u"Btn_Point")
        self.Btn_Point.setGeometry(QRect(100, 420, 60, 60))
        self.Btn_Point.setFont(font)
        self.Btn_Point.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Point.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63);border-radius: 10px;")
        self.Btn_Point.setAutoDefault(False)
        self.Btn_Point.setFlat(False)
        self.Btn_Help = QPushButton(self.centralwidget, clicked = lambda: self.press_it('Help'))
        self.Btn_Help.setObjectName(u"Btn_Help")
        self.Btn_Help.setGeometry(QRect(10, 4, 60, 24))
        self.Btn_Help.setFont(font2)
        self.Btn_Help.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Help.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63); border-radius: 12;")
        self.Btn_Help.setAutoDefault(False)
        self.Btn_Help.setFlat(False)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 30, 380, 80))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setLayoutDirection(Qt.RightToLeft)
        self.scrollArea.setStyleSheet(u"QScrollBar:horizontal {\n"
"	border: none;\n"
"    	background: rgb(63, 63, 63);\n"
"	background-color: rgb(63, 63, 63);\n"
"	border-radius: 0px;\n"
" }\n"
"QScrollBar::handle:horizontal {	\n"
"	background-color: rgb(255, 255, 255);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{	\n"
"	background-color: rgb(255, 157, 9);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {	\n"
"	background-color: rgb(255, 157, 9);\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-page:horizontal {\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal {\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.Box)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-185, 0, 561, 61))
        self.scrollAreaWidgetContents.setStyleSheet(u"border-color: white;")
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Display = QLabel(self.scrollAreaWidgetContents)
        self.Display.setObjectName(u"Display")
        self.Display.setEnabled(True)
        self.Display.setFont(font1)
        self.Display.setAutoFillBackground(False)
        self.Display.setStyleSheet(u"color: white; background-color: rgb(63, 63, 63); border-color: white;")
        self.Display.setFrameShape(QFrame.NoFrame)
        self.Display.setFrameShadow(QFrame.Sunken)
        self.Display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Display.setMargin(10)
        self.horizontalLayout.addWidget(self.Display)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Help
        self.scrollArea_Help = QScrollArea(self.centralwidget)
        self.scrollArea_Help.setObjectName(u"scrollArea_Help")
        self.scrollArea_Help.setGeometry(QRect(0, 0, 400, 500))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_Help.sizePolicy().hasHeightForWidth())
        self.scrollArea_Help.setSizePolicy(sizePolicy)
        self.scrollArea_Help.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea_Help.setStyleSheet(u"QScrollBar:vertical {\n"
"	border: none;\n"
"    	background: rgb(63, 63, 63);\n"
"	background-color: rgb(63, 63, 63);\n"
"	border-radius: 0px;\n"
" }\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(255, 255, 255);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 157, 9);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(255, 157, 9);\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
"    	background: rgb(63, 63, 63);\n"
"	width: 0px;\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
"    	background: rgb(63, 63, 63);\n"
"	width: 0px;\n"
"}")
        self.scrollArea_Help.setFrameShape(QFrame.Box)
        self.scrollArea_Help.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_Help.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 398, 498))
        self.textBrowser = QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 10, 375, 427))
        self.textBrowser.setStyleSheet(u"color: white; background-color: rgb(63, 63, 63);")
        self.Btn_Help_Close = QPushButton(self.scrollAreaWidgetContents_2, clicked = lambda: self.press_it('Help_Close'))
        self.Btn_Help_Close.setObjectName(u"Btn_Help_Close")
        self.Btn_Help_Close.setGeometry(QRect(166, 452, 60, 30))
        self.Btn_Help_Close.setFont(font2)
        self.Btn_Help_Close.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Help_Close.setStyleSheet(u"color: white;background-color: rgb(63, 63, 63); border-radius: 15;")
        self.Btn_Help_Close.setAutoDefault(False)
        self.Btn_Help_Close.setFlat(False)
        self.scrollArea_Help.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_Help.hide()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        # Set default status of buttons
        self.Btn_No_1.setDefault(False)
        self.Btn_No_2.setDefault(False)
        self.Btn_No_3.setDefault(False)
        self.Btn_No_4.setDefault(False)
        self.Btn_No_5.setDefault(False)
        self.Btn_No_6.setDefault(False)
        self.Btn_No_7.setDefault(False)
        self.Btn_No_8.setDefault(False)
        self.Btn_No_9.setDefault(False)
        self.Btn_No_0.setDefault(False)
        self.Btn_Equal.setDefault(False)
        self.Btn_AC.setDefault(False)
        self.Btn_Plus.setDefault(False)
        self.Btn_Minus.setDefault(False)
        self.Btn_Multiply.setDefault(False)
        self.Btn_Devide.setDefault(False)
        self.Btn_Del.setDefault(False)
        self.Btn_Fact.setDefault(False)
        self.Btn_Power.setDefault(False)
        self.Btn_Root.setDefault(False)
        self.Btn_Pi.setDefault(False)
        self.Btn_Sin.setDefault(False)
        self.Btn_Cos.setDefault(False)
        self.Btn_Tan.setDefault(False)
        self.Btn_Point.setDefault(False)
        self.Btn_Help.setDefault(False)
        self.Btn_Help_Close.setDefault(False)
        
        QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.keyPressEvent = self.keyPressEvent # Enable key press event handling

##  @fn keyPressEvent
#   @brief Function for handling the button press - by keyboard
#   @param event The key press event to handle.
    def keyPressEvent(self, event):
        
        key = event.key()
        if self.scrollArea_Help.isHidden():
            if key == Qt.Key_0:
                self.press_it('0')
            elif key == Qt.Key_1:
                self.press_it('1')
            elif key == Qt.Key_2:
                self.press_it('2')
            elif key == Qt.Key_3:
                self.press_it('3')
            elif key == Qt.Key_4:
                self.press_it('4')
            elif key == Qt.Key_5:
                self.press_it('5')
            elif key == Qt.Key_6:
                self.press_it('6')
            elif key == Qt.Key_7:
                self.press_it('7')
            elif key == Qt.Key_8:
                self.press_it('8')
            elif key == Qt.Key_9:
                self.press_it('9')
            elif key == Qt.Key_Plus:
                self.press_it('+')
            elif key == Qt.Key_Minus:
                self.press_it('-')
            elif key == Qt.Key_Asterisk:
                self.press_it('*')
            elif key == Qt.Key_Slash:
                self.press_it('/')
            elif key == Qt.Key_Exclam:
                self.press_it('!')
            elif key == Qt.Key_Period:
                self.press_it('.')
            elif key == Qt.Key_P:
                self.press_it('\u03c0')
            elif key == Qt.Key_AsciiCircum: # Only US keyboard layout
                self.press_it('^')
            elif key == Qt.Key_Enter or key == Qt.Key_Equal or key == Qt.Key_Return:
                self.press_it('=')
            elif key == Qt.Key_Escape:
                self.press_it('AC')
            elif key == Qt.Key_Backspace: 
                self.press_it('Del')
        else:
            if key == Qt.Key_Escape:
                self.scrollArea_Help.hide()
        
##  @fn press_it
#   @brief Function for handling the button press - by click
#   @param pressed The button that was pressed.
#   @return The displayed value.
    History = ''
    Displayed = '0'
    def press_it(self, pressed):

        global Displayed, History
        if pressed == 'Help':
            self.scrollArea_Help.show()
        elif pressed == 'Help_Close':
            self.scrollArea_Help.hide()
        else:
            if pressed == 'AC':
                self.Displayed = '0'
                self.Display.setText(self.Displayed)
            elif pressed == 'Del':
                self.Displayed = self.Display.text()
                if self.Displayed[-3:] in ['cos', 'sin', 'tan']:
                    self.Displayed = self.Displayed[:-3]
                elif self.Displayed[-10:] in ['Math Error']:
                    self.Displayed = self.Displayed[:-10]
                elif self.Displayed[-12:] in ['Syntax Error']:
                    self.Displayed = self.Displayed[:-12]
                else:
                    self.Displayed = self.Displayed[:-1]
                if self.Displayed == '':
                    self.Displayed = '0'
                self.Display.setText(self.Displayed)
            elif pressed == '=':
                try:
                    self.History = eval_expr(self.Displayed)
                    self.Display.setText(self.History)
                    self.Displayed = self.History
                except Exception as e:
                    self.Display.setText(str(e))
            else:
                if self.Displayed == '0':
                    if (pressed == 'sin' or pressed == 'cos' or pressed == 'tan' or 
                        pressed == '\u03c0' or pressed == '0' or pressed == '-' or
                        pressed == '1' or pressed == '2' or pressed == '3' or 
                        pressed == '4' or pressed == '5' or pressed == '6' or 
                        pressed == '7' or pressed == '8' or pressed == '9' or
                        pressed == '+'):
                        self.Displayed = ''
                elif self.Displayed == 'Math Error' or self.Displayed == 'Syntax Error':
                    self.Displayed = ''
                self.Displayed += pressed
                self.Display.setText(self.Displayed)
            return self.Displayed

##  @fn retranslateUi
#   @brief Function for translating the GUI
#   @param MainWindow The main window to translate.
    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.Display.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Btn_No_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Btn_No_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Btn_No_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Btn_No_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Btn_No_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Btn_No_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Btn_No_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Btn_No_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Btn_No_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Btn_No_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Btn_Equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.Btn_AC.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.Btn_Plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Btn_Minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Btn_Multiply.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.Btn_Devide.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.Btn_Del.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.Btn_Fact.setText(QCoreApplication.translate("MainWindow", u"x!", None))
        self.Btn_Power.setText(QCoreApplication.translate("MainWindow", u"x^n", None))
        self.Btn_Root.setText(QCoreApplication.translate("MainWindow", u"n\u221ax", None))
        self.Btn_Pi.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.Btn_Sin.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.Btn_Cos.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.Btn_Tan.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.Btn_Point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.Btn_Help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Error Messages:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">Math Error </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">--&gt; division by zero or exceeded max. number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">Syntax Error</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">--&gt; incorrect format (eg. 5^ , 5+ ,5cos45)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Correct format of input for operands: </span></p>\n"
"<p style=\" margin-top:0px; margin"
                        "-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">(N = Number)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">+, -, *, / 	         --&gt; </span><span style=\" font-size:12pt; font-style:italic\">N+N, N-N, N*N, N/N</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">x!	         --&gt; N!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">sinx, cosx, tanx   --&gt; sinN, cosN, tanN </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">x^n, n\u221ax	         --&gt; N^N, N\u221a"
                        "N</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u03c0 (Pi)	         </span><span style=\" font-size:12pt; font-style:italic;\">--&gt; N</span><span style=\" font-size:12pt;\">*\u03c0</span><span style=\" font-size:12pt;\">, \u03c0*</span><span style=\" font-size:12pt; font-style:italic; \">N, N</span><span style=\" font-size:12pt;\">*\u03c0*</span><span style=\" font-size:12pt; font-style:italic; \">N</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Keyboard:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">Enter, = --&gt; =</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-le"
                        "ft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">Backspace --&gt; Del</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">Esc --&gt; AC (clears result)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">1, 2, 3, ..., 9, 0 --&gt; 1, 2, 3, ..., 9, 0 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">. --&gt; .</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">+ --&gt; +</span></p>\n"
"<p style=\" margin-top:"
                        "0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">- --&gt; -</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">* --&gt; *</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">/ --&gt; /</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">! --&gt; x!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">P --&gt; </span><span style=\" font-size:12pt;\">\u03c0</span></p></body></html>", None))
        self.Btn_Help_Close.setText(QCoreApplication.translate("MainWindow", u"Back", None))

# Main function for running the GUI
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    MainWindow.setWindowTitle('Calculator')
    MainWindow.setWindowIcon(QIcon('Calc-SEG_FAULT.ico'))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

#===============================END-OF-FILE=====================================
