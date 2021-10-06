# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainFZjVNk.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLCDNumber, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QScrollBar, QSizePolicy,
    QSlider, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1185, 724)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setGeometry(QRect(10, 10, 1170, 700))
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription.setWordWrap(True)
        self.label_54 = QLabel(self.topLogoInfo)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(-10, -10, 91, 71))
        self.label_54.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_54.setScaledContents(True)
        self.label_54.setAlignment(Qt.AlignCenter)
        self.label_54.setMargin(15)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.dash_board_btn = QPushButton(self.topMenu)
        self.dash_board_btn.setObjectName(u"dash_board_btn")
        sizePolicy.setHeightForWidth(self.dash_board_btn.sizePolicy().hasHeightForWidth())
        self.dash_board_btn.setSizePolicy(sizePolicy)
        self.dash_board_btn.setMinimumSize(QSize(0, 45))
        self.dash_board_btn.setFont(font)
        self.dash_board_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dash_board_btn.setLayoutDirection(Qt.LeftToRight)
        self.dash_board_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/dashboard.png);")

        self.verticalLayout_8.addWidget(self.dash_board_btn)

        self.datasets_btn = QPushButton(self.topMenu)
        self.datasets_btn.setObjectName(u"datasets_btn")
        sizePolicy.setHeightForWidth(self.datasets_btn.sizePolicy().hasHeightForWidth())
        self.datasets_btn.setSizePolicy(sizePolicy)
        self.datasets_btn.setMinimumSize(QSize(0, 45))
        self.datasets_btn.setFont(font)
        self.datasets_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.datasets_btn.setLayoutDirection(Qt.LeftToRight)
        self.datasets_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/datasets.png);")

        self.verticalLayout_8.addWidget(self.datasets_btn)

        self.model_training_btn = QPushButton(self.topMenu)
        self.model_training_btn.setObjectName(u"model_training_btn")
        sizePolicy.setHeightForWidth(self.model_training_btn.sizePolicy().hasHeightForWidth())
        self.model_training_btn.setSizePolicy(sizePolicy)
        self.model_training_btn.setMinimumSize(QSize(0, 45))
        self.model_training_btn.setFont(font)
        self.model_training_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.model_training_btn.setLayoutDirection(Qt.LeftToRight)
        self.model_training_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/model training.png);")

        self.verticalLayout_8.addWidget(self.model_training_btn)

        self.style_gan_tab_btn = QPushButton(self.topMenu)
        self.style_gan_tab_btn.setObjectName(u"style_gan_tab_btn")
        sizePolicy.setHeightForWidth(self.style_gan_tab_btn.sizePolicy().hasHeightForWidth())
        self.style_gan_tab_btn.setSizePolicy(sizePolicy)
        self.style_gan_tab_btn.setMinimumSize(QSize(0, 45))
        self.style_gan_tab_btn.setFont(font)
        self.style_gan_tab_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.style_gan_tab_btn.setLayoutDirection(Qt.LeftToRight)
        self.style_gan_tab_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/stylegan_icon.png);")

        self.verticalLayout_8.addWidget(self.style_gan_tab_btn)

        self.generated_images_btn = QPushButton(self.topMenu)
        self.generated_images_btn.setObjectName(u"generated_images_btn")
        sizePolicy.setHeightForWidth(self.generated_images_btn.sizePolicy().hasHeightForWidth())
        self.generated_images_btn.setSizePolicy(sizePolicy)
        self.generated_images_btn.setMinimumSize(QSize(0, 45))
        self.generated_images_btn.setFont(font)
        self.generated_images_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.generated_images_btn.setLayoutDirection(Qt.LeftToRight)
        self.generated_images_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/generated images.png);")

        self.verticalLayout_8.addWidget(self.generated_images_btn)

        self.images_library_btn = QPushButton(self.topMenu)
        self.images_library_btn.setObjectName(u"images_library_btn")
        sizePolicy.setHeightForWidth(self.images_library_btn.sizePolicy().hasHeightForWidth())
        self.images_library_btn.setSizePolicy(sizePolicy)
        self.images_library_btn.setMinimumSize(QSize(0, 45))
        self.images_library_btn.setFont(font)
        self.images_library_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.images_library_btn.setLayoutDirection(Qt.LeftToRight)
        self.images_library_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/images library.png);")

        self.verticalLayout_8.addWidget(self.images_library_btn)

        self.logout_btn = QPushButton(self.topMenu)
        self.logout_btn.setObjectName(u"logout_btn")
        sizePolicy.setHeightForWidth(self.logout_btn.sizePolicy().hasHeightForWidth())
        self.logout_btn.setSizePolicy(sizePolicy)
        self.logout_btn.setMinimumSize(QSize(0, 45))
        self.logout_btn.setFont(font)
        self.logout_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout_btn.setLayoutDirection(Qt.LeftToRight)
        self.logout_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_8.addWidget(self.logout_btn)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.account_settings_btn = QPushButton(self.bottomMenu)
        self.account_settings_btn.setObjectName(u"account_settings_btn")
        sizePolicy.setHeightForWidth(self.account_settings_btn.sizePolicy().hasHeightForWidth())
        self.account_settings_btn.setSizePolicy(sizePolicy)
        self.account_settings_btn.setMinimumSize(QSize(0, 45))
        self.account_settings_btn.setFont(font)
        self.account_settings_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.account_settings_btn.setLayoutDirection(Qt.LeftToRight)
        self.account_settings_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/account settings.png);")

        self.verticalLayout_9.addWidget(self.account_settings_btn)

        self.help_btn = QPushButton(self.bottomMenu)
        self.help_btn.setObjectName(u"help_btn")
        sizePolicy.setHeightForWidth(self.help_btn.sizePolicy().hasHeightForWidth())
        self.help_btn.setSizePolicy(sizePolicy)
        self.help_btn.setMinimumSize(QSize(0, 45))
        self.help_btn.setFont(font)
        self.help_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.help_btn.setLayoutDirection(Qt.LeftToRight)
        self.help_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/help.png);")

        self.verticalLayout_9.addWidget(self.help_btn)

        self.about_btn = QPushButton(self.bottomMenu)
        self.about_btn.setObjectName(u"about_btn")
        sizePolicy.setHeightForWidth(self.about_btn.sizePolicy().hasHeightForWidth())
        self.about_btn.setSizePolicy(sizePolicy)
        self.about_btn.setMinimumSize(QSize(0, 45))
        self.about_btn.setFont(font)
        self.about_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_btn.setLayoutDirection(Qt.LeftToRight)
        self.about_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/about.png);")

        self.verticalLayout_9.addWidget(self.about_btn)

        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.CrossCursor))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setLayoutDirection(Qt.RightToLeft)
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.pagesContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget_3 = QStackedWidget(self.pagesContainer)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget_3.sizePolicy().hasHeightForWidth())
        self.stackedWidget_3.setSizePolicy(sizePolicy3)
        self.stackedWidget_3.setMinimumSize(QSize(320, 0))
        self.system_info_usage_graph = QWidget()
        self.system_info_usage_graph.setObjectName(u"system_info_usage_graph")
        self.cpu_usage_widget_2 = QWidget(self.system_info_usage_graph)
        self.cpu_usage_widget_2.setObjectName(u"cpu_usage_widget_2")
        self.cpu_usage_widget_2.setGeometry(QRect(10, 10, 301, 301))
        self.cpu_usage_widget_2.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_70 = QLabel(self.cpu_usage_widget_2)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(80, 10, 131, 20))
        self.label_70.setAlignment(Qt.AlignCenter)
        self.clear_recent_history_btn_5 = QPushButton(self.cpu_usage_widget_2)
        self.clear_recent_history_btn_5.setObjectName(u"clear_recent_history_btn_5")
        self.clear_recent_history_btn_5.setGeometry(QRect(580, 20, 91, 24))
        self.circularProgressBar_Main_2 = QFrame(self.cpu_usage_widget_2)
        self.circularProgressBar_Main_2.setObjectName(u"circularProgressBar_Main_2")
        self.circularProgressBar_Main_2.setGeometry(QRect(30, 40, 240, 240))
        self.circularProgressBar_Main_2.setStyleSheet(u"background-color: none;")
        self.circularProgressBar_Main_2.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main_2.setFrameShadow(QFrame.Raised)
        self.system_info_label_2 = QLabel(self.circularProgressBar_Main_2)
        self.system_info_label_2.setObjectName(u"system_info_label_2")
        self.system_info_label_2.setGeometry(QRect(0, 0, 231, 51))
        self.system_info_label_2.setStyleSheet(u"color: rgb(115, 185, 255); font-size: 12px; padding-left: 2px; padding-right: 2px; border: none;")
        self.system_info_label_2.setAlignment(Qt.AlignCenter)
        self.processor_info_label_2 = QLabel(self.circularProgressBar_Main_2)
        self.processor_info_label_2.setObjectName(u"processor_info_label_2")
        self.processor_info_label_2.setGeometry(QRect(0, 30, 241, 91))
        self.processor_info_label_2.setStyleSheet(u"color: rgb(115, 185, 255); font-size: 12px; padding-left: 2px; padding-right: 2px; border: none;")
        self.processor_info_label_2.setAlignment(Qt.AlignCenter)
        self.processor_info_label_2.setWordWrap(True)
        self.processor_info_label_2.setMargin(5)
        self.show_cpu_graph_btn_3 = QPushButton(self.circularProgressBar_Main_2)
        self.show_cpu_graph_btn_3.setObjectName(u"show_cpu_graph_btn_3")
        self.show_cpu_graph_btn_3.setGeometry(QRect(60, 140, 113, 32))
        self.show_cpu_graph_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_cpu_graph_btn_3.setStyleSheet(u"background-color: rgba(85, 170, 255, 255);\n"
"color: white;")
        self.show_ram_graph_btn_3 = QPushButton(self.circularProgressBar_Main_2)
        self.show_ram_graph_btn_3.setObjectName(u"show_ram_graph_btn_3")
        self.show_ram_graph_btn_3.setGeometry(QRect(60, 180, 113, 32))
        self.show_ram_graph_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_ram_graph_btn_3.setStyleSheet(u"background-color: rgb(255, 44, 174);\n"
"color: white;")
        self.cpu_usage_widget_3 = QWidget(self.system_info_usage_graph)
        self.cpu_usage_widget_3.setObjectName(u"cpu_usage_widget_3")
        self.cpu_usage_widget_3.setGeometry(QRect(10, 320, 301, 271))
        self.cpu_usage_widget_3.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_91 = QLabel(self.cpu_usage_widget_3)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(80, 10, 131, 20))
        self.label_91.setAlignment(Qt.AlignCenter)
        self.clear_recent_history_btn_6 = QPushButton(self.cpu_usage_widget_3)
        self.clear_recent_history_btn_6.setObjectName(u"clear_recent_history_btn_6")
        self.clear_recent_history_btn_6.setGeometry(QRect(580, 20, 91, 24))
        self.listWidget_notifications = QListWidget(self.cpu_usage_widget_3)
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-comment-square.png", QSize(), QIcon.Normal, QIcon.Off)
        font4 = QFont()
        font4.setPointSize(12)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_notifications)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem.setFont(font4);
        __qlistwidgetitem.setIcon(icon4);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_notifications)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1.setFont(font4);
        __qlistwidgetitem1.setIcon(icon4);
        __qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_notifications)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2.setFont(font4);
        __qlistwidgetitem2.setIcon(icon4);
        __qlistwidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.listWidget_notifications.setObjectName(u"listWidget_notifications")
        self.listWidget_notifications.setGeometry(QRect(40, 40, 241, 221))
        self.listWidget_notifications.setMinimumSize(QSize(0, 0))
        self.listWidget_notifications.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.listWidget_notifications.setLayoutDirection(Qt.LeftToRight)
        self.listWidget_notifications.setFrameShape(QFrame.StyledPanel)
        self.listWidget_notifications.setLineWidth(1)
        self.listWidget_notifications.setProperty("showDropIndicator", True)
        self.listWidget_notifications.setAlternatingRowColors(False)
        self.listWidget_notifications.setIconSize(QSize(23, 30))
        self.listWidget_notifications.setFlow(QListView.TopToBottom)
        self.listWidget_notifications.setProperty("isWrapping", True)
        self.listWidget_notifications.setResizeMode(QListView.Adjust)
        self.listWidget_notifications.setSpacing(20)
        self.listWidget_notifications.setViewMode(QListView.ListMode)
        self.listWidget_notifications.setModelColumn(0)
        self.listWidget_notifications.setBatchSize(100)
        self.listWidget_notifications.setWordWrap(False)
        self.listWidget_notifications.setSelectionRectVisible(True)
        self.listWidget_notifications.setItemAlignment(Qt.AlignCenter)
        self.listWidget_notifications.setSortingEnabled(False)
        self.stackedWidget_3.addWidget(self.system_info_usage_graph)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.page_10.setEnabled(True)
        self.page_10.setMaximumSize(QSize(0, 0))
#if QT_CONFIG(accessibility)
        self.page_10.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.page_10.setLayoutDirection(Qt.LeftToRight)
        self.horizont = QHBoxLayout(self.page_10)
        self.horizont.setObjectName(u"horizont")
        self.stackedWidget_3.addWidget(self.page_10)
        self.cpu_ram_circular = QWidget()
        self.cpu_ram_circular.setObjectName(u"cpu_ram_circular")
        self.cpu_usage_widget = QWidget(self.cpu_ram_circular)
        self.cpu_usage_widget.setObjectName(u"cpu_usage_widget")
        self.cpu_usage_widget.setGeometry(QRect(10, 10, 301, 301))
        self.cpu_usage_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_68 = QLabel(self.cpu_usage_widget)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(100, 10, 91, 16))
        self.label_68.setAlignment(Qt.AlignCenter)
        self.clear_recent_history_btn_3 = QPushButton(self.cpu_usage_widget)
        self.clear_recent_history_btn_3.setObjectName(u"clear_recent_history_btn_3")
        self.clear_recent_history_btn_3.setGeometry(QRect(580, 20, 91, 24))
        self.circularProgressBar_Main = QFrame(self.cpu_usage_widget)
        self.circularProgressBar_Main.setObjectName(u"circularProgressBar_Main")
        self.circularProgressBar_Main.setGeometry(QRect(30, 40, 240, 240))
        self.circularProgressBar_Main.setStyleSheet(u"background-color: none;")
        self.circularProgressBar_Main.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main.setFrameShadow(QFrame.Raised)
        self.circularProgressCPU_2 = QFrame(self.circularProgressBar_Main)
        self.circularProgressCPU_2.setObjectName(u"circularProgressCPU_2")
        self.circularProgressCPU_2.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgressCPU_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.400 rgba(85, 170, 255, 255), stop:0.395 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressCPU_2.setFrameShape(QFrame.StyledPanel)
        self.circularProgressCPU_2.setFrameShadow(QFrame.Raised)
        self.circularBg_2 = QFrame(self.circularProgressBar_Main)
        self.circularBg_2.setObjectName(u"circularBg_2")
        self.circularBg_2.setGeometry(QRect(10, 10, 220, 220))
        self.circularBg_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_2.setFrameShape(QFrame.StyledPanel)
        self.circularBg_2.setFrameShadow(QFrame.Raised)
        self.circularContainer_2 = QFrame(self.circularProgressBar_Main)
        self.circularContainer_2.setObjectName(u"circularContainer_2")
        self.circularContainer_2.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainer_2.setBaseSize(QSize(0, 0))
        self.circularContainer_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer_2.setFrameShape(QFrame.StyledPanel)
        self.circularContainer_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.circularContainer_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 40, 171, 158))
        self.infoLayout_2 = QGridLayout(self.layoutWidget_2)
        self.infoLayout_2.setObjectName(u"infoLayout_2")
        self.infoLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName_2 = QLabel(self.layoutWidget_2)
        self.labelAplicationName_2.setObjectName(u"labelAplicationName_2")
        self.labelAplicationName_2.setFont(font)
        self.labelAplicationName_2.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName_2.setAlignment(Qt.AlignCenter)

        self.infoLayout_2.addWidget(self.labelAplicationName_2, 0, 0, 1, 1)

        self.labelPercentageCPU_2 = QLabel(self.layoutWidget_2)
        self.labelPercentageCPU_2.setObjectName(u"labelPercentageCPU_2")
        self.labelPercentageCPU_2.setFont(font)
        self.labelPercentageCPU_2.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.labelPercentageCPU_2.setAlignment(Qt.AlignCenter)
        self.labelPercentageCPU_2.setIndent(-1)

        self.infoLayout_2.addWidget(self.labelPercentageCPU_2, 1, 0, 1, 1)

        self.labelCredits_2 = QLabel(self.layoutWidget_2)
        self.labelCredits_2.setObjectName(u"labelCredits_2")
        self.labelCredits_2.setFont(font)
        self.labelCredits_2.setStyleSheet(u"color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits_2.setAlignment(Qt.AlignCenter)

        self.infoLayout_2.addWidget(self.labelCredits_2, 2, 0, 1, 1)

        self.ram_usage_widget = QWidget(self.cpu_ram_circular)
        self.ram_usage_widget.setObjectName(u"ram_usage_widget")
        self.ram_usage_widget.setGeometry(QRect(10, 320, 301, 271))
        self.ram_usage_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.clear_recent_history_btn_4 = QPushButton(self.ram_usage_widget)
        self.clear_recent_history_btn_4.setObjectName(u"clear_recent_history_btn_4")
        self.clear_recent_history_btn_4.setGeometry(QRect(580, 20, 91, 24))
        self.label_69 = QLabel(self.ram_usage_widget)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(110, 10, 91, 16))
        self.label_69.setAlignment(Qt.AlignCenter)
        self.circularProgressBar_Main_3 = QFrame(self.ram_usage_widget)
        self.circularProgressBar_Main_3.setObjectName(u"circularProgressBar_Main_3")
        self.circularProgressBar_Main_3.setGeometry(QRect(130, 110, 240, 240))
        self.circularProgressBar_Main_3.setStyleSheet(u"background-color: none;")
        self.circularProgressBar_Main_3.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main_3.setFrameShadow(QFrame.Raised)
        self.circularProgressBar_Main_4 = QFrame(self.ram_usage_widget)
        self.circularProgressBar_Main_4.setObjectName(u"circularProgressBar_Main_4")
        self.circularProgressBar_Main_4.setGeometry(QRect(40, 30, 240, 240))
        self.circularProgressBar_Main_4.setStyleSheet(u"background-color: none;")
        self.circularProgressBar_Main_4.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main_4.setFrameShadow(QFrame.Raised)
        self.circularProgressRAM = QFrame(self.circularProgressBar_Main_4)
        self.circularProgressRAM.setObjectName(u"circularProgressRAM")
        self.circularProgressRAM.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgressRAM.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.750 rgba(255, 0, 127, 255), stop:0.745 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressRAM.setFrameShape(QFrame.StyledPanel)
        self.circularProgressRAM.setFrameShadow(QFrame.Raised)
        self.circularBg_3 = QFrame(self.circularProgressBar_Main_4)
        self.circularBg_3.setObjectName(u"circularBg_3")
        self.circularBg_3.setGeometry(QRect(10, 10, 220, 220))
        self.circularBg_3.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_3.setFrameShape(QFrame.StyledPanel)
        self.circularBg_3.setFrameShadow(QFrame.Raised)
        self.circularContainer_3 = QFrame(self.circularProgressBar_Main_4)
        self.circularContainer_3.setObjectName(u"circularContainer_3")
        self.circularContainer_3.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainer_3.setBaseSize(QSize(0, 0))
        self.circularContainer_3.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer_3.setFrameShape(QFrame.StyledPanel)
        self.circularContainer_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.circularContainer_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 40, 171, 158))
        self.infoLayout_3 = QGridLayout(self.layoutWidget_3)
        self.infoLayout_3.setObjectName(u"infoLayout_3")
        self.infoLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName_3 = QLabel(self.layoutWidget_3)
        self.labelAplicationName_3.setObjectName(u"labelAplicationName_3")
        self.labelAplicationName_3.setFont(font)
        self.labelAplicationName_3.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName_3.setAlignment(Qt.AlignCenter)

        self.infoLayout_3.addWidget(self.labelAplicationName_3, 0, 0, 1, 1)

        self.labelPercentageRAM = QLabel(self.layoutWidget_3)
        self.labelPercentageRAM.setObjectName(u"labelPercentageRAM")
        self.labelPercentageRAM.setFont(font)
        self.labelPercentageRAM.setStyleSheet(u"color: rgb(255, 44, 174); padding: 0px; background-color: none;")
        self.labelPercentageRAM.setAlignment(Qt.AlignCenter)
        self.labelPercentageRAM.setIndent(-1)

        self.infoLayout_3.addWidget(self.labelPercentageRAM, 1, 0, 1, 1)

        self.labelCredits_3 = QLabel(self.layoutWidget_3)
        self.labelCredits_3.setObjectName(u"labelCredits_3")
        self.labelCredits_3.setFont(font)
        self.labelCredits_3.setStyleSheet(u"color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits_3.setAlignment(Qt.AlignCenter)

        self.infoLayout_3.addWidget(self.labelCredits_3, 2, 0, 1, 1)

        self.circularBg_3.raise_()
        self.circularProgressRAM.raise_()
        self.circularContainer_3.raise_()
        self.stackedWidget_3.addWidget(self.cpu_ram_circular)

        self.horizontalLayout_7.addWidget(self.stackedWidget_3)

        self.stackedWidget_5 = QStackedWidget(self.pagesContainer)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        sizePolicy3.setHeightForWidth(self.stackedWidget_5.sizePolicy().hasHeightForWidth())
        self.stackedWidget_5.setSizePolicy(sizePolicy3)
        self.stackedWidget_5.setMaximumSize(QSize(16777123, 16777215))
        self.stackedWidget_5.setBaseSize(QSize(0, 0))
        self.stackedWidget_5.setFont(font)
        self.stackedWidget_5.setStyleSheet(u"background: transparent;")
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.login_form = QLabel(self.login_page)
        self.login_form.setObjectName(u"login_form")
        self.login_form.setGeometry(QRect(130, 40, 901, 511))
        self.login_form.setStyleSheet(u"background-color:rgba(16,30,41,255);\n"
"border-radius:10px;\n"
"\n"
"")
        self.logoW = QLabel(self.login_page)
        self.logoW.setObjectName(u"logoW")
        self.logoW.setGeometry(QRect(390, 80, 191, 121))
        self.logoW.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.logoW.setScaledContents(True)
        self.user_name = QLineEdit(self.login_page)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setGeometry(QRect(350, 260, 250, 30))
        self.user_name.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.user_password = QLineEdit(self.login_page)
        self.user_password.setObjectName(u"user_password")
        self.user_password.setGeometry(QRect(350, 330, 250, 30))
        self.user_password.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.user_password.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton(self.login_page)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(350, 400, 250, 40))
        self.login_btn.setFont(font)
        self.login_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.login_success_notification = QWidget(self.login_page)
        self.login_success_notification.setObjectName(u"login_success_notification")
        self.login_success_notification.setGeometry(QRect(330, 210, 551, 241))
        self.login_success_notification.setFont(font)
        self.login_success_notification.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_2 = QLabel(self.login_success_notification)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 30, 121, 41))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setKerning(True)
        self.label_2.setFont(font5)
        self.label_2.setScaledContents(False)
        self.login_success_ok_btn = QPushButton(self.login_success_notification)
        self.login_success_ok_btn.setObjectName(u"login_success_ok_btn")
        self.login_success_ok_btn.setGeometry(QRect(220, 150, 121, 41))
        self.login_success_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_success_ok_btn.raise_()
        self.label_2.raise_()
        self.login_fail_notification = QWidget(self.login_page)
        self.login_fail_notification.setObjectName(u"login_fail_notification")
        self.login_fail_notification.setGeometry(QRect(330, 210, 551, 241))
        self.login_fail_notification.setFont(font)
        self.login_fail_notification.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_3 = QLabel(self.login_fail_notification)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 30, 135, 18))
        self.label_3.setFont(font5)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.login_fail_message = QLabel(self.login_fail_notification)
        self.login_fail_message.setObjectName(u"login_fail_message")
        self.login_fail_message.setGeometry(QRect(150, 80, 261, 61))
        self.login_fail_message.setLayoutDirection(Qt.LeftToRight)
        self.login_fail_message.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.login_fail_message.setAlignment(Qt.AlignCenter)
        self.login_fail_ok_btn = QPushButton(self.login_fail_notification)
        self.login_fail_ok_btn.setObjectName(u"login_fail_ok_btn")
        self.login_fail_ok_btn.setGeometry(QRect(210, 160, 141, 41))
        self.login_fail_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.widget = QWidget(self.login_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(670, 270, 251, 191))
        self.widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.go_to_signup_btn = QPushButton(self.widget)
        self.go_to_signup_btn.setObjectName(u"go_to_signup_btn")
        self.go_to_signup_btn.setGeometry(QRect(50, 130, 151, 41))
        self.go_to_signup_btn.setFont(font)
        self.go_to_signup_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.go_to_signup_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 20, 131, 41))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.forget_credentials_widget = QWidget(self.login_page)
        self.forget_credentials_widget.setObjectName(u"forget_credentials_widget")
        self.forget_credentials_widget.setGeometry(QRect(310, 210, 481, 231))
        self.forget_credentials_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.forget_credentials_widget_ok_btn = QPushButton(self.forget_credentials_widget)
        self.forget_credentials_widget_ok_btn.setObjectName(u"forget_credentials_widget_ok_btn")
        self.forget_credentials_widget_ok_btn.setGeometry(QRect(70, 170, 151, 41))
        self.forget_credentials_widget_ok_btn.setFont(font)
        self.forget_credentials_widget_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.forget_credentials_widget_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_9 = QLabel(self.forget_credentials_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(140, 20, 201, 41))
        self.label_9.setAlignment(Qt.AlignCenter)
        self.forget_credentials_widget_cancel_btn = QPushButton(self.forget_credentials_widget)
        self.forget_credentials_widget_cancel_btn.setObjectName(u"forget_credentials_widget_cancel_btn")
        self.forget_credentials_widget_cancel_btn.setGeometry(QRect(250, 170, 151, 41))
        self.forget_credentials_widget_cancel_btn.setFont(font)
        self.forget_credentials_widget_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.forget_credentials_widget_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.recovery_email = QLineEdit(self.forget_credentials_widget)
        self.recovery_email.setObjectName(u"recovery_email")
        self.recovery_email.setGeometry(QRect(110, 80, 250, 30))
        self.recovery_email.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.recovery_email_error = QLabel(self.forget_credentials_widget)
        self.recovery_email_error.setObjectName(u"recovery_email_error")
        self.recovery_email_error.setGeometry(QRect(110, 120, 231, 41))
        self.recovery_email_error.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.recovery_email_error.setAlignment(Qt.AlignCenter)
        self.recovery_email_error.setWordWrap(True)
        self.recovery_email_error.raise_()
        self.forget_credentials_widget_ok_btn.raise_()
        self.label_9.raise_()
        self.forget_credentials_widget_cancel_btn.raise_()
        self.recovery_email.raise_()
        self.recovery_message_widget = QWidget(self.login_page)
        self.recovery_message_widget.setObjectName(u"recovery_message_widget")
        self.recovery_message_widget.setGeometry(QRect(280, 220, 481, 191))
        self.recovery_message_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.recovery_message_widget_ok_btn = QPushButton(self.recovery_message_widget)
        self.recovery_message_widget_ok_btn.setObjectName(u"recovery_message_widget_ok_btn")
        self.recovery_message_widget_ok_btn.setGeometry(QRect(160, 120, 151, 41))
        self.recovery_message_widget_ok_btn.setFont(font)
        self.recovery_message_widget_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.recovery_message_widget_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_10 = QLabel(self.recovery_message_widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 30, 381, 71))
        self.label_10.setAlignment(Qt.AlignCenter)
        self.new_password_widget = QWidget(self.login_page)
        self.new_password_widget.setObjectName(u"new_password_widget")
        self.new_password_widget.setGeometry(QRect(300, 60, 511, 341))
        self.new_password_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.new_password_widget_ok_btn = QPushButton(self.new_password_widget)
        self.new_password_widget_ok_btn.setObjectName(u"new_password_widget_ok_btn")
        self.new_password_widget_ok_btn.setGeometry(QRect(80, 270, 151, 41))
        self.new_password_widget_ok_btn.setFont(font)
        self.new_password_widget_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_password_widget_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_11 = QLabel(self.new_password_widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(140, 20, 201, 41))
        self.label_11.setAlignment(Qt.AlignCenter)
        self.new_password_widget_cancel_btn = QPushButton(self.new_password_widget)
        self.new_password_widget_cancel_btn.setObjectName(u"new_password_widget_cancel_btn")
        self.new_password_widget_cancel_btn.setGeometry(QRect(290, 270, 151, 41))
        self.new_password_widget_cancel_btn.setFont(font)
        self.new_password_widget_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_password_widget_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.new_password = QLineEdit(self.new_password_widget)
        self.new_password.setObjectName(u"new_password")
        self.new_password.setGeometry(QRect(110, 90, 250, 30))
        self.new_password.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.new_password.setEchoMode(QLineEdit.Password)
        self.new_password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.confirm_new_password = QLineEdit(self.new_password_widget)
        self.confirm_new_password.setObjectName(u"confirm_new_password")
        self.confirm_new_password.setGeometry(QRect(110, 180, 250, 30))
        self.confirm_new_password.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.confirm_new_password.setEchoMode(QLineEdit.Password)
        self.new_password_error = QLabel(self.new_password_widget)
        self.new_password_error.setObjectName(u"new_password_error")
        self.new_password_error.setGeometry(QRect(80, 120, 301, 61))
        self.new_password_error.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.new_password_error.setAlignment(Qt.AlignCenter)
        self.new_password_error.setWordWrap(True)
        self.new_password_confirm_error = QLabel(self.new_password_widget)
        self.new_password_confirm_error.setObjectName(u"new_password_confirm_error")
        self.new_password_confirm_error.setGeometry(QRect(120, 220, 231, 41))
        self.new_password_confirm_error.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.new_password_confirm_error.setAlignment(Qt.AlignCenter)
        self.new_password_confirm_error.setWordWrap(True)
        self.new_password_error.raise_()
        self.new_password_widget_ok_btn.raise_()
        self.label_11.raise_()
        self.new_password_widget_cancel_btn.raise_()
        self.new_password.raise_()
        self.confirm_new_password.raise_()
        self.new_password_confirm_error.raise_()
        self.forget_pass_name_btn = QPushButton(self.login_page)
        self.forget_pass_name_btn.setObjectName(u"forget_pass_name_btn")
        self.forget_pass_name_btn.setGeometry(QRect(320, 470, 301, 31))
        self.forget_pass_name_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.forget_pass_name_btn.setStyleSheet(u"color:rgb(23, 201, 255);")
        self.new_credentials_success = QWidget(self.login_page)
        self.new_credentials_success.setObjectName(u"new_credentials_success")
        self.new_credentials_success.setGeometry(QRect(250, 150, 551, 241))
        self.new_credentials_success.setFont(font)
        self.new_credentials_success.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_13 = QLabel(self.new_credentials_success)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(220, 20, 131, 41))
        self.label_13.setFont(font5)
        self.label_13.setScaledContents(False)
        self.new_credentials_ok_btn = QPushButton(self.new_credentials_success)
        self.new_credentials_ok_btn.setObjectName(u"new_credentials_ok_btn")
        self.new_credentials_ok_btn.setGeometry(QRect(220, 170, 121, 41))
        self.new_credentials_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_14 = QLabel(self.new_credentials_success)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(170, 90, 81, 16))
        self.label_15 = QLabel(self.new_credentials_success)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(170, 130, 81, 16))
        self.new_uname = QLabel(self.new_credentials_success)
        self.new_uname.setObjectName(u"new_uname")
        self.new_uname.setGeometry(QRect(270, 90, 121, 16))
        self.new_uname.setStyleSheet(u"color:rgb(47, 154, 255)")
        self.new_uname.setAlignment(Qt.AlignCenter)
        self.new_upass = QLabel(self.new_credentials_success)
        self.new_upass.setObjectName(u"new_upass")
        self.new_upass.setGeometry(QRect(270, 130, 121, 16))
        self.new_upass.setStyleSheet(u"color:rgb(47, 154, 255)")
        self.new_upass.setAlignment(Qt.AlignCenter)
        self.stackedWidget_5.addWidget(self.login_page)
        self.forget_credentials_widget.raise_()
        self.login_fail_notification.raise_()
        self.recovery_message_widget.raise_()
        self.new_password_widget.raise_()
        self.new_credentials_success.raise_()
        self.login_success_notification.raise_()
        self.login_form.raise_()
        self.logoW.raise_()
        self.user_name.raise_()
        self.user_password.raise_()
        self.widget.raise_()
        self.login_btn.raise_()
        self.forget_pass_name_btn.raise_()
        self.signup_page = QWidget()
        self.signup_page.setObjectName(u"signup_page")
        self.signup_form = QLabel(self.signup_page)
        self.signup_form.setObjectName(u"signup_form")
        self.signup_form.setGeometry(QRect(90, 40, 901, 511))
        self.signup_form.setStyleSheet(u"background-color:rgba(16,30,41,255);\n"
"border-radius:10px;\n"
"\n"
"")
        self.signup_user_password = QLineEdit(self.signup_page)
        self.signup_user_password.setObjectName(u"signup_user_password")
        self.signup_user_password.setGeometry(QRect(180, 380, 250, 30))
        self.signup_user_password.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.signup_user_password.setEchoMode(QLineEdit.Password)
        self.signup_btn = QPushButton(self.signup_page)
        self.signup_btn.setObjectName(u"signup_btn")
        self.signup_btn.setGeometry(QRect(690, 470, 250, 40))
        self.signup_btn.setFont(font)
        self.signup_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.signup_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.widget_2 = QWidget(self.signup_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(690, 80, 251, 131))
        self.widget_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.go_to_login_btn = QPushButton(self.widget_2)
        self.go_to_login_btn.setObjectName(u"go_to_login_btn")
        self.go_to_login_btn.setGeometry(QRect(50, 70, 151, 41))
        self.go_to_login_btn.setFont(font)
        self.go_to_login_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.go_to_login_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 10, 131, 41))
        self.label_5.setAlignment(Qt.AlignCenter)
        self.signup_user_name = QLineEdit(self.signup_page)
        self.signup_user_name.setObjectName(u"signup_user_name")
        self.signup_user_name.setGeometry(QRect(180, 240, 250, 30))
        self.signup_user_name.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.logoW_2 = QLabel(self.signup_page)
        self.logoW_2.setObjectName(u"logoW_2")
        self.logoW_2.setGeometry(QRect(290, 80, 191, 121))
        self.logoW_2.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.logoW_2.setScaledContents(True)
        self.signup_user_email = QLineEdit(self.signup_page)
        self.signup_user_email.setObjectName(u"signup_user_email")
        self.signup_user_email.setGeometry(QRect(180, 310, 250, 30))
        self.signup_user_email.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.signup_confirm_password = QLineEdit(self.signup_page)
        self.signup_confirm_password.setObjectName(u"signup_confirm_password")
        self.signup_confirm_password.setGeometry(QRect(180, 460, 250, 30))
        self.signup_confirm_password.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.signup_confirm_password.setEchoMode(QLineEdit.Password)
        self.username_error = QLabel(self.signup_page)
        self.username_error.setObjectName(u"username_error")
        self.username_error.setGeometry(QRect(450, 240, 241, 41))
        self.username_error.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.username_error.setAlignment(Qt.AlignCenter)
        self.username_error.setWordWrap(True)
        self.email_error = QLabel(self.signup_page)
        self.email_error.setObjectName(u"email_error")
        self.email_error.setGeometry(QRect(450, 310, 231, 41))
        self.email_error.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.email_error.setAlignment(Qt.AlignCenter)
        self.email_error.setWordWrap(True)
        self.password_error = QLabel(self.signup_page)
        self.password_error.setObjectName(u"password_error")
        self.password_error.setGeometry(QRect(450, 380, 231, 61))
        self.password_error.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.password_error.setAlignment(Qt.AlignCenter)
        self.password_error.setWordWrap(True)
        self.password_confirm_error = QLabel(self.signup_page)
        self.password_confirm_error.setObjectName(u"password_confirm_error")
        self.password_confirm_error.setGeometry(QRect(450, 460, 231, 41))
        self.password_confirm_error.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.password_confirm_error.setAlignment(Qt.AlignCenter)
        self.password_confirm_error.setWordWrap(True)
        self.username_already_exists_error = QLabel(self.signup_page)
        self.username_already_exists_error.setObjectName(u"username_already_exists_error")
        self.username_already_exists_error.setGeometry(QRect(440, 250, 241, 41))
        self.username_already_exists_error.setStyleSheet(u"color:rgb(47, 154, 255)")
        self.username_already_exists_error.setAlignment(Qt.AlignCenter)
        self.username_already_exists_error.setWordWrap(True)
        self.signup_success_notification = QWidget(self.signup_page)
        self.signup_success_notification.setObjectName(u"signup_success_notification")
        self.signup_success_notification.setGeometry(QRect(250, 220, 551, 241))
        self.signup_success_notification.setFont(font)
        self.signup_success_notification.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_6 = QLabel(self.signup_success_notification)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(220, 20, 131, 41))
        self.label_6.setFont(font5)
        self.label_6.setScaledContents(False)
        self.signup_success_ok_btn = QPushButton(self.signup_success_notification)
        self.signup_success_ok_btn.setObjectName(u"signup_success_ok_btn")
        self.signup_success_ok_btn.setGeometry(QRect(220, 170, 121, 41))
        self.signup_success_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_7 = QLabel(self.signup_success_notification)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 90, 81, 16))
        self.label_8 = QLabel(self.signup_success_notification)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(170, 130, 81, 16))
        self.notify_signup_uname = QLabel(self.signup_success_notification)
        self.notify_signup_uname.setObjectName(u"notify_signup_uname")
        self.notify_signup_uname.setGeometry(QRect(270, 90, 121, 16))
        self.notify_signup_uname.setStyleSheet(u"color:rgb(47, 154, 255)")
        self.notify_signup_uname.setAlignment(Qt.AlignCenter)
        self.notify_signup_upass = QLabel(self.signup_success_notification)
        self.notify_signup_upass.setObjectName(u"notify_signup_upass")
        self.notify_signup_upass.setGeometry(QRect(270, 130, 121, 16))
        self.notify_signup_upass.setStyleSheet(u"color:rgb(47, 154, 255)")
        self.notify_signup_upass.setAlignment(Qt.AlignCenter)
        self.widget_3 = QWidget(self.signup_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(690, 250, 251, 181))
        self.widget_3.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.upload_profile_pic_btn = QPushButton(self.widget_3)
        self.upload_profile_pic_btn.setObjectName(u"upload_profile_pic_btn")
        self.upload_profile_pic_btn.setGeometry(QRect(50, 120, 151, 41))
        self.upload_profile_pic_btn.setFont(font)
        self.upload_profile_pic_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.upload_profile_pic_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.profile_image = QLabel(self.widget_3)
        self.profile_image.setObjectName(u"profile_image")
        self.profile_image.setGeometry(QRect(80, 20, 91, 81))
        self.profile_image.setPixmap(QPixmap(u":/images/images/images/profile_pic.png"))
        self.profile_image.setScaledContents(True)
        self.profile_image.setAlignment(Qt.AlignCenter)
        self.stackedWidget_5.addWidget(self.signup_page)
        self.signup_success_notification.raise_()
        self.username_already_exists_error.raise_()
        self.password_confirm_error.raise_()
        self.password_error.raise_()
        self.email_error.raise_()
        self.username_error.raise_()
        self.signup_form.raise_()
        self.signup_user_password.raise_()
        self.signup_btn.raise_()
        self.widget_2.raise_()
        self.signup_user_name.raise_()
        self.logoW_2.raise_()
        self.signup_user_email.raise_()
        self.signup_confirm_password.raise_()
        self.widget_3.raise_()
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.profile_page.setStyleSheet(u"background-position: center;\n"
"background-repeat: no-repeat;")
        self.acc_not_verify_widget = QWidget(self.profile_page)
        self.acc_not_verify_widget.setObjectName(u"acc_not_verify_widget")
        self.acc_not_verify_widget.setGeometry(QRect(50, 10, 721, 91))
        self.acc_not_verify_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;")
        self.verify_email_btn = QPushButton(self.acc_not_verify_widget)
        self.verify_email_btn.setObjectName(u"verify_email_btn")
        self.verify_email_btn.setGeometry(QRect(510, 30, 151, 41))
        self.verify_email_btn.setFont(font)
        self.verify_email_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.verify_email_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status = QLabel(self.acc_not_verify_widget)
        self.account_verify_status.setObjectName(u"account_verify_status")
        self.account_verify_status.setGeometry(QRect(20, 20, 221, 41))
        self.account_verify_status.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status.setAlignment(Qt.AlignCenter)
        self.home_dashboard = QLabel(self.profile_page)
        self.home_dashboard.setObjectName(u"home_dashboard")
        self.home_dashboard.setGeometry(QRect(40, 110, 901, 481))
        self.home_dashboard.setStyleSheet(u"background-color:rgba(16,30,41,255);\n"
"border-radius:10px;\n"
"\n"
"")
        self.profile_view_widget = QWidget(self.profile_page)
        self.profile_view_widget.setObjectName(u"profile_view_widget")
        self.profile_view_widget.setGeometry(QRect(90, 150, 651, 401))
        self.profile_view_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;")
        self.profile_pic_change_btn = QPushButton(self.profile_view_widget)
        self.profile_pic_change_btn.setObjectName(u"profile_pic_change_btn")
        self.profile_pic_change_btn.setGeometry(QRect(50, 240, 151, 41))
        self.profile_pic_change_btn.setFont(font)
        self.profile_pic_change_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile_pic_change_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.profile_view_user_name = QLabel(self.profile_view_widget)
        self.profile_view_user_name.setObjectName(u"profile_view_user_name")
        self.profile_view_user_name.setGeometry(QRect(380, 100, 221, 41))
        self.profile_view_email = QLabel(self.profile_view_widget)
        self.profile_view_email.setObjectName(u"profile_view_email")
        self.profile_view_email.setGeometry(QRect(380, 160, 231, 51))
        self.profile_view_pic = QLabel(self.profile_view_widget)
        self.profile_view_pic.setObjectName(u"profile_view_pic")
        self.profile_view_pic.setGeometry(QRect(50, 60, 150, 150))
        self.profile_view_pic.setStyleSheet(u"border-bottom-color: rgb(255, 255, 255);")
        self.profile_view_pic.setPixmap(QPixmap(u":/images/images/images/profile_pic.png"))
        self.profile_view_pic.setScaledContents(True)
        self.deactivate_account_btn = QPushButton(self.profile_view_widget)
        self.deactivate_account_btn.setObjectName(u"deactivate_account_btn")
        self.deactivate_account_btn.setGeometry(QRect(470, 310, 151, 41))
        self.deactivate_account_btn.setFont(font)
        self.deactivate_account_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deactivate_account_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.profile_pic_remove_btn = QPushButton(self.profile_view_widget)
        self.profile_pic_remove_btn.setObjectName(u"profile_pic_remove_btn")
        self.profile_pic_remove_btn.setGeometry(QRect(50, 310, 151, 41))
        self.profile_pic_remove_btn.setFont(font)
        self.profile_pic_remove_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile_pic_remove_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_17 = QLabel(self.profile_view_widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(260, 100, 91, 41))
        self.label_18 = QLabel(self.profile_view_widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(260, 170, 91, 31))
        self.signout_btn = QPushButton(self.profile_view_widget)
        self.signout_btn.setObjectName(u"signout_btn")
        self.signout_btn.setGeometry(QRect(480, 20, 151, 41))
        self.signout_btn.setFont(font)
        self.signout_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.signout_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_stat = QLabel(self.profile_view_widget)
        self.account_verify_stat.setObjectName(u"account_verify_stat")
        self.account_verify_stat.setEnabled(True)
        self.account_verify_stat.setGeometry(QRect(230, 310, 221, 41))
        self.account_verify_stat.setStyleSheet(u"color:rgb(255, 0, 0)")
        self.account_verify_stat.setAlignment(Qt.AlignCenter)
        self.deactivate_account_confirm_widget = QWidget(self.profile_page)
        self.deactivate_account_confirm_widget.setObjectName(u"deactivate_account_confirm_widget")
        self.deactivate_account_confirm_widget.setGeometry(QRect(180, 80, 451, 241))
        self.deactivate_account_confirm_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.deactivate_account_confirm_ok_btn = QPushButton(self.deactivate_account_confirm_widget)
        self.deactivate_account_confirm_ok_btn.setObjectName(u"deactivate_account_confirm_ok_btn")
        self.deactivate_account_confirm_ok_btn.setGeometry(QRect(40, 150, 151, 41))
        self.deactivate_account_confirm_ok_btn.setFont(font)
        self.deactivate_account_confirm_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deactivate_account_confirm_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_12 = QLabel(self.deactivate_account_confirm_widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(80, 30, 301, 41))
        self.label_12.setAlignment(Qt.AlignCenter)
        self.deactivate_account_confirm_cancel_btn = QPushButton(self.deactivate_account_confirm_widget)
        self.deactivate_account_confirm_cancel_btn.setObjectName(u"deactivate_account_confirm_cancel_btn")
        self.deactivate_account_confirm_cancel_btn.setGeometry(QRect(270, 150, 151, 41))
        self.deactivate_account_confirm_cancel_btn.setFont(font)
        self.deactivate_account_confirm_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deactivate_account_confirm_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_3 = QLabel(self.deactivate_account_confirm_widget)
        self.account_verify_status_3.setObjectName(u"account_verify_status_3")
        self.account_verify_status_3.setGeometry(QRect(80, 80, 291, 41))
        self.account_verify_status_3.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status_3.setAlignment(Qt.AlignCenter)
        self.verify_message_widget = QWidget(self.profile_page)
        self.verify_message_widget.setObjectName(u"verify_message_widget")
        self.verify_message_widget.setGeometry(QRect(170, -10, 481, 191))
        self.verify_message_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.verify_message_widget_ok_btn = QPushButton(self.verify_message_widget)
        self.verify_message_widget_ok_btn.setObjectName(u"verify_message_widget_ok_btn")
        self.verify_message_widget_ok_btn.setGeometry(QRect(160, 120, 151, 41))
        self.verify_message_widget_ok_btn.setFont(font)
        self.verify_message_widget_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.verify_message_widget_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_16 = QLabel(self.verify_message_widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(50, 30, 381, 71))
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.raise_()
        self.verify_message_widget_ok_btn.raise_()
        self.acc_verify_done_widget = QWidget(self.profile_page)
        self.acc_verify_done_widget.setObjectName(u"acc_verify_done_widget")
        self.acc_verify_done_widget.setGeometry(QRect(50, 0, 721, 91))
        self.acc_verify_done_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;")
        self.acc_verify_done_btn = QPushButton(self.acc_verify_done_widget)
        self.acc_verify_done_btn.setObjectName(u"acc_verify_done_btn")
        self.acc_verify_done_btn.setGeometry(QRect(520, 30, 151, 41))
        self.acc_verify_done_btn.setFont(font)
        self.acc_verify_done_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.acc_verify_done_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_2 = QLabel(self.acc_verify_done_widget)
        self.account_verify_status_2.setObjectName(u"account_verify_status_2")
        self.account_verify_status_2.setGeometry(QRect(70, 20, 221, 41))
        self.account_verify_status_2.setStyleSheet(u"color:rgb(55, 250, 68)")
        self.account_verify_status_2.setAlignment(Qt.AlignCenter)
        self.account_verify_status_2.raise_()
        self.acc_verify_done_btn.raise_()
        self.stackedWidget_5.addWidget(self.profile_page)
        self.verify_message_widget.raise_()
        self.acc_verify_done_widget.raise_()
        self.deactivate_account_confirm_widget.raise_()
        self.home_dashboard.raise_()
        self.acc_not_verify_widget.raise_()
        self.profile_view_widget.raise_()
        self.content_page = QWidget()
        self.content_page.setObjectName(u"content_page")
        self.stackedWidget_content_pages = QStackedWidget(self.content_page)
        self.stackedWidget_content_pages.setObjectName(u"stackedWidget_content_pages")
        self.stackedWidget_content_pages.setGeometry(QRect(30, 160, 731, 431))
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.recent_activity_widget = QWidget(self.dashboard_page)
        self.recent_activity_widget.setObjectName(u"recent_activity_widget")
        self.recent_activity_widget.setGeometry(QRect(20, 10, 691, 201))
        self.recent_activity_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_21 = QLabel(self.recent_activity_widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(30, 20, 91, 16))
        self.label_21.setAlignment(Qt.AlignCenter)
        self.tableWidget_recent_activity = QTableWidget(self.recent_activity_widget)
        if (self.tableWidget_recent_activity.columnCount() < 4):
            self.tableWidget_recent_activity.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableWidget_recent_activity.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableWidget_recent_activity.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableWidget_recent_activity.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableWidget_recent_activity.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_recent_activity.setObjectName(u"tableWidget_recent_activity")
        self.tableWidget_recent_activity.setGeometry(QRect(40, 40, 631, 141))
        self.tableWidget_recent_activity.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_recent_activity.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_recent_activity.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_recent_activity.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_recent_activity.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_recent_activity.horizontalHeader().setMinimumSectionSize(48)
        self.tableWidget_recent_activity.horizontalHeader().setDefaultSectionSize(170)
        self.clear_recent_history_btn = QPushButton(self.recent_activity_widget)
        self.clear_recent_history_btn.setObjectName(u"clear_recent_history_btn")
        self.clear_recent_history_btn.setGeometry(QRect(580, 20, 91, 24))
        self.clear_recent_history_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_recent_history_btn.setLayoutDirection(Qt.LeftToRight)
        self.no_recent = QLabel(self.recent_activity_widget)
        self.no_recent.setObjectName(u"no_recent")
        self.no_recent.setGeometry(QRect(50, 50, 611, 131))
        self.no_recent.setAlignment(Qt.AlignCenter)
        self.no_recent.raise_()
        self.label_21.raise_()
        self.tableWidget_recent_activity.raise_()
        self.clear_recent_history_btn.raise_()
        self.clear_fav_history_confirm_widget = QWidget(self.dashboard_page)
        self.clear_fav_history_confirm_widget.setObjectName(u"clear_fav_history_confirm_widget")
        self.clear_fav_history_confirm_widget.setGeometry(QRect(170, 90, 451, 241))
        self.clear_fav_history_confirm_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.clear_fav_history_confirm_ok_btn = QPushButton(self.clear_fav_history_confirm_widget)
        self.clear_fav_history_confirm_ok_btn.setObjectName(u"clear_fav_history_confirm_ok_btn")
        self.clear_fav_history_confirm_ok_btn.setGeometry(QRect(40, 150, 151, 41))
        self.clear_fav_history_confirm_ok_btn.setFont(font)
        self.clear_fav_history_confirm_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_fav_history_confirm_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_26 = QLabel(self.clear_fav_history_confirm_widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(80, 30, 301, 41))
        self.label_26.setAlignment(Qt.AlignCenter)
        self.clear_fav_history_confirm_cancel_btn = QPushButton(self.clear_fav_history_confirm_widget)
        self.clear_fav_history_confirm_cancel_btn.setObjectName(u"clear_fav_history_confirm_cancel_btn")
        self.clear_fav_history_confirm_cancel_btn.setGeometry(QRect(270, 150, 151, 41))
        self.clear_fav_history_confirm_cancel_btn.setFont(font)
        self.clear_fav_history_confirm_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_fav_history_confirm_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_7 = QLabel(self.clear_fav_history_confirm_widget)
        self.account_verify_status_7.setObjectName(u"account_verify_status_7")
        self.account_verify_status_7.setGeometry(QRect(80, 80, 291, 41))
        self.account_verify_status_7.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status_7.setAlignment(Qt.AlignCenter)
        self.my_favourites_widget = QWidget(self.dashboard_page)
        self.my_favourites_widget.setObjectName(u"my_favourites_widget")
        self.my_favourites_widget.setGeometry(QRect(20, 230, 691, 201))
        self.my_favourites_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_22 = QLabel(self.my_favourites_widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(30, 20, 91, 16))
        self.label_22.setAlignment(Qt.AlignCenter)
        self.tableWidget_my_favourites = QTableWidget(self.my_favourites_widget)
        if (self.tableWidget_my_favourites.columnCount() < 3):
            self.tableWidget_my_favourites.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_my_favourites.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_my_favourites.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_my_favourites.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidget_my_favourites.setObjectName(u"tableWidget_my_favourites")
        self.tableWidget_my_favourites.setGeometry(QRect(40, 40, 611, 151))
        self.tableWidget_my_favourites.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tableWidget_my_favourites.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_my_favourites.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.tableWidget_my_favourites.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_my_favourites.horizontalHeader().setMinimumSectionSize(48)
        self.tableWidget_my_favourites.horizontalHeader().setDefaultSectionSize(147)
        self.no_favourites = QLabel(self.my_favourites_widget)
        self.no_favourites.setObjectName(u"no_favourites")
        self.no_favourites.setGeometry(QRect(50, 50, 601, 141))
        self.no_favourites.setAlignment(Qt.AlignCenter)
        self.clear_myfavourites_history_btn = QPushButton(self.my_favourites_widget)
        self.clear_myfavourites_history_btn.setObjectName(u"clear_myfavourites_history_btn")
        self.clear_myfavourites_history_btn.setGeometry(QRect(590, 20, 91, 24))
        self.clear_myfavourites_history_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_myfavourites_history_btn.setLayoutDirection(Qt.LeftToRight)
        self.open_favourite_btn = QPushButton(self.my_favourites_widget)
        self.open_favourite_btn.setObjectName(u"open_favourite_btn")
        self.open_favourite_btn.setGeometry(QRect(360, 20, 181, 24))
        self.open_favourite_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_favourite_btn.setLayoutDirection(Qt.LeftToRight)
        self.no_favourites.raise_()
        self.label_22.raise_()
        self.tableWidget_my_favourites.raise_()
        self.clear_myfavourites_history_btn.raise_()
        self.open_favourite_btn.raise_()
        self.clear_history_confirm_widget = QWidget(self.dashboard_page)
        self.clear_history_confirm_widget.setObjectName(u"clear_history_confirm_widget")
        self.clear_history_confirm_widget.setGeometry(QRect(130, 90, 451, 241))
        self.clear_history_confirm_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.clear_history_confirm_ok_btn = QPushButton(self.clear_history_confirm_widget)
        self.clear_history_confirm_ok_btn.setObjectName(u"clear_history_confirm_ok_btn")
        self.clear_history_confirm_ok_btn.setGeometry(QRect(40, 150, 151, 41))
        self.clear_history_confirm_ok_btn.setFont(font)
        self.clear_history_confirm_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_history_confirm_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_25 = QLabel(self.clear_history_confirm_widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(80, 30, 301, 41))
        self.label_25.setAlignment(Qt.AlignCenter)
        self.clear_history_confirm_cancel_btn = QPushButton(self.clear_history_confirm_widget)
        self.clear_history_confirm_cancel_btn.setObjectName(u"clear_history_confirm_cancel_btn")
        self.clear_history_confirm_cancel_btn.setGeometry(QRect(270, 150, 151, 41))
        self.clear_history_confirm_cancel_btn.setFont(font)
        self.clear_history_confirm_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_history_confirm_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_6 = QLabel(self.clear_history_confirm_widget)
        self.account_verify_status_6.setObjectName(u"account_verify_status_6")
        self.account_verify_status_6.setGeometry(QRect(80, 80, 291, 41))
        self.account_verify_status_6.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status_6.setAlignment(Qt.AlignCenter)
        self.account_verify_status_6.raise_()
        self.clear_history_confirm_ok_btn.raise_()
        self.label_25.raise_()
        self.clear_history_confirm_cancel_btn.raise_()
        self.stackedWidget_content_pages.addWidget(self.dashboard_page)
        self.clear_history_confirm_widget.raise_()
        self.clear_fav_history_confirm_widget.raise_()
        self.my_favourites_widget.raise_()
        self.recent_activity_widget.raise_()
        self.usage_graph_page = QWidget()
        self.usage_graph_page.setObjectName(u"usage_graph_page")
        self.cpu_usage_widget_7 = QWidget(self.usage_graph_page)
        self.cpu_usage_widget_7.setObjectName(u"cpu_usage_widget_7")
        self.cpu_usage_widget_7.setGeometry(QRect(10, 10, 711, 411))
        self.cpu_usage_widget_7.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.gridLayoutWidget = QWidget(self.cpu_usage_widget_7)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 90, 691, 281))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_99 = QLabel(self.cpu_usage_widget_7)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(30, 30, 181, 31))
        self.label_99.setAlignment(Qt.AlignCenter)
        self.show_ram_graph_btn = QPushButton(self.cpu_usage_widget_7)
        self.show_ram_graph_btn.setObjectName(u"show_ram_graph_btn")
        self.show_ram_graph_btn.setGeometry(QRect(570, 30, 113, 32))
        self.show_ram_graph_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_ram_graph_btn.setStyleSheet(u"background-color: rgb(255, 44, 174);\n"
"color: white;")
        self.show_cpu_graph_btn = QPushButton(self.cpu_usage_widget_7)
        self.show_cpu_graph_btn.setObjectName(u"show_cpu_graph_btn")
        self.show_cpu_graph_btn.setGeometry(QRect(420, 30, 113, 32))
        self.show_cpu_graph_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_cpu_graph_btn.setStyleSheet(u"background-color: rgba(85, 170, 255, 255);\n"
"color: white;")
        self.show_circular_percent_btn = QPushButton(self.cpu_usage_widget_7)
        self.show_circular_percent_btn.setObjectName(u"show_circular_percent_btn")
        self.show_circular_percent_btn.setGeometry(QRect(260, 30, 113, 32))
        self.show_circular_percent_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_circular_percent_btn.setStyleSheet(u"background-color: rgb(150, 2, 255);\n"
"color: white;")
        self.stackedWidget_content_pages.addWidget(self.usage_graph_page)
        self.sendfeedbackpage = QWidget()
        self.sendfeedbackpage.setObjectName(u"sendfeedbackpage")
        self.feedback_widget = QWidget(self.sendfeedbackpage)
        self.feedback_widget.setObjectName(u"feedback_widget")
        self.feedback_widget.setGeometry(QRect(10, 10, 661, 411))
        self.feedback_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_23 = QLabel(self.feedback_widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 20, 91, 16))
        self.label_23.setAlignment(Qt.AlignCenter)
        self.send_feedback_btn = QPushButton(self.feedback_widget)
        self.send_feedback_btn.setObjectName(u"send_feedback_btn")
        self.send_feedback_btn.setGeometry(QRect(260, 330, 181, 51))
        self.send_feedback_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirm_feedback_widget = QWidget(self.feedback_widget)
        self.confirm_feedback_widget.setObjectName(u"confirm_feedback_widget")
        self.confirm_feedback_widget.setGeometry(QRect(140, 130, 451, 191))
        self.confirm_feedback_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.confirm_feedback_widget_ok_btn = QPushButton(self.confirm_feedback_widget)
        self.confirm_feedback_widget_ok_btn.setObjectName(u"confirm_feedback_widget_ok_btn")
        self.confirm_feedback_widget_ok_btn.setGeometry(QRect(40, 110, 151, 41))
        self.confirm_feedback_widget_ok_btn.setFont(font)
        self.confirm_feedback_widget_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_28 = QLabel(self.confirm_feedback_widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(80, 30, 301, 41))
        self.label_28.setAlignment(Qt.AlignCenter)
        self.confirm_feedback_widget_cancel_btn = QPushButton(self.confirm_feedback_widget)
        self.confirm_feedback_widget_cancel_btn.setObjectName(u"confirm_feedback_widget_cancel_btn")
        self.confirm_feedback_widget_cancel_btn.setGeometry(QRect(260, 110, 151, 41))
        self.confirm_feedback_widget_cancel_btn.setFont(font)
        self.confirm_feedback_widget_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_28.raise_()
        self.confirm_feedback_widget_ok_btn.raise_()
        self.confirm_feedback_widget_cancel_btn.raise_()
        self.feedback = QLineEdit(self.feedback_widget)
        self.feedback.setObjectName(u"feedback")
        self.feedback.setGeometry(QRect(70, 70, 551, 241))
        self.feedback.setCursor(QCursor(Qt.IBeamCursor))
        self.feedback.setStyleSheet(u"background-color:rgb(0, 66, 97);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px;\n"
"padding-top:10px;\n"
"padding-left:10px;\n"
"padding-right:10px\n"
"")
        self.feedback.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.feedback_sent_notification = QWidget(self.feedback_widget)
        self.feedback_sent_notification.setObjectName(u"feedback_sent_notification")
        self.feedback_sent_notification.setGeometry(QRect(140, 50, 431, 181))
        self.feedback_sent_notification.setFont(font)
        self.feedback_sent_notification.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.feedback_success_msg = QLabel(self.feedback_sent_notification)
        self.feedback_success_msg.setObjectName(u"feedback_success_msg")
        self.feedback_success_msg.setGeometry(QRect(90, 40, 241, 41))
        self.feedback_success_msg.setFont(font5)
        self.feedback_success_msg.setScaledContents(False)
        self.feedback_sent_notification_ok_btn = QPushButton(self.feedback_sent_notification)
        self.feedback_sent_notification_ok_btn.setObjectName(u"feedback_sent_notification_ok_btn")
        self.feedback_sent_notification_ok_btn.setGeometry(QRect(150, 110, 121, 41))
        self.feedback_sent_notification.raise_()
        self.confirm_feedback_widget.raise_()
        self.label_23.raise_()
        self.send_feedback_btn.raise_()
        self.feedback.raise_()
        self.stackedWidget_content_pages.addWidget(self.sendfeedbackpage)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.about_us_widget = QWidget(self.about_page)
        self.about_us_widget.setObjectName(u"about_us_widget")
        self.about_us_widget.setGeometry(QRect(20, 10, 691, 411))
        self.about_us_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_50 = QLabel(self.about_us_widget)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(30, 20, 91, 16))
        self.label_50.setAlignment(Qt.AlignCenter)
        self.contact_us_btn = QPushButton(self.about_us_widget)
        self.contact_us_btn.setObjectName(u"contact_us_btn")
        self.contact_us_btn.setGeometry(QRect(260, 330, 181, 51))
        self.contact_us_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_41 = QLabel(self.about_us_widget)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(40, 70, 331, 231))
        self.label_41.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_41.setFrameShape(QFrame.NoFrame)
        self.label_41.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_41.setWordWrap(True)
        self.label_41.setMargin(36)
        self.label_51 = QLabel(self.about_us_widget)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(390, 70, 261, 231))
        self.label_51.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_51.setFrameShape(QFrame.NoFrame)
        self.label_51.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_51.setWordWrap(True)
        self.label_51.setMargin(36)
        self.label_52 = QLabel(self.about_us_widget)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(400, 250, 241, 31))
        self.label_52.setAlignment(Qt.AlignCenter)
        self.label_52.setWordWrap(True)
        self.label_52.setMargin(3)
        self.label_53 = QLabel(self.about_us_widget)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(440, 120, 161, 111))
        self.label_53.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_53.setScaledContents(True)
        self.label_53.setAlignment(Qt.AlignCenter)
        self.label_53.setMargin(15)
        self.stackedWidget_content_pages.addWidget(self.about_page)
        self.datasets_page = QWidget()
        self.datasets_page.setObjectName(u"datasets_page")
        self.datsets_stackedWidget = QStackedWidget(self.datasets_page)
        self.datsets_stackedWidget.setObjectName(u"datsets_stackedWidget")
        self.datsets_stackedWidget.setGeometry(QRect(-10, -10, 681, 431))
        self.create_dataset_page = QWidget()
        self.create_dataset_page.setObjectName(u"create_dataset_page")
        self.datasets_widget = QWidget(self.create_dataset_page)
        self.datasets_widget.setObjectName(u"datasets_widget")
        self.datasets_widget.setGeometry(QRect(10, 10, 661, 421))
        self.datasets_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.search_dataset = QLineEdit(self.datasets_widget)
        self.search_dataset.setObjectName(u"search_dataset")
        self.search_dataset.setGeometry(QRect(390, 20, 250, 30))
        self.search_dataset.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.dataset_found_widget = QWidget(self.datasets_widget)
        self.dataset_found_widget.setObjectName(u"dataset_found_widget")
        self.dataset_found_widget.setGeometry(QRect(50, 50, 501, 351))
        self.dataset_found_widget.setFont(font)
        self.dataset_found_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_33 = QLabel(self.dataset_found_widget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(80, 30, 101, 41))
        self.label_33.setFont(font5)
        self.label_33.setStyleSheet(u"color: rgb(170, 255, 0);")
        self.label_33.setScaledContents(False)
        self.view_searched_dst_btn = QPushButton(self.dataset_found_widget)
        self.view_searched_dst_btn.setObjectName(u"view_searched_dst_btn")
        self.view_searched_dst_btn.setGeometry(QRect(80, 240, 121, 41))
        self.view_searched_dst_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searched_dst_thumbnail_btn = QPushButton(self.dataset_found_widget)
        self.searched_dst_thumbnail_btn.setObjectName(u"searched_dst_thumbnail_btn")
        self.searched_dst_thumbnail_btn.setGeometry(QRect(60, 90, 141, 121))
        self.searched_dst_thumbnail_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searched_dst_thumbnail_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.searched_dst_thumbnail = QLabel(self.dataset_found_widget)
        self.searched_dst_thumbnail.setObjectName(u"searched_dst_thumbnail")
        self.searched_dst_thumbnail.setGeometry(QRect(60, 90, 141, 121))
        self.searched_dst_thumbnail.setCursor(QCursor(Qt.PointingHandCursor))
        self.searched_dst_thumbnail.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.searched_dst_thumbnail.setFrameShape(QFrame.NoFrame)
        self.searched_dst_thumbnail.setAlignment(Qt.AlignCenter)
        self.searched_dst_thumbnail.setWordWrap(True)
        self.searched_dst_thumbnail.setMargin(2)
        self.searched_dst_name = QLabel(self.dataset_found_widget)
        self.searched_dst_name.setObjectName(u"searched_dst_name")
        self.searched_dst_name.setGeometry(QRect(280, 80, 121, 41))
        self.searched_dst_size = QLabel(self.dataset_found_widget)
        self.searched_dst_size.setObjectName(u"searched_dst_size")
        self.searched_dst_size.setGeometry(QRect(280, 140, 121, 41))
        self.searched_dst_cancel_btn = QPushButton(self.dataset_found_widget)
        self.searched_dst_cancel_btn.setObjectName(u"searched_dst_cancel_btn")
        self.searched_dst_cancel_btn.setGeometry(QRect(280, 240, 121, 41))
        self.searched_dst_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searched_dst_size.raise_()
        self.label_33.raise_()
        self.view_searched_dst_btn.raise_()
        self.searched_dst_thumbnail.raise_()
        self.searched_dst_name.raise_()
        self.searched_dst_cancel_btn.raise_()
        self.searched_dst_thumbnail_btn.raise_()
        self.available_datasets_widget = QWidget(self.datasets_widget)
        self.available_datasets_widget.setObjectName(u"available_datasets_widget")
        self.available_datasets_widget.setGeometry(QRect(0, 60, 661, 361))
        self.available_datasets_widget.setFont(font)
        self.available_datasets_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.create_new_dataset_btn = QPushButton(self.available_datasets_widget)
        self.create_new_dataset_btn.setObjectName(u"create_new_dataset_btn")
        self.create_new_dataset_btn.setGeometry(QRect(390, 60, 151, 121))
        self.create_new_dataset_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_new_dataset_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_63 = QLabel(self.available_datasets_widget)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(240, 10, 71, 41))
        self.label_61 = QLabel(self.available_datasets_widget)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(60, 10, 71, 41))
        self.anime_thumbnail_btn = QPushButton(self.available_datasets_widget)
        self.anime_thumbnail_btn.setObjectName(u"anime_thumbnail_btn")
        self.anime_thumbnail_btn.setGeometry(QRect(50, 60, 141, 121))
        self.anime_thumbnail_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.anime_thumbnail_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.human_thumbnail_btn = QPushButton(self.available_datasets_widget)
        self.human_thumbnail_btn.setObjectName(u"human_thumbnail_btn")
        self.human_thumbnail_btn.setGeometry(QRect(210, 60, 151, 121))
        self.human_thumbnail_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.human_thumbnail_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_88 = QLabel(self.available_datasets_widget)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(390, 60, 151, 121))
        self.label_88.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_88.setFrameShape(QFrame.NoFrame)
        self.label_88.setPixmap(QPixmap(u":/icons/images/icons/create_new.png"))
        self.label_88.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_88.setWordWrap(True)
        self.label_88.setMargin(10)
        self.human_thumbnail = QLabel(self.available_datasets_widget)
        self.human_thumbnail.setObjectName(u"human_thumbnail")
        self.human_thumbnail.setGeometry(QRect(210, 60, 151, 121))
        self.human_thumbnail.setCursor(QCursor(Qt.PointingHandCursor))
        self.human_thumbnail.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.human_thumbnail.setFrameShape(QFrame.NoFrame)
        self.human_thumbnail.setAlignment(Qt.AlignCenter)
        self.human_thumbnail.setWordWrap(True)
        self.human_thumbnail.setMargin(2)
        self.anime_thumbnail = QLabel(self.available_datasets_widget)
        self.anime_thumbnail.setObjectName(u"anime_thumbnail")
        self.anime_thumbnail.setGeometry(QRect(50, 60, 141, 121))
        self.anime_thumbnail.setCursor(QCursor(Qt.PointingHandCursor))
        self.anime_thumbnail.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.anime_thumbnail.setFrameShape(QFrame.NoFrame)
        self.anime_thumbnail.setAlignment(Qt.AlignCenter)
        self.anime_thumbnail.setWordWrap(True)
        self.anime_thumbnail.setMargin(2)
        self.new_datset_thumbnail_btn = QPushButton(self.available_datasets_widget)
        self.new_datset_thumbnail_btn.setObjectName(u"new_datset_thumbnail_btn")
        self.new_datset_thumbnail_btn.setGeometry(QRect(210, 230, 151, 121))
        self.new_datset_thumbnail_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_datset_thumbnail_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_87 = QLabel(self.available_datasets_widget)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(50, 190, 71, 41))
        self.flower_thumbnail_btn = QPushButton(self.available_datasets_widget)
        self.flower_thumbnail_btn.setObjectName(u"flower_thumbnail_btn")
        self.flower_thumbnail_btn.setGeometry(QRect(40, 230, 151, 121))
        self.flower_thumbnail_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.flower_thumbnail_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_new_dataset = QLabel(self.available_datasets_widget)
        self.label_new_dataset.setObjectName(u"label_new_dataset")
        self.label_new_dataset.setGeometry(QRect(230, 190, 91, 41))
        self.new_datset_thumbnail = QLabel(self.available_datasets_widget)
        self.new_datset_thumbnail.setObjectName(u"new_datset_thumbnail")
        self.new_datset_thumbnail.setGeometry(QRect(210, 230, 151, 121))
        self.new_datset_thumbnail.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_datset_thumbnail.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_datset_thumbnail.setFrameShape(QFrame.NoFrame)
        self.new_datset_thumbnail.setAlignment(Qt.AlignCenter)
        self.new_datset_thumbnail.setWordWrap(True)
        self.new_datset_thumbnail.setMargin(2)
        self.flower_thumbnail = QLabel(self.available_datasets_widget)
        self.flower_thumbnail.setObjectName(u"flower_thumbnail")
        self.flower_thumbnail.setGeometry(QRect(40, 230, 151, 121))
        self.flower_thumbnail.setCursor(QCursor(Qt.PointingHandCursor))
        self.flower_thumbnail.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.flower_thumbnail.setFrameShape(QFrame.NoFrame)
        self.flower_thumbnail.setAlignment(Qt.AlignCenter)
        self.flower_thumbnail.setWordWrap(True)
        self.flower_thumbnail.setMargin(2)
        self.label_89 = QLabel(self.available_datasets_widget)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(420, 80, 91, 41))
        self.label_89.setAlignment(Qt.AlignCenter)
        self.label_214 = QLabel(self.available_datasets_widget)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setGeometry(QRect(570, 270, 41, 31))
        self.comboBox_3 = QComboBox(self.available_datasets_widget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(550, 310, 101, 34))
        self.comboBox_3.setFont(font)
        self.comboBox_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_3.setIconSize(QSize(16, 16))
        self.comboBox_3.setFrame(True)
        self.label_88.raise_()
        self.new_datset_thumbnail.raise_()
        self.human_thumbnail.raise_()
        self.flower_thumbnail.raise_()
        self.anime_thumbnail.raise_()
        self.create_new_dataset_btn.raise_()
        self.label_63.raise_()
        self.label_61.raise_()
        self.anime_thumbnail_btn.raise_()
        self.human_thumbnail_btn.raise_()
        self.new_datset_thumbnail_btn.raise_()
        self.label_87.raise_()
        self.flower_thumbnail_btn.raise_()
        self.label_new_dataset.raise_()
        self.label_89.raise_()
        self.label_214.raise_()
        self.comboBox_3.raise_()
        self.label_55 = QLabel(self.datasets_widget)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(30, 10, 121, 41))
        self.dataset_not_found_widget = QWidget(self.datasets_widget)
        self.dataset_not_found_widget.setObjectName(u"dataset_not_found_widget")
        self.dataset_not_found_widget.setGeometry(QRect(80, 60, 501, 161))
        self.dataset_not_found_widget.setFont(font)
        self.dataset_not_found_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_34 = QLabel(self.dataset_not_found_widget)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(180, 30, 121, 41))
        self.label_34.setFont(font5)
        self.label_34.setStyleSheet(u"color:rgb(255, 85, 0);")
        self.label_34.setScaledContents(False)
        self.view_searched_ok_btn = QPushButton(self.dataset_not_found_widget)
        self.view_searched_ok_btn.setObjectName(u"view_searched_ok_btn")
        self.view_searched_ok_btn.setGeometry(QRect(180, 110, 121, 41))
        self.view_searched_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dataset_found_widget.raise_()
        self.dataset_not_found_widget.raise_()
        self.search_dataset.raise_()
        self.available_datasets_widget.raise_()
        self.label_55.raise_()
        self.datsets_stackedWidget.addWidget(self.create_dataset_page)
        self.created_dataset_page = QWidget()
        self.created_dataset_page.setObjectName(u"created_dataset_page")
        self.signup_form_2 = QLabel(self.created_dataset_page)
        self.signup_form_2.setObjectName(u"signup_form_2")
        self.signup_form_2.setGeometry(QRect(10, 20, 671, 411))
        self.signup_form_2.setStyleSheet(u"background-color:rgba(16,30,41,255);\n"
"border-radius:10px;\n"
"\n"
"")
        self.new_dtset_name = QLineEdit(self.created_dataset_page)
        self.new_dtset_name.setObjectName(u"new_dtset_name")
        self.new_dtset_name.setGeometry(QRect(40, 110, 250, 30))
        self.new_dtset_name.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.logoW_3 = QLabel(self.created_dataset_page)
        self.logoW_3.setObjectName(u"logoW_3")
        self.logoW_3.setGeometry(QRect(560, 30, 101, 61))
        self.logoW_3.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.logoW_3.setScaledContents(True)
        self.widget_5 = QWidget(self.created_dataset_page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(320, 100, 181, 181))
        self.widget_5.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.new_dst_upload_thumb_btn = QPushButton(self.widget_5)
        self.new_dst_upload_thumb_btn.setObjectName(u"new_dst_upload_thumb_btn")
        self.new_dst_upload_thumb_btn.setGeometry(QRect(10, 120, 161, 41))
        self.new_dst_upload_thumb_btn.setFont(font)
        self.new_dst_upload_thumb_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dst_upload_thumb_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.new_dst_u_image_0 = QLabel(self.widget_5)
        self.new_dst_u_image_0.setObjectName(u"new_dst_u_image_0")
        self.new_dst_u_image_0.setGeometry(QRect(40, 10, 111, 91))
        self.new_dst_u_image_0.setPixmap(QPixmap(u":/images/images/images/01_014.png"))
        self.new_dst_u_image_0.setScaledContents(True)
        self.new_dst_u_image_0.setAlignment(Qt.AlignCenter)
        self.new_dst_u_image_0.setIndent(0)
        self.select_dst_size = QComboBox(self.created_dataset_page)
        self.select_dst_size.addItem("")
        self.select_dst_size.addItem("")
        self.select_dst_size.addItem("")
        self.select_dst_size.setObjectName(u"select_dst_size")
        self.select_dst_size.setGeometry(QRect(140, 170, 151, 34))
        self.select_dst_size.setFont(font)
        self.select_dst_size.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_dst_size.setAutoFillBackground(False)
        self.select_dst_size.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.select_dst_size.setIconSize(QSize(16, 16))
        self.select_dst_size.setFrame(True)
        self.label_231 = QLabel(self.created_dataset_page)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setGeometry(QRect(40, 170, 91, 31))
        self.label_95 = QLabel(self.created_dataset_page)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(40, 240, 91, 41))
        self.label_95.setAlignment(Qt.AlignCenter)
        self.new_dst_u_image_1_btn = QPushButton(self.created_dataset_page)
        self.new_dst_u_image_1_btn.setObjectName(u"new_dst_u_image_1_btn")
        self.new_dst_u_image_1_btn.setGeometry(QRect(40, 310, 111, 91))
        self.new_dst_u_image_1_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dst_u_image_1_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.new_dst_u_image_1 = QLabel(self.created_dataset_page)
        self.new_dst_u_image_1.setObjectName(u"new_dst_u_image_1")
        self.new_dst_u_image_1.setGeometry(QRect(40, 310, 111, 91))
        self.new_dst_u_image_1.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_u_image_1.setFrameShape(QFrame.NoFrame)
        self.new_dst_u_image_1.setPixmap(QPixmap(u":/icons/images/icons/create_new.png"))
        self.new_dst_u_image_1.setAlignment(Qt.AlignCenter)
        self.new_dst_u_image_1.setWordWrap(True)
        self.new_dst_u_image_1.setMargin(2)
        self.new_dst_u_image_1.setIndent(0)
        self.new_dst_u_image_2 = QLabel(self.created_dataset_page)
        self.new_dst_u_image_2.setObjectName(u"new_dst_u_image_2")
        self.new_dst_u_image_2.setGeometry(QRect(160, 310, 111, 91))
        self.new_dst_u_image_2.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_u_image_2.setFrameShape(QFrame.NoFrame)
        self.new_dst_u_image_2.setPixmap(QPixmap(u":/icons/images/icons/create_new.png"))
        self.new_dst_u_image_2.setAlignment(Qt.AlignCenter)
        self.new_dst_u_image_2.setWordWrap(True)
        self.new_dst_u_image_2.setMargin(2)
        self.new_dst_u_image_3 = QLabel(self.created_dataset_page)
        self.new_dst_u_image_3.setObjectName(u"new_dst_u_image_3")
        self.new_dst_u_image_3.setGeometry(QRect(280, 310, 111, 91))
        self.new_dst_u_image_3.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_u_image_3.setFrameShape(QFrame.NoFrame)
        self.new_dst_u_image_3.setPixmap(QPixmap(u":/icons/images/icons/create_new.png"))
        self.new_dst_u_image_3.setAlignment(Qt.AlignCenter)
        self.new_dst_u_image_3.setWordWrap(True)
        self.new_dst_u_image_3.setMargin(2)
        self.new_dst_u_image_3.setIndent(0)
        self.new_dst_u_image_4 = QLabel(self.created_dataset_page)
        self.new_dst_u_image_4.setObjectName(u"new_dst_u_image_4")
        self.new_dst_u_image_4.setGeometry(QRect(400, 310, 111, 91))
        self.new_dst_u_image_4.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_u_image_4.setFrameShape(QFrame.NoFrame)
        self.new_dst_u_image_4.setPixmap(QPixmap(u":/icons/images/icons/create_new.png"))
        self.new_dst_u_image_4.setAlignment(Qt.AlignCenter)
        self.new_dst_u_image_4.setWordWrap(True)
        self.new_dst_u_image_4.setMargin(2)
        self.new_dst_u_image_4.setIndent(0)
        self.new_dst_u_image_5 = QLabel(self.created_dataset_page)
        self.new_dst_u_image_5.setObjectName(u"new_dst_u_image_5")
        self.new_dst_u_image_5.setGeometry(QRect(520, 310, 111, 91))
        self.new_dst_u_image_5.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_u_image_5.setFrameShape(QFrame.NoFrame)
        self.new_dst_u_image_5.setPixmap(QPixmap(u":/icons/images/icons/create_new.png"))
        self.new_dst_u_image_5.setAlignment(Qt.AlignCenter)
        self.new_dst_u_image_5.setWordWrap(True)
        self.new_dst_u_image_5.setMargin(2)
        self.new_dst_u_image_5.setIndent(0)
        self.new_dst_u_image_2_btn = QPushButton(self.created_dataset_page)
        self.new_dst_u_image_2_btn.setObjectName(u"new_dst_u_image_2_btn")
        self.new_dst_u_image_2_btn.setGeometry(QRect(160, 310, 111, 91))
        self.new_dst_u_image_2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dst_u_image_2_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.new_dst_u_image_3_btn = QPushButton(self.created_dataset_page)
        self.new_dst_u_image_3_btn.setObjectName(u"new_dst_u_image_3_btn")
        self.new_dst_u_image_3_btn.setGeometry(QRect(280, 310, 111, 91))
        self.new_dst_u_image_3_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dst_u_image_3_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.new_dst_u_image_4_btn = QPushButton(self.created_dataset_page)
        self.new_dst_u_image_4_btn.setObjectName(u"new_dst_u_image_4_btn")
        self.new_dst_u_image_4_btn.setGeometry(QRect(400, 310, 111, 91))
        self.new_dst_u_image_4_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dst_u_image_4_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.new_dst_u_image_5_btn = QPushButton(self.created_dataset_page)
        self.new_dst_u_image_5_btn.setObjectName(u"new_dst_u_image_5_btn")
        self.new_dst_u_image_5_btn.setGeometry(QRect(520, 310, 111, 91))
        self.new_dst_u_image_5_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dst_u_image_5_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.back_to_dataset_btn_5 = QPushButton(self.created_dataset_page)
        self.back_to_dataset_btn_5.setObjectName(u"back_to_dataset_btn_5")
        self.back_to_dataset_btn_5.setGeometry(QRect(40, 40, 51, 41))
        self.back_to_dataset_btn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_dst_done_btn = QPushButton(self.created_dataset_page)
        self.create_dst_done_btn.setObjectName(u"create_dst_done_btn")
        self.create_dst_done_btn.setGeometry(QRect(520, 200, 111, 71))
        self.create_dst_done_btn.setFont(font)
        self.create_dst_done_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_dst_done_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.dst_success_notification = QWidget(self.created_dataset_page)
        self.dst_success_notification.setObjectName(u"dst_success_notification")
        self.dst_success_notification.setGeometry(QRect(70, 100, 551, 191))
        self.dst_success_notification.setFont(font)
        self.dst_success_notification.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_19 = QLabel(self.dst_success_notification)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(190, 50, 171, 41))
        self.label_19.setFont(font5)
        self.label_19.setStyleSheet(u"color: rgb(170, 255, 0);")
        self.label_19.setScaledContents(False)
        self.dst_success_ok_btn = QPushButton(self.dst_success_notification)
        self.dst_success_ok_btn.setObjectName(u"dst_success_ok_btn")
        self.dst_success_ok_btn.setGeometry(QRect(210, 120, 121, 41))
        self.dst_success_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dst_fail_notification = QWidget(self.created_dataset_page)
        self.dst_fail_notification.setObjectName(u"dst_fail_notification")
        self.dst_fail_notification.setGeometry(QRect(70, 90, 551, 191))
        self.dst_fail_notification.setFont(font)
        self.dst_fail_notification.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_20 = QLabel(self.dst_fail_notification)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(200, 50, 151, 41))
        self.label_20.setFont(font5)
        self.label_20.setStyleSheet(u"\n"
"color: rgb(255, 0, 0);")
        self.label_20.setScaledContents(False)
        self.dst_fail_ok_btn = QPushButton(self.dst_fail_notification)
        self.dst_fail_ok_btn.setObjectName(u"dst_fail_ok_btn")
        self.dst_fail_ok_btn.setGeometry(QRect(210, 120, 121, 41))
        self.dst_fail_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.datsets_stackedWidget.addWidget(self.created_dataset_page)
        self.dst_success_notification.raise_()
        self.dst_fail_notification.raise_()
        self.signup_form_2.raise_()
        self.new_dtset_name.raise_()
        self.logoW_3.raise_()
        self.widget_5.raise_()
        self.select_dst_size.raise_()
        self.label_231.raise_()
        self.new_dst_u_image_1.raise_()
        self.label_95.raise_()
        self.new_dst_u_image_2.raise_()
        self.new_dst_u_image_3.raise_()
        self.new_dst_u_image_4.raise_()
        self.new_dst_u_image_5.raise_()
        self.new_dst_u_image_1_btn.raise_()
        self.new_dst_u_image_2_btn.raise_()
        self.new_dst_u_image_3_btn.raise_()
        self.new_dst_u_image_4_btn.raise_()
        self.new_dst_u_image_5_btn.raise_()
        self.back_to_dataset_btn_5.raise_()
        self.create_dst_done_btn.raise_()
        self.found_dataset_page = QWidget()
        self.found_dataset_page.setObjectName(u"found_dataset_page")
        self.datasets_widget_12 = QWidget(self.found_dataset_page)
        self.datasets_widget_12.setObjectName(u"datasets_widget_12")
        self.datasets_widget_12.setGeometry(QRect(20, 10, 661, 421))
        self.datasets_widget_12.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.new_dataset_name_2 = QLabel(self.datasets_widget_12)
        self.new_dataset_name_2.setObjectName(u"new_dataset_name_2")
        self.new_dataset_name_2.setGeometry(QRect(100, 10, 121, 41))
        self.new_dst_image_8 = QLabel(self.datasets_widget_12)
        self.new_dst_image_8.setObjectName(u"new_dst_image_8")
        self.new_dst_image_8.setGeometry(QRect(220, 100, 151, 121))
        self.new_dst_image_8.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_image_8.setFrameShape(QFrame.NoFrame)
        self.new_dst_image_8.setAlignment(Qt.AlignCenter)
        self.new_dst_image_8.setWordWrap(True)
        self.new_dst_image_8.setMargin(2)
        self.new_dst_image_9 = QLabel(self.datasets_widget_12)
        self.new_dst_image_9.setObjectName(u"new_dst_image_9")
        self.new_dst_image_9.setGeometry(QRect(30, 270, 141, 121))
        self.new_dst_image_9.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_image_9.setFrameShape(QFrame.NoFrame)
        self.new_dst_image_9.setAlignment(Qt.AlignCenter)
        self.new_dst_image_9.setWordWrap(True)
        self.new_dst_image_9.setMargin(2)
        self.new_dst_image_10 = QLabel(self.datasets_widget_12)
        self.new_dst_image_10.setObjectName(u"new_dst_image_10")
        self.new_dst_image_10.setGeometry(QRect(220, 270, 151, 121))
        self.new_dst_image_10.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_image_10.setFrameShape(QFrame.NoFrame)
        self.new_dst_image_10.setAlignment(Qt.AlignCenter)
        self.new_dst_image_10.setWordWrap(True)
        self.new_dst_image_10.setMargin(2)
        self.new_dst_image_11 = QLabel(self.datasets_widget_12)
        self.new_dst_image_11.setObjectName(u"new_dst_image_11")
        self.new_dst_image_11.setGeometry(QRect(420, 100, 151, 121))
        self.new_dst_image_11.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_image_11.setFrameShape(QFrame.NoFrame)
        self.new_dst_image_11.setAlignment(Qt.AlignCenter)
        self.new_dst_image_11.setWordWrap(True)
        self.new_dst_image_11.setMargin(2)
        self.new_dst_image_12 = QLabel(self.datasets_widget_12)
        self.new_dst_image_12.setObjectName(u"new_dst_image_12")
        self.new_dst_image_12.setGeometry(QRect(420, 270, 151, 121))
        self.new_dst_image_12.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_image_12.setFrameShape(QFrame.NoFrame)
        self.new_dst_image_12.setAlignment(Qt.AlignCenter)
        self.new_dst_image_12.setWordWrap(True)
        self.new_dst_image_12.setMargin(2)
        self.back_to_dataset_btn_6 = QPushButton(self.datasets_widget_12)
        self.back_to_dataset_btn_6.setObjectName(u"back_to_dataset_btn_6")
        self.back_to_dataset_btn_6.setGeometry(QRect(30, 10, 51, 41))
        self.back_to_dataset_btn_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_new_dataset_btn_2 = QPushButton(self.datasets_widget_12)
        self.delete_new_dataset_btn_2.setObjectName(u"delete_new_dataset_btn_2")
        self.delete_new_dataset_btn_2.setGeometry(QRect(490, 30, 121, 24))
        self.delete_new_dataset_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.upload_images_btn_2 = QPushButton(self.datasets_widget_12)
        self.upload_images_btn_2.setObjectName(u"upload_images_btn_2")
        self.upload_images_btn_2.setGeometry(QRect(350, 30, 121, 24))
        self.upload_images_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dst_success_notification_2 = QWidget(self.datasets_widget_12)
        self.new_dst_success_notification_2.setObjectName(u"new_dst_success_notification_2")
        self.new_dst_success_notification_2.setGeometry(QRect(30, 60, 551, 201))
        self.new_dst_success_notification_2.setFont(font)
        self.new_dst_success_notification_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_30 = QLabel(self.new_dst_success_notification_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(160, 50, 231, 41))
        self.label_30.setFont(font5)
        self.label_30.setStyleSheet(u"color: rgb(170, 255, 0);")
        self.label_30.setScaledContents(False)
        self.label_30.setAlignment(Qt.AlignCenter)
        self.dst_success_ok_btn_3 = QPushButton(self.new_dst_success_notification_2)
        self.dst_success_ok_btn_3.setObjectName(u"dst_success_ok_btn_3")
        self.dst_success_ok_btn_3.setGeometry(QRect(210, 120, 121, 41))
        self.dst_success_ok_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dst_fail_notification_2 = QWidget(self.datasets_widget_12)
        self.new_dst_fail_notification_2.setObjectName(u"new_dst_fail_notification_2")
        self.new_dst_fail_notification_2.setGeometry(QRect(20, 60, 551, 191))
        self.new_dst_fail_notification_2.setFont(font)
        self.new_dst_fail_notification_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_31 = QLabel(self.new_dst_fail_notification_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(200, 50, 151, 41))
        self.label_31.setFont(font5)
        self.label_31.setStyleSheet(u"\n"
"color: rgb(255, 0, 0);")
        self.label_31.setScaledContents(False)
        self.dst_fail_ok_btn_3 = QPushButton(self.new_dst_fail_notification_2)
        self.dst_fail_ok_btn_3.setObjectName(u"dst_fail_ok_btn_3")
        self.dst_fail_ok_btn_3.setGeometry(QRect(210, 120, 121, 41))
        self.dst_fail_ok_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dst_image_7 = QLabel(self.new_dst_fail_notification_2)
        self.new_dst_image_7.setObjectName(u"new_dst_image_7")
        self.new_dst_image_7.setGeometry(QRect(10, 40, 141, 121))
        self.new_dst_image_7.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_image_7.setFrameShape(QFrame.NoFrame)
        self.new_dst_image_7.setAlignment(Qt.AlignCenter)
        self.new_dst_image_7.setWordWrap(True)
        self.new_dst_image_7.setMargin(2)
        self.new_dataset_del_confirm_widget_2 = QWidget(self.datasets_widget_12)
        self.new_dataset_del_confirm_widget_2.setObjectName(u"new_dataset_del_confirm_widget_2")
        self.new_dataset_del_confirm_widget_2.setGeometry(QRect(100, 40, 451, 241))
        self.new_dataset_del_confirm_widget_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.new_dataset_del_confirm_ok_btn_2 = QPushButton(self.new_dataset_del_confirm_widget_2)
        self.new_dataset_del_confirm_ok_btn_2.setObjectName(u"new_dataset_del_confirm_ok_btn_2")
        self.new_dataset_del_confirm_ok_btn_2.setGeometry(QRect(40, 150, 151, 41))
        self.new_dataset_del_confirm_ok_btn_2.setFont(font)
        self.new_dataset_del_confirm_ok_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dataset_del_confirm_ok_btn_2.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_32 = QLabel(self.new_dataset_del_confirm_widget_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(80, 30, 301, 41))
        self.label_32.setAlignment(Qt.AlignCenter)
        self.new_dataset_del_confirm_cancel_btn_2 = QPushButton(self.new_dataset_del_confirm_widget_2)
        self.new_dataset_del_confirm_cancel_btn_2.setObjectName(u"new_dataset_del_confirm_cancel_btn_2")
        self.new_dataset_del_confirm_cancel_btn_2.setGeometry(QRect(270, 150, 151, 41))
        self.new_dataset_del_confirm_cancel_btn_2.setFont(font)
        self.new_dataset_del_confirm_cancel_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dataset_del_confirm_cancel_btn_2.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_9 = QLabel(self.new_dataset_del_confirm_widget_2)
        self.account_verify_status_9.setObjectName(u"account_verify_status_9")
        self.account_verify_status_9.setGeometry(QRect(80, 80, 291, 41))
        self.account_verify_status_9.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status_9.setAlignment(Qt.AlignCenter)
        self.new_dataset_del_confirm_widget_2.raise_()
        self.new_dst_success_notification_2.raise_()
        self.new_dst_fail_notification_2.raise_()
        self.new_dataset_name_2.raise_()
        self.new_dst_image_8.raise_()
        self.new_dst_image_9.raise_()
        self.new_dst_image_10.raise_()
        self.new_dst_image_11.raise_()
        self.new_dst_image_12.raise_()
        self.back_to_dataset_btn_6.raise_()
        self.delete_new_dataset_btn_2.raise_()
        self.upload_images_btn_2.raise_()
        self.datsets_stackedWidget.addWidget(self.found_dataset_page)
        self.anime_dataset_page = QWidget()
        self.anime_dataset_page.setObjectName(u"anime_dataset_page")
        self.datasets_widget_3 = QWidget(self.anime_dataset_page)
        self.datasets_widget_3.setObjectName(u"datasets_widget_3")
        self.datasets_widget_3.setGeometry(QRect(20, 10, 661, 421))
        self.datasets_widget_3.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.anime_image_1 = QLabel(self.datasets_widget_3)
        self.anime_image_1.setObjectName(u"anime_image_1")
        self.anime_image_1.setGeometry(QRect(30, 90, 141, 121))
        self.anime_image_1.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.anime_image_1.setFrameShape(QFrame.NoFrame)
        self.anime_image_1.setAlignment(Qt.AlignCenter)
        self.anime_image_1.setWordWrap(True)
        self.anime_image_1.setMargin(2)
        self.label_187 = QLabel(self.datasets_widget_3)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setGeometry(QRect(70, 10, 121, 41))
        self.anime_image_2 = QLabel(self.datasets_widget_3)
        self.anime_image_2.setObjectName(u"anime_image_2")
        self.anime_image_2.setGeometry(QRect(220, 90, 151, 121))
        self.anime_image_2.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.anime_image_2.setFrameShape(QFrame.NoFrame)
        self.anime_image_2.setAlignment(Qt.AlignCenter)
        self.anime_image_2.setWordWrap(True)
        self.anime_image_2.setMargin(2)
        self.anime_image_4 = QLabel(self.datasets_widget_3)
        self.anime_image_4.setObjectName(u"anime_image_4")
        self.anime_image_4.setGeometry(QRect(30, 270, 141, 121))
        self.anime_image_4.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.anime_image_4.setFrameShape(QFrame.NoFrame)
        self.anime_image_4.setAlignment(Qt.AlignCenter)
        self.anime_image_4.setWordWrap(True)
        self.anime_image_4.setMargin(2)
        self.anime_image_5 = QLabel(self.datasets_widget_3)
        self.anime_image_5.setObjectName(u"anime_image_5")
        self.anime_image_5.setGeometry(QRect(220, 270, 151, 121))
        self.anime_image_5.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.anime_image_5.setFrameShape(QFrame.NoFrame)
        self.anime_image_5.setAlignment(Qt.AlignCenter)
        self.anime_image_5.setWordWrap(True)
        self.anime_image_5.setMargin(2)
        self.anime_image_3 = QLabel(self.datasets_widget_3)
        self.anime_image_3.setObjectName(u"anime_image_3")
        self.anime_image_3.setGeometry(QRect(420, 90, 151, 121))
        self.anime_image_3.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.anime_image_3.setFrameShape(QFrame.NoFrame)
        self.anime_image_3.setAlignment(Qt.AlignCenter)
        self.anime_image_3.setWordWrap(True)
        self.anime_image_3.setMargin(2)
        self.anime_image_6 = QLabel(self.datasets_widget_3)
        self.anime_image_6.setObjectName(u"anime_image_6")
        self.anime_image_6.setGeometry(QRect(420, 270, 151, 121))
        self.anime_image_6.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.anime_image_6.setFrameShape(QFrame.NoFrame)
        self.anime_image_6.setAlignment(Qt.AlignCenter)
        self.anime_image_6.setWordWrap(True)
        self.anime_image_6.setMargin(2)
        self.listWidget = QListWidget(self.datasets_widget_3)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 70, 591, 341))
        self.back_to_dataset_btn = QPushButton(self.datasets_widget_3)
        self.back_to_dataset_btn.setObjectName(u"back_to_dataset_btn")
        self.back_to_dataset_btn.setGeometry(QRect(10, 10, 51, 41))
        self.back_to_dataset_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.listWidget.raise_()
        self.anime_image_1.raise_()
        self.label_187.raise_()
        self.anime_image_2.raise_()
        self.anime_image_4.raise_()
        self.anime_image_5.raise_()
        self.anime_image_3.raise_()
        self.anime_image_6.raise_()
        self.back_to_dataset_btn.raise_()
        self.datsets_stackedWidget.addWidget(self.anime_dataset_page)
        self.human_dataset_page = QWidget()
        self.human_dataset_page.setObjectName(u"human_dataset_page")
        self.datasets_widget_4 = QWidget(self.human_dataset_page)
        self.datasets_widget_4.setObjectName(u"datasets_widget_4")
        self.datasets_widget_4.setGeometry(QRect(20, 20, 661, 421))
        self.datasets_widget_4.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.human_image_1 = QLabel(self.datasets_widget_4)
        self.human_image_1.setObjectName(u"human_image_1")
        self.human_image_1.setGeometry(QRect(30, 100, 141, 121))
        self.human_image_1.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.human_image_1.setFrameShape(QFrame.NoFrame)
        self.human_image_1.setAlignment(Qt.AlignCenter)
        self.human_image_1.setWordWrap(True)
        self.human_image_1.setMargin(2)
        self.label_190 = QLabel(self.datasets_widget_4)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setGeometry(QRect(80, 10, 121, 41))
        self.human_image_2 = QLabel(self.datasets_widget_4)
        self.human_image_2.setObjectName(u"human_image_2")
        self.human_image_2.setGeometry(QRect(220, 100, 151, 121))
        self.human_image_2.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.human_image_2.setFrameShape(QFrame.NoFrame)
        self.human_image_2.setAlignment(Qt.AlignCenter)
        self.human_image_2.setWordWrap(True)
        self.human_image_2.setMargin(2)
        self.human_image_4 = QLabel(self.datasets_widget_4)
        self.human_image_4.setObjectName(u"human_image_4")
        self.human_image_4.setGeometry(QRect(30, 270, 141, 121))
        self.human_image_4.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.human_image_4.setFrameShape(QFrame.NoFrame)
        self.human_image_4.setAlignment(Qt.AlignCenter)
        self.human_image_4.setWordWrap(True)
        self.human_image_4.setMargin(2)
        self.human_image_5 = QLabel(self.datasets_widget_4)
        self.human_image_5.setObjectName(u"human_image_5")
        self.human_image_5.setGeometry(QRect(220, 270, 151, 121))
        self.human_image_5.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.human_image_5.setFrameShape(QFrame.NoFrame)
        self.human_image_5.setAlignment(Qt.AlignCenter)
        self.human_image_5.setWordWrap(True)
        self.human_image_5.setMargin(2)
        self.human_image_3 = QLabel(self.datasets_widget_4)
        self.human_image_3.setObjectName(u"human_image_3")
        self.human_image_3.setGeometry(QRect(420, 100, 151, 121))
        self.human_image_3.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.human_image_3.setFrameShape(QFrame.NoFrame)
        self.human_image_3.setAlignment(Qt.AlignCenter)
        self.human_image_3.setWordWrap(True)
        self.human_image_3.setMargin(2)
        self.human_image_6 = QLabel(self.datasets_widget_4)
        self.human_image_6.setObjectName(u"human_image_6")
        self.human_image_6.setGeometry(QRect(420, 270, 151, 121))
        self.human_image_6.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.human_image_6.setFrameShape(QFrame.NoFrame)
        self.human_image_6.setAlignment(Qt.AlignCenter)
        self.human_image_6.setWordWrap(True)
        self.human_image_6.setMargin(2)
        self.back_to_dataset_btn_2 = QPushButton(self.datasets_widget_4)
        self.back_to_dataset_btn_2.setObjectName(u"back_to_dataset_btn_2")
        self.back_to_dataset_btn_2.setGeometry(QRect(20, 10, 51, 41))
        self.back_to_dataset_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.datsets_stackedWidget.addWidget(self.human_dataset_page)
        self.new_dataset_page = QWidget()
        self.new_dataset_page.setObjectName(u"new_dataset_page")
        self.datasets_widget_5 = QWidget(self.new_dataset_page)
        self.datasets_widget_5.setObjectName(u"datasets_widget_5")
        self.datasets_widget_5.setGeometry(QRect(20, 20, 661, 421))
        self.datasets_widget_5.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.new_dataset_name = QLabel(self.datasets_widget_5)
        self.new_dataset_name.setObjectName(u"new_dataset_name")
        self.new_dataset_name.setGeometry(QRect(100, 10, 121, 41))
        self.new_dst_image_2 = QLabel(self.datasets_widget_5)
        self.new_dst_image_2.setObjectName(u"new_dst_image_2")
        self.new_dst_image_2.setGeometry(QRect(220, 100, 151, 121))
        self.new_dst_image_2.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_image_2.setFrameShape(QFrame.NoFrame)
        self.new_dst_image_2.setAlignment(Qt.AlignCenter)
        self.new_dst_image_2.setWordWrap(True)
        self.new_dst_image_2.setMargin(2)
        self.new_dst_image_4 = QLabel(self.datasets_widget_5)
        self.new_dst_image_4.setObjectName(u"new_dst_image_4")
        self.new_dst_image_4.setGeometry(QRect(30, 270, 141, 121))
        self.new_dst_image_4.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_image_4.setFrameShape(QFrame.NoFrame)
        self.new_dst_image_4.setAlignment(Qt.AlignCenter)
        self.new_dst_image_4.setWordWrap(True)
        self.new_dst_image_4.setMargin(2)
        self.new_dst_image_5 = QLabel(self.datasets_widget_5)
        self.new_dst_image_5.setObjectName(u"new_dst_image_5")
        self.new_dst_image_5.setGeometry(QRect(220, 270, 151, 121))
        self.new_dst_image_5.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_image_5.setFrameShape(QFrame.NoFrame)
        self.new_dst_image_5.setAlignment(Qt.AlignCenter)
        self.new_dst_image_5.setWordWrap(True)
        self.new_dst_image_5.setMargin(2)
        self.new_dst_image_3 = QLabel(self.datasets_widget_5)
        self.new_dst_image_3.setObjectName(u"new_dst_image_3")
        self.new_dst_image_3.setGeometry(QRect(420, 100, 151, 121))
        self.new_dst_image_3.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_image_3.setFrameShape(QFrame.NoFrame)
        self.new_dst_image_3.setAlignment(Qt.AlignCenter)
        self.new_dst_image_3.setWordWrap(True)
        self.new_dst_image_3.setMargin(2)
        self.new_dst_image_6 = QLabel(self.datasets_widget_5)
        self.new_dst_image_6.setObjectName(u"new_dst_image_6")
        self.new_dst_image_6.setGeometry(QRect(420, 270, 151, 121))
        self.new_dst_image_6.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_image_6.setFrameShape(QFrame.NoFrame)
        self.new_dst_image_6.setAlignment(Qt.AlignCenter)
        self.new_dst_image_6.setWordWrap(True)
        self.new_dst_image_6.setMargin(2)
        self.back_to_dataset_btn_3 = QPushButton(self.datasets_widget_5)
        self.back_to_dataset_btn_3.setObjectName(u"back_to_dataset_btn_3")
        self.back_to_dataset_btn_3.setGeometry(QRect(30, 10, 51, 41))
        self.back_to_dataset_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_new_dataset_btn = QPushButton(self.datasets_widget_5)
        self.delete_new_dataset_btn.setObjectName(u"delete_new_dataset_btn")
        self.delete_new_dataset_btn.setGeometry(QRect(490, 30, 121, 24))
        self.delete_new_dataset_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.upload_images_btn = QPushButton(self.datasets_widget_5)
        self.upload_images_btn.setObjectName(u"upload_images_btn")
        self.upload_images_btn.setGeometry(QRect(350, 30, 121, 24))
        self.upload_images_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dst_success_notification = QWidget(self.datasets_widget_5)
        self.new_dst_success_notification.setObjectName(u"new_dst_success_notification")
        self.new_dst_success_notification.setGeometry(QRect(30, 60, 551, 201))
        self.new_dst_success_notification.setFont(font)
        self.new_dst_success_notification.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_24 = QLabel(self.new_dst_success_notification)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(160, 50, 231, 41))
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"color: rgb(170, 255, 0);")
        self.label_24.setScaledContents(False)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.dst_success_ok_btn_2 = QPushButton(self.new_dst_success_notification)
        self.dst_success_ok_btn_2.setObjectName(u"dst_success_ok_btn_2")
        self.dst_success_ok_btn_2.setGeometry(QRect(210, 120, 121, 41))
        self.dst_success_ok_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dst_fail_notification = QWidget(self.datasets_widget_5)
        self.new_dst_fail_notification.setObjectName(u"new_dst_fail_notification")
        self.new_dst_fail_notification.setGeometry(QRect(20, 60, 551, 191))
        self.new_dst_fail_notification.setFont(font)
        self.new_dst_fail_notification.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_27 = QLabel(self.new_dst_fail_notification)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(200, 50, 151, 41))
        self.label_27.setFont(font5)
        self.label_27.setStyleSheet(u"\n"
"color: rgb(255, 0, 0);")
        self.label_27.setScaledContents(False)
        self.dst_fail_ok_btn_2 = QPushButton(self.new_dst_fail_notification)
        self.dst_fail_ok_btn_2.setObjectName(u"dst_fail_ok_btn_2")
        self.dst_fail_ok_btn_2.setGeometry(QRect(210, 120, 121, 41))
        self.dst_fail_ok_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dst_image_1 = QLabel(self.new_dst_fail_notification)
        self.new_dst_image_1.setObjectName(u"new_dst_image_1")
        self.new_dst_image_1.setGeometry(QRect(10, 40, 141, 121))
        self.new_dst_image_1.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_dst_image_1.setFrameShape(QFrame.NoFrame)
        self.new_dst_image_1.setAlignment(Qt.AlignCenter)
        self.new_dst_image_1.setWordWrap(True)
        self.new_dst_image_1.setMargin(2)
        self.dst_fail_ok_btn_2.raise_()
        self.label_27.raise_()
        self.new_dst_image_1.raise_()
        self.new_dataset_del_confirm_widget = QWidget(self.datasets_widget_5)
        self.new_dataset_del_confirm_widget.setObjectName(u"new_dataset_del_confirm_widget")
        self.new_dataset_del_confirm_widget.setGeometry(QRect(100, 40, 451, 241))
        self.new_dataset_del_confirm_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.new_dataset_del_confirm_ok_btn = QPushButton(self.new_dataset_del_confirm_widget)
        self.new_dataset_del_confirm_ok_btn.setObjectName(u"new_dataset_del_confirm_ok_btn")
        self.new_dataset_del_confirm_ok_btn.setGeometry(QRect(40, 150, 151, 41))
        self.new_dataset_del_confirm_ok_btn.setFont(font)
        self.new_dataset_del_confirm_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dataset_del_confirm_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_29 = QLabel(self.new_dataset_del_confirm_widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(80, 30, 301, 41))
        self.label_29.setAlignment(Qt.AlignCenter)
        self.new_dataset_del_confirm_cancel_btn = QPushButton(self.new_dataset_del_confirm_widget)
        self.new_dataset_del_confirm_cancel_btn.setObjectName(u"new_dataset_del_confirm_cancel_btn")
        self.new_dataset_del_confirm_cancel_btn.setGeometry(QRect(270, 150, 151, 41))
        self.new_dataset_del_confirm_cancel_btn.setFont(font)
        self.new_dataset_del_confirm_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_dataset_del_confirm_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_8 = QLabel(self.new_dataset_del_confirm_widget)
        self.account_verify_status_8.setObjectName(u"account_verify_status_8")
        self.account_verify_status_8.setGeometry(QRect(80, 80, 291, 41))
        self.account_verify_status_8.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status_8.setAlignment(Qt.AlignCenter)
        self.new_dataset_del_confirm_widget.raise_()
        self.new_dst_success_notification.raise_()
        self.new_dst_fail_notification.raise_()
        self.new_dataset_name.raise_()
        self.new_dst_image_2.raise_()
        self.new_dst_image_4.raise_()
        self.new_dst_image_5.raise_()
        self.new_dst_image_6.raise_()
        self.back_to_dataset_btn_3.raise_()
        self.delete_new_dataset_btn.raise_()
        self.upload_images_btn.raise_()
        self.new_dst_image_3.raise_()
        self.datsets_stackedWidget.addWidget(self.new_dataset_page)
        self.flower_datset_page = QWidget()
        self.flower_datset_page.setObjectName(u"flower_datset_page")
        self.datasets_widget_6 = QWidget(self.flower_datset_page)
        self.datasets_widget_6.setObjectName(u"datasets_widget_6")
        self.datasets_widget_6.setGeometry(QRect(20, 10, 661, 421))
        self.datasets_widget_6.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.flower_image_1 = QLabel(self.datasets_widget_6)
        self.flower_image_1.setObjectName(u"flower_image_1")
        self.flower_image_1.setGeometry(QRect(30, 100, 141, 121))
        self.flower_image_1.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.flower_image_1.setFrameShape(QFrame.NoFrame)
        self.flower_image_1.setAlignment(Qt.AlignCenter)
        self.flower_image_1.setWordWrap(True)
        self.flower_image_1.setMargin(2)
        self.label_208 = QLabel(self.datasets_widget_6)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setGeometry(QRect(80, 10, 121, 41))
        self.flower_image_2 = QLabel(self.datasets_widget_6)
        self.flower_image_2.setObjectName(u"flower_image_2")
        self.flower_image_2.setGeometry(QRect(220, 100, 151, 121))
        self.flower_image_2.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.flower_image_2.setFrameShape(QFrame.NoFrame)
        self.flower_image_2.setAlignment(Qt.AlignCenter)
        self.flower_image_2.setWordWrap(True)
        self.flower_image_2.setMargin(2)
        self.flower_image_4 = QLabel(self.datasets_widget_6)
        self.flower_image_4.setObjectName(u"flower_image_4")
        self.flower_image_4.setGeometry(QRect(30, 270, 141, 121))
        self.flower_image_4.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.flower_image_4.setFrameShape(QFrame.NoFrame)
        self.flower_image_4.setAlignment(Qt.AlignCenter)
        self.flower_image_4.setWordWrap(True)
        self.flower_image_4.setMargin(2)
        self.flower_image_5 = QLabel(self.datasets_widget_6)
        self.flower_image_5.setObjectName(u"flower_image_5")
        self.flower_image_5.setGeometry(QRect(220, 270, 151, 121))
        self.flower_image_5.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.flower_image_5.setFrameShape(QFrame.NoFrame)
        self.flower_image_5.setAlignment(Qt.AlignCenter)
        self.flower_image_5.setWordWrap(True)
        self.flower_image_5.setMargin(2)
        self.flower_image_3 = QLabel(self.datasets_widget_6)
        self.flower_image_3.setObjectName(u"flower_image_3")
        self.flower_image_3.setGeometry(QRect(420, 100, 151, 121))
        self.flower_image_3.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.flower_image_3.setFrameShape(QFrame.NoFrame)
        self.flower_image_3.setAlignment(Qt.AlignCenter)
        self.flower_image_3.setWordWrap(True)
        self.flower_image_3.setMargin(2)
        self.flower_image_6 = QLabel(self.datasets_widget_6)
        self.flower_image_6.setObjectName(u"flower_image_6")
        self.flower_image_6.setGeometry(QRect(420, 270, 151, 121))
        self.flower_image_6.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.flower_image_6.setFrameShape(QFrame.NoFrame)
        self.flower_image_6.setAlignment(Qt.AlignCenter)
        self.flower_image_6.setWordWrap(True)
        self.flower_image_6.setMargin(2)
        self.back_to_dataset_btn_4 = QPushButton(self.datasets_widget_6)
        self.back_to_dataset_btn_4.setObjectName(u"back_to_dataset_btn_4")
        self.back_to_dataset_btn_4.setGeometry(QRect(20, 10, 51, 41))
        self.back_to_dataset_btn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.datsets_stackedWidget.addWidget(self.flower_datset_page)
        self.stackedWidget_content_pages.addWidget(self.datasets_page)
        self.model_training_page = QWidget()
        self.model_training_page.setObjectName(u"model_training_page")
        self.stackedWidget_model_training = QStackedWidget(self.model_training_page)
        self.stackedWidget_model_training.setObjectName(u"stackedWidget_model_training")
        self.stackedWidget_model_training.setGeometry(QRect(0, -10, 731, 451))
        self.select_dataset_page = QWidget()
        self.select_dataset_page.setObjectName(u"select_dataset_page")
        self.datasets_widget_7 = QWidget(self.select_dataset_page)
        self.datasets_widget_7.setObjectName(u"datasets_widget_7")
        self.datasets_widget_7.setGeometry(QRect(10, 10, 661, 421))
        self.datasets_widget_7.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_65 = QLabel(self.datasets_widget_7)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(30, 10, 81, 41))
        self.search_dataset_2 = QLineEdit(self.datasets_widget_7)
        self.search_dataset_2.setObjectName(u"search_dataset_2")
        self.search_dataset_2.setGeometry(QRect(390, 20, 250, 30))
        self.search_dataset_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.comboBox_4 = QComboBox(self.datasets_widget_7)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(490, 380, 101, 34))
        self.comboBox_4.setFont(font)
        self.comboBox_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_4.setAutoFillBackground(False)
        self.comboBox_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_4.setIconSize(QSize(16, 16))
        self.comboBox_4.setFrame(True)
        self.label_222 = QLabel(self.datasets_widget_7)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setGeometry(QRect(450, 380, 41, 31))
        self.label_228 = QLabel(self.datasets_widget_7)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setGeometry(QRect(450, 140, 121, 81))
        self.label_228.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_228.setScaledContents(True)
        self.label_228.setAlignment(Qt.AlignCenter)
        self.label_228.setMargin(15)
        self.label_229 = QLabel(self.datasets_widget_7)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setGeometry(QRect(390, 100, 241, 261))
        self.label_229.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_229.setFrameShape(QFrame.NoFrame)
        self.label_229.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_229.setWordWrap(True)
        self.label_229.setMargin(36)
        self.label_230 = QLabel(self.datasets_widget_7)
        self.label_230.setObjectName(u"label_230")
        self.label_230.setGeometry(QRect(410, 230, 201, 121))
        self.label_230.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_230.setFrameShape(QFrame.NoFrame)
        self.label_230.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_230.setWordWrap(True)
        self.label_230.setMargin(0)
        self.available_datasets_widget_2 = QWidget(self.datasets_widget_7)
        self.available_datasets_widget_2.setObjectName(u"available_datasets_widget_2")
        self.available_datasets_widget_2.setGeometry(QRect(-20, 50, 381, 361))
        self.available_datasets_widget_2.setFont(font)
        self.available_datasets_widget_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_64 = QLabel(self.available_datasets_widget_2)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(240, 10, 71, 41))
        self.label_62 = QLabel(self.available_datasets_widget_2)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(60, 10, 71, 41))
        self.anime_thumbnail_btn_2 = QPushButton(self.available_datasets_widget_2)
        self.anime_thumbnail_btn_2.setObjectName(u"anime_thumbnail_btn_2")
        self.anime_thumbnail_btn_2.setGeometry(QRect(50, 60, 141, 121))
        self.anime_thumbnail_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.anime_thumbnail_btn_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.human_thumbnail_btn_2 = QPushButton(self.available_datasets_widget_2)
        self.human_thumbnail_btn_2.setObjectName(u"human_thumbnail_btn_2")
        self.human_thumbnail_btn_2.setGeometry(QRect(210, 60, 151, 121))
        self.human_thumbnail_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.human_thumbnail_btn_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.human_thumbnail_2 = QLabel(self.available_datasets_widget_2)
        self.human_thumbnail_2.setObjectName(u"human_thumbnail_2")
        self.human_thumbnail_2.setGeometry(QRect(210, 60, 151, 121))
        self.human_thumbnail_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.human_thumbnail_2.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.human_thumbnail_2.setFrameShape(QFrame.NoFrame)
        self.human_thumbnail_2.setAlignment(Qt.AlignCenter)
        self.human_thumbnail_2.setWordWrap(True)
        self.human_thumbnail_2.setMargin(2)
        self.anime_thumbnail_2 = QLabel(self.available_datasets_widget_2)
        self.anime_thumbnail_2.setObjectName(u"anime_thumbnail_2")
        self.anime_thumbnail_2.setGeometry(QRect(50, 60, 141, 121))
        self.anime_thumbnail_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.anime_thumbnail_2.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.anime_thumbnail_2.setFrameShape(QFrame.NoFrame)
        self.anime_thumbnail_2.setAlignment(Qt.AlignCenter)
        self.anime_thumbnail_2.setWordWrap(True)
        self.anime_thumbnail_2.setMargin(2)
        self.new_datset_thumbnail_btn_2 = QPushButton(self.available_datasets_widget_2)
        self.new_datset_thumbnail_btn_2.setObjectName(u"new_datset_thumbnail_btn_2")
        self.new_datset_thumbnail_btn_2.setGeometry(QRect(210, 230, 151, 121))
        self.new_datset_thumbnail_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_datset_thumbnail_btn_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_100 = QLabel(self.available_datasets_widget_2)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(50, 190, 71, 41))
        self.flower_thumbnail_btn_2 = QPushButton(self.available_datasets_widget_2)
        self.flower_thumbnail_btn_2.setObjectName(u"flower_thumbnail_btn_2")
        self.flower_thumbnail_btn_2.setGeometry(QRect(40, 230, 151, 121))
        self.flower_thumbnail_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.flower_thumbnail_btn_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_new_dataset_2 = QLabel(self.available_datasets_widget_2)
        self.label_new_dataset_2.setObjectName(u"label_new_dataset_2")
        self.label_new_dataset_2.setGeometry(QRect(230, 190, 91, 41))
        self.new_datset_thumbnail_2 = QLabel(self.available_datasets_widget_2)
        self.new_datset_thumbnail_2.setObjectName(u"new_datset_thumbnail_2")
        self.new_datset_thumbnail_2.setGeometry(QRect(210, 230, 151, 121))
        self.new_datset_thumbnail_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_datset_thumbnail_2.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_datset_thumbnail_2.setFrameShape(QFrame.NoFrame)
        self.new_datset_thumbnail_2.setAlignment(Qt.AlignCenter)
        self.new_datset_thumbnail_2.setWordWrap(True)
        self.new_datset_thumbnail_2.setMargin(2)
        self.flower_thumbnail_2 = QLabel(self.available_datasets_widget_2)
        self.flower_thumbnail_2.setObjectName(u"flower_thumbnail_2")
        self.flower_thumbnail_2.setGeometry(QRect(40, 230, 151, 121))
        self.flower_thumbnail_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.flower_thumbnail_2.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.flower_thumbnail_2.setFrameShape(QFrame.NoFrame)
        self.flower_thumbnail_2.setAlignment(Qt.AlignCenter)
        self.flower_thumbnail_2.setWordWrap(True)
        self.flower_thumbnail_2.setMargin(2)
        self.label_64.raise_()
        self.label_62.raise_()
        self.anime_thumbnail_2.raise_()
        self.label_100.raise_()
        self.label_new_dataset_2.raise_()
        self.new_datset_thumbnail_2.raise_()
        self.flower_thumbnail_2.raise_()
        self.new_datset_thumbnail_btn_2.raise_()
        self.human_thumbnail_2.raise_()
        self.human_thumbnail_btn_2.raise_()
        self.anime_thumbnail_btn_2.raise_()
        self.flower_thumbnail_btn_2.raise_()
        self.dataset_found_widget_2 = QWidget(self.datasets_widget_7)
        self.dataset_found_widget_2.setObjectName(u"dataset_found_widget_2")
        self.dataset_found_widget_2.setGeometry(QRect(130, 20, 501, 351))
        self.dataset_found_widget_2.setFont(font)
        self.dataset_found_widget_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_35 = QLabel(self.dataset_found_widget_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(80, 30, 101, 41))
        self.label_35.setFont(font5)
        self.label_35.setStyleSheet(u"color: rgb(170, 255, 0);")
        self.label_35.setScaledContents(False)
        self.view_searched_dst_btn_2 = QPushButton(self.dataset_found_widget_2)
        self.view_searched_dst_btn_2.setObjectName(u"view_searched_dst_btn_2")
        self.view_searched_dst_btn_2.setGeometry(QRect(80, 240, 121, 41))
        self.view_searched_dst_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.searched_dst_thumbnail_btn_2 = QPushButton(self.dataset_found_widget_2)
        self.searched_dst_thumbnail_btn_2.setObjectName(u"searched_dst_thumbnail_btn_2")
        self.searched_dst_thumbnail_btn_2.setGeometry(QRect(60, 90, 141, 121))
        self.searched_dst_thumbnail_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.searched_dst_thumbnail_btn_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.searched_dst_thumbnail_2 = QLabel(self.dataset_found_widget_2)
        self.searched_dst_thumbnail_2.setObjectName(u"searched_dst_thumbnail_2")
        self.searched_dst_thumbnail_2.setGeometry(QRect(60, 90, 141, 121))
        self.searched_dst_thumbnail_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.searched_dst_thumbnail_2.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.searched_dst_thumbnail_2.setFrameShape(QFrame.NoFrame)
        self.searched_dst_thumbnail_2.setAlignment(Qt.AlignCenter)
        self.searched_dst_thumbnail_2.setWordWrap(True)
        self.searched_dst_thumbnail_2.setMargin(2)
        self.searched_dst_name_2 = QLabel(self.dataset_found_widget_2)
        self.searched_dst_name_2.setObjectName(u"searched_dst_name_2")
        self.searched_dst_name_2.setGeometry(QRect(280, 80, 121, 41))
        self.searched_dst_size_2 = QLabel(self.dataset_found_widget_2)
        self.searched_dst_size_2.setObjectName(u"searched_dst_size_2")
        self.searched_dst_size_2.setGeometry(QRect(280, 140, 121, 41))
        self.searched_dst_cancel_btn_2 = QPushButton(self.dataset_found_widget_2)
        self.searched_dst_cancel_btn_2.setObjectName(u"searched_dst_cancel_btn_2")
        self.searched_dst_cancel_btn_2.setGeometry(QRect(280, 240, 121, 41))
        self.searched_dst_cancel_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.dataset_not_found_widget_2 = QWidget(self.datasets_widget_7)
        self.dataset_not_found_widget_2.setObjectName(u"dataset_not_found_widget_2")
        self.dataset_not_found_widget_2.setGeometry(QRect(50, 30, 251, 161))
        self.dataset_not_found_widget_2.setFont(font)
        self.dataset_not_found_widget_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_36 = QLabel(self.dataset_not_found_widget_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(70, 20, 121, 41))
        self.label_36.setFont(font5)
        self.label_36.setStyleSheet(u"color:rgb(255, 85, 0);")
        self.label_36.setScaledContents(False)
        self.view_searched_ok_btn_2 = QPushButton(self.dataset_not_found_widget_2)
        self.view_searched_ok_btn_2.setObjectName(u"view_searched_ok_btn_2")
        self.view_searched_ok_btn_2.setGeometry(QRect(70, 80, 121, 41))
        self.view_searched_ok_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.dataset_found_widget_2.raise_()
        self.dataset_not_found_widget_2.raise_()
        self.label_65.raise_()
        self.search_dataset_2.raise_()
        self.comboBox_4.raise_()
        self.label_222.raise_()
        self.label_229.raise_()
        self.label_230.raise_()
        self.label_228.raise_()
        self.available_datasets_widget_2.raise_()
        self.stackedWidget_model_training.addWidget(self.select_dataset_page)
        self.model_train_options_page = QWidget()
        self.model_train_options_page.setObjectName(u"model_train_options_page")
        self.datasets_widget_8 = QWidget(self.model_train_options_page)
        self.datasets_widget_8.setObjectName(u"datasets_widget_8")
        self.datasets_widget_8.setGeometry(QRect(10, 30, 661, 421))
        self.datasets_widget_8.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_221 = QLabel(self.datasets_widget_8)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setGeometry(QRect(30, 10, 111, 41))
        self.update_algo_btn = QPushButton(self.datasets_widget_8)
        self.update_algo_btn.setObjectName(u"update_algo_btn")
        self.update_algo_btn.setGeometry(QRect(470, 20, 161, 41))
        self.update_algo_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_algo_widget = QWidget(self.datasets_widget_8)
        self.update_algo_widget.setObjectName(u"update_algo_widget")
        self.update_algo_widget.setGeometry(QRect(130, 100, 481, 231))
        self.update_algo_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.update_algo_ok_btn = QPushButton(self.update_algo_widget)
        self.update_algo_ok_btn.setObjectName(u"update_algo_ok_btn")
        self.update_algo_ok_btn.setGeometry(QRect(70, 170, 151, 41))
        self.update_algo_ok_btn.setFont(font)
        self.update_algo_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_algo_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_39 = QLabel(self.update_algo_widget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(140, 20, 201, 41))
        self.label_39.setAlignment(Qt.AlignCenter)
        self.update_algo_cancel_btn = QPushButton(self.update_algo_widget)
        self.update_algo_cancel_btn.setObjectName(u"update_algo_cancel_btn")
        self.update_algo_cancel_btn.setGeometry(QRect(250, 170, 151, 41))
        self.update_algo_cancel_btn.setFont(font)
        self.update_algo_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_algo_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.admin_key = QLineEdit(self.update_algo_widget)
        self.admin_key.setObjectName(u"admin_key")
        self.admin_key.setGeometry(QRect(110, 80, 250, 30))
        self.admin_key.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.admin_key.setEchoMode(QLineEdit.Password)
        self.key_match_error = QLabel(self.update_algo_widget)
        self.key_match_error.setObjectName(u"key_match_error")
        self.key_match_error.setGeometry(QRect(110, 120, 231, 41))
        self.key_match_error.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.key_match_error.setAlignment(Qt.AlignCenter)
        self.key_match_error.setWordWrap(True)
        self.model_train_widget = QWidget(self.datasets_widget_8)
        self.model_train_widget.setObjectName(u"model_train_widget")
        self.model_train_widget.setGeometry(QRect(80, 70, 541, 331))
        self.model_train_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_223 = QLabel(self.model_train_widget)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setGeometry(QRect(310, 0, 111, 41))
        self.edit_dst_btn = QPushButton(self.model_train_widget)
        self.edit_dst_btn.setObjectName(u"edit_dst_btn")
        self.edit_dst_btn.setGeometry(QRect(310, 210, 151, 41))
        self.edit_dst_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.change_dst_btn = QPushButton(self.model_train_widget)
        self.change_dst_btn.setObjectName(u"change_dst_btn")
        self.change_dst_btn.setGeometry(QRect(310, 270, 151, 41))
        self.change_dst_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_225 = QLabel(self.model_train_widget)
        self.label_225.setObjectName(u"label_225")
        self.label_225.setGeometry(QRect(440, 0, 71, 41))
        self.label_224 = QLabel(self.model_train_widget)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setGeometry(QRect(310, 60, 151, 121))
        self.label_224.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_224.setFrameShape(QFrame.NoFrame)
        self.label_224.setAlignment(Qt.AlignCenter)
        self.label_224.setWordWrap(True)
        self.label_224.setMargin(2)
        self.label_224.setIndent(0)
        self.label_226 = QLabel(self.model_train_widget)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setGeometry(QRect(80, 10, 111, 71))
        self.label_226.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_226.setScaledContents(True)
        self.label_226.setAlignment(Qt.AlignCenter)
        self.label_226.setMargin(15)
        self.label_220 = QLabel(self.model_train_widget)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setGeometry(QRect(10, 0, 241, 331))
        self.label_220.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_220.setFrameShape(QFrame.NoFrame)
        self.label_220.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_220.setWordWrap(True)
        self.label_220.setMargin(36)
        self.label_227 = QLabel(self.model_train_widget)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setGeometry(QRect(30, 80, 201, 191))
        self.label_227.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_227.setFrameShape(QFrame.NoFrame)
        self.label_227.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_227.setWordWrap(True)
        self.label_227.setMargin(0)
        self.run_gan_btn = QPushButton(self.model_train_widget)
        self.run_gan_btn.setObjectName(u"run_gan_btn")
        self.run_gan_btn.setGeometry(QRect(50, 270, 161, 41))
        self.run_gan_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_223.raise_()
        self.edit_dst_btn.raise_()
        self.change_dst_btn.raise_()
        self.label_225.raise_()
        self.label_224.raise_()
        self.label_220.raise_()
        self.label_227.raise_()
        self.label_226.raise_()
        self.run_gan_btn.raise_()
        self.update_algo_widget.raise_()
        self.label_221.raise_()
        self.update_algo_btn.raise_()
        self.model_train_widget.raise_()
        self.stackedWidget_model_training.addWidget(self.model_train_options_page)
        self.model_progress_page = QWidget()
        self.model_progress_page.setObjectName(u"model_progress_page")
        self.datasets_widget_10 = QWidget(self.model_progress_page)
        self.datasets_widget_10.setObjectName(u"datasets_widget_10")
        self.datasets_widget_10.setGeometry(QRect(0, 20, 721, 421))
        self.datasets_widget_10.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_238 = QLabel(self.datasets_widget_10)
        self.label_238.setObjectName(u"label_238")
        self.label_238.setGeometry(QRect(30, 10, 161, 41))
        self.rerun_gan_btn = QPushButton(self.datasets_widget_10)
        self.rerun_gan_btn.setObjectName(u"rerun_gan_btn")
        self.rerun_gan_btn.setGeometry(QRect(20, 280, 161, 41))
        self.rerun_gan_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_training_btn = QPushButton(self.datasets_widget_10)
        self.cancel_training_btn.setObjectName(u"cancel_training_btn")
        self.cancel_training_btn.setGeometry(QRect(20, 340, 161, 41))
        self.cancel_training_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_242 = QLabel(self.datasets_widget_10)
        self.label_242.setObjectName(u"label_242")
        self.label_242.setGeometry(QRect(210, 50, 501, 351))
        self.label_242.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_242.setFrameShape(QFrame.NoFrame)
        self.label_242.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_242.setWordWrap(True)
        self.label_242.setMargin(36)
        self.label_243 = QLabel(self.datasets_widget_10)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setGeometry(QRect(40, 50, 111, 81))
        self.label_243.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_243.setScaledContents(True)
        self.label_243.setAlignment(Qt.AlignCenter)
        self.label_243.setMargin(15)
        self.training_progressBar = QProgressBar(self.datasets_widget_10)
        self.training_progressBar.setObjectName(u"training_progressBar")
        self.training_progressBar.setGeometry(QRect(410, 140, 271, 41))
        self.training_progressBar.setLayoutDirection(Qt.LeftToRight)
        self.training_progressBar.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.training_progressBar.setMaximum(15000)
        self.training_progressBar.setValue(0)
        self.training_progressBar.setAlignment(Qt.AlignCenter)
        self.label_239 = QLabel(self.datasets_widget_10)
        self.label_239.setObjectName(u"label_239")
        self.label_239.setGeometry(QRect(230, 140, 161, 41))
        self.label_239.setAlignment(Qt.AlignCenter)
        self.label_240 = QLabel(self.datasets_widget_10)
        self.label_240.setObjectName(u"label_240")
        self.label_240.setGeometry(QRect(230, 200, 161, 41))
        self.label_240.setAlignment(Qt.AlignCenter)
        self.hours_2 = QLCDNumber(self.datasets_widget_10)
        self.hours_2.setObjectName(u"hours_2")
        self.hours_2.setGeometry(QRect(410, 200, 71, 41))
        self.hours_2.setFrameShadow(QFrame.Raised)
        self.label_244 = QLabel(self.datasets_widget_10)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setGeometry(QRect(230, 270, 161, 41))
        self.label_244.setAlignment(Qt.AlignCenter)
        self.epoch = QLCDNumber(self.datasets_widget_10)
        self.epoch.setObjectName(u"epoch")
        self.epoch.setGeometry(QRect(410, 270, 71, 41))
        self.label_245 = QLabel(self.datasets_widget_10)
        self.label_245.setObjectName(u"label_245")
        self.label_245.setGeometry(QRect(230, 340, 161, 41))
        self.label_245.setAlignment(Qt.AlignCenter)
        self.genrated_images_count = QLCDNumber(self.datasets_widget_10)
        self.genrated_images_count.setObjectName(u"genrated_images_count")
        self.genrated_images_count.setGeometry(QRect(410, 340, 71, 41))
        self.label_246 = QLabel(self.datasets_widget_10)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setGeometry(QRect(490, 200, 51, 41))
        self.label_246.setAlignment(Qt.AlignCenter)
        self.minutes = QLCDNumber(self.datasets_widget_10)
        self.minutes.setObjectName(u"minutes")
        self.minutes.setGeometry(QRect(550, 200, 71, 41))
        self.label_247 = QLabel(self.datasets_widget_10)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setGeometry(QRect(630, 200, 61, 41))
        self.label_247.setAlignment(Qt.AlignCenter)
        self.view_generated_imgs_btn = QPushButton(self.datasets_widget_10)
        self.view_generated_imgs_btn.setObjectName(u"view_generated_imgs_btn")
        self.view_generated_imgs_btn.setGeometry(QRect(520, 340, 161, 41))
        self.view_generated_imgs_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-window-restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.view_generated_imgs_btn.setIcon(icon5)
        self.label_251 = QLabel(self.datasets_widget_10)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setGeometry(QRect(530, 270, 71, 41))
        self.label_251.setAlignment(Qt.AlignCenter)
        self.total_epochs = QLCDNumber(self.datasets_widget_10)
        self.total_epochs.setObjectName(u"total_epochs")
        self.total_epochs.setGeometry(QRect(610, 270, 71, 41))
        self.total_epochs.setProperty("value", 15000.000000000000000)
        self.total_epochs.setProperty("intValue", 15000)
        self.label_252 = QLabel(self.datasets_widget_10)
        self.label_252.setObjectName(u"label_252")
        self.label_252.setGeometry(QRect(230, 80, 161, 41))
        self.label_252.setAlignment(Qt.AlignCenter)
        self.dataset_processing_bar = QProgressBar(self.datasets_widget_10)
        self.dataset_processing_bar.setObjectName(u"dataset_processing_bar")
        self.dataset_processing_bar.setGeometry(QRect(410, 80, 271, 41))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setItalic(False)
        self.dataset_processing_bar.setFont(font6)
        self.dataset_processing_bar.setCursor(QCursor(Qt.ArrowCursor))
        self.dataset_processing_bar.setLayoutDirection(Qt.LeftToRight)
        self.dataset_processing_bar.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.dataset_processing_bar.setValue(0)
        self.dataset_processing_bar.setAlignment(Qt.AlignCenter)
        self.label_233 = QLabel(self.datasets_widget_10)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setGeometry(QRect(10, 130, 181, 121))
        self.label_233.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_233.setFrameShape(QFrame.NoFrame)
        self.label_233.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_233.setWordWrap(True)
        self.label_233.setMargin(10)
        self.cancel_training_confirm_widget = QWidget(self.datasets_widget_10)
        self.cancel_training_confirm_widget.setObjectName(u"cancel_training_confirm_widget")
        self.cancel_training_confirm_widget.setGeometry(QRect(230, 100, 451, 241))
        self.cancel_training_confirm_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.cancel_training_confirm_ok_btn = QPushButton(self.cancel_training_confirm_widget)
        self.cancel_training_confirm_ok_btn.setObjectName(u"cancel_training_confirm_ok_btn")
        self.cancel_training_confirm_ok_btn.setGeometry(QRect(40, 150, 151, 41))
        self.cancel_training_confirm_ok_btn.setFont(font)
        self.cancel_training_confirm_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_training_confirm_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_37 = QLabel(self.cancel_training_confirm_widget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(60, 30, 341, 41))
        self.label_37.setAlignment(Qt.AlignCenter)
        self.cancel_training_confirm_cancel_btn = QPushButton(self.cancel_training_confirm_widget)
        self.cancel_training_confirm_cancel_btn.setObjectName(u"cancel_training_confirm_cancel_btn")
        self.cancel_training_confirm_cancel_btn.setGeometry(QRect(270, 150, 151, 41))
        self.cancel_training_confirm_cancel_btn.setFont(font)
        self.cancel_training_confirm_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_training_confirm_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_10 = QLabel(self.cancel_training_confirm_widget)
        self.account_verify_status_10.setObjectName(u"account_verify_status_10")
        self.account_verify_status_10.setGeometry(QRect(80, 80, 291, 41))
        self.account_verify_status_10.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status_10.setAlignment(Qt.AlignCenter)
        self.rerun_training_confirm_widget = QWidget(self.datasets_widget_10)
        self.rerun_training_confirm_widget.setObjectName(u"rerun_training_confirm_widget")
        self.rerun_training_confirm_widget.setGeometry(QRect(230, 80, 451, 241))
        self.rerun_training_confirm_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.rerun_training_confirm_ok_btn = QPushButton(self.rerun_training_confirm_widget)
        self.rerun_training_confirm_ok_btn.setObjectName(u"rerun_training_confirm_ok_btn")
        self.rerun_training_confirm_ok_btn.setGeometry(QRect(40, 150, 151, 41))
        self.rerun_training_confirm_ok_btn.setFont(font)
        self.rerun_training_confirm_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.rerun_training_confirm_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_38 = QLabel(self.rerun_training_confirm_widget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(60, 30, 341, 41))
        self.label_38.setAlignment(Qt.AlignCenter)
        self.rerun_training_confirm_cancel_btn = QPushButton(self.rerun_training_confirm_widget)
        self.rerun_training_confirm_cancel_btn.setObjectName(u"rerun_training_confirm_cancel_btn")
        self.rerun_training_confirm_cancel_btn.setGeometry(QRect(270, 150, 151, 41))
        self.rerun_training_confirm_cancel_btn.setFont(font)
        self.rerun_training_confirm_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.rerun_training_confirm_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_11 = QLabel(self.rerun_training_confirm_widget)
        self.account_verify_status_11.setObjectName(u"account_verify_status_11")
        self.account_verify_status_11.setGeometry(QRect(80, 80, 291, 41))
        self.account_verify_status_11.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status_11.setAlignment(Qt.AlignCenter)
        self.rerun_training_confirm_widget.raise_()
        self.cancel_training_confirm_widget.raise_()
        self.label_238.raise_()
        self.rerun_gan_btn.raise_()
        self.cancel_training_btn.raise_()
        self.label_242.raise_()
        self.label_243.raise_()
        self.training_progressBar.raise_()
        self.label_239.raise_()
        self.label_240.raise_()
        self.hours_2.raise_()
        self.label_244.raise_()
        self.epoch.raise_()
        self.label_245.raise_()
        self.genrated_images_count.raise_()
        self.label_246.raise_()
        self.minutes.raise_()
        self.label_247.raise_()
        self.view_generated_imgs_btn.raise_()
        self.label_251.raise_()
        self.total_epochs.raise_()
        self.label_252.raise_()
        self.dataset_processing_bar.raise_()
        self.label_233.raise_()
        self.stackedWidget_model_training.addWidget(self.model_progress_page)
        self.train_pause_page = QWidget()
        self.train_pause_page.setObjectName(u"train_pause_page")
        self.datasets_widget_11 = QWidget(self.train_pause_page)
        self.datasets_widget_11.setObjectName(u"datasets_widget_11")
        self.datasets_widget_11.setGeometry(QRect(10, 20, 721, 421))
        self.datasets_widget_11.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_241 = QLabel(self.datasets_widget_11)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setGeometry(QRect(30, 10, 161, 41))
        self.pushButton_17 = QPushButton(self.datasets_widget_11)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(20, 100, 161, 41))
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_21 = QPushButton(self.datasets_widget_11)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(20, 230, 161, 41))
        self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_22 = QPushButton(self.datasets_widget_11)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(20, 300, 161, 41))
        self.pushButton_22.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_248 = QLabel(self.datasets_widget_11)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setGeometry(QRect(200, 20, 501, 351))
        self.label_248.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_248.setFrameShape(QFrame.NoFrame)
        self.label_248.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_248.setWordWrap(True)
        self.label_248.setMargin(36)
        self.label_249 = QLabel(self.datasets_widget_11)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setGeometry(QRect(600, 30, 81, 61))
        self.label_249.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_249.setScaledContents(True)
        self.label_249.setAlignment(Qt.AlignCenter)
        self.label_249.setMargin(15)
        self.label_253 = QLabel(self.datasets_widget_11)
        self.label_253.setObjectName(u"label_253")
        self.label_253.setGeometry(QRect(220, 310, 161, 41))
        self.label_253.setAlignment(Qt.AlignCenter)
        self.lcdNumber_7 = QLCDNumber(self.datasets_widget_11)
        self.lcdNumber_7.setObjectName(u"lcdNumber_7")
        self.lcdNumber_7.setGeometry(QRect(400, 310, 71, 41))
        self.pushButton_23 = QPushButton(self.datasets_widget_11)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(510, 310, 161, 41))
        self.pushButton_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_250 = QLabel(self.datasets_widget_11)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setGeometry(QRect(250, 90, 291, 171))
        self.label_250.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_250.setFrameShape(QFrame.NoFrame)
        self.label_250.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_250.setWordWrap(True)
        self.label_250.setMargin(0)
        self.pushButton_24 = QPushButton(self.datasets_widget_11)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(20, 160, 161, 41))
        self.pushButton_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_25 = QPushButton(self.datasets_widget_11)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(510, 230, 161, 41))
        self.pushButton_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.stackedWidget_model_training.addWidget(self.train_pause_page)
        self.stackedWidget_content_pages.addWidget(self.model_training_page)
        self.stylegan_page = QWidget()
        self.stylegan_page.setObjectName(u"stylegan_page")
        self.stackedWidget_stylegan = QStackedWidget(self.stylegan_page)
        self.stackedWidget_stylegan.setObjectName(u"stackedWidget_stylegan")
        self.stackedWidget_stylegan.setGeometry(QRect(0, 0, 731, 451))
        self.google_account_page = QWidget()
        self.google_account_page.setObjectName(u"google_account_page")
        self.user_name_google = QLineEdit(self.google_account_page)
        self.user_name_google.setObjectName(u"user_name_google")
        self.user_name_google.setGeometry(QRect(120, 170, 250, 30))
        self.user_name_google.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.user_password_google = QLineEdit(self.google_account_page)
        self.user_password_google.setObjectName(u"user_password_google")
        self.user_password_google.setGeometry(QRect(120, 230, 250, 30))
        self.user_password_google.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.user_password_google.setEchoMode(QLineEdit.Password)
        self.google_verify_code_widget = QWidget(self.google_account_page)
        self.google_verify_code_widget.setObjectName(u"google_verify_code_widget")
        self.google_verify_code_widget.setGeometry(QRect(100, 160, 601, 241))
        self.google_verify_code_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;")
        self.google_verify_code_widget_ok_btn = QPushButton(self.google_verify_code_widget)
        self.google_verify_code_widget_ok_btn.setObjectName(u"google_verify_code_widget_ok_btn")
        self.google_verify_code_widget_ok_btn.setGeometry(QRect(150, 170, 151, 41))
        self.google_verify_code_widget_ok_btn.setFont(font)
        self.google_verify_code_widget_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.google_verify_code_widget_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_46 = QLabel(self.google_verify_code_widget)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(120, 20, 351, 41))
        self.label_46.setAlignment(Qt.AlignCenter)
        self.google_verify_code_widget_cancel_btn = QPushButton(self.google_verify_code_widget)
        self.google_verify_code_widget_cancel_btn.setObjectName(u"google_verify_code_widget_cancel_btn")
        self.google_verify_code_widget_cancel_btn.setGeometry(QRect(310, 170, 151, 41))
        self.google_verify_code_widget_cancel_btn.setFont(font)
        self.google_verify_code_widget_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.google_verify_code_widget_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.google_verify_code = QLineEdit(self.google_verify_code_widget)
        self.google_verify_code.setObjectName(u"google_verify_code")
        self.google_verify_code.setGeometry(QRect(170, 80, 250, 30))
        self.google_verify_code.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.verify_code_error = QLabel(self.google_verify_code_widget)
        self.verify_code_error.setObjectName(u"verify_code_error")
        self.verify_code_error.setGeometry(QRect(170, 120, 231, 41))
        self.verify_code_error.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.verify_code_error.setAlignment(Qt.AlignCenter)
        self.verify_code_error.setWordWrap(True)
        self.label_103 = QLabel(self.google_verify_code_widget)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setGeometry(QRect(150, 70, 21, 41))
        self.label_103.setAlignment(Qt.AlignCenter)
        self.google_verify_code_widget_resend_btn = QPushButton(self.google_verify_code_widget)
        self.google_verify_code_widget_resend_btn.setObjectName(u"google_verify_code_widget_resend_btn")
        self.google_verify_code_widget_resend_btn.setGeometry(QRect(480, 120, 111, 41))
        self.google_verify_code_widget_resend_btn.setFont(font)
        self.google_verify_code_widget_resend_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.google_verify_code_widget_resend_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.verify_code_error.raise_()
        self.google_verify_code_widget_ok_btn.raise_()
        self.label_46.raise_()
        self.google_verify_code_widget_cancel_btn.raise_()
        self.google_verify_code.raise_()
        self.label_103.raise_()
        self.google_verify_code_widget_resend_btn.raise_()
        self.recovery_message_widget_2 = QWidget(self.google_account_page)
        self.recovery_message_widget_2.setObjectName(u"recovery_message_widget_2")
        self.recovery_message_widget_2.setGeometry(QRect(130, 160, 481, 191))
        self.recovery_message_widget_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.recovery_message_widget_ok_btn_2 = QPushButton(self.recovery_message_widget_2)
        self.recovery_message_widget_ok_btn_2.setObjectName(u"recovery_message_widget_ok_btn_2")
        self.recovery_message_widget_ok_btn_2.setGeometry(QRect(160, 120, 151, 41))
        self.recovery_message_widget_ok_btn_2.setFont(font)
        self.recovery_message_widget_ok_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.recovery_message_widget_ok_btn_2.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_47 = QLabel(self.recovery_message_widget_2)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(50, 30, 381, 71))
        self.label_47.setAlignment(Qt.AlignCenter)
        self.new_password_widget_2 = QWidget(self.google_account_page)
        self.new_password_widget_2.setObjectName(u"new_password_widget_2")
        self.new_password_widget_2.setGeometry(QRect(150, 0, 511, 341))
        self.new_password_widget_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.new_password_widget_ok_btn_2 = QPushButton(self.new_password_widget_2)
        self.new_password_widget_ok_btn_2.setObjectName(u"new_password_widget_ok_btn_2")
        self.new_password_widget_ok_btn_2.setGeometry(QRect(80, 270, 151, 41))
        self.new_password_widget_ok_btn_2.setFont(font)
        self.new_password_widget_ok_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_password_widget_ok_btn_2.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_48 = QLabel(self.new_password_widget_2)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(140, 20, 201, 41))
        self.label_48.setAlignment(Qt.AlignCenter)
        self.new_password_widget_cancel_btn_2 = QPushButton(self.new_password_widget_2)
        self.new_password_widget_cancel_btn_2.setObjectName(u"new_password_widget_cancel_btn_2")
        self.new_password_widget_cancel_btn_2.setGeometry(QRect(290, 270, 151, 41))
        self.new_password_widget_cancel_btn_2.setFont(font)
        self.new_password_widget_cancel_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_password_widget_cancel_btn_2.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.new_password_2 = QLineEdit(self.new_password_widget_2)
        self.new_password_2.setObjectName(u"new_password_2")
        self.new_password_2.setGeometry(QRect(110, 90, 250, 30))
        self.new_password_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.new_password_2.setEchoMode(QLineEdit.Password)
        self.new_password_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.confirm_new_password_2 = QLineEdit(self.new_password_widget_2)
        self.confirm_new_password_2.setObjectName(u"confirm_new_password_2")
        self.confirm_new_password_2.setGeometry(QRect(110, 180, 250, 30))
        self.confirm_new_password_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.confirm_new_password_2.setEchoMode(QLineEdit.Password)
        self.new_password_error_2 = QLabel(self.new_password_widget_2)
        self.new_password_error_2.setObjectName(u"new_password_error_2")
        self.new_password_error_2.setGeometry(QRect(80, 120, 301, 61))
        self.new_password_error_2.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.new_password_error_2.setAlignment(Qt.AlignCenter)
        self.new_password_error_2.setWordWrap(True)
        self.new_password_confirm_error_2 = QLabel(self.new_password_widget_2)
        self.new_password_confirm_error_2.setObjectName(u"new_password_confirm_error_2")
        self.new_password_confirm_error_2.setGeometry(QRect(120, 220, 231, 41))
        self.new_password_confirm_error_2.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.new_password_confirm_error_2.setAlignment(Qt.AlignCenter)
        self.new_password_confirm_error_2.setWordWrap(True)
        self.login_google_btn = QPushButton(self.google_account_page)
        self.login_google_btn.setObjectName(u"login_google_btn")
        self.login_google_btn.setGeometry(QRect(140, 290, 250, 40))
        self.login_google_btn.setFont(font)
        self.login_google_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_google_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.login_fail_notification_2 = QWidget(self.google_account_page)
        self.login_fail_notification_2.setObjectName(u"login_fail_notification_2")
        self.login_fail_notification_2.setGeometry(QRect(180, 150, 551, 241))
        self.login_fail_notification_2.setFont(font)
        self.login_fail_notification_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_49 = QLabel(self.login_fail_notification_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(220, 30, 135, 18))
        self.label_49.setFont(font5)
        self.label_49.setScaledContents(False)
        self.label_49.setAlignment(Qt.AlignCenter)
        self.login_fail_message_2 = QLabel(self.login_fail_notification_2)
        self.login_fail_message_2.setObjectName(u"login_fail_message_2")
        self.login_fail_message_2.setGeometry(QRect(150, 80, 261, 61))
        self.login_fail_message_2.setLayoutDirection(Qt.LeftToRight)
        self.login_fail_message_2.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.login_fail_message_2.setAlignment(Qt.AlignCenter)
        self.login_fail_ok_btn_2 = QPushButton(self.login_fail_notification_2)
        self.login_fail_ok_btn_2.setObjectName(u"login_fail_ok_btn_2")
        self.login_fail_ok_btn_2.setGeometry(QRect(210, 160, 141, 41))
        self.login_fail_ok_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.forget_pass_name_google_btn = QPushButton(self.google_account_page)
        self.forget_pass_name_google_btn.setObjectName(u"forget_pass_name_google_btn")
        self.forget_pass_name_google_btn.setGeometry(QRect(130, 370, 301, 31))
        self.forget_pass_name_google_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.forget_pass_name_google_btn.setStyleSheet(u"color:rgb(23, 201, 255);")
        self.login_success_notification_2 = QWidget(self.google_account_page)
        self.login_success_notification_2.setObjectName(u"login_success_notification_2")
        self.login_success_notification_2.setGeometry(QRect(180, 150, 551, 241))
        self.login_success_notification_2.setFont(font)
        self.login_success_notification_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_60 = QLabel(self.login_success_notification_2)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(220, 30, 121, 41))
        self.label_60.setFont(font5)
        self.label_60.setScaledContents(False)
        self.login_success_ok_btn_2 = QPushButton(self.login_success_notification_2)
        self.login_success_ok_btn_2.setObjectName(u"login_success_ok_btn_2")
        self.login_success_ok_btn_2.setGeometry(QRect(220, 150, 121, 41))
        self.login_success_ok_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_form_2 = QLabel(self.google_account_page)
        self.login_form_2.setObjectName(u"login_form_2")
        self.login_form_2.setGeometry(QRect(0, 0, 721, 431))
        self.login_form_2.setStyleSheet(u"background-color:rgba(16,30,41,255);\n"
"border-radius:10px;\n"
"\n"
"")
        self.widget_4 = QWidget(self.google_account_page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(450, 160, 251, 191))
        self.widget_4.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.signup_google_btn = QPushButton(self.widget_4)
        self.signup_google_btn.setObjectName(u"signup_google_btn")
        self.signup_google_btn.setGeometry(QRect(50, 130, 151, 41))
        self.signup_google_btn.setFont(font)
        self.signup_google_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.signup_google_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_77 = QLabel(self.widget_4)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(60, 20, 131, 41))
        self.label_77.setAlignment(Qt.AlignCenter)
        self.logoW_6 = QLabel(self.widget_4)
        self.logoW_6.setObjectName(u"logoW_6")
        self.logoW_6.setGeometry(QRect(90, 60, 61, 61))
        self.logoW_6.setPixmap(QPixmap(u":/images/images/images/google_g.png"))
        self.logoW_6.setScaledContents(True)
        self.new_credentials_success_2 = QWidget(self.google_account_page)
        self.new_credentials_success_2.setObjectName(u"new_credentials_success_2")
        self.new_credentials_success_2.setGeometry(QRect(100, 90, 551, 241))
        self.new_credentials_success_2.setFont(font)
        self.new_credentials_success_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_78 = QLabel(self.new_credentials_success_2)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(220, 20, 131, 41))
        self.label_78.setFont(font5)
        self.label_78.setScaledContents(False)
        self.new_credentials_ok_btn_2 = QPushButton(self.new_credentials_success_2)
        self.new_credentials_ok_btn_2.setObjectName(u"new_credentials_ok_btn_2")
        self.new_credentials_ok_btn_2.setGeometry(QRect(220, 170, 121, 41))
        self.new_credentials_ok_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_79 = QLabel(self.new_credentials_success_2)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(170, 90, 81, 16))
        self.label_84 = QLabel(self.new_credentials_success_2)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(170, 130, 81, 16))
        self.new_uname_2 = QLabel(self.new_credentials_success_2)
        self.new_uname_2.setObjectName(u"new_uname_2")
        self.new_uname_2.setGeometry(QRect(270, 90, 121, 16))
        self.new_uname_2.setStyleSheet(u"color:rgb(47, 154, 255)")
        self.new_uname_2.setAlignment(Qt.AlignCenter)
        self.new_upass_2 = QLabel(self.new_credentials_success_2)
        self.new_upass_2.setObjectName(u"new_upass_2")
        self.new_upass_2.setGeometry(QRect(270, 130, 121, 16))
        self.new_upass_2.setStyleSheet(u"color:rgb(47, 154, 255)")
        self.new_upass_2.setAlignment(Qt.AlignCenter)
        self.logoW_4 = QLabel(self.google_account_page)
        self.logoW_4.setObjectName(u"logoW_4")
        self.logoW_4.setGeometry(QRect(500, 10, 191, 121))
        self.logoW_4.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.logoW_4.setScaledContents(True)
        self.logoW_5 = QLabel(self.google_account_page)
        self.logoW_5.setObjectName(u"logoW_5")
        self.logoW_5.setGeometry(QRect(130, 60, 261, 91))
        self.logoW_5.setPixmap(QPixmap(u":/images/images/images/google-logo.png"))
        self.logoW_5.setScaledContents(True)
        self.login_loading_label = QLabel(self.google_account_page)
        self.login_loading_label.setObjectName(u"login_loading_label")
        self.login_loading_label.setGeometry(QRect(110, 170, 291, 171))
        self.login_loading_label.setAlignment(Qt.AlignCenter)
        self.stackedWidget_stylegan.addWidget(self.google_account_page)
        self.login_success_notification_2.raise_()
        self.new_credentials_success_2.raise_()
        self.google_verify_code_widget.raise_()
        self.login_loading_label.raise_()
        self.login_fail_notification_2.raise_()
        self.recovery_message_widget_2.raise_()
        self.new_password_widget_2.raise_()
        self.login_form_2.raise_()
        self.user_name_google.raise_()
        self.user_password_google.raise_()
        self.widget_4.raise_()
        self.logoW_4.raise_()
        self.forget_pass_name_google_btn.raise_()
        self.login_google_btn.raise_()
        self.logoW_5.raise_()
        self.select_dataset_stylegan_page = QWidget()
        self.select_dataset_stylegan_page.setObjectName(u"select_dataset_stylegan_page")
        self.datasets_widget_9 = QWidget(self.select_dataset_stylegan_page)
        self.datasets_widget_9.setObjectName(u"datasets_widget_9")
        self.datasets_widget_9.setGeometry(QRect(10, 10, 661, 421))
        self.datasets_widget_9.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_66 = QLabel(self.datasets_widget_9)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(30, 10, 81, 41))
        self.search_dataset_3 = QLineEdit(self.datasets_widget_9)
        self.search_dataset_3.setObjectName(u"search_dataset_3")
        self.search_dataset_3.setGeometry(QRect(390, 20, 250, 30))
        self.search_dataset_3.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.comboBox_5 = QComboBox(self.datasets_widget_9)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(490, 380, 101, 34))
        self.comboBox_5.setFont(font)
        self.comboBox_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_5.setAutoFillBackground(False)
        self.comboBox_5.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_5.setIconSize(QSize(16, 16))
        self.comboBox_5.setFrame(True)
        self.label_234 = QLabel(self.datasets_widget_9)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setGeometry(QRect(450, 380, 41, 31))
        self.label_235 = QLabel(self.datasets_widget_9)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setGeometry(QRect(450, 140, 121, 81))
        self.label_235.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_235.setScaledContents(True)
        self.label_235.setAlignment(Qt.AlignCenter)
        self.label_235.setMargin(15)
        self.label_236 = QLabel(self.datasets_widget_9)
        self.label_236.setObjectName(u"label_236")
        self.label_236.setGeometry(QRect(390, 100, 241, 261))
        self.label_236.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_236.setFrameShape(QFrame.NoFrame)
        self.label_236.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_236.setWordWrap(True)
        self.label_236.setMargin(36)
        self.label_237 = QLabel(self.datasets_widget_9)
        self.label_237.setObjectName(u"label_237")
        self.label_237.setGeometry(QRect(410, 230, 201, 121))
        self.label_237.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_237.setFrameShape(QFrame.NoFrame)
        self.label_237.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_237.setWordWrap(True)
        self.label_237.setMargin(0)
        self.available_datasets_widget_3 = QWidget(self.datasets_widget_9)
        self.available_datasets_widget_3.setObjectName(u"available_datasets_widget_3")
        self.available_datasets_widget_3.setGeometry(QRect(-20, 50, 381, 361))
        self.available_datasets_widget_3.setFont(font)
        self.available_datasets_widget_3.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_67 = QLabel(self.available_datasets_widget_3)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(240, 10, 71, 41))
        self.label_76 = QLabel(self.available_datasets_widget_3)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(60, 10, 71, 41))
        self.anime_thumbnail_btn_3 = QPushButton(self.available_datasets_widget_3)
        self.anime_thumbnail_btn_3.setObjectName(u"anime_thumbnail_btn_3")
        self.anime_thumbnail_btn_3.setGeometry(QRect(50, 60, 141, 121))
        self.anime_thumbnail_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.anime_thumbnail_btn_3.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.human_thumbnail_btn_3 = QPushButton(self.available_datasets_widget_3)
        self.human_thumbnail_btn_3.setObjectName(u"human_thumbnail_btn_3")
        self.human_thumbnail_btn_3.setGeometry(QRect(210, 60, 151, 121))
        self.human_thumbnail_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.human_thumbnail_btn_3.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.human_thumbnail_3 = QLabel(self.available_datasets_widget_3)
        self.human_thumbnail_3.setObjectName(u"human_thumbnail_3")
        self.human_thumbnail_3.setGeometry(QRect(210, 60, 151, 121))
        self.human_thumbnail_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.human_thumbnail_3.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.human_thumbnail_3.setFrameShape(QFrame.NoFrame)
        self.human_thumbnail_3.setAlignment(Qt.AlignCenter)
        self.human_thumbnail_3.setWordWrap(True)
        self.human_thumbnail_3.setMargin(2)
        self.anime_thumbnail_3 = QLabel(self.available_datasets_widget_3)
        self.anime_thumbnail_3.setObjectName(u"anime_thumbnail_3")
        self.anime_thumbnail_3.setGeometry(QRect(50, 60, 141, 121))
        self.anime_thumbnail_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.anime_thumbnail_3.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.anime_thumbnail_3.setFrameShape(QFrame.NoFrame)
        self.anime_thumbnail_3.setAlignment(Qt.AlignCenter)
        self.anime_thumbnail_3.setWordWrap(True)
        self.anime_thumbnail_3.setMargin(2)
        self.new_datset_thumbnail_btn_3 = QPushButton(self.available_datasets_widget_3)
        self.new_datset_thumbnail_btn_3.setObjectName(u"new_datset_thumbnail_btn_3")
        self.new_datset_thumbnail_btn_3.setGeometry(QRect(210, 230, 151, 121))
        self.new_datset_thumbnail_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_datset_thumbnail_btn_3.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_101 = QLabel(self.available_datasets_widget_3)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(50, 190, 71, 41))
        self.flower_thumbnail_btn_3 = QPushButton(self.available_datasets_widget_3)
        self.flower_thumbnail_btn_3.setObjectName(u"flower_thumbnail_btn_3")
        self.flower_thumbnail_btn_3.setGeometry(QRect(40, 230, 151, 121))
        self.flower_thumbnail_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.flower_thumbnail_btn_3.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_new_dataset_3 = QLabel(self.available_datasets_widget_3)
        self.label_new_dataset_3.setObjectName(u"label_new_dataset_3")
        self.label_new_dataset_3.setGeometry(QRect(230, 190, 91, 41))
        self.new_datset_thumbnail_3 = QLabel(self.available_datasets_widget_3)
        self.new_datset_thumbnail_3.setObjectName(u"new_datset_thumbnail_3")
        self.new_datset_thumbnail_3.setGeometry(QRect(210, 230, 151, 121))
        self.new_datset_thumbnail_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_datset_thumbnail_3.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.new_datset_thumbnail_3.setFrameShape(QFrame.NoFrame)
        self.new_datset_thumbnail_3.setAlignment(Qt.AlignCenter)
        self.new_datset_thumbnail_3.setWordWrap(True)
        self.new_datset_thumbnail_3.setMargin(2)
        self.flower_thumbnail_3 = QLabel(self.available_datasets_widget_3)
        self.flower_thumbnail_3.setObjectName(u"flower_thumbnail_3")
        self.flower_thumbnail_3.setGeometry(QRect(40, 230, 151, 121))
        self.flower_thumbnail_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.flower_thumbnail_3.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.flower_thumbnail_3.setFrameShape(QFrame.NoFrame)
        self.flower_thumbnail_3.setAlignment(Qt.AlignCenter)
        self.flower_thumbnail_3.setWordWrap(True)
        self.flower_thumbnail_3.setMargin(2)
        self.dataset_found_widget_3 = QWidget(self.datasets_widget_9)
        self.dataset_found_widget_3.setObjectName(u"dataset_found_widget_3")
        self.dataset_found_widget_3.setGeometry(QRect(130, 20, 501, 351))
        self.dataset_found_widget_3.setFont(font)
        self.dataset_found_widget_3.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_40 = QLabel(self.dataset_found_widget_3)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(80, 30, 101, 41))
        self.label_40.setFont(font5)
        self.label_40.setStyleSheet(u"color: rgb(170, 255, 0);")
        self.label_40.setScaledContents(False)
        self.view_searched_dst_btn_3 = QPushButton(self.dataset_found_widget_3)
        self.view_searched_dst_btn_3.setObjectName(u"view_searched_dst_btn_3")
        self.view_searched_dst_btn_3.setGeometry(QRect(80, 240, 121, 41))
        self.view_searched_dst_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.searched_dst_thumbnail_btn_3 = QPushButton(self.dataset_found_widget_3)
        self.searched_dst_thumbnail_btn_3.setObjectName(u"searched_dst_thumbnail_btn_3")
        self.searched_dst_thumbnail_btn_3.setGeometry(QRect(60, 90, 141, 121))
        self.searched_dst_thumbnail_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.searched_dst_thumbnail_btn_3.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.searched_dst_thumbnail_3 = QLabel(self.dataset_found_widget_3)
        self.searched_dst_thumbnail_3.setObjectName(u"searched_dst_thumbnail_3")
        self.searched_dst_thumbnail_3.setGeometry(QRect(60, 90, 141, 121))
        self.searched_dst_thumbnail_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.searched_dst_thumbnail_3.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.searched_dst_thumbnail_3.setFrameShape(QFrame.NoFrame)
        self.searched_dst_thumbnail_3.setAlignment(Qt.AlignCenter)
        self.searched_dst_thumbnail_3.setWordWrap(True)
        self.searched_dst_thumbnail_3.setMargin(2)
        self.searched_dst_name_3 = QLabel(self.dataset_found_widget_3)
        self.searched_dst_name_3.setObjectName(u"searched_dst_name_3")
        self.searched_dst_name_3.setGeometry(QRect(280, 80, 121, 41))
        self.searched_dst_size_3 = QLabel(self.dataset_found_widget_3)
        self.searched_dst_size_3.setObjectName(u"searched_dst_size_3")
        self.searched_dst_size_3.setGeometry(QRect(280, 140, 121, 41))
        self.searched_dst_cancel_btn_3 = QPushButton(self.dataset_found_widget_3)
        self.searched_dst_cancel_btn_3.setObjectName(u"searched_dst_cancel_btn_3")
        self.searched_dst_cancel_btn_3.setGeometry(QRect(280, 240, 121, 41))
        self.searched_dst_cancel_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.dataset_not_found_widget_3 = QWidget(self.datasets_widget_9)
        self.dataset_not_found_widget_3.setObjectName(u"dataset_not_found_widget_3")
        self.dataset_not_found_widget_3.setGeometry(QRect(50, 30, 251, 161))
        self.dataset_not_found_widget_3.setFont(font)
        self.dataset_not_found_widget_3.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_42 = QLabel(self.dataset_not_found_widget_3)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(70, 20, 121, 41))
        self.label_42.setFont(font5)
        self.label_42.setStyleSheet(u"color:rgb(255, 85, 0);")
        self.label_42.setScaledContents(False)
        self.view_searched_ok_btn_3 = QPushButton(self.dataset_not_found_widget_3)
        self.view_searched_ok_btn_3.setObjectName(u"view_searched_ok_btn_3")
        self.view_searched_ok_btn_3.setGeometry(QRect(70, 80, 121, 41))
        self.view_searched_ok_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.dataset_found_widget_3.raise_()
        self.dataset_not_found_widget_3.raise_()
        self.label_66.raise_()
        self.search_dataset_3.raise_()
        self.comboBox_5.raise_()
        self.label_234.raise_()
        self.label_236.raise_()
        self.label_237.raise_()
        self.available_datasets_widget_3.raise_()
        self.label_235.raise_()
        self.stackedWidget_stylegan.addWidget(self.select_dataset_stylegan_page)
        self.pretrained_models_page = QWidget()
        self.pretrained_models_page.setObjectName(u"pretrained_models_page")
        self.datasets_widget_13 = QWidget(self.pretrained_models_page)
        self.datasets_widget_13.setObjectName(u"datasets_widget_13")
        self.datasets_widget_13.setGeometry(QRect(10, 30, 661, 421))
        self.datasets_widget_13.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_254 = QLabel(self.datasets_widget_13)
        self.label_254.setObjectName(u"label_254")
        self.label_254.setGeometry(QRect(30, 10, 131, 51))
        self.label_254.setWordWrap(True)
        self.update_stylegan_algo_btn = QPushButton(self.datasets_widget_13)
        self.update_stylegan_algo_btn.setObjectName(u"update_stylegan_algo_btn")
        self.update_stylegan_algo_btn.setGeometry(QRect(470, 20, 161, 41))
        self.update_stylegan_algo_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_algo_widget_2 = QWidget(self.datasets_widget_13)
        self.update_algo_widget_2.setObjectName(u"update_algo_widget_2")
        self.update_algo_widget_2.setGeometry(QRect(130, 100, 481, 231))
        self.update_algo_widget_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.update_algo_ok_btn_2 = QPushButton(self.update_algo_widget_2)
        self.update_algo_ok_btn_2.setObjectName(u"update_algo_ok_btn_2")
        self.update_algo_ok_btn_2.setGeometry(QRect(70, 170, 151, 41))
        self.update_algo_ok_btn_2.setFont(font)
        self.update_algo_ok_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_algo_ok_btn_2.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_43 = QLabel(self.update_algo_widget_2)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(140, 20, 201, 41))
        self.label_43.setAlignment(Qt.AlignCenter)
        self.update_algo_cancel_btn_2 = QPushButton(self.update_algo_widget_2)
        self.update_algo_cancel_btn_2.setObjectName(u"update_algo_cancel_btn_2")
        self.update_algo_cancel_btn_2.setGeometry(QRect(250, 170, 151, 41))
        self.update_algo_cancel_btn_2.setFont(font)
        self.update_algo_cancel_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_algo_cancel_btn_2.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.admin_key_2 = QLineEdit(self.update_algo_widget_2)
        self.admin_key_2.setObjectName(u"admin_key_2")
        self.admin_key_2.setGeometry(QRect(110, 80, 250, 30))
        self.admin_key_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(42,86,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px\n"
"")
        self.admin_key_2.setEchoMode(QLineEdit.Password)
        self.key_match_error_2 = QLabel(self.update_algo_widget_2)
        self.key_match_error_2.setObjectName(u"key_match_error_2")
        self.key_match_error_2.setGeometry(QRect(110, 120, 231, 41))
        self.key_match_error_2.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.key_match_error_2.setAlignment(Qt.AlignCenter)
        self.key_match_error_2.setWordWrap(True)
        self.model_train_widget_2 = QWidget(self.datasets_widget_13)
        self.model_train_widget_2.setObjectName(u"model_train_widget_2")
        self.model_train_widget_2.setGeometry(QRect(30, 70, 591, 331))
        self.model_train_widget_2.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_258 = QLabel(self.model_train_widget_2)
        self.label_258.setObjectName(u"label_258")
        self.label_258.setGeometry(QRect(20, 10, 141, 101))
        self.label_258.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_258.setScaledContents(True)
        self.label_258.setAlignment(Qt.AlignCenter)
        self.label_258.setMargin(15)
        self.label_259 = QLabel(self.model_train_widget_2)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setGeometry(QRect(0, -10, 401, 331))
        self.label_259.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_259.setFrameShape(QFrame.NoFrame)
        self.label_259.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_259.setWordWrap(True)
        self.label_259.setMargin(36)
        self.label_260 = QLabel(self.model_train_widget_2)
        self.label_260.setObjectName(u"label_260")
        self.label_260.setGeometry(QRect(20, 110, 361, 161))
        self.label_260.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_260.setFrameShape(QFrame.NoFrame)
        self.label_260.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_260.setWordWrap(True)
        self.label_260.setMargin(0)
        self.style_gan1_btn = QPushButton(self.model_train_widget_2)
        self.style_gan1_btn.setObjectName(u"style_gan1_btn")
        self.style_gan1_btn.setGeometry(QRect(30, 270, 161, 41))
        self.style_gan1_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.style_gan2_btn = QPushButton(self.model_train_widget_2)
        self.style_gan2_btn.setObjectName(u"style_gan2_btn")
        self.style_gan2_btn.setGeometry(QRect(210, 270, 161, 41))
        self.style_gan2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_261 = QLabel(self.model_train_widget_2)
        self.label_261.setObjectName(u"label_261")
        self.label_261.setGeometry(QRect(240, 10, 121, 111))
        self.label_261.setPixmap(QPixmap(u":/images/images/images/nvidia1.png"))
        self.label_261.setScaledContents(True)
        self.label_261.setAlignment(Qt.AlignCenter)
        self.label_261.setMargin(15)
        self.label_262 = QLabel(self.model_train_widget_2)
        self.label_262.setObjectName(u"label_262")
        self.label_262.setGeometry(QRect(410, 0, 181, 171))
        self.label_262.setPixmap(QPixmap(u":/images/images/images/stylegananim1.gif"))
        self.label_262.setScaledContents(True)
        self.label_262.setAlignment(Qt.AlignCenter)
        self.label_262.setMargin(15)
        self.label_263 = QLabel(self.model_train_widget_2)
        self.label_263.setObjectName(u"label_263")
        self.label_263.setGeometry(QRect(410, 160, 181, 171))
        self.label_263.setPixmap(QPixmap(u":/images/images/images/stylegananim2.gif"))
        self.label_263.setScaledContents(True)
        self.label_263.setAlignment(Qt.AlignCenter)
        self.label_263.setMargin(15)
        self.label_259.raise_()
        self.label_260.raise_()
        self.style_gan1_btn.raise_()
        self.label_258.raise_()
        self.style_gan2_btn.raise_()
        self.label_261.raise_()
        self.label_262.raise_()
        self.label_263.raise_()
        self.train_stylegan_btn = QPushButton(self.datasets_widget_13)
        self.train_stylegan_btn.setObjectName(u"train_stylegan_btn")
        self.train_stylegan_btn.setGeometry(QRect(290, 20, 161, 41))
        self.train_stylegan_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout_google_btn = QPushButton(self.datasets_widget_13)
        self.logout_google_btn.setObjectName(u"logout_google_btn")
        self.logout_google_btn.setGeometry(QRect(180, 20, 91, 41))
        self.logout_google_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stackedWidget_stylegan.addWidget(self.pretrained_models_page)
        self.stylegan1_page = QWidget()
        self.stylegan1_page.setObjectName(u"stylegan1_page")
        self.datasets_widget_19 = QWidget(self.stylegan1_page)
        self.datasets_widget_19.setObjectName(u"datasets_widget_19")
        self.datasets_widget_19.setGeometry(QRect(10, 0, 721, 421))
        self.datasets_widget_19.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_277 = QLabel(self.datasets_widget_19)
        self.label_277.setObjectName(u"label_277")
        self.label_277.setGeometry(QRect(20, 60, 461, 321))
        self.label_277.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_277.setFrameShape(QFrame.NoFrame)
        self.label_277.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_277.setWordWrap(True)
        self.label_277.setMargin(36)
        self.output_size_style1 = QComboBox(self.datasets_widget_19)
        self.output_size_style1.addItem("")
        self.output_size_style1.addItem("")
        self.output_size_style1.addItem("")
        self.output_size_style1.addItem("")
        self.output_size_style1.addItem("")
        self.output_size_style1.setObjectName(u"output_size_style1")
        self.output_size_style1.setGeometry(QRect(260, 160, 101, 41))
        self.output_size_style1.setFont(font)
        self.output_size_style1.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_size_style1.setAutoFillBackground(False)
        self.output_size_style1.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.output_size_style1.setEditable(True)
        self.output_size_style1.setIconSize(QSize(16, 16))
        self.output_size_style1.setFrame(True)
        self.runtime_env_style1 = QComboBox(self.datasets_widget_19)
        self.runtime_env_style1.addItem("")
        self.runtime_env_style1.addItem("")
        self.runtime_env_style1.setObjectName(u"runtime_env_style1")
        self.runtime_env_style1.setGeometry(QRect(260, 100, 101, 41))
        self.runtime_env_style1.setFont(font)
        self.runtime_env_style1.setCursor(QCursor(Qt.PointingHandCursor))
        self.runtime_env_style1.setAutoFillBackground(False)
        self.runtime_env_style1.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.runtime_env_style1.setEditable(False)
        self.runtime_env_style1.setIconSize(QSize(16, 16))
        self.runtime_env_style1.setFrame(True)
        self.mount_gdrive_style1_btn = QPushButton(self.datasets_widget_19)
        self.mount_gdrive_style1_btn.setObjectName(u"mount_gdrive_style1_btn")
        self.mount_gdrive_style1_btn.setGeometry(QRect(60, 220, 181, 41))
        self.mount_gdrive_style1_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_31 = QPushButton(self.datasets_widget_19)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setGeometry(QRect(60, 100, 181, 41))
        self.pushButton_31.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_281 = QLabel(self.datasets_widget_19)
        self.label_281.setObjectName(u"label_281")
        self.label_281.setGeometry(QRect(390, 70, 81, 61))
        self.label_281.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_281.setScaledContents(True)
        self.label_281.setAlignment(Qt.AlignCenter)
        self.label_281.setMargin(15)
        self.generate_images_style1_btn = QPushButton(self.datasets_widget_19)
        self.generate_images_style1_btn.setObjectName(u"generate_images_style1_btn")
        self.generate_images_style1_btn.setGeometry(QRect(50, 280, 211, 71))
        self.generate_images_style1_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_309 = QLabel(self.datasets_widget_19)
        self.label_309.setObjectName(u"label_309")
        self.label_309.setGeometry(QRect(520, 70, 111, 41))
        self.pushButton_20 = QPushButton(self.datasets_widget_19)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(60, 160, 181, 41))
        self.pushButton_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_282 = QLabel(self.datasets_widget_19)
        self.label_282.setObjectName(u"label_282")
        self.label_282.setGeometry(QRect(280, 210, 171, 151))
        self.label_282.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_282.setFrameShape(QFrame.NoFrame)
        self.label_282.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_282.setWordWrap(True)
        self.label_282.setMargin(0)
        self.label_295 = QLabel(self.datasets_widget_19)
        self.label_295.setObjectName(u"label_295")
        self.label_295.setGeometry(QRect(90, 10, 161, 41))
        self.label_296 = QLabel(self.datasets_widget_19)
        self.label_296.setObjectName(u"label_296")
        self.label_296.setGeometry(QRect(390, 140, 81, 71))
        self.label_296.setPixmap(QPixmap(u":/images/images/images/nvidia2.png"))
        self.label_296.setScaledContents(True)
        self.label_296.setAlignment(Qt.AlignCenter)
        self.label_296.setMargin(15)
        self.selected_dst_style1 = QComboBox(self.datasets_widget_19)
        self.selected_dst_style1.addItem("")
        self.selected_dst_style1.addItem("")
        self.selected_dst_style1.addItem("")
        self.selected_dst_style1.addItem("")
        self.selected_dst_style1.addItem("")
        self.selected_dst_style1.setObjectName(u"selected_dst_style1")
        self.selected_dst_style1.setEnabled(True)
        self.selected_dst_style1.setGeometry(QRect(510, 130, 151, 41))
        self.selected_dst_style1.setFont(font)
        self.selected_dst_style1.setCursor(QCursor(Qt.PointingHandCursor))
        self.selected_dst_style1.setAutoFillBackground(False)
        self.selected_dst_style1.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.selected_dst_style1.setEditable(False)
        self.selected_dst_style1.setIconSize(QSize(16, 16))
        self.selected_dst_style1.setFrame(True)
        self.back_to_models_btn_1 = QPushButton(self.datasets_widget_19)
        self.back_to_models_btn_1.setObjectName(u"back_to_models_btn_1")
        self.back_to_models_btn_1.setGeometry(QRect(20, 10, 51, 41))
        self.back_to_models_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_size_error = QLabel(self.datasets_widget_19)
        self.output_size_error.setObjectName(u"output_size_error")
        self.output_size_error.setGeometry(QRect(60, 210, 191, 61))
        self.output_size_error.setStyleSheet(u"\n"
"color:rgb(255, 135, 87)")
        self.output_size_error.setScaledContents(False)
        self.output_size_error.setAlignment(Qt.AlignCenter)
        self.output_size_error.setWordWrap(True)
        self.output_size_error.setMargin(7)
        self.runtime_env_error = QLabel(self.datasets_widget_19)
        self.runtime_env_error.setObjectName(u"runtime_env_error")
        self.runtime_env_error.setGeometry(QRect(270, 220, 191, 131))
        self.runtime_env_error.setStyleSheet(u"\n"
"color:rgb(255, 135, 87)")
        self.runtime_env_error.setScaledContents(False)
        self.runtime_env_error.setAlignment(Qt.AlignCenter)
        self.runtime_env_error.setWordWrap(True)
        self.runtime_env_error.setMargin(7)
        self.label_255 = QLabel(self.datasets_widget_19)
        self.label_255.setObjectName(u"label_255")
        self.label_255.setGeometry(QRect(500, 220, 171, 151))
        self.label_255.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_255.setFrameShape(QFrame.NoFrame)
        self.label_255.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_255.setWordWrap(True)
        self.label_255.setMargin(11)
        self.runtime_env_error.raise_()
        self.output_size_error.raise_()
        self.label_277.raise_()
        self.output_size_style1.raise_()
        self.runtime_env_style1.raise_()
        self.mount_gdrive_style1_btn.raise_()
        self.pushButton_31.raise_()
        self.label_281.raise_()
        self.generate_images_style1_btn.raise_()
        self.label_309.raise_()
        self.pushButton_20.raise_()
        self.label_282.raise_()
        self.label_295.raise_()
        self.label_296.raise_()
        self.selected_dst_style1.raise_()
        self.back_to_models_btn_1.raise_()
        self.label_255.raise_()
        self.stackedWidget_stylegan.addWidget(self.stylegan1_page)
        self.stylegan1_progress_page = QWidget()
        self.stylegan1_progress_page.setObjectName(u"stylegan1_progress_page")
        self.datasets_widget_18 = QWidget(self.stylegan1_progress_page)
        self.datasets_widget_18.setObjectName(u"datasets_widget_18")
        self.datasets_widget_18.setGeometry(QRect(0, 0, 721, 421))
        self.datasets_widget_18.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_288 = QLabel(self.datasets_widget_18)
        self.label_288.setObjectName(u"label_288")
        self.label_288.setGeometry(QRect(30, 10, 161, 41))
        self.rerun_style1gan_btn = QPushButton(self.datasets_widget_18)
        self.rerun_style1gan_btn.setObjectName(u"rerun_style1gan_btn")
        self.rerun_style1gan_btn.setGeometry(QRect(20, 300, 161, 41))
        self.rerun_style1gan_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_progress_style1_btn = QPushButton(self.datasets_widget_18)
        self.cancel_progress_style1_btn.setObjectName(u"cancel_progress_style1_btn")
        self.cancel_progress_style1_btn.setGeometry(QRect(20, 350, 161, 41))
        self.cancel_progress_style1_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_292 = QLabel(self.datasets_widget_18)
        self.label_292.setObjectName(u"label_292")
        self.label_292.setGeometry(QRect(210, 80, 501, 321))
        self.label_292.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_292.setFrameShape(QFrame.NoFrame)
        self.label_292.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_292.setWordWrap(True)
        self.label_292.setMargin(36)
        self.label_298 = QLabel(self.datasets_widget_18)
        self.label_298.setObjectName(u"label_298")
        self.label_298.setGeometry(QRect(40, 40, 111, 81))
        self.label_298.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_298.setScaledContents(True)
        self.label_298.setAlignment(Qt.AlignCenter)
        self.label_298.setMargin(15)
        self.label_301 = QLabel(self.datasets_widget_18)
        self.label_301.setObjectName(u"label_301")
        self.label_301.setGeometry(QRect(230, 180, 161, 41))
        self.label_301.setAlignment(Qt.AlignCenter)
        self.label_302 = QLabel(self.datasets_widget_18)
        self.label_302.setObjectName(u"label_302")
        self.label_302.setGeometry(QRect(230, 240, 161, 41))
        self.label_302.setAlignment(Qt.AlignCenter)
        self.stylegan1_hours = QLCDNumber(self.datasets_widget_18)
        self.stylegan1_hours.setObjectName(u"stylegan1_hours")
        self.stylegan1_hours.setGeometry(QRect(410, 240, 71, 41))
        self.stylegan1_hours.setFrameShadow(QFrame.Raised)
        self.label_303 = QLabel(self.datasets_widget_18)
        self.label_303.setObjectName(u"label_303")
        self.label_303.setGeometry(QRect(230, 320, 161, 41))
        self.label_303.setAlignment(Qt.AlignCenter)
        self.genrated_images_count_stylegan1 = QLCDNumber(self.datasets_widget_18)
        self.genrated_images_count_stylegan1.setObjectName(u"genrated_images_count_stylegan1")
        self.genrated_images_count_stylegan1.setGeometry(QRect(410, 320, 71, 41))
        self.label_304 = QLabel(self.datasets_widget_18)
        self.label_304.setObjectName(u"label_304")
        self.label_304.setGeometry(QRect(490, 240, 51, 41))
        self.label_304.setAlignment(Qt.AlignCenter)
        self.stylegan1_minutes = QLCDNumber(self.datasets_widget_18)
        self.stylegan1_minutes.setObjectName(u"stylegan1_minutes")
        self.stylegan1_minutes.setGeometry(QRect(550, 240, 71, 41))
        self.label_305 = QLabel(self.datasets_widget_18)
        self.label_305.setObjectName(u"label_305")
        self.label_305.setGeometry(QRect(630, 240, 61, 41))
        self.label_305.setAlignment(Qt.AlignCenter)
        self.view_style1_generated_imgs_btn = QPushButton(self.datasets_widget_18)
        self.view_style1_generated_imgs_btn.setObjectName(u"view_style1_generated_imgs_btn")
        self.view_style1_generated_imgs_btn.setGeometry(QRect(520, 320, 161, 41))
        self.view_style1_generated_imgs_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.view_style1_generated_imgs_btn.setIcon(icon5)
        self.label_306 = QLabel(self.datasets_widget_18)
        self.label_306.setObjectName(u"label_306")
        self.label_306.setGeometry(QRect(230, 120, 161, 41))
        self.label_306.setAlignment(Qt.AlignCenter)
        self.label_307 = QLabel(self.datasets_widget_18)
        self.label_307.setObjectName(u"label_307")
        self.label_307.setGeometry(QRect(10, 120, 191, 161))
        self.label_307.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_307.setFrameShape(QFrame.NoFrame)
        self.label_307.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_307.setWordWrap(True)
        self.label_307.setMargin(10)
        self.cancel_stylegan1_confirm_widget = QWidget(self.datasets_widget_18)
        self.cancel_stylegan1_confirm_widget.setObjectName(u"cancel_stylegan1_confirm_widget")
        self.cancel_stylegan1_confirm_widget.setGeometry(QRect(230, 100, 451, 241))
        self.cancel_stylegan1_confirm_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.cancel_stylegan1_confirm_ok_btn = QPushButton(self.cancel_stylegan1_confirm_widget)
        self.cancel_stylegan1_confirm_ok_btn.setObjectName(u"cancel_stylegan1_confirm_ok_btn")
        self.cancel_stylegan1_confirm_ok_btn.setGeometry(QRect(40, 150, 151, 41))
        self.cancel_stylegan1_confirm_ok_btn.setFont(font)
        self.cancel_stylegan1_confirm_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_stylegan1_confirm_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_98 = QLabel(self.cancel_stylegan1_confirm_widget)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(60, 30, 341, 41))
        self.label_98.setAlignment(Qt.AlignCenter)
        self.cancel_stylegan1_confirm_cancel_btn = QPushButton(self.cancel_stylegan1_confirm_widget)
        self.cancel_stylegan1_confirm_cancel_btn.setObjectName(u"cancel_stylegan1_confirm_cancel_btn")
        self.cancel_stylegan1_confirm_cancel_btn.setGeometry(QRect(270, 150, 151, 41))
        self.cancel_stylegan1_confirm_cancel_btn.setFont(font)
        self.cancel_stylegan1_confirm_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_stylegan1_confirm_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_16 = QLabel(self.cancel_stylegan1_confirm_widget)
        self.account_verify_status_16.setObjectName(u"account_verify_status_16")
        self.account_verify_status_16.setGeometry(QRect(80, 80, 291, 41))
        self.account_verify_status_16.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status_16.setAlignment(Qt.AlignCenter)
        self.rerun_stylegan1_confirm_widget = QWidget(self.datasets_widget_18)
        self.rerun_stylegan1_confirm_widget.setObjectName(u"rerun_stylegan1_confirm_widget")
        self.rerun_stylegan1_confirm_widget.setGeometry(QRect(230, 80, 451, 241))
        self.rerun_stylegan1_confirm_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.rerun_stylegan1_confirm_ok_btn = QPushButton(self.rerun_stylegan1_confirm_widget)
        self.rerun_stylegan1_confirm_ok_btn.setObjectName(u"rerun_stylegan1_confirm_ok_btn")
        self.rerun_stylegan1_confirm_ok_btn.setGeometry(QRect(40, 150, 151, 41))
        self.rerun_stylegan1_confirm_ok_btn.setFont(font)
        self.rerun_stylegan1_confirm_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.rerun_stylegan1_confirm_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_102 = QLabel(self.rerun_stylegan1_confirm_widget)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(60, 30, 341, 41))
        self.label_102.setAlignment(Qt.AlignCenter)
        self.rerun_tstylegan1_confirm_cancel_btn = QPushButton(self.rerun_stylegan1_confirm_widget)
        self.rerun_tstylegan1_confirm_cancel_btn.setObjectName(u"rerun_tstylegan1_confirm_cancel_btn")
        self.rerun_tstylegan1_confirm_cancel_btn.setGeometry(QRect(270, 150, 151, 41))
        self.rerun_tstylegan1_confirm_cancel_btn.setFont(font)
        self.rerun_tstylegan1_confirm_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.rerun_tstylegan1_confirm_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_17 = QLabel(self.rerun_stylegan1_confirm_widget)
        self.account_verify_status_17.setObjectName(u"account_verify_status_17")
        self.account_verify_status_17.setGeometry(QRect(80, 80, 291, 41))
        self.account_verify_status_17.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status_17.setAlignment(Qt.AlignCenter)
        self.label_311 = QLabel(self.datasets_widget_18)
        self.label_311.setObjectName(u"label_311")
        self.label_311.setGeometry(QRect(630, 10, 51, 51))
        self.label_311.setPixmap(QPixmap(u":/images/images/images/nvidia2.png"))
        self.label_311.setScaledContents(True)
        self.label_311.setAlignment(Qt.AlignCenter)
        self.label_311.setMargin(0)
        self.loading_label_dst = QLabel(self.datasets_widget_18)
        self.loading_label_dst.setObjectName(u"loading_label_dst")
        self.loading_label_dst.setGeometry(QRect(410, 90, 71, 71))
        self.loading_label_dst.setStyleSheet(u"background-color: rgb(210, 254, 255,255);")
        self.loading_label_dst.setScaledContents(True)
        self.loading_label_dst.setMargin(0)
        self.style_gan_plabel = QLabel(self.datasets_widget_18)
        self.style_gan_plabel.setObjectName(u"style_gan_plabel")
        self.style_gan_plabel.setGeometry(QRect(410, 160, 71, 71))
        self.style_gan_plabel.setStyleSheet(u"background-color: rgb(210, 254, 255,255);")
        self.style_gan_plabel.setPixmap(QPixmap(u":/images/images/images/tick.png"))
        self.style_gan_plabel.setScaledContents(True)
        self.style_gan_plabel.setMargin(0)
        self.progress_number = QLCDNumber(self.datasets_widget_18)
        self.progress_number.setObjectName(u"progress_number")
        self.progress_number.setGeometry(QRect(390, 180, 71, 41))
        self.progress_number.setStyleSheet(u"background-color: rgb(210, 254, 255,255);")
        self.progress_number.setFrameShadow(QFrame.Raised)
        self.label_264 = QLabel(self.datasets_widget_18)
        self.label_264.setObjectName(u"label_264")
        self.label_264.setGeometry(QRect(540, 90, 141, 141))
        self.label_264.setPixmap(QPixmap(u":/images/images/images/stylegananim1.gif"))
        self.label_264.setScaledContents(True)
        self.label_264.setAlignment(Qt.AlignCenter)
        self.label_264.setMargin(15)
        self.back_to_style1_page_btn = QPushButton(self.datasets_widget_18)
        self.back_to_style1_page_btn.setObjectName(u"back_to_style1_page_btn")
        self.back_to_style1_page_btn.setGeometry(QRect(170, 10, 51, 41))
        self.back_to_style1_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_stylegan1_confirm_widget.raise_()
        self.style_gan_plabel.raise_()
        self.rerun_stylegan1_confirm_widget.raise_()
        self.label_288.raise_()
        self.rerun_style1gan_btn.raise_()
        self.cancel_progress_style1_btn.raise_()
        self.label_292.raise_()
        self.label_298.raise_()
        self.label_301.raise_()
        self.label_302.raise_()
        self.stylegan1_hours.raise_()
        self.label_303.raise_()
        self.genrated_images_count_stylegan1.raise_()
        self.label_304.raise_()
        self.stylegan1_minutes.raise_()
        self.label_305.raise_()
        self.view_style1_generated_imgs_btn.raise_()
        self.label_306.raise_()
        self.label_307.raise_()
        self.label_311.raise_()
        self.loading_label_dst.raise_()
        self.progress_number.raise_()
        self.label_264.raise_()
        self.back_to_style1_page_btn.raise_()
        self.stackedWidget_stylegan.addWidget(self.stylegan1_progress_page)
        self.stylegan2_page = QWidget()
        self.stylegan2_page.setObjectName(u"stylegan2_page")
        self.datasets_widget_16 = QWidget(self.stylegan2_page)
        self.datasets_widget_16.setObjectName(u"datasets_widget_16")
        self.datasets_widget_16.setGeometry(QRect(10, 0, 721, 421))
        self.datasets_widget_16.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_276 = QLabel(self.datasets_widget_16)
        self.label_276.setObjectName(u"label_276")
        self.label_276.setGeometry(QRect(20, 60, 461, 321))
        self.label_276.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_276.setFrameShape(QFrame.NoFrame)
        self.label_276.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_276.setWordWrap(True)
        self.label_276.setMargin(36)
        self.end_image_style2 = QComboBox(self.datasets_widget_16)
        self.end_image_style2.addItem("")
        self.end_image_style2.addItem("")
        self.end_image_style2.addItem("")
        self.end_image_style2.addItem("")
        self.end_image_style2.setObjectName(u"end_image_style2")
        self.end_image_style2.setGeometry(QRect(380, 160, 71, 41))
        self.end_image_style2.setFont(font)
        self.end_image_style2.setCursor(QCursor(Qt.PointingHandCursor))
        self.end_image_style2.setAutoFillBackground(False)
        self.end_image_style2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.end_image_style2.setEditable(True)
        self.end_image_style2.setIconSize(QSize(16, 16))
        self.end_image_style2.setFrame(True)
        self.runtime_env_style2 = QComboBox(self.datasets_widget_16)
        self.runtime_env_style2.addItem("")
        self.runtime_env_style2.addItem("")
        self.runtime_env_style2.setObjectName(u"runtime_env_style2")
        self.runtime_env_style2.setGeometry(QRect(260, 100, 101, 41))
        self.runtime_env_style2.setFont(font)
        self.runtime_env_style2.setCursor(QCursor(Qt.PointingHandCursor))
        self.runtime_env_style2.setAutoFillBackground(False)
        self.runtime_env_style2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.runtime_env_style2.setEditable(False)
        self.runtime_env_style2.setIconSize(QSize(16, 16))
        self.runtime_env_style2.setFrame(True)
        self.mount_gdrive_style2_btn = QPushButton(self.datasets_widget_16)
        self.mount_gdrive_style2_btn.setObjectName(u"mount_gdrive_style2_btn")
        self.mount_gdrive_style2_btn.setGeometry(QRect(60, 220, 181, 41))
        self.mount_gdrive_style2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_30 = QPushButton(self.datasets_widget_16)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(60, 100, 181, 41))
        self.pushButton_30.setCursor(QCursor(Qt.ArrowCursor))
        self.label_278 = QLabel(self.datasets_widget_16)
        self.label_278.setObjectName(u"label_278")
        self.label_278.setGeometry(QRect(390, 70, 81, 61))
        self.label_278.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_278.setScaledContents(True)
        self.label_278.setAlignment(Qt.AlignCenter)
        self.label_278.setMargin(15)
        self.generate_images_style2_btn = QPushButton(self.datasets_widget_16)
        self.generate_images_style2_btn.setObjectName(u"generate_images_style2_btn")
        self.generate_images_style2_btn.setGeometry(QRect(50, 280, 211, 71))
        self.generate_images_style2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_300 = QLabel(self.datasets_widget_16)
        self.label_300.setObjectName(u"label_300")
        self.label_300.setGeometry(QRect(520, 70, 111, 41))
        self.pushButton_19 = QPushButton(self.datasets_widget_16)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(60, 160, 181, 41))
        self.pushButton_19.setCursor(QCursor(Qt.ArrowCursor))
        self.label_279 = QLabel(self.datasets_widget_16)
        self.label_279.setObjectName(u"label_279")
        self.label_279.setGeometry(QRect(290, 210, 171, 151))
        self.label_279.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_279.setFrameShape(QFrame.NoFrame)
        self.label_279.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_279.setWordWrap(True)
        self.label_279.setMargin(0)
        self.label_280 = QLabel(self.datasets_widget_16)
        self.label_280.setObjectName(u"label_280")
        self.label_280.setGeometry(QRect(100, 10, 161, 41))
        self.label_297 = QLabel(self.datasets_widget_16)
        self.label_297.setObjectName(u"label_297")
        self.label_297.setGeometry(QRect(590, 140, 81, 71))
        self.label_297.setPixmap(QPixmap(u":/images/images/images/nvidia2.png"))
        self.label_297.setScaledContents(True)
        self.label_297.setAlignment(Qt.AlignCenter)
        self.label_297.setMargin(15)
        self.selected_dst_style2 = QComboBox(self.datasets_widget_16)
        self.selected_dst_style2.addItem("")
        self.selected_dst_style2.addItem("")
        self.selected_dst_style2.addItem("")
        self.selected_dst_style2.addItem("")
        self.selected_dst_style2.addItem("")
        self.selected_dst_style2.addItem("")
        self.selected_dst_style2.setObjectName(u"selected_dst_style2")
        self.selected_dst_style2.setGeometry(QRect(510, 110, 151, 41))
        self.selected_dst_style2.setFont(font)
        self.selected_dst_style2.setCursor(QCursor(Qt.PointingHandCursor))
        self.selected_dst_style2.setAutoFillBackground(False)
        self.selected_dst_style2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.selected_dst_style2.setEditable(False)
        self.selected_dst_style2.setIconSize(QSize(16, 16))
        self.selected_dst_style2.setFrame(True)
        self.start_image_style2 = QComboBox(self.datasets_widget_16)
        self.start_image_style2.addItem("")
        self.start_image_style2.addItem("")
        self.start_image_style2.addItem("")
        self.start_image_style2.addItem("")
        self.start_image_style2.addItem("")
        self.start_image_style2.setObjectName(u"start_image_style2")
        self.start_image_style2.setGeometry(QRect(260, 160, 71, 41))
        self.start_image_style2.setFont(font)
        self.start_image_style2.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_image_style2.setAutoFillBackground(False)
        self.start_image_style2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.start_image_style2.setEditable(True)
        self.start_image_style2.setIconSize(QSize(16, 16))
        self.start_image_style2.setFrame(True)
        self.label_299 = QLabel(self.datasets_widget_16)
        self.label_299.setObjectName(u"label_299")
        self.label_299.setGeometry(QRect(350, 170, 21, 31))
        self.label_299.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_299.setFrameShape(QFrame.NoFrame)
        self.label_299.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_299.setWordWrap(True)
        self.label_299.setMargin(0)
        self.back_to_models_btn_2 = QPushButton(self.datasets_widget_16)
        self.back_to_models_btn_2.setObjectName(u"back_to_models_btn_2")
        self.back_to_models_btn_2.setGeometry(QRect(20, 10, 51, 41))
        self.back_to_models_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_256 = QLabel(self.datasets_widget_16)
        self.label_256.setObjectName(u"label_256")
        self.label_256.setGeometry(QRect(500, 220, 171, 151))
        self.label_256.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_256.setFrameShape(QFrame.NoFrame)
        self.label_256.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_256.setWordWrap(True)
        self.label_256.setMargin(11)
        self.output_size_error_2 = QLabel(self.datasets_widget_16)
        self.output_size_error_2.setObjectName(u"output_size_error_2")
        self.output_size_error_2.setGeometry(QRect(60, 210, 191, 61))
        self.output_size_error_2.setStyleSheet(u"\n"
"color:rgb(255, 135, 87)")
        self.output_size_error_2.setScaledContents(False)
        self.output_size_error_2.setAlignment(Qt.AlignCenter)
        self.output_size_error_2.setWordWrap(True)
        self.output_size_error_2.setMargin(7)
        self.runtime_env_error_2 = QLabel(self.datasets_widget_16)
        self.runtime_env_error_2.setObjectName(u"runtime_env_error_2")
        self.runtime_env_error_2.setGeometry(QRect(270, 220, 191, 131))
        self.runtime_env_error_2.setStyleSheet(u"\n"
"color:rgb(255, 135, 87)")
        self.runtime_env_error_2.setScaledContents(False)
        self.runtime_env_error_2.setAlignment(Qt.AlignCenter)
        self.runtime_env_error_2.setWordWrap(True)
        self.runtime_env_error_2.setMargin(7)
        self.runtime_env_error_2.raise_()
        self.output_size_error_2.raise_()
        self.label_276.raise_()
        self.end_image_style2.raise_()
        self.runtime_env_style2.raise_()
        self.mount_gdrive_style2_btn.raise_()
        self.pushButton_30.raise_()
        self.label_278.raise_()
        self.generate_images_style2_btn.raise_()
        self.label_300.raise_()
        self.pushButton_19.raise_()
        self.label_279.raise_()
        self.label_280.raise_()
        self.label_297.raise_()
        self.selected_dst_style2.raise_()
        self.start_image_style2.raise_()
        self.label_299.raise_()
        self.back_to_models_btn_2.raise_()
        self.label_256.raise_()
        self.stackedWidget_stylegan.addWidget(self.stylegan2_page)
        self.stylegan2_progress_page = QWidget()
        self.stylegan2_progress_page.setObjectName(u"stylegan2_progress_page")
        self.datasets_widget_20 = QWidget(self.stylegan2_progress_page)
        self.datasets_widget_20.setObjectName(u"datasets_widget_20")
        self.datasets_widget_20.setGeometry(QRect(0, 10, 721, 421))
        self.datasets_widget_20.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_289 = QLabel(self.datasets_widget_20)
        self.label_289.setObjectName(u"label_289")
        self.label_289.setGeometry(QRect(30, 10, 161, 41))
        self.rerun_style2gan_btn = QPushButton(self.datasets_widget_20)
        self.rerun_style2gan_btn.setObjectName(u"rerun_style2gan_btn")
        self.rerun_style2gan_btn.setGeometry(QRect(20, 300, 161, 41))
        self.rerun_style2gan_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_progress_style2_btn = QPushButton(self.datasets_widget_20)
        self.cancel_progress_style2_btn.setObjectName(u"cancel_progress_style2_btn")
        self.cancel_progress_style2_btn.setGeometry(QRect(20, 350, 161, 41))
        self.cancel_progress_style2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_293 = QLabel(self.datasets_widget_20)
        self.label_293.setObjectName(u"label_293")
        self.label_293.setGeometry(QRect(210, 80, 501, 321))
        self.label_293.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_293.setFrameShape(QFrame.NoFrame)
        self.label_293.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_293.setWordWrap(True)
        self.label_293.setMargin(36)
        self.label_308 = QLabel(self.datasets_widget_20)
        self.label_308.setObjectName(u"label_308")
        self.label_308.setGeometry(QRect(40, 40, 111, 81))
        self.label_308.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_308.setScaledContents(True)
        self.label_308.setAlignment(Qt.AlignCenter)
        self.label_308.setMargin(15)
        self.label_310 = QLabel(self.datasets_widget_20)
        self.label_310.setObjectName(u"label_310")
        self.label_310.setGeometry(QRect(230, 180, 161, 41))
        self.label_310.setAlignment(Qt.AlignCenter)
        self.label_312 = QLabel(self.datasets_widget_20)
        self.label_312.setObjectName(u"label_312")
        self.label_312.setGeometry(QRect(230, 240, 161, 41))
        self.label_312.setAlignment(Qt.AlignCenter)
        self.stylegan2_hours = QLCDNumber(self.datasets_widget_20)
        self.stylegan2_hours.setObjectName(u"stylegan2_hours")
        self.stylegan2_hours.setGeometry(QRect(410, 240, 71, 41))
        self.stylegan2_hours.setFrameShadow(QFrame.Raised)
        self.label_313 = QLabel(self.datasets_widget_20)
        self.label_313.setObjectName(u"label_313")
        self.label_313.setGeometry(QRect(230, 320, 161, 41))
        self.label_313.setAlignment(Qt.AlignCenter)
        self.genrated_images_count_stylegan2 = QLCDNumber(self.datasets_widget_20)
        self.genrated_images_count_stylegan2.setObjectName(u"genrated_images_count_stylegan2")
        self.genrated_images_count_stylegan2.setGeometry(QRect(410, 320, 71, 41))
        self.label_314 = QLabel(self.datasets_widget_20)
        self.label_314.setObjectName(u"label_314")
        self.label_314.setGeometry(QRect(490, 240, 51, 41))
        self.label_314.setAlignment(Qt.AlignCenter)
        self.stylegan2_minutes = QLCDNumber(self.datasets_widget_20)
        self.stylegan2_minutes.setObjectName(u"stylegan2_minutes")
        self.stylegan2_minutes.setGeometry(QRect(550, 240, 71, 41))
        self.label_315 = QLabel(self.datasets_widget_20)
        self.label_315.setObjectName(u"label_315")
        self.label_315.setGeometry(QRect(630, 240, 61, 41))
        self.label_315.setAlignment(Qt.AlignCenter)
        self.view_style2_generated_imgs_btn = QPushButton(self.datasets_widget_20)
        self.view_style2_generated_imgs_btn.setObjectName(u"view_style2_generated_imgs_btn")
        self.view_style2_generated_imgs_btn.setGeometry(QRect(520, 320, 161, 41))
        self.view_style2_generated_imgs_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.view_style2_generated_imgs_btn.setIcon(icon5)
        self.label_316 = QLabel(self.datasets_widget_20)
        self.label_316.setObjectName(u"label_316")
        self.label_316.setGeometry(QRect(230, 120, 161, 41))
        self.label_316.setAlignment(Qt.AlignCenter)
        self.label_317 = QLabel(self.datasets_widget_20)
        self.label_317.setObjectName(u"label_317")
        self.label_317.setGeometry(QRect(10, 120, 191, 161))
        self.label_317.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_317.setFrameShape(QFrame.NoFrame)
        self.label_317.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_317.setWordWrap(True)
        self.label_317.setMargin(10)
        self.cancel_stylegan2_confirm_widget = QWidget(self.datasets_widget_20)
        self.cancel_stylegan2_confirm_widget.setObjectName(u"cancel_stylegan2_confirm_widget")
        self.cancel_stylegan2_confirm_widget.setGeometry(QRect(230, 100, 451, 241))
        self.cancel_stylegan2_confirm_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.cancel_stylegan2_confirm_ok_btn = QPushButton(self.cancel_stylegan2_confirm_widget)
        self.cancel_stylegan2_confirm_ok_btn.setObjectName(u"cancel_stylegan2_confirm_ok_btn")
        self.cancel_stylegan2_confirm_ok_btn.setGeometry(QRect(40, 150, 151, 41))
        self.cancel_stylegan2_confirm_ok_btn.setFont(font)
        self.cancel_stylegan2_confirm_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_stylegan2_confirm_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_104 = QLabel(self.cancel_stylegan2_confirm_widget)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setGeometry(QRect(60, 30, 341, 41))
        self.label_104.setAlignment(Qt.AlignCenter)
        self.cancel_stylegan2_confirm_cancel_btn = QPushButton(self.cancel_stylegan2_confirm_widget)
        self.cancel_stylegan2_confirm_cancel_btn.setObjectName(u"cancel_stylegan2_confirm_cancel_btn")
        self.cancel_stylegan2_confirm_cancel_btn.setGeometry(QRect(270, 150, 151, 41))
        self.cancel_stylegan2_confirm_cancel_btn.setFont(font)
        self.cancel_stylegan2_confirm_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_stylegan2_confirm_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_18 = QLabel(self.cancel_stylegan2_confirm_widget)
        self.account_verify_status_18.setObjectName(u"account_verify_status_18")
        self.account_verify_status_18.setGeometry(QRect(80, 80, 291, 41))
        self.account_verify_status_18.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status_18.setAlignment(Qt.AlignCenter)
        self.rerun_stylegan2_confirm_widget = QWidget(self.datasets_widget_20)
        self.rerun_stylegan2_confirm_widget.setObjectName(u"rerun_stylegan2_confirm_widget")
        self.rerun_stylegan2_confirm_widget.setGeometry(QRect(230, 80, 451, 241))
        self.rerun_stylegan2_confirm_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.rerun_stylegan2_confirm_ok_btn = QPushButton(self.rerun_stylegan2_confirm_widget)
        self.rerun_stylegan2_confirm_ok_btn.setObjectName(u"rerun_stylegan2_confirm_ok_btn")
        self.rerun_stylegan2_confirm_ok_btn.setGeometry(QRect(40, 150, 151, 41))
        self.rerun_stylegan2_confirm_ok_btn.setFont(font)
        self.rerun_stylegan2_confirm_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.rerun_stylegan2_confirm_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_105 = QLabel(self.rerun_stylegan2_confirm_widget)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setGeometry(QRect(60, 30, 341, 41))
        self.label_105.setAlignment(Qt.AlignCenter)
        self.rerun_tstylegan2_confirm_cancel_btn = QPushButton(self.rerun_stylegan2_confirm_widget)
        self.rerun_tstylegan2_confirm_cancel_btn.setObjectName(u"rerun_tstylegan2_confirm_cancel_btn")
        self.rerun_tstylegan2_confirm_cancel_btn.setGeometry(QRect(270, 150, 151, 41))
        self.rerun_tstylegan2_confirm_cancel_btn.setFont(font)
        self.rerun_tstylegan2_confirm_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.rerun_tstylegan2_confirm_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_19 = QLabel(self.rerun_stylegan2_confirm_widget)
        self.account_verify_status_19.setObjectName(u"account_verify_status_19")
        self.account_verify_status_19.setGeometry(QRect(80, 80, 291, 41))
        self.account_verify_status_19.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status_19.setAlignment(Qt.AlignCenter)
        self.label_318 = QLabel(self.datasets_widget_20)
        self.label_318.setObjectName(u"label_318")
        self.label_318.setGeometry(QRect(630, 10, 51, 51))
        self.label_318.setPixmap(QPixmap(u":/images/images/images/nvidia2.png"))
        self.label_318.setScaledContents(True)
        self.label_318.setAlignment(Qt.AlignCenter)
        self.label_318.setMargin(0)
        self.loading_label_dst_2 = QLabel(self.datasets_widget_20)
        self.loading_label_dst_2.setObjectName(u"loading_label_dst_2")
        self.loading_label_dst_2.setGeometry(QRect(410, 90, 71, 71))
        self.loading_label_dst_2.setStyleSheet(u"background-color: rgb(210, 254, 255,255);")
        self.loading_label_dst_2.setScaledContents(True)
        self.loading_label_dst_2.setMargin(0)
        self.style_gan_plabel_2 = QLabel(self.datasets_widget_20)
        self.style_gan_plabel_2.setObjectName(u"style_gan_plabel_2")
        self.style_gan_plabel_2.setGeometry(QRect(410, 160, 71, 71))
        self.style_gan_plabel_2.setStyleSheet(u"background-color: rgb(210, 254, 255,255);")
        self.style_gan_plabel_2.setPixmap(QPixmap(u":/images/images/images/tick.png"))
        self.style_gan_plabel_2.setScaledContents(True)
        self.style_gan_plabel_2.setMargin(0)
        self.progress_number_2 = QLCDNumber(self.datasets_widget_20)
        self.progress_number_2.setObjectName(u"progress_number_2")
        self.progress_number_2.setGeometry(QRect(390, 180, 71, 41))
        self.progress_number_2.setStyleSheet(u"background-color: rgb(210, 254, 255,255);")
        self.progress_number_2.setFrameShadow(QFrame.Raised)
        self.label_265 = QLabel(self.datasets_widget_20)
        self.label_265.setObjectName(u"label_265")
        self.label_265.setGeometry(QRect(540, 90, 141, 141))
        self.label_265.setPixmap(QPixmap(u":/images/images/images/stylegananim1.gif"))
        self.label_265.setScaledContents(True)
        self.label_265.setAlignment(Qt.AlignCenter)
        self.label_265.setMargin(15)
        self.back_to_style2_page_btn = QPushButton(self.datasets_widget_20)
        self.back_to_style2_page_btn.setObjectName(u"back_to_style2_page_btn")
        self.back_to_style2_page_btn.setGeometry(QRect(170, 10, 51, 41))
        self.back_to_style2_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.rerun_stylegan2_confirm_widget.raise_()
        self.cancel_stylegan2_confirm_widget.raise_()
        self.style_gan_plabel_2.raise_()
        self.label_289.raise_()
        self.rerun_style2gan_btn.raise_()
        self.cancel_progress_style2_btn.raise_()
        self.label_293.raise_()
        self.label_308.raise_()
        self.label_310.raise_()
        self.label_312.raise_()
        self.stylegan2_hours.raise_()
        self.label_313.raise_()
        self.genrated_images_count_stylegan2.raise_()
        self.label_314.raise_()
        self.stylegan2_minutes.raise_()
        self.label_315.raise_()
        self.view_style2_generated_imgs_btn.raise_()
        self.label_316.raise_()
        self.label_317.raise_()
        self.label_318.raise_()
        self.loading_label_dst_2.raise_()
        self.progress_number_2.raise_()
        self.label_265.raise_()
        self.back_to_style2_page_btn.raise_()
        self.stackedWidget_stylegan.addWidget(self.stylegan2_progress_page)
        self.stackedWidget_content_pages.addWidget(self.stylegan_page)
        self.generated_images_page = QWidget()
        self.generated_images_page.setObjectName(u"generated_images_page")
        self.outputs_widget = QWidget(self.generated_images_page)
        self.outputs_widget.setObjectName(u"outputs_widget")
        self.outputs_widget.setGeometry(QRect(20, 0, 661, 421))
        self.outputs_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_232 = QLabel(self.outputs_widget)
        self.label_232.setObjectName(u"label_232")
        self.label_232.setGeometry(QRect(30, 10, 121, 41))
        self.output_folder_btn = QPushButton(self.outputs_widget)
        self.output_folder_btn.setObjectName(u"output_folder_btn")
        self.output_folder_btn.setGeometry(QRect(400, 10, 181, 41))
        self.output_folder_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.generated_images_stackedWidget = QStackedWidget(self.outputs_widget)
        self.generated_images_stackedWidget.setObjectName(u"generated_images_stackedWidget")
        self.generated_images_stackedWidget.setGeometry(QRect(20, 60, 631, 351))
        self.output_thumbs_view_page = QWidget()
        self.output_thumbs_view_page.setObjectName(u"output_thumbs_view_page")
        self.output_image_6_btn = QPushButton(self.output_thumbs_view_page)
        self.output_image_6_btn.setObjectName(u"output_image_6_btn")
        self.output_image_6_btn.setGeometry(QRect(430, 230, 151, 121))
        self.output_image_6_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_6_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.output_image_4 = QLabel(self.output_thumbs_view_page)
        self.output_image_4.setObjectName(u"output_image_4")
        self.output_image_4.setGeometry(QRect(50, 230, 141, 121))
        self.output_image_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_4.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.output_image_4.setFrameShape(QFrame.NoFrame)
        self.output_image_4.setAlignment(Qt.AlignCenter)
        self.output_image_4.setWordWrap(True)
        self.output_image_4.setMargin(2)
        self.make_fav1_btn = QPushButton(self.output_thumbs_view_page)
        self.make_fav1_btn.setObjectName(u"make_fav1_btn")
        self.make_fav1_btn.setGeometry(QRect(50, 10, 141, 31))
        self.make_fav1_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_4_btn = QPushButton(self.output_thumbs_view_page)
        self.output_image_4_btn.setObjectName(u"output_image_4_btn")
        self.output_image_4_btn.setGeometry(QRect(50, 230, 141, 121))
        self.output_image_4_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_4_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.remove_fav3_btn = QPushButton(self.output_thumbs_view_page)
        self.remove_fav3_btn.setObjectName(u"remove_fav3_btn")
        self.remove_fav3_btn.setGeometry(QRect(430, 10, 141, 31))
        self.remove_fav3_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_1_btn = QPushButton(self.output_thumbs_view_page)
        self.output_image_1_btn.setObjectName(u"output_image_1_btn")
        self.output_image_1_btn.setGeometry(QRect(50, 50, 141, 121))
        self.output_image_1_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_1_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.remove_fav1_btn = QPushButton(self.output_thumbs_view_page)
        self.remove_fav1_btn.setObjectName(u"remove_fav1_btn")
        self.remove_fav1_btn.setGeometry(QRect(50, 10, 141, 31))
        self.remove_fav1_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_6 = QLabel(self.output_thumbs_view_page)
        self.output_image_6.setObjectName(u"output_image_6")
        self.output_image_6.setGeometry(QRect(430, 230, 151, 121))
        self.output_image_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_6.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.output_image_6.setFrameShape(QFrame.NoFrame)
        self.output_image_6.setAlignment(Qt.AlignCenter)
        self.output_image_6.setWordWrap(True)
        self.output_image_6.setMargin(2)
        self.make_fav6_btn = QPushButton(self.output_thumbs_view_page)
        self.make_fav6_btn.setObjectName(u"make_fav6_btn")
        self.make_fav6_btn.setGeometry(QRect(430, 190, 141, 31))
        self.make_fav6_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.make_fav5_btn = QPushButton(self.output_thumbs_view_page)
        self.make_fav5_btn.setObjectName(u"make_fav5_btn")
        self.make_fav5_btn.setGeometry(QRect(240, 190, 141, 31))
        self.make_fav5_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_fav5_btn = QPushButton(self.output_thumbs_view_page)
        self.remove_fav5_btn.setObjectName(u"remove_fav5_btn")
        self.remove_fav5_btn.setGeometry(QRect(240, 190, 141, 31))
        self.remove_fav5_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_5_btn = QPushButton(self.output_thumbs_view_page)
        self.output_image_5_btn.setObjectName(u"output_image_5_btn")
        self.output_image_5_btn.setGeometry(QRect(230, 230, 151, 121))
        self.output_image_5_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_5_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.make_fav4_btn = QPushButton(self.output_thumbs_view_page)
        self.make_fav4_btn.setObjectName(u"make_fav4_btn")
        self.make_fav4_btn.setGeometry(QRect(50, 190, 141, 31))
        self.make_fav4_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_1 = QLabel(self.output_thumbs_view_page)
        self.output_image_1.setObjectName(u"output_image_1")
        self.output_image_1.setGeometry(QRect(50, 50, 141, 121))
        self.output_image_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_1.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.output_image_1.setFrameShape(QFrame.NoFrame)
        self.output_image_1.setAlignment(Qt.AlignCenter)
        self.output_image_1.setWordWrap(True)
        self.output_image_1.setMargin(2)
        self.output_image_2 = QLabel(self.output_thumbs_view_page)
        self.output_image_2.setObjectName(u"output_image_2")
        self.output_image_2.setGeometry(QRect(230, 50, 141, 121))
        self.output_image_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_2.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.output_image_2.setFrameShape(QFrame.NoFrame)
        self.output_image_2.setAlignment(Qt.AlignCenter)
        self.output_image_2.setWordWrap(True)
        self.output_image_2.setMargin(2)
        self.output_image_5 = QLabel(self.output_thumbs_view_page)
        self.output_image_5.setObjectName(u"output_image_5")
        self.output_image_5.setGeometry(QRect(230, 230, 151, 121))
        self.output_image_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_5.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.output_image_5.setFrameShape(QFrame.NoFrame)
        self.output_image_5.setAlignment(Qt.AlignCenter)
        self.output_image_5.setWordWrap(True)
        self.output_image_5.setMargin(2)
        self.remove_fav4_btn = QPushButton(self.output_thumbs_view_page)
        self.remove_fav4_btn.setObjectName(u"remove_fav4_btn")
        self.remove_fav4_btn.setGeometry(QRect(50, 190, 141, 31))
        self.remove_fav4_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.make_fav2_btn = QPushButton(self.output_thumbs_view_page)
        self.make_fav2_btn.setObjectName(u"make_fav2_btn")
        self.make_fav2_btn.setGeometry(QRect(230, 10, 141, 31))
        self.make_fav2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_3 = QLabel(self.output_thumbs_view_page)
        self.output_image_3.setObjectName(u"output_image_3")
        self.output_image_3.setGeometry(QRect(430, 50, 151, 121))
        self.output_image_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_3.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.output_image_3.setFrameShape(QFrame.NoFrame)
        self.output_image_3.setAlignment(Qt.AlignCenter)
        self.output_image_3.setWordWrap(True)
        self.output_image_3.setMargin(2)
        self.output_image_2_btn = QPushButton(self.output_thumbs_view_page)
        self.output_image_2_btn.setObjectName(u"output_image_2_btn")
        self.output_image_2_btn.setGeometry(QRect(230, 50, 141, 121))
        self.output_image_2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_2_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.remove_fav2_btn = QPushButton(self.output_thumbs_view_page)
        self.remove_fav2_btn.setObjectName(u"remove_fav2_btn")
        self.remove_fav2_btn.setGeometry(QRect(230, 10, 141, 31))
        self.remove_fav2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_fav6_btn = QPushButton(self.output_thumbs_view_page)
        self.remove_fav6_btn.setObjectName(u"remove_fav6_btn")
        self.remove_fav6_btn.setGeometry(QRect(430, 190, 141, 31))
        self.remove_fav6_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.make_fav3_btn = QPushButton(self.output_thumbs_view_page)
        self.make_fav3_btn.setObjectName(u"make_fav3_btn")
        self.make_fav3_btn.setGeometry(QRect(430, 10, 141, 31))
        self.make_fav3_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_3_btn = QPushButton(self.output_thumbs_view_page)
        self.output_image_3_btn.setObjectName(u"output_image_3_btn")
        self.output_image_3_btn.setGeometry(QRect(430, 50, 151, 121))
        self.output_image_3_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_image_3_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.generated_images_stackedWidget.addWidget(self.output_thumbs_view_page)
        self.output_image_1.raise_()
        self.output_image_5.raise_()
        self.output_image_6.raise_()
        self.remove_fav6_btn.raise_()
        self.remove_fav5_btn.raise_()
        self.remove_fav4_btn.raise_()
        self.remove_fav2_btn.raise_()
        self.remove_fav1_btn.raise_()
        self.output_image_6_btn.raise_()
        self.output_image_4.raise_()
        self.make_fav1_btn.raise_()
        self.output_image_4_btn.raise_()
        self.remove_fav3_btn.raise_()
        self.output_image_1_btn.raise_()
        self.make_fav6_btn.raise_()
        self.make_fav5_btn.raise_()
        self.output_image_5_btn.raise_()
        self.make_fav4_btn.raise_()
        self.output_image_2.raise_()
        self.make_fav2_btn.raise_()
        self.output_image_3.raise_()
        self.output_image_2_btn.raise_()
        self.make_fav3_btn.raise_()
        self.output_image_3_btn.raise_()
        self.output_list_view_page = QWidget()
        self.output_list_view_page.setObjectName(u"output_list_view_page")
        self.tableWidget_generated_images = QTableWidget(self.output_list_view_page)
        if (self.tableWidget_generated_images.columnCount() < 3):
            self.tableWidget_generated_images.setColumnCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_generated_images.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_generated_images.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_generated_images.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        self.tableWidget_generated_images.setObjectName(u"tableWidget_generated_images")
        self.tableWidget_generated_images.setGeometry(QRect(10, 20, 611, 281))
        self.tableWidget_generated_images.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tableWidget_generated_images.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_generated_images.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.tableWidget_generated_images.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_generated_images.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_generated_images.horizontalHeader().setMinimumSectionSize(48)
        self.tableWidget_generated_images.horizontalHeader().setDefaultSectionSize(147)
        self.open_output_list_img_btn = QPushButton(self.output_list_view_page)
        self.open_output_list_img_btn.setObjectName(u"open_output_list_img_btn")
        self.open_output_list_img_btn.setGeometry(QRect(470, 23, 151, 41))
        self.open_output_list_img_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_output_list_img_btn.setLayoutDirection(Qt.LeftToRight)
        self.customize_image_btn = QPushButton(self.output_list_view_page)
        self.customize_image_btn.setObjectName(u"customize_image_btn")
        self.customize_image_btn.setGeometry(QRect(420, 310, 161, 31))
        self.customize_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.customize_image_btn.setLayoutDirection(Qt.LeftToRight)
        self.delete_image_btn = QPushButton(self.output_list_view_page)
        self.delete_image_btn.setObjectName(u"delete_image_btn")
        self.delete_image_btn.setGeometry(QRect(20, 310, 161, 31))
        self.delete_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_image_btn.setLayoutDirection(Qt.LeftToRight)
        self.make_fav_list_image_btn = QPushButton(self.output_list_view_page)
        self.make_fav_list_image_btn.setObjectName(u"make_fav_list_image_btn")
        self.make_fav_list_image_btn.setGeometry(QRect(200, 310, 201, 31))
        self.make_fav_list_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.make_fav_list_image_btn.setLayoutDirection(Qt.LeftToRight)
        self.delete_img_confirm_widget = QWidget(self.output_list_view_page)
        self.delete_img_confirm_widget.setObjectName(u"delete_img_confirm_widget")
        self.delete_img_confirm_widget.setGeometry(QRect(20, 110, 561, 241))
        self.delete_img_confirm_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.delete_img_confirm_ok_btn = QPushButton(self.delete_img_confirm_widget)
        self.delete_img_confirm_ok_btn.setObjectName(u"delete_img_confirm_ok_btn")
        self.delete_img_confirm_ok_btn.setGeometry(QRect(130, 150, 151, 41))
        self.delete_img_confirm_ok_btn.setFont(font)
        self.delete_img_confirm_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_img_confirm_ok_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_107 = QLabel(self.delete_img_confirm_widget)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setGeometry(QRect(60, 30, 451, 41))
        self.label_107.setAlignment(Qt.AlignCenter)
        self.delete_img_confirm_cancel_btn = QPushButton(self.delete_img_confirm_widget)
        self.delete_img_confirm_cancel_btn.setObjectName(u"delete_img_confirm_cancel_btn")
        self.delete_img_confirm_cancel_btn.setGeometry(QRect(330, 150, 151, 41))
        self.delete_img_confirm_cancel_btn.setFont(font)
        self.delete_img_confirm_cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_img_confirm_cancel_btn.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_21 = QLabel(self.delete_img_confirm_widget)
        self.account_verify_status_21.setObjectName(u"account_verify_status_21")
        self.account_verify_status_21.setGeometry(QRect(80, 80, 411, 41))
        self.account_verify_status_21.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status_21.setAlignment(Qt.AlignCenter)
        self.fav_added_notification = QWidget(self.output_list_view_page)
        self.fav_added_notification.setObjectName(u"fav_added_notification")
        self.fav_added_notification.setGeometry(QRect(50, 30, 551, 241))
        self.fav_added_notification.setFont(font)
        self.fav_added_notification.setStyleSheet(u"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_85 = QLabel(self.fav_added_notification)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(220, 30, 121, 41))
        self.label_85.setFont(font5)
        self.label_85.setScaledContents(False)
        self.fav_added_notification_ok_btn = QPushButton(self.fav_added_notification)
        self.fav_added_notification_ok_btn.setObjectName(u"fav_added_notification_ok_btn")
        self.fav_added_notification_ok_btn.setGeometry(QRect(220, 150, 121, 41))
        self.fav_added_notification_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.generated_images_stackedWidget.addWidget(self.output_list_view_page)
        self.fav_added_notification.raise_()
        self.delete_img_confirm_widget.raise_()
        self.tableWidget_generated_images.raise_()
        self.open_output_list_img_btn.raise_()
        self.customize_image_btn.raise_()
        self.delete_image_btn.raise_()
        self.make_fav_list_image_btn.raise_()
        self.no_outputs_page = QWidget()
        self.no_outputs_page.setObjectName(u"no_outputs_page")
        self.no_outputs_widget = QLabel(self.no_outputs_page)
        self.no_outputs_widget.setObjectName(u"no_outputs_widget")
        self.no_outputs_widget.setGeometry(QRect(20, 20, 601, 311))
        self.no_outputs_widget.setAlignment(Qt.AlignCenter)
        self.generated_images_stackedWidget.addWidget(self.no_outputs_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.generated_images_stackedWidget.addWidget(self.page)
        self.outputs_list_view_btn = QPushButton(self.outputs_widget)
        self.outputs_list_view_btn.setObjectName(u"outputs_list_view_btn")
        self.outputs_list_view_btn.setGeometry(QRect(200, 10, 181, 41))
        self.outputs_list_view_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.outputs_thumb_view_btn = QPushButton(self.outputs_widget)
        self.outputs_thumb_view_btn.setObjectName(u"outputs_thumb_view_btn")
        self.outputs_thumb_view_btn.setGeometry(QRect(200, 10, 181, 41))
        self.outputs_thumb_view_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stackedWidget_content_pages.addWidget(self.generated_images_page)
        self.image_customization = QWidget()
        self.image_customization.setObjectName(u"image_customization")
        self.img_cutom_widget = QWidget(self.image_customization)
        self.img_cutom_widget.setObjectName(u"img_cutom_widget")
        self.img_cutom_widget.setGeometry(QRect(10, 0, 661, 421))
        self.img_cutom_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_266 = QLabel(self.img_cutom_widget)
        self.label_266.setObjectName(u"label_266")
        self.label_266.setGeometry(QRect(30, 10, 121, 41))
        self.save_changes_image_btn = QPushButton(self.img_cutom_widget)
        self.save_changes_image_btn.setObjectName(u"save_changes_image_btn")
        self.save_changes_image_btn.setGeometry(QRect(300, 10, 141, 41))
        self.save_changes_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_to_img_custom_btn = QPushButton(self.img_cutom_widget)
        self.back_to_img_custom_btn.setObjectName(u"back_to_img_custom_btn")
        self.back_to_img_custom_btn.setGeometry(QRect(590, 10, 51, 41))
        self.back_to_img_custom_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.store_image_btn = QPushButton(self.img_cutom_widget)
        self.store_image_btn.setObjectName(u"store_image_btn")
        self.store_image_btn.setGeometry(QRect(450, 10, 131, 41))
        self.store_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.changes_success_notification = QWidget(self.img_cutom_widget)
        self.changes_success_notification.setObjectName(u"changes_success_notification")
        self.changes_success_notification.setGeometry(QRect(50, 60, 551, 221))
        self.changes_success_notification.setFont(font)
        self.changes_success_notification.setStyleSheet(u"border-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_118 = QLabel(self.changes_success_notification)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(180, 30, 201, 41))
        self.label_118.setFont(font5)
        self.label_118.setScaledContents(False)
        self.label_118.setAlignment(Qt.AlignCenter)
        self.changes_success_ok_btn = QPushButton(self.changes_success_notification)
        self.changes_success_ok_btn.setObjectName(u"changes_success_ok_btn")
        self.changes_success_ok_btn.setGeometry(QRect(220, 150, 121, 41))
        self.changes_success_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.store_success_notification = QWidget(self.img_cutom_widget)
        self.store_success_notification.setObjectName(u"store_success_notification")
        self.store_success_notification.setGeometry(QRect(50, 60, 551, 231))
        self.store_success_notification.setFont(font)
        self.store_success_notification.setStyleSheet(u"border-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_119 = QLabel(self.store_success_notification)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setGeometry(QRect(180, 30, 201, 41))
        self.label_119.setFont(font5)
        self.label_119.setScaledContents(False)
        self.label_119.setAlignment(Qt.AlignCenter)
        self.store_success_ok_btn = QPushButton(self.store_success_notification)
        self.store_success_ok_btn.setObjectName(u"store_success_ok_btn")
        self.store_success_ok_btn.setGeometry(QRect(220, 150, 121, 41))
        self.store_success_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_120 = QLabel(self.img_cutom_widget)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setGeometry(QRect(0, 60, 661, 361))
        self.label_120.setStyleSheet(u"background-color: rgba(0, 40, 59,255);")
        self.reset_changes_image_btn = QPushButton(self.img_cutom_widget)
        self.reset_changes_image_btn.setObjectName(u"reset_changes_image_btn")
        self.reset_changes_image_btn.setGeometry(QRect(150, 10, 141, 41))
        self.reset_changes_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.changes_reset_notification = QWidget(self.img_cutom_widget)
        self.changes_reset_notification.setObjectName(u"changes_reset_notification")
        self.changes_reset_notification.setGeometry(QRect(60, 50, 551, 301))
        self.changes_reset_notification.setFont(font)
        self.changes_reset_notification.setStyleSheet(u"border-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgba(0, 40, 59,240);\n"
"border-radius:10px;")
        self.label_121 = QLabel(self.changes_reset_notification)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(180, 30, 201, 41))
        self.label_121.setFont(font5)
        self.label_121.setScaledContents(False)
        self.label_121.setAlignment(Qt.AlignCenter)
        self.changes_reset_ok_btn = QPushButton(self.changes_reset_notification)
        self.changes_reset_ok_btn.setObjectName(u"changes_reset_ok_btn")
        self.changes_reset_ok_btn.setGeometry(QRect(220, 150, 121, 41))
        self.changes_reset_ok_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.changes_reset_notification.raise_()
        self.changes_success_notification.raise_()
        self.store_success_notification.raise_()
        self.label_266.raise_()
        self.save_changes_image_btn.raise_()
        self.back_to_img_custom_btn.raise_()
        self.store_image_btn.raise_()
        self.reset_changes_image_btn.raise_()
        self.label_120.raise_()
        self.stackedWidget_img_cutom = QStackedWidget(self.image_customization)
        self.stackedWidget_img_cutom.setObjectName(u"stackedWidget_img_cutom")
        self.stackedWidget_img_cutom.setGeometry(QRect(10, 60, 661, 361))
        self.stackedWidget_img_cutom.setMinimumSize(QSize(0, 0))
        self.img_custom_home = QWidget()
        self.img_custom_home.setObjectName(u"img_custom_home")
        self.rotate_image_btn = QPushButton(self.img_custom_home)
        self.rotate_image_btn.setObjectName(u"rotate_image_btn")
        self.rotate_image_btn.setGeometry(QRect(500, 270, 151, 61))
        self.rotate_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.rotate_image_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_136 = QLabel(self.img_custom_home)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(510, 120, 51, 41))
        self.label_136.setPixmap(QPixmap(u":/icons/images/images/map.png"))
        self.label_136.setAlignment(Qt.AlignCenter)
        self.edge_detect_image_btn = QPushButton(self.img_custom_home)
        self.edge_detect_image_btn.setObjectName(u"edge_detect_image_btn")
        self.edge_detect_image_btn.setGeometry(QRect(500, 190, 151, 61))
        self.edge_detect_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.edge_detect_image_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_133 = QLabel(self.img_custom_home)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setGeometry(QRect(580, 50, 51, 41))
        self.label_133.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.contrast_image_btn = QPushButton(self.img_custom_home)
        self.contrast_image_btn.setObjectName(u"contrast_image_btn")
        self.contrast_image_btn.setGeometry(QRect(10, 190, 141, 61))
        self.contrast_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.contrast_image_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.draw_image_btn = QPushButton(self.img_custom_home)
        self.draw_image_btn.setObjectName(u"draw_image_btn")
        self.draw_image_btn.setGeometry(QRect(10, 270, 141, 61))
        self.draw_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.draw_image_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_144 = QLabel(self.img_custom_home)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setGeometry(QRect(110, 200, 51, 41))
        self.label_144.setPixmap(QPixmap(u":/icons/images/images/contrast.png"))
        self.label_144.setAlignment(Qt.AlignCenter)
        self.selected_image = QLabel(self.img_custom_home)
        self.selected_image.setObjectName(u"selected_image")
        self.selected_image.setGeometry(QRect(160, 20, 331, 331))
        self.selected_image.setPixmap(QPixmap(u":/images/images/images/stylegananim1.gif"))
        self.selected_image.setAlignment(Qt.AlignCenter)
        self.translate_image_btn = QPushButton(self.img_custom_home)
        self.translate_image_btn.setObjectName(u"translate_image_btn")
        self.translate_image_btn.setGeometry(QRect(500, 110, 151, 61))
        self.translate_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.translate_image_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_135 = QLabel(self.img_custom_home)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setGeometry(QRect(550, 120, 91, 41))
        self.label_135.setFont(font)
        self.label_135.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_135.setWordWrap(True)
        self.label_140 = QLabel(self.img_custom_home)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setGeometry(QRect(510, 280, 51, 41))
        self.label_140.setPixmap(QPixmap(u":/icons/images/images/rotate-left.png"))
        self.label_140.setAlignment(Qt.AlignCenter)
        self.crop_image_btn = QPushButton(self.img_custom_home)
        self.crop_image_btn.setObjectName(u"crop_image_btn")
        self.crop_image_btn.setGeometry(QRect(500, 40, 151, 61))
        self.crop_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.crop_image_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_142 = QLabel(self.img_custom_home)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setGeometry(QRect(90, 130, 51, 41))
        self.label_142.setPixmap(QPixmap(u":/icons/images/images/options.png"))
        self.label_142.setAlignment(Qt.AlignCenter)
        self.apply_effects_btn = QPushButton(self.img_custom_home)
        self.apply_effects_btn.setObjectName(u"apply_effects_btn")
        self.apply_effects_btn.setGeometry(QRect(10, 40, 141, 61))
        self.apply_effects_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.apply_effects_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_143 = QLabel(self.img_custom_home)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setGeometry(QRect(20, 200, 91, 41))
        self.label_143.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_131 = QLabel(self.img_custom_home)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setGeometry(QRect(20, 50, 81, 41))
        self.label_131.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_145 = QLabel(self.img_custom_home)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setGeometry(QRect(20, 280, 51, 41))
        self.label_145.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_137 = QLabel(self.img_custom_home)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setGeometry(QRect(550, 200, 91, 41))
        self.label_137.setFont(font)
        self.label_137.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_137.setWordWrap(True)
        self.label_141 = QLabel(self.img_custom_home)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setGeometry(QRect(20, 130, 61, 41))
        self.label_141.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_146 = QLabel(self.img_custom_home)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setGeometry(QRect(80, 280, 51, 41))
        self.label_146.setPixmap(QPixmap(u":/icons/images/images/pen.png"))
        self.label_146.setAlignment(Qt.AlignCenter)
        self.label_134 = QLabel(self.img_custom_home)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setGeometry(QRect(510, 50, 51, 41))
        self.label_134.setPixmap(QPixmap(u":/icons/images/images/crop.png"))
        self.label_134.setAlignment(Qt.AlignCenter)
        self.label_138 = QLabel(self.img_custom_home)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setGeometry(QRect(510, 200, 51, 41))
        self.label_138.setPixmap(QPixmap(u":/icons/images/images/eye.png"))
        self.label_138.setAlignment(Qt.AlignCenter)
        self.label_139 = QLabel(self.img_custom_home)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setGeometry(QRect(570, 280, 71, 41))
        self.label_139.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_132 = QLabel(self.img_custom_home)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setGeometry(QRect(100, 50, 51, 41))
        self.label_132.setPixmap(QPixmap(u":/icons/images/images/image.png"))
        self.label_132.setAlignment(Qt.AlignCenter)
        self.style_image_btn = QPushButton(self.img_custom_home)
        self.style_image_btn.setObjectName(u"style_image_btn")
        self.style_image_btn.setGeometry(QRect(10, 120, 141, 61))
        self.style_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.style_image_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.open_cutomized_image_btn = QPushButton(self.img_custom_home)
        self.open_cutomized_image_btn.setObjectName(u"open_cutomized_image_btn")
        self.open_cutomized_image_btn.setGeometry(QRect(160, 20, 331, 331))
        self.open_cutomized_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_cutomized_image_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.stackedWidget_img_cutom.addWidget(self.img_custom_home)
        self.label_136.raise_()
        self.label_144.raise_()
        self.selected_image.raise_()
        self.label_135.raise_()
        self.label_140.raise_()
        self.label_142.raise_()
        self.label_143.raise_()
        self.label_145.raise_()
        self.label_137.raise_()
        self.label_141.raise_()
        self.label_134.raise_()
        self.label_138.raise_()
        self.label_139.raise_()
        self.label_132.raise_()
        self.label_131.raise_()
        self.apply_effects_btn.raise_()
        self.style_image_btn.raise_()
        self.label_146.raise_()
        self.contrast_image_btn.raise_()
        self.draw_image_btn.raise_()
        self.label_133.raise_()
        self.crop_image_btn.raise_()
        self.translate_image_btn.raise_()
        self.edge_detect_image_btn.raise_()
        self.rotate_image_btn.raise_()
        self.open_cutomized_image_btn.raise_()
        self.img_contrast = QWidget()
        self.img_contrast.setObjectName(u"img_contrast")
        self.half_brightness_btn = QPushButton(self.img_contrast)
        self.half_brightness_btn.setObjectName(u"half_brightness_btn")
        self.half_brightness_btn.setGeometry(QRect(20, 40, 111, 61))
        self.half_brightness_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.half_brightness_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.selected_image_filter = QLabel(self.img_contrast)
        self.selected_image_filter.setObjectName(u"selected_image_filter")
        self.selected_image_filter.setGeometry(QRect(280, 20, 331, 331))
        self.selected_image_filter.setPixmap(QPixmap(u":/images/images/images/stylegananim1.gif"))
        self.selected_image_filter.setAlignment(Qt.AlignCenter)
        self.label_178 = QLabel(self.img_contrast)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setGeometry(QRect(20, 50, 111, 41))
        self.label_178.setAlignment(Qt.AlignCenter)
        self.double_brightness_btn = QPushButton(self.img_contrast)
        self.double_brightness_btn.setObjectName(u"double_brightness_btn")
        self.double_brightness_btn.setGeometry(QRect(20, 110, 111, 61))
        self.double_brightness_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.double_brightness_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_179 = QLabel(self.img_contrast)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setGeometry(QRect(20, 120, 111, 41))
        self.label_179.setAlignment(Qt.AlignCenter)
        self.zero_sharpness_btn = QPushButton(self.img_contrast)
        self.zero_sharpness_btn.setObjectName(u"zero_sharpness_btn")
        self.zero_sharpness_btn.setGeometry(QRect(20, 180, 111, 61))
        self.zero_sharpness_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.zero_sharpness_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_180 = QLabel(self.img_contrast)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setGeometry(QRect(20, 190, 111, 41))
        self.label_180.setAlignment(Qt.AlignCenter)
        self.double_sharpness_btn = QPushButton(self.img_contrast)
        self.double_sharpness_btn.setObjectName(u"double_sharpness_btn")
        self.double_sharpness_btn.setGeometry(QRect(20, 250, 111, 61))
        self.double_sharpness_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.double_sharpness_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_181 = QLabel(self.img_contrast)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setGeometry(QRect(20, 260, 111, 41))
        self.label_181.setAlignment(Qt.AlignCenter)
        self.half_contrast_btn = QPushButton(self.img_contrast)
        self.half_contrast_btn.setObjectName(u"half_contrast_btn")
        self.half_contrast_btn.setGeometry(QRect(140, 40, 111, 61))
        self.half_contrast_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.half_contrast_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_188 = QLabel(self.img_contrast)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setGeometry(QRect(140, 50, 111, 41))
        self.label_188.setAlignment(Qt.AlignCenter)
        self.double_contrast_btn = QPushButton(self.img_contrast)
        self.double_contrast_btn.setObjectName(u"double_contrast_btn")
        self.double_contrast_btn.setGeometry(QRect(140, 110, 111, 61))
        self.double_contrast_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.double_contrast_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_189 = QLabel(self.img_contrast)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setGeometry(QRect(140, 120, 111, 41))
        self.label_189.setAlignment(Qt.AlignCenter)
        self.half_color_btn = QPushButton(self.img_contrast)
        self.half_color_btn.setObjectName(u"half_color_btn")
        self.half_color_btn.setGeometry(QRect(140, 180, 111, 61))
        self.half_color_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.half_color_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_191 = QLabel(self.img_contrast)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setGeometry(QRect(140, 190, 111, 41))
        self.label_191.setAlignment(Qt.AlignCenter)
        self.double_color_btn = QPushButton(self.img_contrast)
        self.double_color_btn.setObjectName(u"double_color_btn")
        self.double_color_btn.setGeometry(QRect(140, 250, 111, 61))
        self.double_color_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.double_color_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_192 = QLabel(self.img_contrast)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setGeometry(QRect(140, 260, 111, 41))
        self.label_192.setAlignment(Qt.AlignCenter)
        self.open_cutomized_image_btn_2 = QPushButton(self.img_contrast)
        self.open_cutomized_image_btn_2.setObjectName(u"open_cutomized_image_btn_2")
        self.open_cutomized_image_btn_2.setGeometry(QRect(280, 20, 331, 331))
        self.open_cutomized_image_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_cutomized_image_btn_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.stackedWidget_img_cutom.addWidget(self.img_contrast)
        self.selected_image_filter.raise_()
        self.label_178.raise_()
        self.label_179.raise_()
        self.label_180.raise_()
        self.label_181.raise_()
        self.label_188.raise_()
        self.label_189.raise_()
        self.label_191.raise_()
        self.label_192.raise_()
        self.half_brightness_btn.raise_()
        self.half_contrast_btn.raise_()
        self.double_brightness_btn.raise_()
        self.double_contrast_btn.raise_()
        self.zero_sharpness_btn.raise_()
        self.double_sharpness_btn.raise_()
        self.double_color_btn.raise_()
        self.half_color_btn.raise_()
        self.open_cutomized_image_btn_2.raise_()
        self.img_filters = QWidget()
        self.img_filters.setObjectName(u"img_filters")
        self.mean_filter_btn = QPushButton(self.img_filters)
        self.mean_filter_btn.setObjectName(u"mean_filter_btn")
        self.mean_filter_btn.setGeometry(QRect(40, 30, 111, 61))
        self.mean_filter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.mean_filter_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.bilateral_filter_btn = QPushButton(self.img_filters)
        self.bilateral_filter_btn.setObjectName(u"bilateral_filter_btn")
        self.bilateral_filter_btn.setGeometry(QRect(40, 240, 111, 61))
        self.bilateral_filter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bilateral_filter_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.selected_image_filter_2 = QLabel(self.img_filters)
        self.selected_image_filter_2.setObjectName(u"selected_image_filter_2")
        self.selected_image_filter_2.setGeometry(QRect(270, 10, 331, 331))
        self.selected_image_filter_2.setPixmap(QPixmap(u":/images/images/images/stylegananim1.gif"))
        self.selected_image_filter_2.setAlignment(Qt.AlignCenter)
        self.label_183 = QLabel(self.img_filters)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setGeometry(QRect(40, 40, 111, 41))
        self.label_183.setAlignment(Qt.AlignCenter)
        self.label_184 = QLabel(self.img_filters)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setGeometry(QRect(40, 180, 111, 41))
        self.label_184.setAlignment(Qt.AlignCenter)
        self.median_filter_btn = QPushButton(self.img_filters)
        self.median_filter_btn.setObjectName(u"median_filter_btn")
        self.median_filter_btn.setGeometry(QRect(40, 100, 111, 61))
        self.median_filter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.median_filter_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_185 = QLabel(self.img_filters)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setGeometry(QRect(40, 110, 111, 41))
        self.label_185.setAlignment(Qt.AlignCenter)
        self.gaussian_filter_btn = QPushButton(self.img_filters)
        self.gaussian_filter_btn.setObjectName(u"gaussian_filter_btn")
        self.gaussian_filter_btn.setGeometry(QRect(40, 170, 111, 61))
        self.gaussian_filter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.gaussian_filter_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_186 = QLabel(self.img_filters)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setGeometry(QRect(40, 250, 111, 41))
        self.label_186.setAlignment(Qt.AlignCenter)
        self.open_cutomized_image_btn_3 = QPushButton(self.img_filters)
        self.open_cutomized_image_btn_3.setObjectName(u"open_cutomized_image_btn_3")
        self.open_cutomized_image_btn_3.setGeometry(QRect(270, 10, 331, 331))
        self.open_cutomized_image_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_cutomized_image_btn_3.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.stackedWidget_img_cutom.addWidget(self.img_filters)
        self.selected_image_filter_2.raise_()
        self.label_183.raise_()
        self.label_184.raise_()
        self.label_185.raise_()
        self.gaussian_filter_btn.raise_()
        self.label_186.raise_()
        self.mean_filter_btn.raise_()
        self.median_filter_btn.raise_()
        self.bilateral_filter_btn.raise_()
        self.open_cutomized_image_btn_3.raise_()
        self.edge_detection = QWidget()
        self.edge_detection.setObjectName(u"edge_detection")
        self.selected_image_filter_3 = QLabel(self.edge_detection)
        self.selected_image_filter_3.setObjectName(u"selected_image_filter_3")
        self.selected_image_filter_3.setGeometry(QRect(280, 10, 331, 331))
        self.selected_image_filter_3.setPixmap(QPixmap(u":/images/images/images/stylegananim1.gif"))
        self.selected_image_filter_3.setAlignment(Qt.AlignCenter)
        self.detect_edges_2_btn = QPushButton(self.edge_detection)
        self.detect_edges_2_btn.setObjectName(u"detect_edges_2_btn")
        self.detect_edges_2_btn.setGeometry(QRect(50, 30, 191, 61))
        self.detect_edges_2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.detect_edges_2_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.open_cutomized_image_btn_5 = QPushButton(self.edge_detection)
        self.open_cutomized_image_btn_5.setObjectName(u"open_cutomized_image_btn_5")
        self.open_cutomized_image_btn_5.setGeometry(QRect(280, 10, 331, 331))
        self.open_cutomized_image_btn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_cutomized_image_btn_5.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_196 = QLabel(self.edge_detection)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setGeometry(QRect(50, 40, 191, 41))
        self.label_196.setAlignment(Qt.AlignCenter)
        self.detect_edges_5_btn = QPushButton(self.edge_detection)
        self.detect_edges_5_btn.setObjectName(u"detect_edges_5_btn")
        self.detect_edges_5_btn.setGeometry(QRect(50, 120, 191, 61))
        self.detect_edges_5_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.detect_edges_5_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_197 = QLabel(self.edge_detection)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setGeometry(QRect(50, 130, 191, 41))
        self.label_197.setAlignment(Qt.AlignCenter)
        self.label_198 = QLabel(self.edge_detection)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setGeometry(QRect(50, 220, 191, 41))
        self.label_198.setAlignment(Qt.AlignCenter)
        self.detect_rough_edges_btn = QPushButton(self.edge_detection)
        self.detect_rough_edges_btn.setObjectName(u"detect_rough_edges_btn")
        self.detect_rough_edges_btn.setGeometry(QRect(50, 210, 191, 61))
        self.detect_rough_edges_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.detect_rough_edges_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.stackedWidget_img_cutom.addWidget(self.edge_detection)
        self.selected_image_filter_3.raise_()
        self.open_cutomized_image_btn_5.raise_()
        self.label_196.raise_()
        self.label_197.raise_()
        self.label_198.raise_()
        self.detect_rough_edges_btn.raise_()
        self.detect_edges_2_btn.raise_()
        self.detect_edges_5_btn.raise_()
        self.rotate_image = QWidget()
        self.rotate_image.setObjectName(u"rotate_image")
        self.open_cutomized_image_btn_6 = QPushButton(self.rotate_image)
        self.open_cutomized_image_btn_6.setObjectName(u"open_cutomized_image_btn_6")
        self.open_cutomized_image_btn_6.setGeometry(QRect(140, 0, 331, 331))
        self.open_cutomized_image_btn_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_cutomized_image_btn_6.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.selected_image_filter_4 = QLabel(self.rotate_image)
        self.selected_image_filter_4.setObjectName(u"selected_image_filter_4")
        self.selected_image_filter_4.setGeometry(QRect(140, 0, 331, 331))
        self.selected_image_filter_4.setPixmap(QPixmap(u":/images/images/images/stylegananim1.gif"))
        self.selected_image_filter_4.setAlignment(Qt.AlignCenter)
        self.rotate_image_slider = QSlider(self.rotate_image)
        self.rotate_image_slider.setObjectName(u"rotate_image_slider")
        self.rotate_image_slider.setGeometry(QRect(140, 330, 331, 33))
        self.rotate_image_slider.setMaximumSize(QSize(16777215, 16777215))
        self.rotate_image_slider.setBaseSize(QSize(0, 0))
        self.rotate_image_slider.setCursor(QCursor(Qt.OpenHandCursor))
        self.rotate_image_slider.setMaximum(360)
        self.rotate_image_slider.setOrientation(Qt.Horizontal)
        self.rotate_image_slider.setInvertedAppearance(False)
        self.label_270 = QLabel(self.rotate_image)
        self.label_270.setObjectName(u"label_270")
        self.label_270.setGeometry(QRect(110, 310, 31, 31))
        self.label_271 = QLabel(self.rotate_image)
        self.label_271.setObjectName(u"label_271")
        self.label_271.setGeometry(QRect(480, 310, 31, 31))
        self.stackedWidget_img_cutom.addWidget(self.rotate_image)
        self.selected_image_filter_4.raise_()
        self.rotate_image_slider.raise_()
        self.label_270.raise_()
        self.label_271.raise_()
        self.open_cutomized_image_btn_6.raise_()
        self.crop_image = QWidget()
        self.crop_image.setObjectName(u"crop_image")
        self.selected_image_filter_5 = QLabel(self.crop_image)
        self.selected_image_filter_5.setObjectName(u"selected_image_filter_5")
        self.selected_image_filter_5.setGeometry(QRect(280, 10, 331, 331))
        self.selected_image_filter_5.setPixmap(QPixmap(u":/images/images/images/stylegananim1.gif"))
        self.selected_image_filter_5.setAlignment(Qt.AlignCenter)
        self.apply_crop_btn = QPushButton(self.crop_image)
        self.apply_crop_btn.setObjectName(u"apply_crop_btn")
        self.apply_crop_btn.setGeometry(QRect(50, 20, 111, 61))
        self.apply_crop_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.apply_crop_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.open_cutomized_image_btn_7 = QPushButton(self.crop_image)
        self.open_cutomized_image_btn_7.setObjectName(u"open_cutomized_image_btn_7")
        self.open_cutomized_image_btn_7.setGeometry(QRect(280, 10, 331, 331))
        self.open_cutomized_image_btn_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_cutomized_image_btn_7.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_199 = QLabel(self.crop_image)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setGeometry(QRect(50, 20, 111, 61))
        self.label_199.setAlignment(Qt.AlignCenter)
        self.label_116 = QLabel(self.crop_image)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(50, 170, 201, 171))
        self.label_116.setPixmap(QPixmap(u":/images/images/images/croper.PNG"))
        self.label_116.setScaledContents(True)
        self.label_117 = QLabel(self.crop_image)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(80, 200, 91, 101))
        self.label_117.setPixmap(QPixmap(u":/images/images/images/arrow.png"))
        self.label_117.setScaledContents(True)
        self.label_274 = QLabel(self.crop_image)
        self.label_274.setObjectName(u"label_274")
        self.label_274.setGeometry(QRect(40, 90, 211, 71))
        self.label_274.setWordWrap(True)
        self.stackedWidget_img_cutom.addWidget(self.crop_image)
        self.selected_image_filter_5.raise_()
        self.open_cutomized_image_btn_7.raise_()
        self.label_199.raise_()
        self.apply_crop_btn.raise_()
        self.label_116.raise_()
        self.label_117.raise_()
        self.label_274.raise_()
        self.draw_on_image = QWidget()
        self.draw_on_image.setObjectName(u"draw_on_image")
        self.use_pen_btn = QPushButton(self.draw_on_image)
        self.use_pen_btn.setObjectName(u"use_pen_btn")
        self.use_pen_btn.setGeometry(QRect(50, 30, 111, 61))
        self.use_pen_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.use_pen_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_200 = QLabel(self.draw_on_image)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setGeometry(QRect(50, 30, 111, 61))
        self.label_200.setAlignment(Qt.AlignCenter)
        self.selected_image_filter_6 = QLabel(self.draw_on_image)
        self.selected_image_filter_6.setObjectName(u"selected_image_filter_6")
        self.selected_image_filter_6.setGeometry(QRect(280, 10, 331, 331))
        self.selected_image_filter_6.setPixmap(QPixmap(u":/images/images/images/stylegananim1.gif"))
        self.selected_image_filter_6.setAlignment(Qt.AlignCenter)
        self.open_cutomized_image_btn_8 = QPushButton(self.draw_on_image)
        self.open_cutomized_image_btn_8.setObjectName(u"open_cutomized_image_btn_8")
        self.open_cutomized_image_btn_8.setGeometry(QRect(280, 10, 331, 331))
        self.open_cutomized_image_btn_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_cutomized_image_btn_8.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_201 = QLabel(self.draw_on_image)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setGeometry(QRect(50, 120, 111, 61))
        self.label_201.setAlignment(Qt.AlignCenter)
        self.use_brush_btn = QPushButton(self.draw_on_image)
        self.use_brush_btn.setObjectName(u"use_brush_btn")
        self.use_brush_btn.setGeometry(QRect(50, 120, 111, 61))
        self.use_brush_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.use_brush_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.stackedWidget_img_cutom.addWidget(self.draw_on_image)
        self.label_200.raise_()
        self.selected_image_filter_6.raise_()
        self.open_cutomized_image_btn_8.raise_()
        self.use_pen_btn.raise_()
        self.label_201.raise_()
        self.use_brush_btn.raise_()
        self.img_styling = QWidget()
        self.img_styling.setObjectName(u"img_styling")
        self.selected_image_content = QLabel(self.img_styling)
        self.selected_image_content.setObjectName(u"selected_image_content")
        self.selected_image_content.setGeometry(QRect(0, 20, 331, 331))
        self.selected_image_content.setPixmap(QPixmap(u":/images/images/images/stylegananim1.gif"))
        self.selected_image_content.setAlignment(Qt.AlignCenter)
        self.label_268 = QLabel(self.img_styling)
        self.label_268.setObjectName(u"label_268")
        self.label_268.setGeometry(QRect(100, -10, 121, 31))
        self.label_268.setAlignment(Qt.AlignCenter)
        self.selected_style_image = QLabel(self.img_styling)
        self.selected_style_image.setObjectName(u"selected_style_image")
        self.selected_style_image.setGeometry(QRect(330, 20, 331, 331))
        self.selected_style_image.setPixmap(QPixmap(u":/images/images/images/stylegananim1.gif"))
        self.selected_style_image.setAlignment(Qt.AlignCenter)
        self.label_182 = QLabel(self.img_styling)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setGeometry(QRect(70, 300, 171, 61))
        self.label_182.setStyleSheet(u"background-color: rgba(0, 40, 59,255);")
        self.label_182.setAlignment(Qt.AlignCenter)
        self.apply_mask_btn = QPushButton(self.img_styling)
        self.apply_mask_btn.setObjectName(u"apply_mask_btn")
        self.apply_mask_btn.setGeometry(QRect(70, 300, 171, 61))
        self.apply_mask_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.apply_mask_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.select_style_img_btn = QPushButton(self.img_styling)
        self.select_style_img_btn.setObjectName(u"select_style_img_btn")
        self.select_style_img_btn.setGeometry(QRect(330, 20, 331, 331))
        self.select_style_img_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_style_img_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.open_cutomized_image_btn_4 = QPushButton(self.img_styling)
        self.open_cutomized_image_btn_4.setObjectName(u"open_cutomized_image_btn_4")
        self.open_cutomized_image_btn_4.setGeometry(QRect(0, 20, 331, 331))
        self.open_cutomized_image_btn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_cutomized_image_btn_4.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_269 = QLabel(self.img_styling)
        self.label_269.setObjectName(u"label_269")
        self.label_269.setGeometry(QRect(420, -10, 121, 31))
        self.label_269.setAlignment(Qt.AlignCenter)
        self.blend_image_btn = QPushButton(self.img_styling)
        self.blend_image_btn.setObjectName(u"blend_image_btn")
        self.blend_image_btn.setGeometry(QRect(420, 300, 171, 61))
        self.blend_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.blend_image_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_194 = QLabel(self.img_styling)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setGeometry(QRect(420, 300, 171, 61))
        self.label_194.setStyleSheet(u"background-color: rgba(0, 40, 59,255);")
        self.label_194.setAlignment(Qt.AlignCenter)
        self.style_result_label = QLabel(self.img_styling)
        self.style_result_label.setObjectName(u"style_result_label")
        self.style_result_label.setGeometry(QRect(0, 0, 661, 361))
        self.style_result_label.setStyleSheet(u"background-color: rgba(0, 40, 59,255);")
        self.style_img_result = QLabel(self.img_styling)
        self.style_img_result.setObjectName(u"style_img_result")
        self.style_img_result.setGeometry(QRect(170, 20, 331, 331))
        self.style_img_result.setScaledContents(True)
        self.style_img_result.setAlignment(Qt.AlignCenter)
        self.style_img_result_btn = QPushButton(self.img_styling)
        self.style_img_result_btn.setObjectName(u"style_img_result_btn")
        self.style_img_result_btn.setGeometry(QRect(170, 20, 331, 331))
        self.style_img_result_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.style_img_result_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.style_img_result_cross_btn = QPushButton(self.img_styling)
        self.style_img_result_cross_btn.setObjectName(u"style_img_result_cross_btn")
        self.style_img_result_cross_btn.setGeometry(QRect(600, 20, 51, 41))
        self.style_img_result_cross_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.blend_image_slider = QSlider(self.img_styling)
        self.blend_image_slider.setObjectName(u"blend_image_slider")
        self.blend_image_slider.setGeometry(QRect(90, 330, 481, 22))
        self.blend_image_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.blend_image_slider.setOrientation(Qt.Horizontal)
        self.blend_image_slider.setInvertedAppearance(True)
        self.blend_image_slider.setInvertedControls(False)
        self.label_290 = QLabel(self.img_styling)
        self.label_290.setObjectName(u"label_290")
        self.label_290.setGeometry(QRect(510, 270, 101, 31))
        self.label_291 = QLabel(self.img_styling)
        self.label_291.setObjectName(u"label_291")
        self.label_291.setGeometry(QRect(50, 270, 91, 31))
        self.bitwise_or_btn = QPushButton(self.img_styling)
        self.bitwise_or_btn.setObjectName(u"bitwise_or_btn")
        self.bitwise_or_btn.setGeometry(QRect(520, 100, 131, 61))
        self.bitwise_or_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bitwise_or_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.bitwise_and_btn = QPushButton(self.img_styling)
        self.bitwise_and_btn.setObjectName(u"bitwise_and_btn")
        self.bitwise_and_btn.setGeometry(QRect(520, 180, 131, 61))
        self.bitwise_and_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bitwise_and_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.bitwise_xor_btn = QPushButton(self.img_styling)
        self.bitwise_xor_btn.setObjectName(u"bitwise_xor_btn")
        self.bitwise_xor_btn.setGeometry(QRect(520, 270, 131, 61))
        self.bitwise_xor_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bitwise_xor_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.bitwise_not_btn = QPushButton(self.img_styling)
        self.bitwise_not_btn.setObjectName(u"bitwise_not_btn")
        self.bitwise_not_btn.setGeometry(QRect(20, 120, 131, 61))
        self.bitwise_not_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bitwise_not_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.blacknwhite_btn = QPushButton(self.img_styling)
        self.blacknwhite_btn.setObjectName(u"blacknwhite_btn")
        self.blacknwhite_btn.setGeometry(QRect(20, 220, 131, 61))
        self.blacknwhite_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.blacknwhite_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.stackedWidget_img_cutom.addWidget(self.img_styling)
        self.bitwise_and_btn.raise_()
        self.bitwise_not_btn.raise_()
        self.bitwise_or_btn.raise_()
        self.bitwise_xor_btn.raise_()
        self.blacknwhite_btn.raise_()
        self.blend_image_slider.raise_()
        self.style_img_result.raise_()
        self.style_img_result_btn.raise_()
        self.style_img_result_cross_btn.raise_()
        self.style_result_label.raise_()
        self.label_290.raise_()
        self.label_291.raise_()
        self.selected_image_content.raise_()
        self.label_268.raise_()
        self.selected_style_image.raise_()
        self.label_269.raise_()
        self.open_cutomized_image_btn_4.raise_()
        self.select_style_img_btn.raise_()
        self.label_182.raise_()
        self.apply_mask_btn.raise_()
        self.label_194.raise_()
        self.blend_image_btn.raise_()
        self.image_translation = QWidget()
        self.image_translation.setObjectName(u"image_translation")
        self.s_img = QLabel(self.image_translation)
        self.s_img.setObjectName(u"s_img")
        self.s_img.setGeometry(QRect(190, 80, 161, 161))
        self.s_img.setPixmap(QPixmap(u":/images/images/images/trans-style.jpg"))
        self.s_img.setScaledContents(True)
        self.s_img.setAlignment(Qt.AlignCenter)
        self.label_193 = QLabel(self.image_translation)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setGeometry(QRect(240, 280, 171, 61))
        self.label_193.setStyleSheet(u"background-color: rgba(0, 40, 59,255);")
        self.label_193.setAlignment(Qt.AlignCenter)
        self.apply_translation_btn = QPushButton(self.image_translation)
        self.apply_translation_btn.setObjectName(u"apply_translation_btn")
        self.apply_translation_btn.setGeometry(QRect(240, 280, 171, 61))
        self.apply_translation_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.apply_translation_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.c_img = QLabel(self.image_translation)
        self.c_img.setObjectName(u"c_img")
        self.c_img.setGeometry(QRect(10, 80, 161, 161))
        self.c_img.setPixmap(QPixmap(u":/images/images/images/trans-content.jpg"))
        self.c_img.setScaledContents(True)
        self.c_img.setAlignment(Qt.AlignCenter)
        self.label_272 = QLabel(self.image_translation)
        self.label_272.setObjectName(u"label_272")
        self.label_272.setGeometry(QRect(200, 30, 121, 31))
        self.label_272.setAlignment(Qt.AlignCenter)
        self.label_273 = QLabel(self.image_translation)
        self.label_273.setObjectName(u"label_273")
        self.label_273.setGeometry(QRect(20, 30, 121, 31))
        self.label_273.setAlignment(Qt.AlignCenter)
        self.s_img_2 = QLabel(self.image_translation)
        self.s_img_2.setObjectName(u"s_img_2")
        self.s_img_2.setGeometry(QRect(430, 70, 191, 181))
        self.s_img_2.setPixmap(QPixmap(u":/images/images/images/trans-result.png"))
        self.s_img_2.setScaledContents(True)
        self.s_img_2.setAlignment(Qt.AlignCenter)
        self.label_283 = QLabel(self.image_translation)
        self.label_283.setObjectName(u"label_283")
        self.label_283.setGeometry(QRect(470, 30, 121, 31))
        self.label_283.setAlignment(Qt.AlignCenter)
        self.label_123 = QLabel(self.image_translation)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setGeometry(QRect(370, 140, 51, 41))
        self.label_123.setPixmap(QPixmap(u":/icons/images/icons/cil-chevron-right.png"))
        self.label_123.setScaledContents(True)
        self.stackedWidget_img_cutom.addWidget(self.image_translation)
        self.s_img.raise_()
        self.c_img.raise_()
        self.label_272.raise_()
        self.label_273.raise_()
        self.label_193.raise_()
        self.apply_translation_btn.raise_()
        self.s_img_2.raise_()
        self.label_283.raise_()
        self.label_123.raise_()
        self.image_translation_process = QWidget()
        self.image_translation_process.setObjectName(u"image_translation_process")
        self.style_img_result_2 = QLabel(self.image_translation_process)
        self.style_img_result_2.setObjectName(u"style_img_result_2")
        self.style_img_result_2.setGeometry(QRect(170, 10, 331, 331))
        self.style_img_result_2.setPixmap(QPixmap(u":/images/images/images/stylegananim1.gif"))
        self.style_img_result_2.setScaledContents(True)
        self.style_img_result_2.setAlignment(Qt.AlignCenter)
        self.style_result_label_2 = QLabel(self.image_translation_process)
        self.style_result_label_2.setObjectName(u"style_result_label_2")
        self.style_result_label_2.setGeometry(QRect(0, 0, 661, 361))
        self.style_result_label_2.setStyleSheet(u"background-color: rgba(0, 40, 59,255);")
        self.style_gan_plabel_4 = QLabel(self.image_translation_process)
        self.style_gan_plabel_4.setObjectName(u"style_gan_plabel_4")
        self.style_gan_plabel_4.setGeometry(QRect(60, 70, 231, 221))
        self.style_gan_plabel_4.setStyleSheet(u"background-color: rgb(210, 254, 255,255);")
        self.style_gan_plabel_4.setPixmap(QPixmap(u":/images/images/images/tick.png"))
        self.style_gan_plabel_4.setScaledContents(True)
        self.style_gan_plabel_4.setMargin(0)
        self.phase1_label = QLabel(self.image_translation_process)
        self.phase1_label.setObjectName(u"phase1_label")
        self.phase1_label.setGeometry(QRect(60, 70, 231, 221))
        self.phase1_label.setFont(font)
        self.phase1_label.setAlignment(Qt.AlignCenter)
        self.label_284 = QLabel(self.image_translation_process)
        self.label_284.setObjectName(u"label_284")
        self.label_284.setGeometry(QRect(120, 20, 121, 41))
        self.label_285 = QLabel(self.image_translation_process)
        self.label_285.setObjectName(u"label_285")
        self.label_285.setGeometry(QRect(440, 20, 121, 41))
        self.style_gan_plabel_5 = QLabel(self.image_translation_process)
        self.style_gan_plabel_5.setObjectName(u"style_gan_plabel_5")
        self.style_gan_plabel_5.setGeometry(QRect(380, 70, 231, 221))
        self.style_gan_plabel_5.setStyleSheet(u"background-color: rgb(210, 254, 255,255);")
        self.style_gan_plabel_5.setPixmap(QPixmap(u":/images/images/images/tick.png"))
        self.style_gan_plabel_5.setScaledContents(True)
        self.style_gan_plabel_5.setMargin(0)
        self.phase2_label = QLabel(self.image_translation_process)
        self.phase2_label.setObjectName(u"phase2_label")
        self.phase2_label.setGeometry(QRect(380, 70, 231, 221))
        self.phase2_label.setFont(font)
        self.phase2_label.setAlignment(Qt.AlignCenter)
        self.label_127 = QLabel(self.image_translation_process)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setGeometry(QRect(60, 310, 561, 41))
        self.label_127.setFont(font)
        self.stackedWidget_img_cutom.addWidget(self.image_translation_process)
        self.style_img_result_2.raise_()
        self.style_result_label_2.raise_()
        self.style_gan_plabel_4.raise_()
        self.label_284.raise_()
        self.label_285.raise_()
        self.style_gan_plabel_5.raise_()
        self.phase2_label.raise_()
        self.label_127.raise_()
        self.phase1_label.raise_()
        self.image_translation_result = QWidget()
        self.image_translation_result.setObjectName(u"image_translation_result")
        self.content_image = QLabel(self.image_translation_result)
        self.content_image.setObjectName(u"content_image")
        self.content_image.setGeometry(QRect(30, 100, 161, 161))
        self.content_image.setPixmap(QPixmap(u":/images/images/images/trans-content.jpg"))
        self.content_image.setScaledContents(True)
        self.content_image.setAlignment(Qt.AlignCenter)
        self.label_275 = QLabel(self.image_translation_result)
        self.label_275.setObjectName(u"label_275")
        self.label_275.setGeometry(QRect(220, 50, 121, 31))
        self.label_275.setAlignment(Qt.AlignCenter)
        self.label_128 = QLabel(self.image_translation_result)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setGeometry(QRect(390, 160, 51, 41))
        self.label_128.setPixmap(QPixmap(u":/icons/images/icons/cil-chevron-right.png"))
        self.label_128.setScaledContents(True)
        self.translated_image = QLabel(self.image_translation_result)
        self.translated_image.setObjectName(u"translated_image")
        self.translated_image.setGeometry(QRect(450, 90, 191, 181))
        self.translated_image.setPixmap(QPixmap(u":/images/images/images/trans-result.png"))
        self.translated_image.setScaledContents(True)
        self.translated_image.setAlignment(Qt.AlignCenter)
        self.label_286 = QLabel(self.image_translation_result)
        self.label_286.setObjectName(u"label_286")
        self.label_286.setGeometry(QRect(490, 50, 121, 31))
        self.label_286.setAlignment(Qt.AlignCenter)
        self.style_image = QLabel(self.image_translation_result)
        self.style_image.setObjectName(u"style_image")
        self.style_image.setGeometry(QRect(210, 100, 161, 161))
        self.style_image.setPixmap(QPixmap(u":/images/images/images/trans-style.jpg"))
        self.style_image.setScaledContents(True)
        self.style_image.setAlignment(Qt.AlignCenter)
        self.label_287 = QLabel(self.image_translation_result)
        self.label_287.setObjectName(u"label_287")
        self.label_287.setGeometry(QRect(40, 50, 121, 31))
        self.label_287.setAlignment(Qt.AlignCenter)
        self.translated_image_btn = QPushButton(self.image_translation_result)
        self.translated_image_btn.setObjectName(u"translated_image_btn")
        self.translated_image_btn.setGeometry(QRect(450, 90, 191, 181))
        self.translated_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.translated_image_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.translate_new_btn = QPushButton(self.image_translation_result)
        self.translate_new_btn.setObjectName(u"translate_new_btn")
        self.translate_new_btn.setGeometry(QRect(30, 290, 171, 61))
        self.translate_new_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.translate_new_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_195 = QLabel(self.image_translation_result)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setGeometry(QRect(30, 290, 171, 61))
        self.label_195.setStyleSheet(u"background-color: rgba(0, 40, 59,255);")
        self.label_195.setAlignment(Qt.AlignCenter)
        self.stackedWidget_img_cutom.addWidget(self.image_translation_result)
        self.content_image.raise_()
        self.label_275.raise_()
        self.label_128.raise_()
        self.translated_image.raise_()
        self.label_286.raise_()
        self.style_image.raise_()
        self.label_287.raise_()
        self.translated_image_btn.raise_()
        self.label_195.raise_()
        self.translate_new_btn.raise_()
        self.stackedWidget_content_pages.addWidget(self.image_customization)
        self.images_library_page = QWidget()
        self.images_library_page.setObjectName(u"images_library_page")
        self.images_library_widget = QWidget(self.images_library_page)
        self.images_library_widget.setObjectName(u"images_library_widget")
        self.images_library_widget.setGeometry(QRect(20, 10, 691, 411))
        self.images_library_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_72 = QLabel(self.images_library_widget)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(30, 70, 321, 271))
        self.label_72.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_72.setFrameShape(QFrame.NoFrame)
        self.label_72.setAlignment(Qt.AlignCenter)
        self.label_72.setWordWrap(True)
        self.label_72.setMargin(36)
        self.label_73 = QLabel(self.images_library_widget)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(390, 70, 271, 261))
        self.label_73.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_73.setFrameShape(QFrame.NoFrame)
        self.label_73.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_73.setWordWrap(True)
        self.label_73.setMargin(36)
        self.label_74 = QLabel(self.images_library_widget)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(410, 270, 241, 31))
        self.label_74.setAlignment(Qt.AlignCenter)
        self.label_74.setWordWrap(True)
        self.label_74.setMargin(3)
        self.label_75 = QLabel(self.images_library_widget)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(450, 120, 161, 111))
        self.label_75.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_75.setScaledContents(True)
        self.label_75.setAlignment(Qt.AlignCenter)
        self.label_75.setMargin(15)
        self.stackedWidget_content_pages.addWidget(self.images_library_page)
        self.help_page = QWidget()
        self.help_page.setObjectName(u"help_page")
        self.help_widget = QWidget(self.help_page)
        self.help_widget.setObjectName(u"help_widget")
        self.help_widget.setGeometry(QRect(20, 10, 691, 411))
        self.help_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_80 = QLabel(self.help_widget)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(30, 70, 321, 271))
        self.label_80.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_80.setFrameShape(QFrame.NoFrame)
        self.label_80.setAlignment(Qt.AlignCenter)
        self.label_80.setWordWrap(True)
        self.label_80.setMargin(36)
        self.label_81 = QLabel(self.help_widget)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(390, 70, 271, 261))
        self.label_81.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_81.setFrameShape(QFrame.NoFrame)
        self.label_81.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_81.setWordWrap(True)
        self.label_81.setMargin(36)
        self.label_82 = QLabel(self.help_widget)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(410, 270, 241, 31))
        self.label_82.setAlignment(Qt.AlignCenter)
        self.label_82.setWordWrap(True)
        self.label_82.setMargin(3)
        self.label_83 = QLabel(self.help_widget)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(450, 120, 161, 111))
        self.label_83.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_83.setScaledContents(True)
        self.label_83.setAlignment(Qt.AlignCenter)
        self.label_83.setMargin(15)
        self.stackedWidget_content_pages.addWidget(self.help_page)
        self.stackedWidget_top_icons = QStackedWidget(self.content_page)
        self.stackedWidget_top_icons.setObjectName(u"stackedWidget_top_icons")
        self.stackedWidget_top_icons.setGeometry(QRect(30, 9, 701, 131))
        self.nav_icons_page = QWidget()
        self.nav_icons_page.setObjectName(u"nav_icons_page")
        self.about_icon_widget = QWidget(self.nav_icons_page)
        self.about_icon_widget.setObjectName(u"about_icon_widget")
        self.about_icon_widget.setGeometry(QRect(540, 0, 131, 121))
        self.about_icon_widget.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_icon_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_71 = QLabel(self.about_icon_widget)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(40, 20, 41, 41))
        self.label_71.setPixmap(QPixmap(u":/images/images/images/info.png"))
        self.label_71.setScaledContents(True)
        self.label_90 = QLabel(self.about_icon_widget)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(20, 80, 91, 16))
        self.label_90.setAlignment(Qt.AlignCenter)
        self.about_icon_btn = QPushButton(self.about_icon_widget)
        self.about_icon_btn.setObjectName(u"about_icon_btn")
        self.about_icon_btn.setGeometry(QRect(0, 0, 131, 121))
        self.about_icon_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_icon_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.send_feedback_icon_widget = QWidget(self.nav_icons_page)
        self.send_feedback_icon_widget.setObjectName(u"send_feedback_icon_widget")
        self.send_feedback_icon_widget.setGeometry(QRect(360, 0, 131, 121))
        self.send_feedback_icon_widget.setCursor(QCursor(Qt.PointingHandCursor))
        self.send_feedback_icon_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_92 = QLabel(self.send_feedback_icon_widget)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(40, 20, 41, 41))
        self.label_92.setPixmap(QPixmap(u":/images/images/images/Frame 1345.png"))
        self.label_92.setScaledContents(True)
        self.label_93 = QLabel(self.send_feedback_icon_widget)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(20, 80, 91, 16))
        self.label_93.setAlignment(Qt.AlignCenter)
        self.send_feedback_icon_btn = QPushButton(self.send_feedback_icon_widget)
        self.send_feedback_icon_btn.setObjectName(u"send_feedback_icon_btn")
        self.send_feedback_icon_btn.setGeometry(QRect(0, 0, 131, 121))
        self.send_feedback_icon_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.send_feedback_icon_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.recent_activity_icon_widget = QWidget(self.nav_icons_page)
        self.recent_activity_icon_widget.setObjectName(u"recent_activity_icon_widget")
        self.recent_activity_icon_widget.setGeometry(QRect(10, 0, 131, 121))
        self.recent_activity_icon_widget.setCursor(QCursor(Qt.PointingHandCursor))
        self.recent_activity_icon_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_94 = QLabel(self.recent_activity_icon_widget)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(50, 20, 41, 41))
        self.label_94.setPixmap(QPixmap(u":/images/images/images/Frame 16.png"))
        self.label_94.setScaledContents(True)
        self.label_96 = QLabel(self.recent_activity_icon_widget)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(20, 80, 91, 16))
        self.label_96.setAlignment(Qt.AlignCenter)
        self.recent_activity_icon_btn = QPushButton(self.recent_activity_icon_widget)
        self.recent_activity_icon_btn.setObjectName(u"recent_activity_icon_btn")
        self.recent_activity_icon_btn.setGeometry(QRect(0, 0, 131, 121))
        self.recent_activity_icon_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.recent_activity_icon_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.myfav_icon_widget = QWidget(self.nav_icons_page)
        self.myfav_icon_widget.setObjectName(u"myfav_icon_widget")
        self.myfav_icon_widget.setGeometry(QRect(170, 0, 131, 121))
        self.myfav_icon_widget.setCursor(QCursor(Qt.PointingHandCursor))
        self.myfav_icon_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label_97 = QLabel(self.myfav_icon_widget)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(40, 20, 41, 41))
        self.label_97.setPixmap(QPixmap(u":/images/images/images/Frame 1344.png"))
        self.label_97.setScaledContents(True)
        self.label_108 = QLabel(self.myfav_icon_widget)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setGeometry(QRect(20, 80, 91, 16))
        self.label_108.setAlignment(Qt.AlignCenter)
        self.myfav_icon_btn = QPushButton(self.myfav_icon_widget)
        self.myfav_icon_btn.setObjectName(u"myfav_icon_btn")
        self.myfav_icon_btn.setGeometry(QRect(0, 0, 131, 121))
        self.myfav_icon_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.myfav_icon_btn.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.stackedWidget_top_icons.addWidget(self.nav_icons_page)
        self.verify_email_page = QWidget()
        self.verify_email_page.setObjectName(u"verify_email_page")
        self.acc_not_verify_widget_2 = QWidget(self.verify_email_page)
        self.acc_not_verify_widget_2.setObjectName(u"acc_not_verify_widget_2")
        self.acc_not_verify_widget_2.setGeometry(QRect(10, 0, 691, 121))
        self.acc_not_verify_widget_2.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;")
        self.verify_email_btn_2 = QPushButton(self.acc_not_verify_widget_2)
        self.verify_email_btn_2.setObjectName(u"verify_email_btn_2")
        self.verify_email_btn_2.setGeometry(QRect(400, 30, 151, 41))
        self.verify_email_btn_2.setFont(font)
        self.verify_email_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.verify_email_btn_2.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton::hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.account_verify_status_4 = QLabel(self.acc_not_verify_widget_2)
        self.account_verify_status_4.setObjectName(u"account_verify_status_4")
        self.account_verify_status_4.setGeometry(QRect(80, 30, 221, 41))
        self.account_verify_status_4.setStyleSheet(u"color:rgb(255, 135, 87)")
        self.account_verify_status_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget_top_icons.addWidget(self.verify_email_page)
        self.stackedWidget_5.addWidget(self.content_page)
        self.login_first_page = QWidget()
        self.login_first_page.setObjectName(u"login_first_page")
        self.LoginFirst_widget = QWidget(self.login_first_page)
        self.LoginFirst_widget.setObjectName(u"LoginFirst_widget")
        self.LoginFirst_widget.setGeometry(QRect(50, 70, 691, 411))
        self.LoginFirst_widget.setStyleSheet(u"background-color: rgba(0, 40, 59,255);\n"
"border-radius:10px;\n"
"pressed{\n"
"background-color:rgba(2,65,118,100);\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.go_to_login_btn_2 = QPushButton(self.LoginFirst_widget)
        self.go_to_login_btn_2.setObjectName(u"go_to_login_btn_2")
        self.go_to_login_btn_2.setGeometry(QRect(100, 280, 181, 51))
        self.go_to_login_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_56 = QLabel(self.LoginFirst_widget)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(50, 70, 301, 171))
        self.label_56.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_56.setFrameShape(QFrame.NoFrame)
        self.label_56.setAlignment(Qt.AlignCenter)
        self.label_56.setWordWrap(True)
        self.label_56.setMargin(36)
        self.label_57 = QLabel(self.LoginFirst_widget)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(390, 70, 271, 261))
        self.label_57.setStyleSheet(u"background-color: rgb(0, 66, 97);")
        self.label_57.setFrameShape(QFrame.NoFrame)
        self.label_57.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_57.setWordWrap(True)
        self.label_57.setMargin(36)
        self.label_58 = QLabel(self.LoginFirst_widget)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(410, 270, 241, 31))
        self.label_58.setAlignment(Qt.AlignCenter)
        self.label_58.setWordWrap(True)
        self.label_58.setMargin(3)
        self.label_59 = QLabel(self.LoginFirst_widget)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(450, 120, 161, 111))
        self.label_59.setPixmap(QPixmap(u":/images/images/images/LogoW.png"))
        self.label_59.setScaledContents(True)
        self.label_59.setAlignment(Qt.AlignCenter)
        self.label_59.setMargin(15)
        self.stackedWidget_5.addWidget(self.login_first_page)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-218, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon7)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font7 = QFont()
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font7);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem33)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget_5.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.stackedWidget_5.addWidget(self.new_page)

        self.horizontalLayout_7.addWidget(self.stackedWidget_5)

        self.stackedWidget_5.raise_()
        self.stackedWidget_3.raise_()

        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setMinimumSize(QSize(0, 0))
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setEnabled(True)
        self.topMenus.setMinimumSize(QSize(0, 0))
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_hide_gadgets = QPushButton(self.topMenus)
        self.btn_hide_gadgets.setObjectName(u"btn_hide_gadgets")
        sizePolicy.setHeightForWidth(self.btn_hide_gadgets.sizePolicy().hasHeightForWidth())
        self.btn_hide_gadgets.setSizePolicy(sizePolicy)
        self.btn_hide_gadgets.setMinimumSize(QSize(0, 45))
        self.btn_hide_gadgets.setFont(font)
        self.btn_hide_gadgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_hide_gadgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_hide_gadgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-input.png);")

        self.verticalLayout_14.addWidget(self.btn_hide_gadgets)

        self.btn_sysinfo = QPushButton(self.topMenus)
        self.btn_sysinfo.setObjectName(u"btn_sysinfo")
        sizePolicy.setHeightForWidth(self.btn_sysinfo.sizePolicy().hasHeightForWidth())
        self.btn_sysinfo.setSizePolicy(sizePolicy)
        self.btn_sysinfo.setMinimumSize(QSize(0, 45))
        self.btn_sysinfo.setFont(font)
        self.btn_sysinfo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sysinfo.setLayoutDirection(Qt.LeftToRight)
        self.btn_sysinfo.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);")

        self.verticalLayout_14.addWidget(self.btn_sysinfo)

        self.btn_usage = QPushButton(self.topMenus)
        self.btn_usage.setObjectName(u"btn_usage")
        sizePolicy.setHeightForWidth(self.btn_usage.sizePolicy().hasHeightForWidth())
        self.btn_usage.setSizePolicy(sizePolicy)
        self.btn_usage.setMinimumSize(QSize(0, 45))
        self.btn_usage.setFont(font)
        self.btn_usage.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_usage.setLayoutDirection(Qt.LeftToRight)
        self.btn_usage.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart.png);")

        self.verticalLayout_14.addWidget(self.btn_usage)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font8 = QFont()
        font8.setBold(False)
        font8.setItalic(False)
        self.creditsLabel.setFont(font8)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget_3.setCurrentIndex(2)
        self.listWidget_notifications.setCurrentRow(-1)
        self.stackedWidget_5.setCurrentIndex(3)
        self.stackedWidget_content_pages.setCurrentIndex(0)
        self.datsets_stackedWidget.setCurrentIndex(0)
        self.stackedWidget_model_training.setCurrentIndex(0)
        self.stackedWidget_stylegan.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"AI Images", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Toolkit for AI Image Collection", None))
        self.label_54.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.dash_board_btn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.datasets_btn.setText(QCoreApplication.translate("MainWindow", u"Datasets", None))
        self.model_training_btn.setText(QCoreApplication.translate("MainWindow", u"Model Training", None))
        self.style_gan_tab_btn.setText(QCoreApplication.translate("MainWindow", u"Style GAN", None))
        self.generated_images_btn.setText(QCoreApplication.translate("MainWindow", u"Generated Images", None))
        self.images_library_btn.setText(QCoreApplication.translate("MainWindow", u"Images Library", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.account_settings_btn.setText(QCoreApplication.translate("MainWindow", u"Account Settings", None))
        self.help_btn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"**AI Images Toolkit**  AI IMAGES is a platform where designers and animators can\n"
"find a best matched character for their bussiness requirements. All the images\n"
"generated by our trained models are purely artificial in nature. Our goal is to\n"
"improve the output quality of the artificial images using best practices in the\n"
"field of GAN models.  AI Images @ 2021 All Rights Reserved  Version: 1.0.0\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">AI Images Toolkit</span>  AI IMAGES is a platform where designers and animators can find a best matched character for their bussiness requirements. All the images generated by our trained models are purely artificial in nature. Our goal is to improve the output quality of the artificial images using best practices in the field of GAN models.  AI Images @ 2021 All Rights Reserved  Version: 1.0.0</p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"AI IMAGES TOOLKIT - A SOLUTION FOR THE DESIGNERS TO GET A DESIRED AI GENERATED CHARACTER", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.clear_recent_history_btn_5.setText(QCoreApplication.translate("MainWindow", u"Clear History", None))
        self.system_info_label_2.setText(QCoreApplication.translate("MainWindow", u"Darwin", None))
        self.processor_info_label_2.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.show_cpu_graph_btn_3.setText(QCoreApplication.translate("MainWindow", u"Show CPU Graph", None))
        self.show_ram_graph_btn_3.setText(QCoreApplication.translate("MainWindow", u"Show RAM Graph", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.clear_recent_history_btn_6.setText(QCoreApplication.translate("MainWindow", u"Clear History", None))

        __sortingEnabled = self.listWidget_notifications.isSortingEnabled()
        self.listWidget_notifications.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_notifications.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Notification 1", None));
        ___qlistwidgetitem1 = self.listWidget_notifications.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Notification 2", None));
        ___qlistwidgetitem2 = self.listWidget_notifications.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Notification 3", None));
        self.listWidget_notifications.setSortingEnabled(__sortingEnabled)

        self.label_68.setText(QCoreApplication.translate("MainWindow", u"CPU USAGE", None))
        self.clear_recent_history_btn_3.setText(QCoreApplication.translate("MainWindow", u"Clear History", None))
        self.labelAplicationName_2.setText(QCoreApplication.translate("MainWindow", u"<strong>CPU</strong> USAGE", None))
        self.labelPercentageCPU_2.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">60</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>", None))
        self.labelCredits_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.clear_recent_history_btn_4.setText(QCoreApplication.translate("MainWindow", u"Clear History", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"RAM USAGE", None))
        self.labelAplicationName_3.setText(QCoreApplication.translate("MainWindow", u"<strong>RAM</strong> USAGE", None))
        self.labelPercentageRAM.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">25</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>", None))
        self.labelCredits_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.login_form.setText("")
        self.logoW.setText("")
        self.user_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.user_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"LOG IN", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LOGIN SUCCESSFUL", None))
        self.login_success_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"LOGIN UNSUCCESSFUL", None))
        self.login_fail_message.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.login_fail_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.go_to_signup_btn.setText(QCoreApplication.translate("MainWindow", u"SIGN UP", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Register Your Self", None))
        self.forget_credentials_widget_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Enter your Email address", None))
        self.forget_credentials_widget_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.recovery_email.setText("")
        self.recovery_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.recovery_email_error.setText("")
        self.recovery_message_widget_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Check in your Inbox or Junk for the lost credentials", None))
        self.new_password_widget_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Enter your New Password", None))
        self.new_password_widget_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.new_password.setText("")
        self.new_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.confirm_new_password.setText("")
        self.confirm_new_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm New Password", None))
        self.new_password_error.setText("")
        self.new_password_confirm_error.setText("")
        self.forget_pass_name_btn.setText(QCoreApplication.translate("MainWindow", u"Forgot your User Name or Password!", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"NEW CREDENTIALS", None))
        self.new_credentials_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.new_uname.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.new_upass.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.signup_form.setText("")
        self.signup_user_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.signup_btn.setText(QCoreApplication.translate("MainWindow", u"SIGN UP", None))
        self.go_to_login_btn.setText(QCoreApplication.translate("MainWindow", u"LOG IN", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Already Registered ", None))
        self.signup_user_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.logoW_2.setText("")
        self.signup_user_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.signup_confirm_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.username_error.setText(QCoreApplication.translate("MainWindow", u"Must start with a letter. Prefer an alphanumeric i.e. 'name125' LIMIT : 4-8", None))
        self.email_error.setText(QCoreApplication.translate("MainWindow", u"Must have a proper format i.e. 'mail@gmail.com'", None))
        self.password_error.setText(QCoreApplication.translate("MainWindow", u"Must have a proper format i.e. 'password!123' and contain atleast one special character LIMIT : 8-15", None))
        self.password_confirm_error.setText(QCoreApplication.translate("MainWindow", u"Password Mismatch", None))
        self.username_already_exists_error.setText(QCoreApplication.translate("MainWindow", u"We are Sorry! The user already exists! Try a different username", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SIGNUP SUCCESSFUL", None))
        self.signup_success_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.notify_signup_uname.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.notify_signup_upass.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.upload_profile_pic_btn.setText(QCoreApplication.translate("MainWindow", u"Upload Your Picture", None))
        self.profile_image.setText("")
        self.verify_email_btn.setText(QCoreApplication.translate("MainWindow", u"Verify Email", None))
        self.account_verify_status.setText(QCoreApplication.translate("MainWindow", u"Your Account is not Verified!", None))
        self.home_dashboard.setText("")
        self.profile_pic_change_btn.setText(QCoreApplication.translate("MainWindow", u"Change Picture", None))
        self.profile_view_user_name.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.profile_view_email.setText(QCoreApplication.translate("MainWindow", u"Email Address", None))
        self.profile_view_pic.setText("")
        self.deactivate_account_btn.setText(QCoreApplication.translate("MainWindow", u"Deactivate Account", None))
        self.profile_pic_remove_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Picture", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Email Address", None))
        self.signout_btn.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.account_verify_stat.setText(QCoreApplication.translate("MainWindow", u"Account Not Verified!", None))
        self.deactivate_account_confirm_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Do you want to deactivate your account?", None))
        self.deactivate_account_confirm_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.account_verify_status_3.setText(QCoreApplication.translate("MainWindow", u"WARNING: All of the account will be lost!", None))
        self.verify_message_widget_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Check in your Inbox or Junk for the account verification!", None))
        self.acc_verify_done_btn.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.account_verify_status_2.setText(QCoreApplication.translate("MainWindow", u"Your Account is Verified!", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Recent", None))
        ___qtablewidgetitem = self.tableWidget_recent_activity.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ACTIVITY", None));
        ___qtablewidgetitem1 = self.tableWidget_recent_activity.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"DATE", None));
        ___qtablewidgetitem2 = self.tableWidget_recent_activity.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"TIME", None));
        ___qtablewidgetitem3 = self.tableWidget_recent_activity.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"LEVEL", None));
        self.clear_recent_history_btn.setText(QCoreApplication.translate("MainWindow", u"Clear History", None))
        self.no_recent.setText(QCoreApplication.translate("MainWindow", u"No Recent Activity", None))
        self.clear_fav_history_confirm_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Do you want to clear your favourites history?", None))
        self.clear_fav_history_confirm_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.account_verify_status_7.setText(QCoreApplication.translate("MainWindow", u"WARNING: All of the history will be lost!", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"My favourites", None))
        ___qtablewidgetitem4 = self.tableWidget_my_favourites.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ITEM", None));
        ___qtablewidgetitem5 = self.tableWidget_my_favourites.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CATEGORY", None));
        ___qtablewidgetitem6 = self.tableWidget_my_favourites.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"FAVOURITE SINCE", None));
        self.no_favourites.setText(QCoreApplication.translate("MainWindow", u"No Favourites Items", None))
        self.clear_myfavourites_history_btn.setText(QCoreApplication.translate("MainWindow", u"Clear History", None))
        self.open_favourite_btn.setText(QCoreApplication.translate("MainWindow", u"Open Selected Favourite", None))
        self.clear_history_confirm_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Do you want to clear your recent activity history?", None))
        self.clear_history_confirm_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.account_verify_status_6.setText(QCoreApplication.translate("MainWindow", u"WARNING: All of the history will be lost!", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"RAM/CPU USAGE GRAPH", None))
        self.show_ram_graph_btn.setText(QCoreApplication.translate("MainWindow", u"Show RAM Graph", None))
        self.show_cpu_graph_btn.setText(QCoreApplication.translate("MainWindow", u"Show CPU Graph", None))
        self.show_circular_percent_btn.setText(QCoreApplication.translate("MainWindow", u"Show Circular %", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Feedback", None))
        self.send_feedback_btn.setText(QCoreApplication.translate("MainWindow", u"Send Message", None))
        self.confirm_feedback_widget_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Do you want to send your feedback?", None))
        self.confirm_feedback_widget_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.feedback.setText("")
        self.feedback.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter you feedback here!", None))
        self.feedback_success_msg.setText(QCoreApplication.translate("MainWindow", u"Feedback Sent! Thanks for your support", None))
        self.feedback_sent_notification_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"About Us", None))
        self.contact_us_btn.setText(QCoreApplication.translate("MainWindow", u"Contact Us", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"AI IMAGES is a platform where designers and animators can find a best matched character for their bussiness requirements. All the images generated by our trained models are purely artificial in nature. Our goal is to improve the output quality of the artificial images using best practices in the field of GAN models. ", None))
        self.label_51.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"AI IMAGES @ 2021 All Rights Reserved", None))
        self.label_53.setText("")
        self.search_dataset.setText("")
        self.search_dataset.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seach Custom Dataset ...", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Dataset Found", None))
        self.view_searched_dst_btn.setText(QCoreApplication.translate("MainWindow", u"View Dataset", None))
        self.searched_dst_thumbnail_btn.setText("")
        self.searched_dst_thumbnail.setText("")
        self.searched_dst_name.setText(QCoreApplication.translate("MainWindow", u"dataset name", None))
        self.searched_dst_size.setText(QCoreApplication.translate("MainWindow", u"size", None))
        self.searched_dst_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.create_new_dataset_btn.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Human", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Anime", None))
        self.anime_thumbnail_btn.setText("")
        self.human_thumbnail_btn.setText("")
        self.label_88.setText("")
        self.human_thumbnail.setText("")
        self.anime_thumbnail.setText("")
        self.new_datset_thumbnail_btn.setText("")
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Flowers", None))
        self.flower_thumbnail_btn.setText("")
        self.label_new_dataset.setText(QCoreApplication.translate("MainWindow", u"New Dataset", None))
        self.new_datset_thumbnail.setText("")
        self.flower_thumbnail.setText("")
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"Sort", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"By Name", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"By Date", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"By Size", None))

        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Available Datasets", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Dataset Not Found!", None))
        self.view_searched_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.signup_form_2.setText("")
        self.new_dtset_name.setText("")
        self.new_dtset_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter New Dataset Name", None))
        self.logoW_3.setText("")
        self.new_dst_upload_thumb_btn.setText(QCoreApplication.translate("MainWindow", u"Thumbnail", None))
        self.new_dst_u_image_0.setText("")
        self.select_dst_size.setItemText(0, QCoreApplication.translate("MainWindow", u"less than 1 GB", None))
        self.select_dst_size.setItemText(1, QCoreApplication.translate("MainWindow", u"greater than 1 GB", None))
        self.select_dst_size.setItemText(2, QCoreApplication.translate("MainWindow", u"greater than 2 GB", None))

        self.label_231.setText(QCoreApplication.translate("MainWindow", u"Dataset Size", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Upload Images", None))
        self.new_dst_u_image_1_btn.setText("")
        self.new_dst_u_image_1.setText("")
        self.new_dst_u_image_2.setText("")
        self.new_dst_u_image_3.setText("")
        self.new_dst_u_image_4.setText("")
        self.new_dst_u_image_5.setText("")
        self.new_dst_u_image_2_btn.setText("")
        self.new_dst_u_image_3_btn.setText("")
        self.new_dst_u_image_4_btn.setText("")
        self.new_dst_u_image_5_btn.setText("")
        self.back_to_dataset_btn_5.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.create_dst_done_btn.setText(QCoreApplication.translate("MainWindow", u"Create Dataset", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Dataset Created Successfully", None))
        self.dst_success_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Unable to create dataset!", None))
        self.dst_fail_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.new_dataset_name_2.setText(QCoreApplication.translate("MainWindow", u"Searched Dataset", None))
        self.new_dst_image_8.setText("")
        self.new_dst_image_9.setText("")
        self.new_dst_image_10.setText("")
        self.new_dst_image_11.setText("")
        self.new_dst_image_12.setText("")
        self.back_to_dataset_btn_6.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.delete_new_dataset_btn_2.setText(QCoreApplication.translate("MainWindow", u"Delete Dataset", None))
        self.upload_images_btn_2.setText(QCoreApplication.translate("MainWindow", u"Upload Images", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Image Added Successfully", None))
        self.dst_success_ok_btn_3.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Unable to delete dataset!", None))
        self.dst_fail_ok_btn_3.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.new_dst_image_7.setText("")
        self.new_dataset_del_confirm_ok_btn_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Do you want to delete the dataset?", None))
        self.new_dataset_del_confirm_cancel_btn_2.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.account_verify_status_9.setText(QCoreApplication.translate("MainWindow", u"WARNING: All of the data will be lost!", None))
        self.anime_image_1.setText("")
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"Anime Dataset", None))
        self.anime_image_2.setText("")
        self.anime_image_4.setText("")
        self.anime_image_5.setText("")
        self.anime_image_3.setText("")
        self.anime_image_6.setText("")
        self.back_to_dataset_btn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.human_image_1.setText("")
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"Human Dataset", None))
        self.human_image_2.setText("")
        self.human_image_4.setText("")
        self.human_image_5.setText("")
        self.human_image_3.setText("")
        self.human_image_6.setText("")
        self.back_to_dataset_btn_2.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.new_dataset_name.setText(QCoreApplication.translate("MainWindow", u"New Dataset", None))
        self.new_dst_image_2.setText("")
        self.new_dst_image_4.setText("")
        self.new_dst_image_5.setText("")
        self.new_dst_image_3.setText("")
        self.new_dst_image_6.setText("")
        self.back_to_dataset_btn_3.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.delete_new_dataset_btn.setText(QCoreApplication.translate("MainWindow", u"Delete Dataset", None))
        self.upload_images_btn.setText(QCoreApplication.translate("MainWindow", u"Upload Images", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Image Added Successfully", None))
        self.dst_success_ok_btn_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Unable to delete dataset!", None))
        self.dst_fail_ok_btn_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.new_dst_image_1.setText("")
        self.new_dataset_del_confirm_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Do you want to delete the dataset?", None))
        self.new_dataset_del_confirm_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.account_verify_status_8.setText(QCoreApplication.translate("MainWindow", u"WARNING: All of the data will be lost!", None))
        self.flower_image_1.setText("")
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"Flowers Dataset", None))
        self.flower_image_2.setText("")
        self.flower_image_4.setText("")
        self.flower_image_5.setText("")
        self.flower_image_3.setText("")
        self.flower_image_6.setText("")
        self.back_to_dataset_btn_4.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Select Dataset", None))
        self.search_dataset_2.setText("")
        self.search_dataset_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seach Custom Dataset ...", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"By Name", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"By Date", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"By Size", None))

        self.label_222.setText(QCoreApplication.translate("MainWindow", u"Sort", None))
        self.label_228.setText("")
        self.label_229.setText("")
        self.label_230.setText(QCoreApplication.translate("MainWindow", u"The artificial output images will be generated on the basis of the selected dataset. Please choose the dataset wisely that best fits your need.", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Human", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Anime", None))
        self.anime_thumbnail_btn_2.setText("")
        self.human_thumbnail_btn_2.setText("")
        self.human_thumbnail_2.setText("")
        self.anime_thumbnail_2.setText("")
        self.new_datset_thumbnail_btn_2.setText("")
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Flowers", None))
        self.flower_thumbnail_btn_2.setText("")
        self.label_new_dataset_2.setText(QCoreApplication.translate("MainWindow", u"New Dataset", None))
        self.new_datset_thumbnail_2.setText("")
        self.flower_thumbnail_2.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Dataset Found", None))
        self.view_searched_dst_btn_2.setText(QCoreApplication.translate("MainWindow", u"Select Dataset", None))
        self.searched_dst_thumbnail_btn_2.setText("")
        self.searched_dst_thumbnail_2.setText("")
        self.searched_dst_name_2.setText(QCoreApplication.translate("MainWindow", u"dataset name", None))
        self.searched_dst_size_2.setText(QCoreApplication.translate("MainWindow", u"size", None))
        self.searched_dst_cancel_btn_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Dataset Not Found!", None))
        self.view_searched_ok_btn_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"Model Training", None))
        self.update_algo_btn.setText(QCoreApplication.translate("MainWindow", u"UPDATE ALGORITHM", None))
        self.update_algo_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Enter Secret Admin Key", None))
        self.update_algo_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.admin_key.setText("")
        self.admin_key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Admin Key", None))
        self.key_match_error.setText("")
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"Selected Dataset", None))
        self.edit_dst_btn.setText(QCoreApplication.translate("MainWindow", u"EDIT DATASET", None))
        self.change_dst_btn.setText(QCoreApplication.translate("MainWindow", u"CHANGE DATASET", None))
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"Human", None))
        self.label_224.setText("")
        self.label_226.setText("")
        self.label_220.setText("")
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"By starting the training process the output images will be generated on the basis of the selected dataset. Choose the dataset that best fits your need. Please be patient, the training process can take some time! View generated images tab for the results", None))
        self.run_gan_btn.setText(QCoreApplication.translate("MainWindow", u"RUN GAN TRAINING", None))
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"Model Training Progress", None))
        self.rerun_gan_btn.setText(QCoreApplication.translate("MainWindow", u"RE-RUN GAN TRAINING", None))
        self.cancel_training_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL TRAINING", None))
        self.label_242.setText("")
        self.label_243.setText("")
        self.label_239.setText(QCoreApplication.translate("MainWindow", u"Training Progress", None))
        self.label_240.setText(QCoreApplication.translate("MainWindow", u"Time Spent", None))
        self.label_244.setText(QCoreApplication.translate("MainWindow", u"Current Epoch", None))
        self.label_245.setText(QCoreApplication.translate("MainWindow", u" Images Generated", None))
        self.label_246.setText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.label_247.setText(QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.view_generated_imgs_btn.setText(QCoreApplication.translate("MainWindow", u"VIEW OUTPUT  ", None))
        self.label_251.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_252.setText(QCoreApplication.translate("MainWindow", u"Dataset Processing", None))
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"The training process is on going. Please be patient for the output results as the GAN model requires some time to train for better results!", None))
        self.cancel_training_confirm_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Do you want to terminate the model training process?", None))
        self.cancel_training_confirm_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.account_verify_status_10.setText(QCoreApplication.translate("MainWindow", u"WARNING: All of the training progress will be lost!", None))
        self.rerun_training_confirm_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Do you want to restart the model training process?", None))
        self.rerun_training_confirm_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.account_verify_status_11.setText(QCoreApplication.translate("MainWindow", u"WARNING: All of the training progress will be lost!", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"Training Paused", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"RE-RUN GAN TRAINING", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"RESUME TRAINING", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"CANCEL TRAINING", None))
        self.label_248.setText("")
        self.label_249.setText("")
        self.label_253.setText(QCoreApplication.translate("MainWindow", u" Images Generated", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"VIEW OUTPUT", None))
        self.label_250.setText(QCoreApplication.translate("MainWindow", u"The training process has been paused. You can view the progress so far. Please don't forget to resume the training anytime you want!", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"VIEW POGRESS", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"RESUME TRAINING", None))
        self.user_name_google.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.user_password_google.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.google_verify_code_widget_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Enter your 6-digit Verification Code Sent to Your Phone", None))
        self.google_verify_code_widget_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.google_verify_code.setText("")
        self.google_verify_code.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXXXX", None))
        self.verify_code_error.setText(QCoreApplication.translate("MainWindow", u"Invalid Code! Try again", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"G-", None))
        self.google_verify_code_widget_resend_btn.setText(QCoreApplication.translate("MainWindow", u"RESEND", None))
        self.recovery_message_widget_ok_btn_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Check in your Inbox or Junk for the lost credentials", None))
        self.new_password_widget_ok_btn_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Enter your New Password", None))
        self.new_password_widget_cancel_btn_2.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.new_password_2.setText("")
        self.new_password_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.confirm_new_password_2.setText("")
        self.confirm_new_password_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm New Password", None))
        self.new_password_error_2.setText("")
        self.new_password_confirm_error_2.setText("")
        self.login_google_btn.setText(QCoreApplication.translate("MainWindow", u"LOG IN TO GOOGLE", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"LOGIN UNSUCCESSFUL", None))
        self.login_fail_message_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.login_fail_ok_btn_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.forget_pass_name_google_btn.setText(QCoreApplication.translate("MainWindow", u"Forgot your User Name or Password!", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"LOGIN SUCCESSFUL", None))
        self.login_success_ok_btn_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.login_form_2.setText("")
        self.signup_google_btn.setText(QCoreApplication.translate("MainWindow", u"SIGN UP", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Register Your Self", None))
        self.logoW_6.setText("")
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"NEW CREDENTIALS", None))
        self.new_credentials_ok_btn_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.new_uname_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.new_upass_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.logoW_4.setText("")
        self.logoW_5.setText("")
        self.login_loading_label.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Select Dataset", None))
        self.search_dataset_3.setText("")
        self.search_dataset_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seach Custom Dataset ...", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"By Name", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"By Date", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"By Size", None))

        self.label_234.setText(QCoreApplication.translate("MainWindow", u"Sort", None))
        self.label_235.setText("")
        self.label_236.setText("")
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"The artificial output images will be generated on the basis of the selected dataset. Please choose the dataset wisely that best fits your need.", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Human", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Anime", None))
        self.anime_thumbnail_btn_3.setText("")
        self.human_thumbnail_btn_3.setText("")
        self.human_thumbnail_3.setText("")
        self.anime_thumbnail_3.setText("")
        self.new_datset_thumbnail_btn_3.setText("")
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Flowers", None))
        self.flower_thumbnail_btn_3.setText("")
        self.label_new_dataset_3.setText(QCoreApplication.translate("MainWindow", u"New Dataset", None))
        self.new_datset_thumbnail_3.setText("")
        self.flower_thumbnail_3.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Dataset Found", None))
        self.view_searched_dst_btn_3.setText(QCoreApplication.translate("MainWindow", u"Select Dataset", None))
        self.searched_dst_thumbnail_btn_3.setText("")
        self.searched_dst_thumbnail_3.setText("")
        self.searched_dst_name_3.setText(QCoreApplication.translate("MainWindow", u"dataset name", None))
        self.searched_dst_size_3.setText(QCoreApplication.translate("MainWindow", u"size", None))
        self.searched_dst_cancel_btn_3.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Dataset Not Found!", None))
        self.view_searched_ok_btn_3.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_254.setText(QCoreApplication.translate("MainWindow", u"Style GAN Pretrained Models", None))
        self.update_stylegan_algo_btn.setText(QCoreApplication.translate("MainWindow", u"UPDATE ALGORITHM", None))
        self.update_algo_ok_btn_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Enter Secret Admin Key", None))
        self.update_algo_cancel_btn_2.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.admin_key_2.setText("")
        self.admin_key_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Admin Key", None))
        self.key_match_error_2.setText("")
        self.label_258.setText("")
        self.label_259.setText("")
        self.label_260.setText(QCoreApplication.translate("MainWindow", u"Welcome to styleGAN (NVIDIA) \"We propose an alternative generator architecture for generative adversarial networks, borrowing from style transfer literature.\" The quality of the output images are high class, even it is difficult to tell the generated image is real or fake. The pretrained stylegan models provide a quick service to have access to high quality images. StyleGAN 2 generates images of very high quality! ", None))
        self.style_gan1_btn.setText(QCoreApplication.translate("MainWindow", u"Style GAN 1", None))
        self.style_gan2_btn.setText(QCoreApplication.translate("MainWindow", u"Style GAN 2", None))
        self.label_261.setText("")
        self.label_262.setText("")
        self.label_263.setText("")
        self.train_stylegan_btn.setText(QCoreApplication.translate("MainWindow", u"TRAIN STYLEGAN MODEL", None))
        self.logout_google_btn.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.label_277.setText("")
        self.output_size_style1.setItemText(0, QCoreApplication.translate("MainWindow", u"10", None))
        self.output_size_style1.setItemText(1, QCoreApplication.translate("MainWindow", u"20", None))
        self.output_size_style1.setItemText(2, QCoreApplication.translate("MainWindow", u"30", None))
        self.output_size_style1.setItemText(3, QCoreApplication.translate("MainWindow", u"40", None))
        self.output_size_style1.setItemText(4, QCoreApplication.translate("MainWindow", u"50", None))

        self.output_size_style1.setCurrentText(QCoreApplication.translate("MainWindow", u"10", None))
        self.runtime_env_style1.setItemText(0, QCoreApplication.translate("MainWindow", u"GPU", None))
        self.runtime_env_style1.setItemText(1, QCoreApplication.translate("MainWindow", u"TPU", None))

        self.runtime_env_style1.setCurrentText(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.mount_gdrive_style1_btn.setText(QCoreApplication.translate("MainWindow", u"MOUNT G-DRIVE", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"RUNTIME ENVIRONMENT", None))
        self.label_281.setText("")
        self.generate_images_style1_btn.setText(QCoreApplication.translate("MainWindow", u"GENERATE STYLEGAN IMAGES", None))
        self.label_309.setText(QCoreApplication.translate("MainWindow", u"Selected Dataset", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"OUTPUT IMAGES SIZE", None))
        self.label_282.setText(QCoreApplication.translate("MainWindow", u"The stylegan 1 pretrained model will generate images of high quality according. Please be patient after pressing generate images button!", None))
        self.label_295.setText(QCoreApplication.translate("MainWindow", u"Style GAN 1", None))
        self.label_296.setText("")
        self.selected_dst_style1.setItemText(0, QCoreApplication.translate("MainWindow", u"human", None))
        self.selected_dst_style1.setItemText(1, QCoreApplication.translate("MainWindow", u"celebrity", None))
        self.selected_dst_style1.setItemText(2, QCoreApplication.translate("MainWindow", u"cats", None))
        self.selected_dst_style1.setItemText(3, QCoreApplication.translate("MainWindow", u"cars", None))
        self.selected_dst_style1.setItemText(4, QCoreApplication.translate("MainWindow", u"bedrooms", None))

        self.selected_dst_style1.setCurrentText(QCoreApplication.translate("MainWindow", u"human", None))
        self.back_to_models_btn_1.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.output_size_error.setText(QCoreApplication.translate("MainWindow", u"Invalid Output Size! Try again", None))
        self.runtime_env_error.setText(QCoreApplication.translate("MainWindow", u"The runtime environment as \"TPU\" may be very slow and tedious. We reccoment to use \"GPU\" for the efficiency of the processes! ", None))
        self.label_255.setText(QCoreApplication.translate("MainWindow", u"Choose the dataset that best fits your need. Please be patient, the process can take some time! View generated images tab for the results", None))
        self.label_288.setText(QCoreApplication.translate("MainWindow", u"Style GAN 1 Progress", None))
        self.rerun_style1gan_btn.setText(QCoreApplication.translate("MainWindow", u"REGENERATE IMAGES", None))
        self.cancel_progress_style1_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL PROGRESS", None))
        self.label_292.setText("")
        self.label_298.setText("")
        self.label_301.setText(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.label_302.setText(QCoreApplication.translate("MainWindow", u"Time Spent", None))
        self.label_303.setText(QCoreApplication.translate("MainWindow", u" Images Generated", None))
        self.label_304.setText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.label_305.setText(QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.view_style1_generated_imgs_btn.setText(QCoreApplication.translate("MainWindow", u"VIEW OUTPUT  ", None))
        self.label_306.setText(QCoreApplication.translate("MainWindow", u"Dataset Processing", None))
        self.label_307.setText(QCoreApplication.translate("MainWindow", u"The image generation process is on going. Please be patient for the output results as the STYLE GAN 1 requires some time to generate high quality results using pretrained model!", None))
        self.cancel_stylegan1_confirm_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Do you want to terminate the image generation process?", None))
        self.cancel_stylegan1_confirm_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.account_verify_status_16.setText(QCoreApplication.translate("MainWindow", u"WARNING: All of the progress will be lost!", None))
        self.rerun_stylegan1_confirm_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Do you want to restart the image generation process?", None))
        self.rerun_tstylegan1_confirm_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.account_verify_status_17.setText(QCoreApplication.translate("MainWindow", u"WARNING: All of the  progress will be lost!", None))
        self.label_311.setText("")
        self.loading_label_dst.setText("")
        self.style_gan_plabel.setText("")
        self.label_264.setText("")
        self.back_to_style1_page_btn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_276.setText("")
        self.end_image_style2.setItemText(0, QCoreApplication.translate("MainWindow", u"20", None))
        self.end_image_style2.setItemText(1, QCoreApplication.translate("MainWindow", u"30", None))
        self.end_image_style2.setItemText(2, QCoreApplication.translate("MainWindow", u"40", None))
        self.end_image_style2.setItemText(3, QCoreApplication.translate("MainWindow", u"50", None))

        self.end_image_style2.setCurrentText(QCoreApplication.translate("MainWindow", u"20", None))
        self.runtime_env_style2.setItemText(0, QCoreApplication.translate("MainWindow", u"GPU", None))
        self.runtime_env_style2.setItemText(1, QCoreApplication.translate("MainWindow", u"TPU", None))

        self.runtime_env_style2.setCurrentText(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.mount_gdrive_style2_btn.setText(QCoreApplication.translate("MainWindow", u"MOUNT G-DRIVE", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"RUNTIME ENVIRONMENT", None))
        self.label_278.setText("")
        self.generate_images_style2_btn.setText(QCoreApplication.translate("MainWindow", u"GENERATE STYLEGAN IMAGES", None))
        self.label_300.setText(QCoreApplication.translate("MainWindow", u"Selected Dataset", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"OUTPUT IMAGES RANGE", None))
        self.label_279.setText(QCoreApplication.translate("MainWindow", u"The stylegan 2 pretrained model will generate images of very high quality according. Please be patient after pressing generate images button!", None))
        self.label_280.setText(QCoreApplication.translate("MainWindow", u"Style GAN 2", None))
        self.label_297.setText("")
        self.selected_dst_style2.setItemText(0, QCoreApplication.translate("MainWindow", u"human", None))
        self.selected_dst_style2.setItemText(1, QCoreApplication.translate("MainWindow", u"anime", None))
        self.selected_dst_style2.setItemText(2, QCoreApplication.translate("MainWindow", u"cat", None))
        self.selected_dst_style2.setItemText(3, QCoreApplication.translate("MainWindow", u"church", None))
        self.selected_dst_style2.setItemText(4, QCoreApplication.translate("MainWindow", u"car", None))
        self.selected_dst_style2.setItemText(5, QCoreApplication.translate("MainWindow", u"horse", None))

        self.selected_dst_style2.setCurrentText(QCoreApplication.translate("MainWindow", u"human", None))
        self.start_image_style2.setItemText(0, QCoreApplication.translate("MainWindow", u"10", None))
        self.start_image_style2.setItemText(1, QCoreApplication.translate("MainWindow", u"20", None))
        self.start_image_style2.setItemText(2, QCoreApplication.translate("MainWindow", u"30", None))
        self.start_image_style2.setItemText(3, QCoreApplication.translate("MainWindow", u"40", None))
        self.start_image_style2.setItemText(4, QCoreApplication.translate("MainWindow", u"50", None))

        self.start_image_style2.setCurrentText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_299.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.back_to_models_btn_2.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_256.setText(QCoreApplication.translate("MainWindow", u"Choose the dataset that best fits your need. Please be patient, the process can take some time! View generated images tab for the results", None))
        self.output_size_error_2.setText(QCoreApplication.translate("MainWindow", u"Invalid Output Size Range! Try again", None))
        self.runtime_env_error_2.setText(QCoreApplication.translate("MainWindow", u"The runtime environment as \"TPU\" may be very slow and tedious. We reccoment to use \"GPU\" for the efficiency of the processes! ", None))
        self.label_289.setText(QCoreApplication.translate("MainWindow", u"Style GAN 2 Progress", None))
        self.rerun_style2gan_btn.setText(QCoreApplication.translate("MainWindow", u"REGENERATE IMAGES", None))
        self.cancel_progress_style2_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL PROGRESS", None))
        self.label_293.setText("")
        self.label_308.setText("")
        self.label_310.setText(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.label_312.setText(QCoreApplication.translate("MainWindow", u"Time Spent", None))
        self.label_313.setText(QCoreApplication.translate("MainWindow", u" Images Generated", None))
        self.label_314.setText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.label_315.setText(QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.view_style2_generated_imgs_btn.setText(QCoreApplication.translate("MainWindow", u"VIEW OUTPUT  ", None))
        self.label_316.setText(QCoreApplication.translate("MainWindow", u"Dataset Processing", None))
        self.label_317.setText(QCoreApplication.translate("MainWindow", u"The image generation process is on going. Please be patient for the output results as the STYLE GAN 2 requires some time to generate very high quality results using pretrained model!", None))
        self.cancel_stylegan2_confirm_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Do you want to terminate the image generation process?", None))
        self.cancel_stylegan2_confirm_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.account_verify_status_18.setText(QCoreApplication.translate("MainWindow", u"WARNING: All of the progress will be lost!", None))
        self.rerun_stylegan2_confirm_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Do you want to restart the image generation process?", None))
        self.rerun_tstylegan2_confirm_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.account_verify_status_19.setText(QCoreApplication.translate("MainWindow", u"WARNING: All of the  progress will be lost!", None))
        self.label_318.setText("")
        self.loading_label_dst_2.setText("")
        self.style_gan_plabel_2.setText("")
        self.label_265.setText("")
        self.back_to_style2_page_btn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"Output Images", None))
        self.output_folder_btn.setText(QCoreApplication.translate("MainWindow", u"OPEN OUTPUT FOLDER", None))
        self.output_image_6_btn.setText("")
        self.output_image_4.setText("")
        self.make_fav1_btn.setText(QCoreApplication.translate("MainWindow", u"Make Favourite", None))
        self.output_image_4_btn.setText("")
        self.remove_fav3_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Favourite", None))
        self.output_image_1_btn.setText("")
        self.remove_fav1_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Favourite", None))
        self.output_image_6.setText("")
        self.make_fav6_btn.setText(QCoreApplication.translate("MainWindow", u"Make Favourite", None))
        self.make_fav5_btn.setText(QCoreApplication.translate("MainWindow", u"Make Favourite", None))
        self.remove_fav5_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Favourite", None))
        self.output_image_5_btn.setText("")
        self.make_fav4_btn.setText(QCoreApplication.translate("MainWindow", u"Make Favourite", None))
        self.output_image_1.setText("")
        self.output_image_2.setText("")
        self.output_image_5.setText("")
        self.remove_fav4_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Favourite", None))
        self.make_fav2_btn.setText(QCoreApplication.translate("MainWindow", u"Make Favourite", None))
        self.output_image_3.setText("")
        self.output_image_2_btn.setText("")
        self.remove_fav2_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Favourite", None))
        self.remove_fav6_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Favourite", None))
        self.make_fav3_btn.setText(QCoreApplication.translate("MainWindow", u"Make Favourite", None))
        self.output_image_3_btn.setText("")
        ___qtablewidgetitem7 = self.tableWidget_generated_images.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"VIEW", None));
        ___qtablewidgetitem8 = self.tableWidget_generated_images.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem9 = self.tableWidget_generated_images.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"GENERATED AT", None));
        self.open_output_list_img_btn.setText(QCoreApplication.translate("MainWindow", u"Open Selected Image", None))
        self.customize_image_btn.setText(QCoreApplication.translate("MainWindow", u"Customize Selected Image", None))
        self.delete_image_btn.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Image", None))
        self.make_fav_list_image_btn.setText(QCoreApplication.translate("MainWindow", u"Make Favourite Selected Image", None))
        self.delete_img_confirm_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Do you want to delete the selected image?", None))
        self.delete_img_confirm_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.account_verify_status_21.setText(QCoreApplication.translate("MainWindow", u"WARNING: Image will be permanently deleted from the database!", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"LOGIN SUCCESSFUL", None))
        self.fav_added_notification_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.no_outputs_widget.setText(QCoreApplication.translate("MainWindow", u"No Output Items", None))
        self.outputs_list_view_btn.setText(QCoreApplication.translate("MainWindow", u"LIST VIEW", None))
        self.outputs_thumb_view_btn.setText(QCoreApplication.translate("MainWindow", u"THUMBNAIL VIEW", None))
        self.label_266.setText(QCoreApplication.translate("MainWindow", u"Selected Image", None))
        self.save_changes_image_btn.setText(QCoreApplication.translate("MainWindow", u"SAVE CHANGES", None))
        self.back_to_img_custom_btn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.store_image_btn.setText(QCoreApplication.translate("MainWindow", u"STORE NEW IMAGE", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"CHANGES SAVED SUCCESSFUL", None))
        self.changes_success_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"IMAGE STORED SUCCESSFUL", None))
        self.store_success_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_120.setText("")
        self.reset_changes_image_btn.setText(QCoreApplication.translate("MainWindow", u"RESET CHANGES", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"ALL CHANGES RESET SUCCESSFUL", None))
        self.changes_reset_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.rotate_image_btn.setText("")
        self.label_136.setText("")
        self.edge_detect_image_btn.setText("")
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"CROP", None))
        self.contrast_image_btn.setText("")
        self.draw_image_btn.setText("")
        self.label_144.setText("")
        self.selected_image.setText("")
        self.translate_image_btn.setText("")
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"IMAGE TRANSLATION", None))
        self.label_140.setText("")
        self.crop_image_btn.setText("")
        self.label_142.setText("")
        self.apply_effects_btn.setText("")
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"SET CONTRAST", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"APPLY FILTERS", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"DRAW", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"EDGE DETECTION", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"STYLING", None))
        self.label_146.setText("")
        self.label_134.setText("")
        self.label_138.setText("")
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"ROTATE", None))
        self.label_132.setText("")
        self.style_image_btn.setText("")
        self.open_cutomized_image_btn.setText("")
        self.half_brightness_btn.setText("")
        self.selected_image_filter.setText("")
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"Half Brightness", None))
        self.double_brightness_btn.setText("")
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"Double Brightness", None))
        self.zero_sharpness_btn.setText("")
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"Zero Sharpness", None))
        self.double_sharpness_btn.setText("")
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Double Sharpness", None))
        self.half_contrast_btn.setText("")
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"Half Contrast", None))
        self.double_contrast_btn.setText("")
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"Double Contrast", None))
        self.half_color_btn.setText("")
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"Half Color", None))
        self.double_color_btn.setText("")
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"Double Color", None))
        self.open_cutomized_image_btn_2.setText("")
        self.mean_filter_btn.setText("")
        self.bilateral_filter_btn.setText("")
        self.selected_image_filter_2.setText("")
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"Mean Filtering", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"Gaussian Filter", None))
        self.median_filter_btn.setText("")
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Median Filter", None))
        self.gaussian_filter_btn.setText("")
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"Bilateral Filter", None))
        self.open_cutomized_image_btn_3.setText("")
        self.selected_image_filter_3.setText("")
        self.detect_edges_2_btn.setText("")
        self.open_cutomized_image_btn_5.setText("")
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"Detect Edges with Sigma = 2", None))
        self.detect_edges_5_btn.setText("")
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"Detect Edges with Sigma = 5", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"Detect Rough Edges", None))
        self.detect_rough_edges_btn.setText("")
        self.open_cutomized_image_btn_6.setText("")
        self.selected_image_filter_4.setText("")
        self.label_270.setText(QCoreApplication.translate("MainWindow", u"360'", None))
        self.label_271.setText(QCoreApplication.translate("MainWindow", u"0'", None))
        self.selected_image_filter_5.setText("")
        self.apply_crop_btn.setText("")
        self.open_cutomized_image_btn_7.setText("")
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"Crop Image", None))
        self.label_116.setText("")
        self.label_117.setText("")
        self.label_274.setText(QCoreApplication.translate("MainWindow", u"Crop the image in right-downward direction!", None))
        self.use_pen_btn.setText("")
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"Use Pen", None))
        self.selected_image_filter_6.setText("")
        self.open_cutomized_image_btn_8.setText("")
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"Use Brush", None))
        self.use_brush_btn.setText("")
        self.selected_image_content.setText("")
        self.label_268.setText(QCoreApplication.translate("MainWindow", u"Mask Image", None))
        self.selected_style_image.setText("")
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"Apply Mask", None))
        self.apply_mask_btn.setText("")
        self.select_style_img_btn.setText("")
        self.open_cutomized_image_btn_4.setText("")
        self.label_269.setText(QCoreApplication.translate("MainWindow", u"Blender Image", None))
        self.blend_image_btn.setText("")
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"Blend Images", None))
        self.style_result_label.setText("")
        self.style_img_result.setText("")
        self.style_img_result_btn.setText("")
        self.style_img_result_cross_btn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_290.setText(QCoreApplication.translate("MainWindow", u"Content Image", None))
        self.label_291.setText(QCoreApplication.translate("MainWindow", u"Blender Image", None))
        self.bitwise_or_btn.setText(QCoreApplication.translate("MainWindow", u"APPLY BITWISE OR", None))
        self.bitwise_and_btn.setText(QCoreApplication.translate("MainWindow", u"APPLY BITWISE AND", None))
        self.bitwise_xor_btn.setText(QCoreApplication.translate("MainWindow", u"APPLY BITWISE XOR", None))
        self.bitwise_not_btn.setText(QCoreApplication.translate("MainWindow", u"NEGATIVE", None))
        self.blacknwhite_btn.setText(QCoreApplication.translate("MainWindow", u"BLACK & WHITE", None))
        self.s_img.setText("")
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"Apply Image Translation", None))
        self.apply_translation_btn.setText("")
        self.c_img.setText("")
        self.label_272.setText(QCoreApplication.translate("MainWindow", u"Style Image", None))
        self.label_273.setText(QCoreApplication.translate("MainWindow", u"Content Image", None))
        self.s_img_2.setText("")
        self.label_283.setText(QCoreApplication.translate("MainWindow", u"Translated Image", None))
        self.label_123.setText("")
        self.style_img_result_2.setText("")
        self.style_result_label_2.setText("")
        self.style_gan_plabel_4.setText("")
        self.phase1_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">0 % Done</span></p></body></html>", None))
        self.label_284.setText(QCoreApplication.translate("MainWindow", u"PHASE 1 PROGRESS", None))
        self.label_285.setText(QCoreApplication.translate("MainWindow", u"PHASE 2 PROGRESS", None))
        self.style_gan_plabel_5.setText("")
        self.phase2_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">0 % Done</span></p></body></html>", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; color:#ff0000;\">NOTE: </span><span style=\" font-size:14pt;\">First Select the &quot;</span><span style=\" font-size:14pt; font-weight:700; font-style:italic;\">Content Image</span><span style=\" font-size:14pt;\">&quot; then the &quot;</span><span style=\" font-size:14pt; font-weight:700; font-style:italic;\">Style Image</span><span style=\" font-size:14pt;\">&quot;!</span></p></body></html>", None))
        self.content_image.setText("")
        self.label_275.setText(QCoreApplication.translate("MainWindow", u"Style Image", None))
        self.label_128.setText("")
        self.translated_image.setText("")
        self.label_286.setText(QCoreApplication.translate("MainWindow", u"Translated Image", None))
        self.style_image.setText("")
        self.label_287.setText(QCoreApplication.translate("MainWindow", u"Content Image", None))
        self.translated_image_btn.setText("")
        self.translate_new_btn.setText("")
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"Translate New Image", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"IMAGES LIBRARY PAGE", None))
        self.label_73.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"AI IMAGES @ 2021 All Rights Reserved", None))
        self.label_75.setText("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"HELP PAGE", None))
        self.label_81.setText("")
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"AI IMAGES @ 2021 All Rights Reserved", None))
        self.label_83.setText("")
        self.label_71.setText("")
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.about_icon_btn.setText("")
        self.label_92.setText("")
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Send Feedback", None))
        self.send_feedback_icon_btn.setText("")
        self.label_94.setText("")
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Recent Activity", None))
        self.recent_activity_icon_btn.setText("")
        self.label_97.setText("")
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"My Favourites", None))
        self.myfav_icon_btn.setText("")
        self.verify_email_btn_2.setText(QCoreApplication.translate("MainWindow", u"Verify Email", None))
        self.account_verify_status_4.setText(QCoreApplication.translate("MainWindow", u"Your Account is not Verified!", None))
        self.go_to_login_btn_2.setText(QCoreApplication.translate("MainWindow", u"Go To Login", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"PLEASE LOGIN YOURSELF FIRST!", None))
        self.label_57.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"AI IMAGES @ 2021 All Rights Reserved", None))
        self.label_59.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem23 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem24 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem25 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem26 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem27 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem28 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem30 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem31 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem32 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem33 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled1)

        self.label.setText(QCoreApplication.translate("MainWindow", u"NEW PAGE TEST", None))
        self.btn_hide_gadgets.setText(QCoreApplication.translate("MainWindow", u"Hide Gadgets", None))
        self.btn_sysinfo.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.btn_usage.setText(QCoreApplication.translate("MainWindow", u"Usage %", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"AI IMAGES TOOLKIT", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"version: 1.0.0", None))
    # retranslateUi

