# //////////////////////////////////////////////////////////////////////////////////////////
#
#                                                   FINAL YEAR PROJECT

#                                 BY:
#                                                 ALLAH RAKHIO SP18-BCS-25
#                                                 AWAIS KAZMI SP18-BCS-154

#                                 Supervisors:
#                                                 Dr. Akber Abid Gardezi
#                                                 Mr. Qasim Malik [Co - Supervisor]

#                                 Evaluation Committee:
#                                                 Mr. Tehseen Riaz Abbasi
#                                                 Dr. Inayat Ur Rehman
#
# //////////////////////////////////////////////////////////////////////////////////////////////


# Import Required Libraries and Modules
# ///////////////////////////////////////////////////////////////
import sys
import _pickle as cPickle
import platform
import os
import time
import glob
import webbrowser

import cv2
import base64

import numpy
import pymongo
import bcrypt
import re
import sys
import platform
import smtplib
import easyimap as ei
import psutil
import pyqtgraph as pg
import numpy as np
import pandas as pd
import pickle
import threading
import undetected_chromedriver.v2 as uc
import threading
import zipfile
import subprocess
import skimage
import skimage.feature
import skimage.viewer
from PIL import Image
from resizeimage import resizeimage

# Import Required Packages
# ///////////////////////////////////////////////////////////////
from bson.binary import Binary
from PIL import ImageEnhance
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from matplotlib import pyplot as plt
from pathlib import Path
from pyqtgraph import PlotWidget
from collections import deque
from email.message import EmailMessage
from string import Template
from datetime import datetime
from modules.common import Sketcher
# Import GUI and Modules and Widgets
# ///////////////////////////////////////////////////////////////
import PySide6
from PySide6 import QtGui, QtCore
from modules import *
from widgets import *

# Set MongoDB Database
# ///////////////////////////////////////////////////////////////
client = pymongo.MongoClient()
db = client["AI_images"]
users = db["User_login"]
users_activity = db["User_recent_activity"]
users_favourites = db["User_favourites"]
datasets = db["Datasets"]
output_images = db["Output_images"]
admin_keys = db["Admin_keys"]

# Setting Chrome Driver PATH and SIZE
# ///////////////////////////////////////////////////////////////
CHROME_PATH = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
CHROMEDRIVER_PATH = 'C:/Program Files (x86)/chromedriver.exe'
WINDOW_SIZE = "1920,1080"

# Setting Chrome Driver Options
# ///////////////////////////////////////////////////////////////
chrome_options = Options()
prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": r"C:\Users\SYS\Downloads\AI Images\\",
                 "directory_upgrade": True}
chrome_options.add_experimental_option("prefs",prefs)
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH


# Set Global Widgets
# ///////////////////////////////////////////////////////////////
widgets = None
# GLOBALS
counter = 0
jumper = 10
custom_image = 0
# Set Email Services
# ///////////////////////////////////////////////////////////////
app_password = "wspeshfphgmsbbrq"
host_user = "awaiskfiverr@gmail.com"
smtp = smtplib.SMTP_SSL('smtp.gmail.com',465)
smtp.login(host_user, app_password)
server = ei.connect("imap.gmail.com", host_user, app_password)
#confirm_email = server.mail(server.listids()[0])
#uemail = confirm_email.from_addr
#confirm_email.title

# MAIN WINDOW CLASS
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set Global Widgets
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # Initialize CPU and RAM Statistics
        # ///////////////////////////////////////////////////////////////
        self.cpu_percent = 0
        self.ram_percent = 0
        self.traces = dict()
        self.timestamp = 0
        self.timeaxis = []
        self.cpuaxis = []
        self.ramaxis = []

        # Custom Title Bar for the Application | Use As "False" For Mac Or Linux Operating Systems
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # Application Name and Description
        # ///////////////////////////////////////////////////////////////
        title = "AI IMAGES TOOLKIT"
        description = "AI IMAGES TOOLKIT - A SOLUTION FOR THE DESIGNERS TO GET A DESIRED AI GENERATED CHARACTER."
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # Menu Toggle Option
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # UI Definitions Setting
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget Parameters
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Gadgets Graphs
        # ///////////////////////////////////////////////////////////////
        self.current_timer_graph = None
        self.graph_lim = 15
        self.deque_timestamp = deque([], maxlen=self.graph_lim + 20)
        self.deque_cpu = deque([], maxlen=self.graph_lim + 20)
        self.deque_ram = deque([], maxlen=self.graph_lim + 20)
        widgets.system_info_label_2.setText(
            f"{platform.system()} {platform.machine()}")
        widgets.processor_info_label_2.setText(
            f"Processor: {platform.processor()}")

        # CPU Graph Position Settings
        # ///////////////////////////////////////////////////////////////
        widgets.graphwidget1 = PlotWidget(title="CPU percent")
        x1_axis = widgets.graphwidget1.getAxis('bottom')
        x1_axis.setLabel(text='Time since start (s)')
        y1_axis = widgets.graphwidget1.getAxis('left')
        y1_axis.setLabel(text='Percent')

        # RAM Graph Position Settings
        # ///////////////////////////////////////////////////////////////
        widgets.graphwidget2 = PlotWidget(title="RAM percent")
        x2_axis = widgets.graphwidget2.getAxis('bottom')
        x2_axis.setLabel(text='Time since start (s)')
        y2_axis = widgets.graphwidget2.getAxis('left')
        y2_axis.setLabel(text='Percent')

        # Buttons for Showing Graphs
        # ///////////////////////////////////////////////////////////////
        widgets.show_cpu_graph_btn.clicked.connect(self.show_cpu_graph)
        widgets.show_cpu_graph_btn_3.clicked.connect(self.show_cpu_graph)
        widgets.show_ram_graph_btn.clicked.connect(self.show_ram_graph)
        widgets.show_ram_graph_btn_3.clicked.connect(self.show_ram_graph)
        widgets.gridLayout_3.addWidget(widgets.graphwidget1, 0, 0, 1, 3)
        widgets.gridLayout_3.addWidget(widgets.graphwidget2, 0, 0, 1, 3)

        # Setting QTimer() for Live Statistics Data
        # ///////////////////////////////////////////////////////////////
        self.current_timer_systemStat = QtCore.QTimer()
        self.search_timer = QtCore.QTimer()

        # Setting QTimer() for System Stats for Every 1 Second
        # ///////////////////////////////////////////////////////////////
        self.current_timer_systemStat.timeout.connect(
            self.getsystemStatpercent)
        self.current_timer_systemStat.start(1000)

        # Setting QTimer() for Dataset Quick Search for Every 6 Second
        # ///////////////////////////////////////////////////////////////
        self.search_timer.timeout.connect(self.getSearch)
        self.search_timer.start(6000)
        self.translation_process = False

        # Show CPU Function Call
        # ///////////////////////////////////////////////////////////////
        self.show_cpu_graph()

        # Setting Button Clicks Connection
        # ///////////////////////////////////////////////////////////////

        widgets.account_settings_btn.clicked.connect(self.buttonClick)
        widgets.datasets_btn.clicked.connect(self.buttonClick)
        widgets.model_training_btn.clicked.connect(self.buttonClick)
        widgets.generated_images_btn.clicked.connect(self.buttonClick)
        widgets.images_library_btn.clicked.connect(self.buttonClick)
        widgets.help_btn.clicked.connect(self.buttonClick)
        widgets.login_btn.clicked.connect(self.buttonClick)
        widgets.go_to_login_btn.clicked.connect(self.buttonClick)
        widgets.go_to_login_btn_2.clicked.connect(self.buttonClick)
        widgets.signup_btn.clicked.connect(self.buttonClick)
        widgets.go_to_signup_btn.clicked.connect(self.buttonClick)
        widgets.login_success_ok_btn.clicked.connect(self.buttonClick)
        widgets.login_fail_ok_btn.clicked.connect(self.buttonClick)
        widgets.signup_success_ok_btn.clicked.connect(self.buttonClick)
        widgets.forget_pass_name_btn.clicked.connect(self.buttonClick)
        widgets.forget_credentials_widget_ok_btn.clicked.connect(self.buttonClick)
        widgets.forget_credentials_widget_cancel_btn.clicked.connect(self.buttonClick)
        widgets.recovery_message_widget_ok_btn.clicked.connect(self.buttonClick)
        widgets.new_password_widget_ok_btn.clicked.connect(self.buttonClick)
        widgets.new_password_widget_cancel_btn.clicked.connect(self.buttonClick)
        widgets.new_credentials_ok_btn.clicked.connect(self.buttonClick)
        widgets.verify_email_btn.clicked.connect(self.buttonClick)
        widgets.verify_email_btn_2.clicked.connect(self.buttonClick)
        widgets.acc_verify_done_btn.clicked.connect(self.buttonClick)
        widgets.verify_message_widget_ok_btn.clicked.connect(self.buttonClick)
        widgets.upload_profile_pic_btn.clicked.connect(self.buttonClick)
        widgets.profile_pic_change_btn.clicked.connect(self.buttonClick)
        widgets.profile_pic_remove_btn.clicked.connect(self.buttonClick)
        widgets.deactivate_account_btn.clicked.connect(self.buttonClick)
        widgets.deactivate_account_confirm_ok_btn.clicked.connect(self.buttonClick)
        widgets.deactivate_account_confirm_cancel_btn.clicked.connect(self.buttonClick)
        widgets.logout_btn.clicked.connect(self.buttonClick)
        widgets.btn_logout.clicked.connect(self.buttonClick)
        widgets.signout_btn.clicked.connect(self.buttonClick)
        widgets.about_btn.clicked.connect(self.buttonClick)
        widgets.recent_activity_icon_btn.clicked.connect(self.buttonClick)
        widgets.myfav_icon_btn.clicked.connect(self.buttonClick)
        widgets.send_feedback_icon_btn.clicked.connect(self.buttonClick)
        widgets.about_icon_btn.clicked.connect(self.buttonClick)
        widgets.dash_board_btn.clicked.connect(self.buttonClick)
        widgets.clear_recent_history_btn.clicked.connect(self.buttonClick)
        widgets.clear_history_confirm_ok_btn.clicked.connect(self.buttonClick)
        widgets.clear_history_confirm_cancel_btn.clicked.connect(self.buttonClick)
        widgets.clear_myfavourites_history_btn.clicked.connect(self.buttonClick)
        widgets.clear_fav_history_confirm_ok_btn.clicked.connect(self.buttonClick)
        widgets.clear_fav_history_confirm_cancel_btn.clicked.connect(self.buttonClick)
        widgets.send_feedback_btn.clicked.connect(self.buttonClick)
        widgets.confirm_feedback_widget_ok_btn.clicked.connect(self.buttonClick)
        widgets.confirm_feedback_widget_cancel_btn.clicked.connect(self.buttonClick)
        widgets.feedback_sent_notification_ok_btn.clicked.connect(self.buttonClick)
        widgets.contact_us_btn.clicked.connect(self.buttonClick)
        widgets.btn_sysinfo.clicked.connect(self.buttonClick)
        widgets.btn_usage.clicked.connect(self.buttonClick)
        widgets.show_ram_graph_btn_3.clicked.connect(self.buttonClick)
        widgets.show_cpu_graph_btn_3.clicked.connect(self.buttonClick)
        widgets.btn_hide_gadgets.clicked.connect(self.buttonClick)
        widgets.show_circular_percent_btn.clicked.connect(self.buttonClick)
        widgets.output_image_1_btn.clicked.connect(self.buttonClick)
        widgets.output_image_2_btn.clicked.connect(self.buttonClick)
        widgets.output_image_3_btn.clicked.connect(self.buttonClick)
        widgets.output_image_4_btn.clicked.connect(self.buttonClick)
        widgets.output_image_5_btn.clicked.connect(self.buttonClick)
        widgets.output_image_6_btn.clicked.connect(self.buttonClick)
        widgets.anime_thumbnail_btn.clicked.connect(self.buttonClick)
        widgets.human_thumbnail_btn.clicked.connect(self.buttonClick)
        widgets.flower_thumbnail_btn.clicked.connect(self.buttonClick)
        widgets.new_datset_thumbnail_btn.clicked.connect(self.buttonClick)
        widgets.create_new_dataset_btn.clicked.connect(self.buttonClick)
        widgets.anime_thumbnail_btn_2.clicked.connect(self.buttonClick)
        widgets.human_thumbnail_btn_2.clicked.connect(self.buttonClick)
        widgets.flower_thumbnail_btn_2.clicked.connect(self.buttonClick)
        widgets.new_datset_thumbnail_btn_2.clicked.connect(self.buttonClick)
        widgets.back_to_dataset_btn.clicked.connect(self.buttonClick)
        widgets.back_to_dataset_btn_2.clicked.connect(self.buttonClick)
        widgets.back_to_dataset_btn_3.clicked.connect(self.buttonClick)
        widgets.back_to_dataset_btn_4.clicked.connect(self.buttonClick)
        widgets.back_to_dataset_btn_5.clicked.connect(self.buttonClick)
        widgets.back_to_dataset_btn_6.clicked.connect(self.buttonClick)
        widgets.new_dst_u_image_1_btn.clicked.connect(self.buttonClick)
        widgets.new_dst_u_image_2_btn.clicked.connect(self.buttonClick)
        widgets.new_dst_u_image_3_btn.clicked.connect(self.buttonClick)
        widgets.new_dst_u_image_4_btn.clicked.connect(self.buttonClick)
        widgets.new_dst_u_image_5_btn.clicked.connect(self.buttonClick)
        widgets.new_dst_upload_thumb_btn.clicked.connect(self.buttonClick)
        widgets.create_dst_done_btn.clicked.connect(self.buttonClick)
        widgets.dst_fail_ok_btn.clicked.connect(self.buttonClick)
        widgets.dst_success_ok_btn.clicked.connect(self.buttonClick)
        widgets.upload_images_btn.clicked.connect(self.buttonClick)
        widgets.delete_new_dataset_btn.clicked.connect(self.buttonClick)
        widgets.new_dataset_del_confirm_ok_btn.clicked.connect(self.buttonClick)
        widgets.new_dataset_del_confirm_cancel_btn.clicked.connect(self.buttonClick)
        widgets.dst_fail_ok_btn_2.clicked.connect(self.buttonClick)
        widgets.dst_success_ok_btn_2.clicked.connect(self.buttonClick)
        widgets.dst_fail_ok_btn_3.clicked.connect(self.buttonClick)
        widgets.dst_success_ok_btn_3.clicked.connect(self.buttonClick)
        widgets.new_dataset_del_confirm_ok_btn_2.clicked.connect(self.buttonClick)
        widgets.new_dataset_del_confirm_cancel_btn_2.clicked.connect(self.buttonClick)
        widgets.delete_new_dataset_btn_2.clicked.connect(self.buttonClick)
        widgets.upload_images_btn_2.clicked.connect(self.buttonClick)
        widgets.view_searched_ok_btn.clicked.connect(self.buttonClick)
        widgets.searched_dst_cancel_btn.clicked.connect(self.buttonClick)
        widgets.searched_dst_thumbnail_btn.clicked.connect(self.buttonClick)
        widgets.view_searched_dst_btn.clicked.connect(self.buttonClick)
        widgets.searched_dst_cancel_btn_2.clicked.connect(self.buttonClick)
        widgets.view_searched_dst_btn_2.clicked.connect(self.buttonClick)
        widgets.view_searched_ok_btn_2.clicked.connect(self.buttonClick)
        widgets.run_gan_btn.clicked.connect(self.buttonClick)
        widgets.change_dst_btn.clicked.connect(self.buttonClick)
        widgets.rerun_gan_btn.clicked.connect(self.buttonClick)
        widgets.cancel_training_btn.clicked.connect(self.buttonClick)
        widgets.view_generated_imgs_btn.clicked.connect(self.buttonClick)
        widgets.make_fav1_btn.clicked.connect(self.buttonClick)
        widgets.make_fav2_btn.clicked.connect(self.buttonClick)
        widgets.make_fav3_btn.clicked.connect(self.buttonClick)
        widgets.make_fav4_btn.clicked.connect(self.buttonClick)
        widgets.make_fav5_btn.clicked.connect(self.buttonClick)
        widgets.make_fav6_btn.clicked.connect(self.buttonClick)
        widgets.remove_fav1_btn.clicked.connect(self.buttonClick)
        widgets.remove_fav2_btn.clicked.connect(self.buttonClick)
        widgets.remove_fav3_btn.clicked.connect(self.buttonClick)
        widgets.remove_fav4_btn.clicked.connect(self.buttonClick)
        widgets.remove_fav5_btn.clicked.connect(self.buttonClick)
        widgets.remove_fav6_btn.clicked.connect(self.buttonClick)
        widgets.cancel_training_confirm_ok_btn.clicked.connect(self.buttonClick)
        widgets.cancel_training_confirm_cancel_btn.clicked.connect(self.buttonClick)
        widgets.rerun_training_confirm_ok_btn.clicked.connect(self.buttonClick)
        widgets.rerun_training_confirm_cancel_btn.clicked.connect(self.buttonClick)
        widgets.open_favourite_btn.clicked.connect(self.buttonClick)
        widgets.open_output_list_img_btn.clicked.connect(self.buttonClick)
        widgets.update_algo_btn.clicked.connect(self.buttonClick)
        widgets.update_algo_ok_btn.clicked.connect(self.buttonClick)
        widgets.update_algo_cancel_btn.clicked.connect(self.buttonClick)
        widgets.outputs_thumb_view_btn.clicked.connect(self.buttonClick)
        widgets.outputs_list_view_btn.clicked.connect(self.buttonClick)
        widgets.output_folder_btn.clicked.connect(self.buttonClick)
#stylegan widgets
        widgets.style_gan_tab_btn.clicked.connect(self.buttonClick)
        widgets.login_google_btn.clicked.connect(self.buttonClick)
        widgets.login_success_ok_btn_2.clicked.connect(self.buttonClick)
        widgets.login_fail_ok_btn_2.clicked.connect(self.buttonClick)

        widgets.forget_pass_name_google_btn.clicked.connect(self.buttonClick)
        widgets.signup_google_btn.clicked.connect(self.buttonClick)
        widgets.google_verify_code_widget_ok_btn.clicked.connect(self.buttonClick)
        widgets.google_verify_code_widget_cancel_btn.clicked.connect(self.buttonClick)
        widgets.google_verify_code_widget_resend_btn.clicked.connect(self.buttonClick)

        widgets.anime_thumbnail_btn_3.clicked.connect(self.buttonClick)
        widgets.human_thumbnail_btn_3.clicked.connect(self.buttonClick)
        widgets.flower_thumbnail_btn_3.clicked.connect(self.buttonClick)
        widgets.new_datset_thumbnail_btn_3.clicked.connect(self.buttonClick)
        widgets.style_gan1_btn.clicked.connect(self.buttonClick)
        widgets.style_gan2_btn.clicked.connect(self.buttonClick)
        widgets.logout_google_btn.clicked.connect(self.buttonClick)
        widgets.train_stylegan_btn.clicked.connect(self.buttonClick)
        widgets.update_stylegan_algo_btn.clicked.connect(self.buttonClick)
        widgets.update_algo_ok_btn_2.clicked.connect(self.buttonClick)
        widgets.update_algo_cancel_btn_2.clicked.connect(self.buttonClick)
        widgets.back_to_models_btn_1.clicked.connect(self.buttonClick)
        widgets.back_to_models_btn_2.clicked.connect(self.buttonClick)
        widgets.mount_gdrive_style1_btn.clicked.connect(self.buttonClick)
        widgets.generate_images_style1_btn.clicked.connect(self.buttonClick)
        widgets.rerun_style1gan_btn.clicked.connect(self.buttonClick)
        widgets.cancel_progress_style1_btn.clicked.connect(self.buttonClick)
        widgets.view_style1_generated_imgs_btn.clicked.connect(self.buttonClick)

        widgets.rerun_stylegan1_confirm_ok_btn.clicked.connect(self.buttonClick)
        widgets.rerun_tstylegan1_confirm_cancel_btn.clicked.connect(self.buttonClick)
        widgets.cancel_stylegan1_confirm_ok_btn.clicked.connect(self.buttonClick)
        widgets.cancel_stylegan1_confirm_cancel_btn.clicked.connect(self.buttonClick)

        widgets.mount_gdrive_style2_btn.clicked.connect(self.buttonClick)
        widgets.generate_images_style2_btn.clicked.connect(self.buttonClick)
        widgets.rerun_style2gan_btn.clicked.connect(self.buttonClick)
        widgets.cancel_progress_style2_btn.clicked.connect(self.buttonClick)
        widgets.view_style2_generated_imgs_btn.clicked.connect(self.buttonClick)
        widgets.back_to_style1_page_btn.clicked.connect(self.buttonClick)
        widgets.back_to_style2_page_btn.clicked.connect(self.buttonClick)
        widgets.rerun_stylegan2_confirm_ok_btn.clicked.connect(self.buttonClick)
        widgets.rerun_tstylegan2_confirm_cancel_btn.clicked.connect(self.buttonClick)
        widgets.cancel_stylegan2_confirm_ok_btn.clicked.connect(self.buttonClick)
        widgets.cancel_stylegan2_confirm_cancel_btn.clicked.connect(self.buttonClick)
    # image customization widgets
        widgets.customize_image_btn.clicked.connect(self.buttonClick)
        widgets.save_changes_image_btn.clicked.connect(self.buttonClick)
        widgets.apply_effects_btn.clicked.connect(self.buttonClick)
        widgets.style_image_btn.clicked.connect(self.buttonClick)
        widgets.contrast_image_btn.clicked.connect(self.buttonClick)
        widgets.draw_image_btn.clicked.connect(self.buttonClick)
        widgets.crop_image_btn.clicked.connect(self.buttonClick)
        widgets.translate_image_btn.clicked.connect(self.buttonClick)
        widgets.edge_detect_image_btn.clicked.connect(self.buttonClick)
        widgets.rotate_image_btn.clicked.connect(self.buttonClick)
        widgets.half_brightness_btn.clicked.connect(self.buttonClick)
        widgets.double_brightness_btn.clicked.connect(self.buttonClick)
        widgets.zero_sharpness_btn.clicked.connect(self.buttonClick)
        widgets.double_sharpness_btn.clicked.connect(self.buttonClick)
        widgets.half_contrast_btn.clicked.connect(self.buttonClick)
        widgets.double_contrast_btn.clicked.connect(self.buttonClick)
        widgets.half_color_btn.clicked.connect(self.buttonClick)
        widgets.double_color_btn.clicked.connect(self.buttonClick)
        widgets.mean_filter_btn.clicked.connect(self.buttonClick)
        widgets.median_filter_btn.clicked.connect(self.buttonClick)
        widgets.gaussian_filter_btn.clicked.connect(self.buttonClick)
        widgets.bilateral_filter_btn.clicked.connect(self.buttonClick)


        widgets.select_style_img_btn.clicked.connect(self.buttonClick)
        widgets.back_to_img_custom_btn.clicked.connect(self.buttonClick)
        widgets.open_cutomized_image_btn.clicked.connect(self.buttonClick)
        widgets.open_cutomized_image_btn_2.clicked.connect(self.buttonClick)
        widgets.open_cutomized_image_btn_3.clicked.connect(self.buttonClick)
        widgets.open_cutomized_image_btn_4.clicked.connect(self.buttonClick)

        widgets.open_cutomized_image_btn_5.clicked.connect(self.buttonClick)
        widgets.open_cutomized_image_btn_6.clicked.connect(self.buttonClick)
        widgets.open_cutomized_image_btn_7.clicked.connect(self.buttonClick)
        widgets.open_cutomized_image_btn_8.clicked.connect(self.buttonClick)

        widgets.apply_mask_btn.clicked.connect(self.buttonClick)
        widgets.blend_image_btn.clicked.connect(self.buttonClick)
        widgets.style_img_result_btn.clicked.connect(self.buttonClick)
        widgets.style_img_result_cross_btn.clicked.connect(self.buttonClick)
        widgets.translated_image_btn.clicked.connect(self.buttonClick)
        widgets.translate_new_btn.clicked.connect(self.buttonClick)



        widgets.use_pen_btn.clicked.connect(self.buttonClick)
        widgets.use_brush_btn.clicked.connect(self.buttonClick)
        widgets.bitwise_or_btn.clicked.connect(self.buttonClick)
        widgets.bitwise_and_btn.clicked.connect(self.buttonClick)
        widgets.bitwise_xor_btn.clicked.connect(self.buttonClick)
        widgets.bitwise_not_btn.clicked.connect(self.buttonClick)
        widgets.blacknwhite_btn.clicked.connect(self.buttonClick)
        widgets.detect_edges_2_btn.clicked.connect(self.buttonClick)
        widgets.detect_edges_5_btn.clicked.connect(self.buttonClick)
        widgets.detect_rough_edges_btn.clicked.connect(self.buttonClick)
        widgets.apply_crop_btn.clicked.connect(self.buttonClick)
        widgets.apply_translation_btn.clicked.connect(self.buttonClick)
        widgets.store_image_btn.clicked.connect(self.buttonClick)
        widgets.changes_success_ok_btn.clicked.connect(self.buttonClick)
        widgets.store_success_ok_btn.clicked.connect(self.buttonClick)
        widgets.reset_changes_image_btn.clicked.connect(self.buttonClick)
        widgets.changes_reset_ok_btn.clicked.connect(self.buttonClick)

        # Hiding the Gadgets Widgets in the Start Before Login
        widgets.edit_dst_btn.hide()
        widgets.stackedWidget_3.hide()

        # Function for Extra Left Box
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # Function for Extra Right Box
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # Call Show Function to Show Application
        # ///////////////////////////////////////////////////////////////
        self.show()

        # Custom Theme Settings
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            self.setThemeHack(self)

        # SET First PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        global loggedIn
        loggedIn = False
        widgets.stackedWidget_5.setCurrentWidget(widgets.login_page)

        print(type(self.cpu_percent))
        print(type(self.timestamp))
   #  Function for Live Dataset Search
   # ///////////////////////////////////////////////////////////////
    def getSearch(self):
        Datasets.dataset_search_activate(self,widgets)

    # Function for Theme Settings
    # ///////////////////////////////////////////////////////////////
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """
        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
        self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.tableWidget.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.scrollArea.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")

    # Function for the Conversion of QImage into an opencv MAT format
    # ///////////////////////////////////////////////////////////////
    def QImageToCvMat(self, q_img):
        q_img.save('temp.png', 'png')
        mat = cv2.imread('temp.png')
        os.remove("temp.png")
        return mat

    # Function for the Conversion of Picture Data to Bytes for the Database Storage Purpose
    # ///////////////////////////////////////////////////////////////
    def convert_pixmap_to_bytes(self, pixmap):
        ba = QtCore.QByteArray()
        buff = QtCore.QBuffer(ba)
        buff.open(QtCore.QIODevice.WriteOnly)
        ok = pixmap.save(buff, "PNG")
        assert ok
        pixmap_bytes = ba.data()
        print(type(pixmap_bytes))
        #  return converted data in bytes form
        return pixmap_bytes

    # Function for the Conversion of Bytes Data of Pictures to Pixmaps for the UI View Purpose
    # ///////////////////////////////////////////////////////////////
    def convert_bytes_to_pixmap(self, pixmap_bytes):
        # If no data is given, show default App Logo
        if pixmap_bytes == "":
            return "./images/images/LogoW.png"

        # Using QByteArray
        ba = QtCore.QByteArray(pixmap_bytes)
        pixmap = QtGui.QPixmap()
        ok = pixmap.loadFromData(ba, "PNG")
        assert ok
        print(type(pixmap))
        #  return converted data in pixmap form
        return pixmap

    # Function for getting a JPG or PNG file from the disk and Converting to pixmap data
    # ///////////////////////////////////////////////////////////////
    def getImage(self):
        # getting png or jpg files from the disk
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Image files (*.jpg *.png)")
        imagePath = fname[0]
        # converting file data to pixmap
        pixmap = QPixmap(imagePath)
        # returning image as a pixmap
        return pixmap

    # Function to Open the Output Image in the CV2 viewer
    # ///////////////////////////////////////////////////////////////
    def open_image(self, image):
        # getting image size
        size = image.size()
        # getting image width
        h = size.width()
        # getting image height
        w = size.height()
        # Get the QImage Item and convert it to a byte string
        qimg = image.toImage()
        byte_str = qimg.bits().tobytes()
        # Using the np.frombuffer function to convert the byte string into an np array
        img = np.frombuffer(byte_str, dtype=np.uint8).reshape((w, h, 4))
        # Opening image in the cv2 image viewer
        cv2.imshow('image', img)
        return

    #  Function for CPU/RAM Percentage Show
    # ///////////////////////////////////////////////////////////////
    def getsystemStatpercent(self):
        # gives a single float value
        self.cpu_percent = psutil.cpu_percent()
        self.ram_percent = psutil.virtual_memory().percent
        self.setValue(self.cpu_percent, self.ui.labelPercentageCPU_2,
                      self.ui.circularProgressCPU_2, "rgba(85, 170, 255, 255)")
        self.setValue(self.ram_percent, self.ui.labelPercentageRAM,
                      self.ui.circularProgressRAM, "rgba(255, 0, 127, 255)")

    #  Function for Starting CPU Graph having 1 Second Delay
    # ///////////////////////////////////////////////////////////////
    def start_cpu_graph(self):
        # self.timeaxis = []
        # self.cpuaxis = []
        if self.current_timer_graph:
            self.current_timer_graph.stop()
            self.current_timer_graph.deleteLater()
            self.current_timer_graph = None
        self.current_timer_graph = QtCore.QTimer()
        self.current_timer_graph.timeout.connect(self.update_cpu)
        self.current_timer_graph.start(1000)

    #  Function to Update CPU Usage Percentage Change
    # ///////////////////////////////////////////////////////////////
    def update_cpu(self):
        self.timestamp += 1
        self.deque_timestamp.append(self.timestamp)
        self.deque_cpu.append(self.cpu_percent)
        self.deque_ram.append(self.ram_percent)
        timeaxis_list = list(self.deque_timestamp)
        cpu_list = list(self.deque_cpu)
        if self.timestamp > self.graph_lim:
            widgets.graphwidget1.setRange(xRange=[self.timestamp - self.graph_lim + 1, self.timestamp], yRange=[
                min(cpu_list[-self.graph_lim:]), max(cpu_list[-self.graph_lim:])])
        self.set_plotdata(name="cpu", data_x=timeaxis_list,
                          data_y=cpu_list)

    #  Function for Starting RAM Graph having 1 Second Delay
    # ///////////////////////////////////////////////////////////////
    def start_ram_graph(self):
        if self.current_timer_graph:
            self.current_timer_graph.stop()
            self.current_timer_graph.deleteLater()
            self.current_timer_graph = None
        self.current_timer_graph = QtCore.QTimer()
        self.current_timer_graph.timeout.connect(self.update_ram)
        self.current_timer_graph.start(1000)

    #  Function to Update RAM Usage Percentage Change
    # ///////////////////////////////////////////////////////////////
    def update_ram(self):
        self.timestamp += 1
        self.deque_timestamp.append(self.timestamp)
        self.deque_cpu.append(self.cpu_percent)
        self.deque_ram.append(self.ram_percent)
        timeaxis_list = list(self.deque_timestamp)
        ram_list = list(self.deque_ram)
        if self.timestamp > self.graph_lim:
            widgets.graphwidget2.setRange(xRange=[self.timestamp - self.graph_lim + 1, self.timestamp], yRange=[
                min(ram_list[-self.graph_lim:]), max(ram_list[-self.graph_lim:])])
        self.set_plotdata(name="ram", data_x=timeaxis_list,
                          data_y=ram_list)

    #  Function to Show CPU Usage Graph
    # ///////////////////////////////////////////////////////////////
    def show_cpu_graph(self):
        widgets.graphwidget2.hide()
        widgets.graphwidget1.show()
        self.start_cpu_graph()
        widgets.show_cpu_graph_btn.setEnabled(False)
        widgets.show_cpu_graph_btn_3.setEnabled(False)
        widgets.show_ram_graph_btn.setEnabled(True)
        widgets.show_ram_graph_btn_3.setEnabled(True)

        #  Setting Styles for active/inactive Graph Button on Graph Page
        # ///////////////////////////////////////////////////////////////
        widgets.show_cpu_graph_btn_3.setStyleSheet(
            "QPushButton" "{" "background-color : rgba(0, 0, 0,0);" "}"
        )
        widgets.show_ram_graph_btn.setStyleSheet(
            "QPushButton"
            "{"
            "background-color : rgb(255, 44, 174);"
            "}"
            "QPushButton"
            "{"
            "color : white;"
            "}"
        )
        #  Setting Styles for active/inactive Graph Buttons on Gadgets Widget
        # ///////////////////////////////////////////////////////////////
        widgets.show_cpu_graph_btn.setStyleSheet(
            "QPushButton" "{" "background-color : rgba(0, 0, 0,0);" "}"
        )
        widgets.show_ram_graph_btn_3.setStyleSheet(
            "QPushButton"
            "{"
            "background-color : rgb(255, 44, 174);"
            "}"
            "QPushButton"
            "{"
            "color : white;"
            "}"
        )

    #  Function to Show RAM Usage Graph
    # ///////////////////////////////////////////////////////////////
    def show_ram_graph(self):
        widgets.graphwidget1.hide()
        widgets.graphwidget2.show()
        # self.graphwidget2.autoRange()
        self.start_ram_graph()
        widgets.show_ram_graph_btn.setEnabled(False)
        widgets.show_ram_graph_btn_3.setEnabled(False)

        widgets.show_cpu_graph_btn.setEnabled(True)
        widgets.show_cpu_graph_btn_3.setEnabled(True)

        widgets.show_ram_graph_btn.setStyleSheet(
            "QPushButton" "{" "background-color : rgba(0, 0, 0,0);" "}"
        )
        widgets.show_ram_graph_btn_3.setStyleSheet(
            "QPushButton" "{" "background-color : rgba(0, 0, 0,0);" "}"
        )
        widgets.show_cpu_graph_btn.setStyleSheet(
            "QPushButton"
            "{"
            "background-color : rgba(85, 170, 255, 255);"
            "}"
            "QPushButton"
            "{"
            "color : white;"
            "}"
        )
        widgets.show_cpu_graph_btn_3.setStyleSheet(
            "QPushButton"
            "{"
            "background-color : rgba(85, 170, 255, 255);"
            "}"
            "QPushButton"
            "{"
            "color : white;"
            "}"
        )

    #  Function to Plot RAM/CPU Usage Data on Graph Across X-Y axis
    # ///////////////////////////////////////////////////////////////
    def set_plotdata(self, name, data_x, data_y):
        # print('set_data')
        if name in self.traces:
            self.traces[name].setData(data_x, data_y)
        else:
            if name == "cpu":
                self.traces[name] = widgets.graphwidget1.getPlotItem().plot(
                    pen=pg.mkPen((85, 170, 255), width=3))
            elif name == "ram":
                self.traces[name] = widgets.graphwidget2.getPlotItem().plot(
                    pen=pg.mkPen((255, 0, 127), width=3))

    #  Function to SET VALUES TO DEF progressBarValue
    # ///////////////////////////////////////////////////////////////
    def setValue(self, value, labelPercentage, progressBarName, color):
        sliderValue = value
        # HTML TEXT PERCENTAGE
        htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""
        labelPercentage.setText(htmlText.replace(
            "{VALUE}", f"{sliderValue:.1f}"))

        # CALL DEF progressBarValue
        self.progressBarValue(sliderValue, progressBarName, color)

    #  Function for DEF PROGRESS BAR VALUE
    # ///////////////////////////////////////////////////////////////
    def progressBarValue(self, value, widget, color):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
         QFrame{
            border-radius: 110px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
         }
         """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace(
            "{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        widget.setStyleSheet(newStylesheet)


    # BUTTONS CLICK FUNCTIONS CALLS
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW LOGIN PAGE
        if (btnName == "go_to_login_btn" or btnName == "go_to_login_btn_2"):
            # setting the stacked widgets to display login page
            widgets.stackedWidget_5.setCurrentWidget(widgets.login_page)
            # resetting the styles of other application widgets
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SUBMIT LOGIN_FORM
        if btnName == "login_btn":
            # getting the entered user name form the login form
            username = widgets.user_name.text()
            # getting the entered user password form the login form
            password = widgets.user_password.text()
            # calling the login function to validate the login request
            validate_login = User_Profile.login(self,username,password)
            # if the login success message is returned
            if validate_login == "Logged successfully":
                # prompt the successful login notification
                widgets.login_success_notification.raise_()
            # if the login fail message is returned
            else:
                # prompt the Failed login notification
                widgets.login_fail_message.setText(validate_login)
                widgets.login_fail_notification.raise_()

        # LOGIN_FORM forget username password SUBMIT
        if btnName == "forget_pass_name_btn":
            # prompt the Forget Credentials Widget
            widgets.forget_credentials_widget.raise_()

        # forget username password ok button
        if btnName == "forget_credentials_widget_ok_btn":
            # getting the entered user email from the form
            user_email = widgets.recovery_email.text()
            # calling the function to find the user by email in the database
            user = User_Profile.find_user_by_email(self, user_email)
            # if the user not exists in the database
            if user == "The user doesn't exists!":
                # prompting the error => email not registered
                widgets.recovery_email_error.setText("Email is not registered!")
            # if the user exists in the database
            else:
                # setting the IMAP email service to receive the credential recovery email
                ser = ei.connect("imap.gmail.com", host_user, app_password)
                # getting the latest email in the inbox from the system
                c_mail = ser.mail(ser.listids()[0])
                # getting the email sender address
                c_mail.from_addr
                # getting the email title
                c_mail.title
                # removing the forget credentials widget from the app display
                widgets.forget_credentials_widget.lower()
                # if the mail title is 'NewPassword'
                if c_mail.title == "NewPassword":
                    # prompt the new password widget on the app display
                    widgets.new_password_widget.raise_()
                # if the 'NewPassword' title not found
                else:
                    # updating the user 'Applied for Forgotten Password or User Name' activity in the database
                    User_Profile.update_recent_activity(self, user["name"], 'Applied for Forgotten Password or User Name', 'High',widgets)
                    # prompt the recovery message notification on the app display
                    widgets.recovery_message_widget.raise_()

        # forget username password cancel button
        if btnName == "forget_credentials_widget_cancel_btn":
            # removing the forget credentials widget from the app display
            widgets.forget_credentials_widget.lower()

        # forget uname recovery message ok button
        if btnName == "recovery_message_widget_ok_btn":
            # getting the user email from the from the recovery email widget
            user_email = widgets.recovery_email.text()
            # calling the function to send the user details to the user by email
            User_Profile.send_user_details_to_email(self, user_email)
            # remove the recovery message notification from the app display
            widgets.recovery_message_widget.lower()

        # new password message ok button
        if btnName == "new_password_widget_ok_btn":
            # getting the entered user new password
            new_password = widgets.new_password.text()
            # getting the entered user confirm new password
            confirm_new_password = widgets.confirm_new_password.text()
            # setting the IMAP email service to receive the credential recovery email
            serv = ei.connect("imap.gmail.com", host_user, app_password)
            # getting the latest email in the inbox from the system
            confirm_mail = serv.mail(serv.listids()[0])
            # getting the email sender address
            confirm_mail.from_addr
            # getting the email title
            confirm_mail.title
            # calling the function to update the new user password in the database
            validate_new_password = User_Profile.update_new_password(self, new_password, confirm_new_password, confirm_mail.from_addr)
            # if the wrong new password pattern followed message is returned
            if validate_new_password == "Password Search Unsuccessful":
                # prompt the password error on the app display
                widgets.new_password_error.setText("Must have a proper format i.e. 'password!123' and contain atleast one special character LIMIT : 8-15")

            # if the confirmed new password message is returned
            elif validate_new_password == "Pass Confirmed Unsuccessful":
                # prompt the password mismatch error on the app display
                widgets.new_password_error.setText("")
                widgets.new_password_confirm_error.setText("Password Mismatch")

            # if the password is correctly entered entered
            else:
                # setting the labels with the new user credentials
                widgets.new_uname.setText(validate_new_password)
                widgets.new_upass.setText(new_password)

                # prompt the new credentials widget on the app display
                widgets.new_credentials_success.raise_()
                # removing the new password widget from the app display
                widgets.new_password_widget.lower()
                # updating the user 'New User Credentials Set' activity in the database
                User_Profile.update_recent_activity(self, widgets.new_uname.text(), 'New User Credentials Set','High',widgets)

        # new password message cancel button
        if btnName == "new_password_widget_cancel_btn":
            # removing the new password widget from the app display
            widgets.new_password_widget.lower()

        # new credentials message ok button
        if btnName == "new_credentials_ok_btn":
            # prompt the new credentials success message on the app display
            widgets.new_credentials_success.lower()

        # login_success_notification
        if btnName == "login_success_ok_btn":
            # setting the global 'LoggedIn' variable to 'True'
            global loggedIn
            loggedIn = True
            # removing the login success message  from the app display
            widgets.login_success_notification.lower()
            # getting the user name
            username = widgets.user_name.text()

            # finding the user by the user email
            user = User_Profile.find_user_by_name(self,username);
            # calling the function to load user favourite items stored in the database to display
            User_Profile.load_myfavourites(self, widgets.user_name.text(), widgets)
            # calling the function to load user activity stored in the database to display
            User_Profile.load_recent_activity(self, widgets.user_name.text(), widgets)
            # updating the user 'Logged in Successfully' activity in the database
            User_Profile.update_recent_activity(self, user["name"],'Logged in Successfully', 'High',widgets)
            # getting the user profile_pic data stored in the database
            image = user["profile_pic"]
            # converting the profile image data from bytes to pixmap for display purpose
            pixmap = self.convert_bytes_to_pixmap(image)
            # displaying the profile image on the profile pic widget
            widgets.profile_view_pic.setPixmap(pixmap)
            # setting the name label with the specified user name
            widgets.profile_view_user_name.setText(user["name"])
            # setting the email label with the specified user email
            widgets.profile_view_email.setText(user["email"])
            # show the quick navigation stacked widget on the screen
            widgets.stackedWidget_3.show()
            # switch main stacked widget to content page on the screen
            widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
            # checking if the user account is not verified
            if user["verified_account"] == False:
                # switch quick navigation stacked widget to verify_email_page page on the screen
                widgets.stackedWidget_top_icons.setCurrentWidget(widgets.verify_email_page)
            # checking if the user account is verified
            elif user["verified_account"] == True:
                # switch quick navigation stacked widget back to nav_icons_page page on the screen
                widgets.stackedWidget_top_icons.setCurrentWidget(widgets.nav_icons_page)
            # resetting the app styles
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # login_fail_notification
        if btnName == "login_fail_ok_btn":
            # removing the login fail message  from the app display
            widgets.login_fail_notification.lower()

        # SHOW SIGNUP PAGE
        if btnName == "go_to_signup_btn":
            # switch main stacked widget to 'signup_page' page on the screen
            widgets.stackedWidget_5.setCurrentWidget(widgets.signup_page)
            # resetting the app styles
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # signup_profile-pic upload btn
        if btnName == "upload_profile_pic_btn":
            # calling a function to upload the profile picture and store it on the database
            widgets.profile_image.setPixmap(QPixmap(self.getImage()))
            # resizing the profile image for better display
            widgets.profile_image.resize(70, 70)

        # SIGNUP FORM
        if btnName == "signup_btn":
            # getting the entered user name form the signup form
            username = widgets.signup_user_name.text()
            # getting the entered user email form the signup form
            email = widgets.signup_user_email.text()
            # getting the entered user password form the signup form
            password = widgets.signup_user_password.text()
            # getting the entered user confirm password form the signup form
            confirm_password = widgets.signup_confirm_password.text()
            # getting the uploaded user profile picture form the signup form
            profile_image = widgets.profile_image.pixmap()
            # calling a function to validate the signup form
            validate_signup = User_Profile.register(self, username, email, password, confirm_password,profile_image)
            # if the registration success message is returned
            if validate_signup == "Registered successfully":
                # prompt the user credentials to remember on the app display
                widgets.notify_signup_uname.setText(username)
                widgets.notify_signup_upass.setText(password)
                # prompt the signup success message on the app display
                widgets.signup_success_notification.raise_()
                # removing the username_already_exists_error message  from the app display
                widgets.username_already_exists_error.lower()
                # removing the username_error message  from the app display
                widgets.username_error.lower()
                # removing the email_error message  from the app display
                widgets.email_error.lower()
                # removing the password_error message  from the app display
                widgets.password_error.lower()
                # removing the password_confirm_error message  from the app display
                widgets.password_confirm_error.lower()
                # updating the user 'Registered Successfully' activity in the database
                User_Profile.update_recent_activity(self, username, 'Registered Successfully', 'High',widgets)
                # printing the registration success message on the console
                print('Registered successfully')

            # if the registration wrong Username message is returned
            elif validate_signup == "Username Search Unsuccessful":
                # prompt the username_error message on the app display
                widgets.username_error.raise_()
                # removing the username_already_exists_error message  from the app display
                widgets.username_already_exists_error.lower()
                # removing the email_error message  from the app display
                widgets.email_error.lower()
                # removing the password_error message  from the app display
                widgets.password_error.lower()
                # removing the password_confirm_error message  from the app display
                widgets.password_confirm_error.lower()
                # printing the Username Search Unsuccessful message on the console
                print('Username Search Unsuccessful')

            # if the user already exists message is returned
            elif validate_signup == "The user already exists!":
                # prompt the username_already_exists_error message on the app display
                widgets.username_already_exists_error.raise_()
                # remove the username_error message from the app display
                widgets.username_error.lower()
                # removing the email_error message  from the app display
                widgets.email_error.lower()
                # removing the password_error message  from the app display
                widgets.password_error.lower()
                # removing the password_confirm_error message  from the app display
                widgets.password_confirm_error.lower()
                # printing the The user already exists! message on the console
                print('The user already exists!')

            # if the registration wrong Email message is returned
            elif validate_signup == "Email Search Unsuccessful":
                # prompt the email_error message on the app display
                widgets.email_error.raise_()
                # remove the username_already_exists_error message  from the app display
                widgets.username_already_exists_error.lower()
                # remove the username_error message from the app display
                widgets.username_error.lower()
                # removing the password_error message  from the app display
                widgets.password_error.lower()
                # removing the password_confirm_error message  from the app display
                widgets.password_confirm_error.lower()
                # printing the Email Search Unsuccessful message on the console
                print('Email Search Unsuccessful')

            # if the registration wrong Password message is returned
            elif validate_signup == "Password Search Unsuccessful":
                # prompt the password_error message on the app display
                widgets.password_error.raise_()
                # remove the username_already_exists_error message from the app display
                widgets.username_already_exists_error.lower()
                # remove the username_error message from the app display
                widgets.username_error.lower()
                # remove the email_error message from the app display
                widgets.email_error.lower()
                # removing the password_confirm_error message  from the app display
                widgets.password_confirm_error.lower()
                # printing the Password Search Unsuccessful message on the console
                print('Password Search Unsuccessful')

            # if the registration wrong Confirmed Password message is returned
            elif validate_signup == "Pass Confirmed Unsuccessful":
                # prompt the password_confirm_error message on the app display
                widgets.password_confirm_error.raise_()
                # remove the username_already_exists_error message from the app display
                widgets.username_already_exists_error.lower()
                # remove the username_error message from the app display
                widgets.username_error.lower()
                # remove the email_error message from the app display
                widgets.email_error.lower()
                # removing the password_error message  from the app display
                widgets.password_error.lower()
                # printing the Pass Confirmed Unsuccessful message on the console
                print('Pass Confirmed Unsuccessful')

        # signup_success_notification
        if btnName == "signup_success_ok_btn":
            # prompt the signup_success_notification message on the app display
            widgets.signup_success_notification.lower()
            # switch main stacked widget to 'login_page' page on the screen
            widgets.stackedWidget_5.setCurrentWidget(widgets.login_page)

        # dash_board page
        if btnName == "dash_board_btn" \
                or btnName == "recent_activity_icon_btn" or btnName == "myfav_icon_btn":
            # checking if the user is not loggedIn
            if loggedIn == False:
                # switch main stacked widget to 'login_first_page' page on the screen
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)

            # checking if the user is loggedIn
            else:
                # switch main stacked widget to 'content_page' page on the screen
                widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
                # switch content_page stacked widget to 'dashboard_page' page on the screen
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.dashboard_page)
                # getting the user name from the name label
                username = widgets.user_name.text()
                # calling the function to find the user by user name in the database
                user = User_Profile.find_user_by_name(self, username)

                # checking if the user account is not verified
                if user["verified_account"] == False:
                    # switch quick navigation stacked widget to verify_email_page on the screen
                    widgets.stackedWidget_top_icons.setCurrentWidget(widgets.verify_email_page)

                # checking if the user account is verified
                elif user["verified_account"] == True:
                    # switch quick navigation stacked widget back to nav_icons_page on the screen
                    widgets.stackedWidget_top_icons.setCurrentWidget(widgets.nav_icons_page)

                # checking if the user favourite items are empty in the database
                if users_favourites.find_one({"user_name": widgets.user_name.text()}) is None:
                    # prompt the no_favourites widget on the dashboard display
                    widgets.no_favourites.raise_()
                    # hide the open favourite button
                    widgets.open_favourite_btn.hide()
                    # hide the clear all favourites button
                    widgets.clear_myfavourites_history_btn.hide()

                # checking if the user favourite items are not empty in the database
                if users_favourites.find_one({"user_name": widgets.user_name.text()}):
                    # remove the no_favourites widget from the dashboard display
                    widgets.no_favourites.lower()
                    # show the open favourite button
                    widgets.open_favourite_btn.show()
                    # show the clear all favourites button
                    widgets.clear_myfavourites_history_btn.show()

                # checking if the user Activity is empty in the database
                if users_activity.find_one({"user_name": widgets.user_name.text()}) is None:
                    # prompt the no_activity widget on the dashboard display
                    widgets.no_recent.raise_()
                    # hide the clear all activity button
                    widgets.clear_recent_history_btn.hide()

                # checking if the user Activity is not empty in the database
                if users_activity.find_one({"user_name": widgets.user_name.text()}):
                    # remove the no_activity widget from the dashboard display
                    widgets.no_recent.lower()
                    # show the clear all activity button
                    widgets.clear_recent_history_btn.show()

        # clear_recent_history btn
        if btnName == "clear_recent_history_btn":
                # prompt the clear_history_confirm_widget on the dashboard display
                widgets.clear_history_confirm_widget.raise_()

        # clear_recent_history confirm ok btn
        if btnName == "clear_history_confirm_ok_btn":
            # remove the clear_history_confirm_widget from the dashboard display
            widgets.clear_history_confirm_widget.lower()
            # calling a function to remove all the activity history from the database
            User_Profile.clear_recent_activity_history(self,widgets.user_name.text(),widgets)

        # clear_recent_history confirm cancel btn
        if btnName == "clear_history_confirm_cancel_btn":
            # remove the clear_history_confirm_widget from the dashboard display
            widgets.clear_history_confirm_widget.lower()

        # clear_fav_history btn
        if btnName == "clear_myfavourites_history_btn":
            # prompt the clear_fav_history_confirm_widget on the dashboard display
            widgets.clear_fav_history_confirm_widget.raise_()

        # clear_fav_history confirm ok btn
        if btnName == "clear_fav_history_confirm_ok_btn":
            # remove the clear_fav_history_confirm_widget from the dashboard display
            widgets.clear_fav_history_confirm_widget.lower()
            # calling a function to remove all the favourite history from the database
            User_Profile.clear_myfavourites_history(self, widgets.user_name.text(), widgets)

        # clear_fav_history confirm cancel btn
        if btnName == "clear_fav_history_confirm_cancel_btn":
            # remove the clear_fav_history_confirm_widget from the dashboard display
            widgets.clear_fav_history_confirm_widget.lower()

        # feedback page
        if btnName == "send_feedback_icon_btn" or btnName == "contact_us_btn":
            # switch content_page stacked widget to 'sendfeedbackpage' page on the screen
            widgets.stackedWidget_content_pages.setCurrentWidget(widgets.sendfeedbackpage)

        # send feedback btn
        if btnName == "send_feedback_btn":
            # getting the feedback text from the input widget
            user_feedback = widgets.feedback.text()
            # if the feedback is empty
            if user_feedback is None:
                # setting the success message label to Your Feedback is Empty!
                widgets.feedback_success_msg.setText('Your Feedback is Empty!')
                # prompt the feedback_sent_notification on the display
                widgets.feedback_sent_notification.raise_()

            # if the feedback is not empty
            if user_feedback:
                # prompt the confirm_feedback_widget on the display
                widgets.confirm_feedback_widget.raise_()

        # send feedback confirmation ok btn
        if btnName == "confirm_feedback_widget_ok_btn":
            # finding the user from the database by using user name
            user = User_Profile.find_user_by_name(self, widgets.user_name.text())
            # getting the feedback from the feedback input widget
            user_feedback = widgets.feedback.text()
            # calling a function to send the user email having the user feedback
            User_Profile.send_feedback(self, user["email"], user_feedback)
            # setting the success message label with Feedback Sent! Thanks for your support!
            widgets.feedback_success_msg.setText('Feedback Sent! Thanks for your support!')
            # prompt the feedback_sent_notification on the dashboard display
            widgets.feedback_sent_notification.raise_()
            # remove the confirm_feedback_widget from the dashboard display
            widgets.confirm_feedback_widget.lower()
            # updating the user 'Feedback Sent' activity in the database
            User_Profile.update_recent_activity(self, user["name"], 'Feedback Sent', 'Medium', widgets)

        # send feedback confirmation cancel btn
        if btnName == "confirm_feedback_widget_cancel_btn":
            # remove the confirm_feedback_widget from the dashboard display
            widgets.confirm_feedback_widget.lower()

        # feedback_sent_notification ok btn
        if btnName == "feedback_sent_notification_ok_btn":
            # remove the feedback_sent_notification from the dashboard display
            widgets.feedback_sent_notification.lower()

        # About us page
        if btnName == "about_icon_btn" or btnName == "about_btn":
            # checking if the user is not loggedIn
            if loggedIn == False:
                # switch main stacked widget to 'login_first_page' page on the screen
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)

            # checking if the user is loggedIn
            else:
                # switch main stacked widget to 'content_page' page on the screen
                widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
                # switch content_page stacked widget to 'about_page' page on the screen
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.about_page)

        # SHOW Profile PAGE
        if btnName == "account_settings_btn":
            # checking if the user is not loggedIn
            if loggedIn == False:
                # switch main stacked widget to 'login_first_page' page on the screen
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)

            # checking if the user is loggedIn
            else:
                # getting the user name from the user name label
                username = widgets.user_name.text()
                # finding the user in the database by the user name
                user = User_Profile.find_user_by_name(self, username);
                # checking if the user account is verified
                if user["verified_account"] == True:
                    # hiding the inappropriate widgets from the display
                    widgets.acc_verify_done_widget.hide()
                    widgets.verify_message_widget.hide()
                    widgets.acc_not_verify_widget.hide()

                    widgets.account_verify_stat.setText('Your Account is Verified!')

                    widgets.account_verify_stat.setStyleSheet(
                        "QLabel" "{" "color: rgb(55, 250, 68);" "}"
                    )

                if user["verified_account"] == False:

                    widgets.acc_verify_done_widget.show()
                    widgets.verify_message_widget.show()
                    widgets.acc_not_verify_widget.show()

                    widgets.account_verify_stat.setText('Account Not Verified!')

                    widgets.account_verify_stat.setStyleSheet(
                        "QLabel" "{" "color: rgb(255, 0, 0);" "}"
                    )

                widgets.stackedWidget_5.setCurrentWidget(widgets.profile_page)

                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # Verify_email
        if btnName == "verify_email_btn" or btnName == "verify_email_btn_2":
            servv = ei.connect("imap.gmail.com", host_user, app_password)
            ver_mail = servv.mail(servv.listids()[0])
            ver_mail.from_addr
            ver_mail.title
            widgets.acc_not_verify_widget.lower()
            if ver_mail.title == "ActivateMe":
                widgets.acc_verify_done_widget.raise_()

            else:
                widgets.stackedWidget_5.setCurrentWidget(widgets.profile_page)
                usr_name = widgets.user_name.text()
                usr = User_Profile.find_user_by_name(self, usr_name)
                User_Profile.send_verify_email_to_user_email(self, usr["email"])
                widgets.verify_message_widget.raise_()
                User_Profile.update_recent_activity(self, usr_name, 'Applied for Account Verification', 'Medium',
                                                    widgets)

        # Verify_email message ok btn
        if btnName == "verify_message_widget_ok_btn":
            widgets.verify_message_widget.lower()
            widgets.acc_not_verify_widget.raise_()

        # Verify_email success done btn
        if btnName == "acc_verify_done_btn":
            usr_name = widgets.user_name.text()
            User_Profile.update_account_verification(self, usr_name)
            widgets.acc_verify_done_widget.hide()
            widgets.verify_message_widget.hide()
            widgets.acc_not_verify_widget.hide()
            widgets.account_verify_stat.setText('Your Account is Verified!')
            widgets.account_verify_stat.setStyleSheet(
                "QLabel" "{" "color: rgb(55, 250, 68);" "}"
            )

            widgets.stackedWidget_top_icons.setCurrentWidget(widgets.nav_icons_page)
            User_Profile.update_recent_activity(self, usr_name, 'Account Verified Successfully', 'High', widgets)

        # deactivate_account
        if btnName == "deactivate_account_btn":
            widgets.deactivate_account_confirm_widget.raise_()

        # deactivate_account_ok
        if btnName == "deactivate_account_confirm_ok_btn":
            User_Profile.deactivate_account(self, widgets.profile_view_user_name.text())
            widgets.deactivate_account_confirm_widget.lower()
            widgets.stackedWidget_3.hide()
            widgets.stackedWidget_5.setCurrentWidget(widgets.login_page)

        # deactivate_account_cancel
        if btnName == "deactivate_account_confirm_cancel_btn":
            widgets.deactivate_account_confirm_widget.lower()

        # change_profile-pic
        if btnName == "profile_pic_change_btn":
            new_pixmap = QPixmap(self.getImage())
            if new_pixmap != widgets.profile_view_pic.pixmap():
                User_Profile.update_recent_activity(self, widgets.user_name.text(), 'Profile Pic Changed', 'Medium',
                                                    widgets)
            widgets.profile_view_pic.setPixmap(new_pixmap)
            username = widgets.user_name.text()
            user = User_Profile.find_user_by_name(self, username)
            User_Profile.update_profile_pic(self, user["name"], new_pixmap)

        # remove_profile-pic
        if btnName == "profile_pic_remove_btn":
            username = widgets.profile_view_user_name.text()
            User_Profile.remove_profile_pic(self, username)
            User_Profile.update_recent_activity(self, username, 'Profile Pic Removed', 'Medium', widgets)
            widgets.profile_view_pic.setPixmap("./images/images/profile_pic.png")

        # logout
        if btnName == "logout_btn" or btnName == "btn_logout" or btnName == "signout_btn":
            loggedIn = False
            username = widgets.profile_view_user_name.text()
            logout = User_Profile.logout(self, username)
            if logout == 'Logged out successfully':
                widgets.stackedWidget_3.hide()
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_page)
                User_Profile.update_logout_activity(self, username, 'Logged Out', 'High')

        if btnName == "datasets_btn":
            if loggedIn == False:
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)
            else:
                Datasets.load_datasets_thumbs(self,widgets)
                widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.datasets_page)
                if datasets.count() == 3:
                    widgets.label_new_dataset.hide()
                    widgets.new_datset_thumbnail.hide()
                    widgets.new_datset_thumbnail_btn.hide()

                elif datasets.count() > 3:
                    new_dst_load = Datasets.load_new_dataset(self, widgets)
                    if new_dst_load == "new dataset loaded":
                        widgets.label_new_dataset.show()
                        widgets.new_datset_thumbnail.show()
                        widgets.new_datset_thumbnail_btn.show()
                    elif new_dst_load == "new dataset not loaded":
                        widgets.label_new_dataset.hide()
                        widgets.new_datset_thumbnail.hide()
                        widgets.new_datset_thumbnail_btn.hide()

        if btnName == "model_training_btn":
            if loggedIn == False:
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)
            else:
                Datasets.load_datasets_thumbs(self, widgets)
                widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.model_training_page)
                if datasets.count() == 3:
                    widgets.label_new_dataset_2.hide()
                    widgets.new_datset_thumbnail_2.hide()
                    widgets.new_datset_thumbnail_btn_2.hide()

                elif datasets.count() > 3:
                    new_dst_load = Datasets.load_new_dataset(self, widgets)
                    if new_dst_load == "new dataset loaded":
                        widgets.label_new_dataset_2.show()
                        widgets.new_datset_thumbnail_2.show()
                        widgets.new_datset_thumbnail_btn_2.show()
                    elif new_dst_load == "new dataset not loaded":
                        widgets.label_new_dataset_2.hide()
                        widgets.new_datset_thumbnail_2.hide()
                        widgets.new_datset_thumbnail_btn_2.hide()

        if btnName == "style_gan_tab_btn":
            if loggedIn == False:
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)
            else:
                widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.stylegan_page)
                if Style_Gan_Model.login_success == False:
                    widgets.stackedWidget_stylegan.setCurrentWidget(widgets.google_account_page)

        # SUBMIT GOOGLE LOGIN_FORM
        if btnName == "login_google_btn":
            # getting the entered user name form the login form
            username = widgets.user_name_google.text()
            # getting the entered user password form the login form
            password = widgets.user_password_google.text()
            # calling the login function to validate the login request
            threading.Thread(target=Style_Gan_Model.sign_in_google_account, args=[self, username, password,widgets]).start()
            #Style_Gan_Model.sign_in_google_account(self, username, password)
            # if the login success message is returned
            threading.Thread(target=Style_Gan_Model.login_status, args=[self,widgets]).start()
            # Loading the GIF
            self.google_dots_loading = QMovie(":/images/images/images/swirly-dots-to-chrome.gif")
            widgets.login_loading_label.setMovie(self.google_dots_loading)
            self.google_dots_loading.start()
            widgets.login_loading_label.raise_()

        # login_success_notification
        if btnName == "login_success_ok_btn_2":
            # removing the login success message  from the app display
            widgets.login_success_notification_2.lower()
            # getting the user name
            username = widgets.user_name.text()

            # finding the user by the user email
            user = User_Profile.find_user_by_name(self, username);
            # updating the user 'Logged in Successfully' activity in the database
            User_Profile.update_recent_activity(self, user["name"], 'Logged in to Google Successfully', 'High', widgets)
            Datasets.load_datasets_thumbs(self, widgets)

            if self.translation_process == False:
                # switch style gan stacked widget to models page on the screen
                widgets.stackedWidget_stylegan.setCurrentWidget(widgets.pretrained_models_page)
                self.human_gif = QMovie(":/images/images/images/stylegananim1.gif")
                widgets.label_262.setMovie(self.human_gif)
                self.human_gif.start()
                self.anime_gif = QMovie(":/images/images/images/stylegananim2.gif")
                widgets.label_263.setMovie(self.anime_gif)
                self.anime_gif.start()
            elif self.translation_process == True:
                self.dst_gif = QMovie(":/images/images/images/loadingAnimation.gif")
                self.tick_gif = QMovie(":/images/images/images/tick.gif")
                self.tick = QPixmap(":/images/images/images/tick.png")
                widgets.style_gan_plabel_4.setMovie(self.dst_gif)
                self.tick_gif.start()
                self.dst_gif.start()
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.image_customization)
                widgets.stackedWidget_img_cutom.setCurrentWidget(widgets.image_translation_process)
                threading.Thread(target=Image_Customization.translate_images, args=[self, widgets]).start()
        # login_fail_notification
        if btnName == "login_fail_ok_btn_2":
            # removing the login fail message  from the app display
            widgets.login_fail_notification_2.lower()

        if btnName == "forget_pass_name_google_btn":
            # link to google accounts
            webbrowser.open('https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

        if btnName == "signup_google_btn":
            Style_Gan_Model.sign_up_google_account(self)

        if btnName == "google_verify_code_widget_ok_btn":
            threading.Thread(target=Style_Gan_Model.verify_code, args=[self,widgets.google_verify_code.text(),widgets]).start()
        #google_verify_code

        if btnName == "google_verify_code_widget_cancel_btn":
            widgets.google_verify_code_widget.lower()
            Style_Gan_Model.driver.close()
            widgets.login_loading_label.lower()

        if btnName == "style_gan1_btn":
            # switch style gan stacked widget to models page on the screen
            widgets.stackedWidget_stylegan.setCurrentWidget(widgets.stylegan1_page)

        if btnName == "style_gan2_btn":
            # switch style gan stacked widget to models page on the screen
            widgets.stackedWidget_stylegan.setCurrentWidget(widgets.stylegan2_page)

        if btnName == "logout_google_btn":
            # logout from the google account
            Style_Gan_Model.driver.close()
            Style_Gan_Model.login_fail = False
            Style_Gan_Model.login_success = False
            widgets.stackedWidget_stylegan.setCurrentWidget(widgets.google_account_page)

        if btnName == "train_stylegan_btn":
            # switch style gan stacked widget to models page on the screen
            widgets.update_algo_widget_2.raise_()

        if btnName == "update_stylegan_algo_btn":
            widgets.update_algo_widget_2.raise_()

        if btnName == "update_algo_ok_btn_2":
            key = widgets.admin_key.text()
            match_result = User_Profile.match_admin_secret_key(self,key)
            if match_result == 'Key Found':
                user = widgets.user_name_2.text()
                widgets.key_match_error_2.setText("")
                widgets.update_algo_widget_2.lower()
                User_Profile.update_recent_activity(self, user, "Started Algo Update",'High', widgets)
                #Gan_Model.update_algo(self)
                User_Profile.update_recent_activity(self, user, "Ended Algo Update",'High', widgets)
            elif match_result == 'Key Not Found':
                widgets.key_match_error_2.setText("Key Not Found")

        if btnName == "update_algo_cancel_btn_2":
            widgets.update_algo_widget_2.lower()

        if btnName == "back_to_models_btn_1":
            widgets.stackedWidget_stylegan.setCurrentWidget(widgets.pretrained_models_page)

        if btnName == "back_to_models_btn_2":
            widgets.stackedWidget_stylegan.setCurrentWidget(widgets.pretrained_models_page)

        if btnName == "generate_images_style1_btn":
            if (widgets.output_size_style1.currentText()).isnumeric() == False:
                widgets.output_size_error.raise_()
            if widgets.runtime_env_style1.currentText() != 'GPU':
                widgets.runtime_env_error.raise_()
            if (widgets.output_size_style1.currentText()).isnumeric() and (widgets.runtime_env_style1.currentText()) == 'GPU':
                if Style_Gan_Model.process1_running == False:
                    # calling the run style gan 1 algo to generate images of high quality
                    dataset = Style_Gan_Model.selected_dataset(self,widgets)
                    self.dst_gif = QMovie(":/images/images/images/loadingAnimation.gif")
                    self.tick_gif = QMovie(":/images/images/images/tick.gif")
                    self.tick = QPixmap(":/images/images/images/tick.png")
                    widgets.loading_label_dst.setMovie(self.dst_gif)
                    widgets.label_264.setMovie(self.human_gif)
                    self.tick_gif.start()
                    self.dst_gif.start()
                    threading.Thread(target=Style_Gan_Model.run_style_gan1, args=[self, abs(int((widgets.output_size_style1.currentText()))), dataset,widgets]).start()
                    widgets.stackedWidget_stylegan.setCurrentWidget(widgets.stylegan1_progress_page)
                    widgets.output_size_error.lower()
                    widgets.runtime_env_error.lower()
                else:
                    widgets.stackedWidget_stylegan.setCurrentWidget(widgets.stylegan1_progress_page)
                    widgets.output_size_error.lower()
                    widgets.runtime_env_error.lower()

        if btnName == "view_style1_generated_imgs_btn":
            Style_Gan_Model.store_stylegan1_outputs(self)

        if btnName == "rerun_style1gan_btn":
            widgets.rerun_stylegan1_confirm_widget.raise_()

        if btnName == "rerun_stylegan1_confirm_ok_btn":
            widgets.rerun_stylegan1_confirm_widget.lower()
            dataset = Style_Gan_Model.selected_dataset(self, widgets)
            self.dst_gif = QMovie(":/images/images/images/loadingAnimation.gif")
            self.tick_gif = QMovie(":/images/images/images/tick.gif")
            self.tick = QPixmap(":/images/images/images/tick.png")
            widgets.loading_label_dst.setMovie(self.dst_gif)
            widgets.label_264.setMovie(self.human_gif)
            self.tick_gif.start()
            self.dst_gif.start()
            Style_Gan_Model.refresh_with_alert(Style_Gan_Model.driver)
            threading.Thread(target=Style_Gan_Model.run_style_gan1,
                             args=[self, abs(int((widgets.output_size_style1.currentText()))), dataset,
                                   widgets]).start()
            widgets.stackedWidget_stylegan.setCurrentWidget(widgets.stylegan1_progress_page)
            widgets.output_size_error.lower()
            widgets.runtime_env_error.lower()

        if btnName == "rerun_stylegan1_confirm_cancel_btn":
            widgets.rerun_stylegan1_confirm_widget.lower()

        if btnName == "cancel_progress_style1_btn":
            widgets.cancel_stylegan1_confirm_widget.raise_()

        if btnName == "cancel_stylegan1_confirm_ok_btn":
            widgets.cancel_stylegan1_confirm_widget.lower()
            # Open a new window
            Style_Gan_Model.refresh_with_alert(Style_Gan_Model.driver)
            widgets.stackedWidget_stylegan.setCurrentWidget(widgets.stylegan1_page)

        if btnName == "cancel_stylegan1_confirm_cancel_btn":
            widgets.cancel_stylegan1_confirm_widget.lower()

        if btnName == "generate_images_style2_btn":
            start_val = int(widgets.start_image_style2.currentText())
            end_val = int(widgets.end_image_style2.currentText())

            if (widgets.start_image_style2.currentText()).isnumeric() == False or (widgets.end_image_style2.currentText()).isnumeric() == False or start_val>end_val:
                widgets.output_size_error_2.raise_()

            if widgets.runtime_env_style2.currentText() != 'GPU':
                widgets.runtime_env_error_2.raise_()
            if (widgets.start_image_style2.currentText()).isnumeric() and (widgets.end_image_style2.currentText()).isnumeric() and (widgets.runtime_env_style1.currentText()) == 'GPU' and  start_val<end_val:
                if Style_Gan_Model.process2_running == False:
                    # calling the run style gan 1 algo to generate images of high quality
                    style2_dataset = Style_Gan_Model.selected_dataset_2(self, widgets)
                    self.dst_gif_2 = QMovie(":/images/images/images/loadingAnimation.gif")
                    self.tick_gif_2 = QMovie(":/images/images/images/tick.gif")
                    self.tick_2 = QPixmap(":/images/images/images/tick.png")
                    widgets.loading_label_dst_2.setMovie(self.dst_gif_2)
                    widgets.label_265.setMovie(self.anime_gif)
                    self.tick_gif_2.start()
                    self.dst_gif_2.start()
                    threading.Thread(target=Style_Gan_Model.run_style_gan2,args=[self, abs(start_val),abs(end_val),style2_dataset,widgets]).start()
                    widgets.stackedWidget_stylegan.setCurrentWidget(widgets.stylegan2_progress_page)
                    widgets.output_size_error_2.lower()
                    widgets.runtime_env_error_2.lower()
                else:
                    widgets.stackedWidget_stylegan.setCurrentWidget(widgets.stylegan2_progress_page)
                    widgets.output_size_error_2.lower()
                    widgets.runtime_env_error_2.lower()

        if btnName == "view_style2_generated_imgs_btn":
            Style_Gan_Model.store_stylegan2_outputs(self)

        if btnName == "rerun_style2gan_btn":
            widgets.rerun_stylegan2_confirm_widget.raise_()

        if btnName == "rerun_stylegan2_confirm_ok_btn":
            start_val = int(widgets.start_image_style2.currentText())
            end_val = int(widgets.end_image_style2.currentText())
            widgets.rerun_stylegan2_confirm_widget.lower()
            style2_dataset = Style_Gan_Model.selected_dataset_2(self, widgets)
            self.dst_gif_2 = QMovie(":/images/images/images/loadingAnimation.gif")
            self.tick_gif_2 = QMovie(":/images/images/images/tick.gif")
            self.tick_2 = QPixmap(":/images/images/images/tick.png")
            widgets.loading_label_dst_2.setMovie(self.dst_gif_2)
            widgets.label_265.setMovie(self.anime_gif)
            self.tick_gif_2.start()
            self.dst_gif_2.start()
            Style_Gan_Model.refresh_with_alert(Style_Gan_Model.driver)
            threading.Thread(target=Style_Gan_Model.run_style_gan2,
                             args=[self, abs(start_val), abs(end_val), style2_dataset, widgets]).start()
            widgets.stackedWidget_stylegan.setCurrentWidget(widgets.stylegan2_progress_page)
            widgets.output_size_error_2.lower()
            widgets.runtime_env_error_2.lower()

        if btnName == "rerun_tstylegan2_confirm_cancel_btn":
            widgets.rerun_stylegan2_confirm_widget.lower()

        if btnName == "cancel_progress_style2_btn":
            widgets.cancel_stylegan2_confirm_widget.raise_()

        if btnName == "cancel_stylegan2_confirm_ok_btn":
            widgets.cancel_stylegan2_confirm_widget.lower()
            # Open a new window
            Style_Gan_Model.refresh_with_alert(Style_Gan_Model.driver)
            widgets.stackedWidget_stylegan.setCurrentWidget(widgets.stylegan2_page)

        if btnName == "cancel_stylegan2_confirm_cancel_btn":
            widgets.cancel_stylegan2_confirm_widget.lower()

        if btnName == "back_to_style1_page_btn":
            widgets.stackedWidget_stylegan.setCurrentWidget(widgets.stylegan1_page)

        if btnName == "back_to_style2_page_btn":
            widgets.stackedWidget_stylegan.setCurrentWidget(widgets.stylegan2_page)

        if btnName == "generated_images_btn":
            if loggedIn == False:
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)
            else:
                outputs_load_status = Outputs.load_output_images_thumbs(self, widgets)
                print(outputs_load_status)
                if outputs_load_status == "output loaded success":
                    widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
                    username = widgets.user_name.text()
                    Outputs.load_favourite_btns(self, username, widgets)
                    widgets.stackedWidget_content_pages.setCurrentWidget(widgets.generated_images_page)
                    widgets.generated_images_stackedWidget.setCurrentWidget(widgets.output_thumbs_view_page)
                    widgets.outputs_thumb_view_btn.hide()
                    widgets.outputs_list_view_btn.show()
                elif outputs_load_status == "no outputs":
                    widgets.stackedWidget_content_pages.setCurrentWidget(widgets.generated_images_page)
                    widgets.generated_images_stackedWidget.setCurrentWidget(widgets.no_outputs_page)
                    widgets.outputs_thumb_view_btn.hide()
                    widgets.outputs_list_view_btn.hide()

        if btnName == "images_library_btn":
            if loggedIn == False:
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)
            else:
                widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.images_library_page)

        if btnName == "help_btn":
            if loggedIn == False:
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)
            else:
                widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.help_page)

        if btnName == "btn_sysinfo":
            if loggedIn == False:
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)
            else:
                widgets.stackedWidget_3.setCurrentWidget(widgets.system_info_usage_graph)

        if btnName == "btn_usage":
            if loggedIn == False:
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)
            else:
                widgets.stackedWidget_3.setCurrentWidget(widgets.cpu_ram_circular)

        if btnName == "show_circular_percent_btn":
            widgets.show_circular_percent_btn.setStyleSheet(
                "QPushButton" "{" "background-color : rgba(0, 0, 0,0);" "}"
            )
            widgets.stackedWidget_3.setCurrentWidget(widgets.cpu_ram_circular)

        if btnName == "show_ram_graph_btn_3":
            if loggedIn == False:
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)
            else:
                widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.usage_graph_page)

        if btnName == "show_cpu_graph_btn_3":
            if loggedIn == False:
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)
            else:
                widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.usage_graph_page)

        if btnName == "btn_hide_gadgets":
            if loggedIn == False:
                widgets.stackedWidget_5.setCurrentWidget(widgets.login_first_page)
            else:
                if widgets.btn_hide_gadgets.text() == 'Hide Gadgets':
                    widgets.stackedWidget_3.hide()
                    widgets.btn_hide_gadgets.setText('Show Gadgets')
                elif widgets.btn_hide_gadgets.text() == 'Show Gadgets':
                    widgets.stackedWidget_3.show()
                    widgets.btn_hide_gadgets.setText('Hide Gadgets')

        if btnName == "output_image_1_btn" or btnName == "output_image_2_btn" or btnName == "output_image_3_btn" or btnName == "output_image_4_btn" or btnName == "output_image_5_btn" or btnName== "output_image_6_btn":
            if btnName == "output_image_1_btn":
                self.open_image(widgets.output_image_1.pixmap())
            elif btnName == "output_image_2_btn":
                self.open_image(widgets.output_image_2.pixmap())
            elif btnName == "output_image_3_btn":
                self.open_image(widgets.output_image_3.pixmap())
            elif btnName == "output_image_4_btn":
                self.open_image(widgets.output_image_4.pixmap())
            elif btnName == "output_image_5_btn":
                self.open_image(widgets.output_image_5.pixmap())
            elif btnName == "output_image_6_btn":
                self.open_image(widgets.output_image_6.pixmap())

        if btnName == "output_folder_btn":
            Outputs.open_output_folder(self)

        if btnName == "create_new_dataset_btn":
            widgets.datsets_stackedWidget.setCurrentWidget(widgets.created_dataset_page)

        if btnName == "anime_thumbnail_btn":
            Datasets.load_anime_dataset_imgs(self,widgets)
            widgets.datsets_stackedWidget.setCurrentWidget(widgets.anime_dataset_page)

        if btnName == "human_thumbnail_btn":
            Datasets.load_human_dataset_imgs(self, widgets)
            widgets.datsets_stackedWidget.setCurrentWidget(widgets.human_dataset_page)

        if btnName == "flower_thumbnail_btn":
            Datasets.load_flower_dataset_imgs(self,widgets)
            widgets.datsets_stackedWidget.setCurrentWidget(widgets.flower_datset_page)

        if btnName == "new_datset_thumbnail_btn":
            Datasets.load_flower_dataset_imgs(self,widgets)
            widgets.datsets_stackedWidget.setCurrentWidget(widgets.new_dataset_page)

        if btnName == "back_to_dataset_btn" or btnName == "back_to_dataset_btn_2" or btnName == "back_to_dataset_btn_3" or btnName == "back_to_dataset_btn_4" or btnName == "back_to_dataset_btn_5" or btnName == "back_to_dataset_btn_6":
            widgets.datsets_stackedWidget.setCurrentWidget(widgets.create_dataset_page)

        if btnName == "new_dst_upload_thumb_btn":
            widgets.new_dst_u_image_0.setPixmap(QPixmap(self.getImage()))
            # widgets.profile_image.resize(70, 70)

        if btnName == "new_dst_u_image_1_btn":
            widgets.new_dst_u_image_1.setPixmap(QPixmap(self.getImage()))
            # widgets.profile_image.resize(70, 70)

        if btnName == "new_dst_u_image_2_btn":
            widgets.new_dst_u_image_2.setPixmap(QPixmap(self.getImage()))
            # widgets.profile_image.resize(70, 70)

        if btnName == "new_dst_u_image_3_btn":
            widgets.new_dst_u_image_3.setPixmap(QPixmap(self.getImage()))
            # widgets.profile_image.resize(70, 70)

        if btnName == "new_dst_u_image_4_btn":
            widgets.new_dst_u_image_4.setPixmap(QPixmap(self.getImage()))
            # widgets.profile_image.resize(70, 70)

        if btnName == "new_dst_u_image_5_btn":
            widgets.new_dst_u_image_5.setPixmap(QPixmap(self.getImage()))
            # widgets.profile_image.resize(70, 70)

        if btnName == "create_dst_done_btn":
            dataset_creation = Datasets.create_dataset(self,widgets)
            if  dataset_creation == "dataset not created":
                widgets.dst_fail_notification.raise_()
            elif dataset_creation == "dataset created":
                user = widgets.user_name.text()
                User_Profile.update_recent_activity(self, user, 'Created Dataset',
                                                    'High', widgets)
                widgets.dst_success_notification.raise_()

        if btnName == "dst_success_ok_btn":
            widgets.dst_success_notification.lower()
            new_dst_load = Datasets.load_new_dataset(self, widgets)
            if new_dst_load == "new dataset loaded":
                widgets.label_new_dataset.show()
                widgets.new_datset_thumbnail.show()
                widgets.new_datset_thumbnail_btn.show()
            elif new_dst_load == "new dataset not loaded":
                widgets.label_new_dataset.hide()
                widgets.new_datset_thumbnail.hide()
                widgets.new_datset_thumbnail_btn.hide()
            widgets.datsets_stackedWidget.setCurrentWidget(widgets.create_dataset_page)

        if btnName == "dst_fail_ok_btn":
            widgets.dst_fail_notification.lower()

        if btnName == "upload_images_btn":
            widgets.new_dst_image_6.setPixmap(QPixmap(self.getImage()))
            new_image_to_dst = Datasets.add_image_to_dataset(self, widgets)
            if new_image_to_dst == 'image added':
                user = widgets.user_name.text()
                User_Profile.update_recent_activity(self, user, 'Uploaded Image',
                                                    'High', widgets)
                widgets.label_24.setText('Image Added Successfully')
                widgets.new_dst_success_notification.raise_()
            elif new_image_to_dst == 'image not added':
                widgets.label_27.setText('Unable to add image')
                widgets.new_dst_fail_notification.raise_()

        if btnName == "delete_new_dataset_btn":
            widgets.new_dataset_del_confirm_widget.raise_()

        if btnName == "new_dataset_del_confirm_ok_btn":
            widgets.new_dataset_del_confirm_widget.lower()
            dataset_deletion = Datasets.delete_new_dataset(self)
            if dataset_deletion == 'dataset deleted':
                user = widgets.user_name.text()
                User_Profile.update_recent_activity(self, user, 'Dateset Deleted',
                                                    'High', widgets)
                new_dst_load = Datasets.load_new_dataset(self, widgets)
                if new_dst_load == "new dataset loaded":
                    widgets.label_new_dataset.show()
                    widgets.new_datset_thumbnail.show()
                    widgets.new_datset_thumbnail_btn.show()
                elif new_dst_load == "new dataset not loaded":
                    widgets.label_new_dataset.hide()
                    widgets.new_datset_thumbnail.hide()
                    widgets.new_datset_thumbnail_btn.hide()
                widgets.datsets_stackedWidget.setCurrentWidget(widgets.create_dataset_page)

            elif dataset_deletion == 'unable to delete':
                widgets.label_27.setText('Unable to delete dataset')
                widgets.new_dst_fail_notification.raise_()

        if btnName == "new_dataset_del_confirm_cancel_btn":
            widgets.new_dataset_del_confirm_widget.lower()

        if btnName == "dst_fail_ok_btn_2":
            widgets.new_dst_fail_notification.lower()

        if btnName == "dst_success_ok_btn_2":
            widgets.new_dst_success_notification.lower()

        if btnName == "searched_dst_thumbnail_btn" or btnName == "view_searched_dst_btn":
            Datasets.load_searched_dataset(self,widgets)
            widgets.dataset_found_widget.lower()
            widgets.datsets_stackedWidget.setCurrentWidget(widgets.found_dataset_page)

        if btnName == "searched_dst_cancel_btn":
            widgets.dataset_found_widget.lower()

        if btnName == "searched_dst_cancel_btn_2":
            widgets.dataset_found_widget_2.lower()

        if btnName == "view_searched_ok_btn":
            widgets.dataset_not_found_widget.lower()

        if btnName == "view_searched_ok_btn_2":
            widgets.dataset_not_found_widget_2.lower()

        if btnName == "upload_images_btn_2":
            widgets.new_dst_image_12.setPixmap(QPixmap(self.getImage()))
            new_image_to_dst = Datasets.add_image_to_searched_dataset(self, widgets)
            if new_image_to_dst == 'image added':
                user = widgets.user_name.text()
                User_Profile.update_recent_activity(self, user, 'Uploaded Image',
                                                    'High', widgets)
                widgets.label_30.setText('Image Added Successfully')
                widgets.new_dst_success_notification_2.raise_()
            elif new_image_to_dst == 'image not added':
                widgets.label_31.setText('Unable to add image')
                widgets.new_dst_fail_notification_2.raise_()

        if btnName == "delete_new_dataset_btn_2":
            widgets.new_dataset_del_confirm_widget_2.raise_()

        if btnName == "new_dataset_del_confirm_cancel_btn_2":
            widgets.new_dataset_del_confirm_widget_2.lower()

        if btnName == "new_dataset_del_confirm_ok_btn_2":
            widgets.new_dataset_del_confirm_widget_2.lower()
            dataset_deletion = Datasets.delete_searched_dataset(self,widgets)
            if dataset_deletion == 'dataset deleted':
                new_dst_load = Datasets.load_new_dataset(self, widgets)
                if new_dst_load == "new dataset loaded":
                    widgets.label_new_dataset.show()
                    widgets.new_datset_thumbnail.show()
                    widgets.new_datset_thumbnail_btn.show()
                elif new_dst_load == "new dataset not loaded":
                    widgets.label_new_dataset.hide()
                    widgets.new_datset_thumbnail.hide()
                    widgets.new_datset_thumbnail_btn.hide()
                widgets.datsets_stackedWidget.setCurrentWidget(widgets.create_dataset_page)
            elif dataset_deletion == 'unable to delete':
                widgets.label_31.setText('Unable to delete dataset')
                widgets.new_dst_fail_notification_2.raise_()


        if btnName == "dst_fail_ok_btn_3":
            widgets.new_dst_fail_notification_2.lower()

        if btnName == "dst_success_ok_btn_3":
            widgets.new_dst_success_notification_2.lower()

        if btnName == "human_thumbnail_btn_2":
            widgets.stackedWidget_model_training.setCurrentWidget(widgets.model_train_options_page)
            widgets.label_224.setPixmap(widgets.human_thumbnail_2.pixmap())


        if btnName == "run_gan_btn":
            user = widgets.user_name.text()
            User_Profile.update_recent_activity(self, user, 'Started Training',
                                                'High', widgets)
            Gan_Model.train_model(self,widgets)
            User_Profile.update_recent_activity(self, user, 'Ended Training',
                                                'High', widgets)

        if btnName == "change_dst_btn":
            widgets.stackedWidget_model_training.setCurrentWidget(widgets.select_dataset_page)

        if btnName == "rerun_gan_btn":
            widgets.rerun_training_confirm_widget.raise_()

        if btnName == "cancel_training_btn":
            widgets.cancel_training_confirm_widget.raise_()

        if btnName == "cancel_training_confirm_ok_btn":
            widgets.stackedWidget_model_training.setCurrentWidget(widgets.select_dataset_page)

        if btnName == "cancel_training_confirm_cancel_btn":
            widgets.cancel_training_confirm_widget.lower()

        if btnName == "rerun_training_confirm_ok_btn":
            user = widgets.user_name.text()
            User_Profile.update_recent_activity(self, user, 'ReStarted Training',
                                                'High', widgets)
            Gan_Model.train_model(self, widgets)
            User_Profile.update_recent_activity(self, user, 'Ended Training',
                                            'High', widgets)
        if btnName == "rerun_training_confirm_cancel_btn":
            widgets.rerun_training_confirm_widget.lower()


        if btnName == "view_generated_imgs_btn":
            outputs_load_status = Outputs.load_output_images_thumbs(self, widgets)
            if outputs_load_status == "output loaded success":
                widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
                username = widgets.user_name.text()
                Outputs.load_favourite_btns(self, username, widgets)
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.generated_images_page)
                widgets.generated_images_stackedWidget.setCurrentWidget(widgets.output_thumbs_view_page)
                widgets.outputs_thumb_view_btn.hide()
                widgets.outputs_list_view_btn.show()
            elif outputs_load_status == "no outputs":
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.generated_images_page)
                widgets.generated_images_stackedWidget.setCurrentWidget(widgets.no_outputs_page)
                widgets.outputs_thumb_view_btn.hide()
                widgets.outputs_list_view_btn.hide()

        if btnName == "make_fav1_btn":
            username = widgets.user_name.text()
            Outputs.update_myfavourites(self, username, widgets.output_image_1.pixmap(),"Image", widgets)
            widgets.make_fav1_btn.hide()
            widgets.remove_fav1_btn.show()
            User_Profile.update_recent_activity(self, username, 'Favourite Added',
                                                'High', widgets)

        if btnName == "make_fav2_btn":
            username = widgets.user_name.text()
            Outputs.update_myfavourites(self, username, widgets.output_image_2.pixmap(), "Image", widgets)
            widgets.make_fav2_btn.hide()
            widgets.remove_fav2_btn.show()
            User_Profile.update_recent_activity(self, username, 'Favourite Added',
                                                'High', widgets)

        if btnName == "make_fav3_btn":
            username = widgets.user_name.text()
            Outputs.update_myfavourites(self, username, widgets.output_image_3.pixmap(), "Image", widgets)
            widgets.make_fav3_btn.hide()
            widgets.remove_fav3_btn.show()
            User_Profile.update_recent_activity(self, username, 'Favourite Added',
                                                'High', widgets)

        if btnName == "make_fav4_btn":
            username = widgets.user_name.text()
            Outputs.update_myfavourites(self, username, widgets.output_image_4.pixmap(), "Image", widgets)
            widgets.make_fav4_btn.hide()
            widgets.remove_fav4_btn.show()
            User_Profile.update_recent_activity(self, username, 'Favourite Added',
                                                'High', widgets)

        if btnName == "make_fav5_btn":
            username = widgets.user_name.text()
            Outputs.update_myfavourites(self, username, widgets.output_image_5.pixmap(), "Image", widgets)
            widgets.make_fav5_btn.hide()
            widgets.remove_fav5_btn.show()
            User_Profile.update_recent_activity(self, username, 'Favourite Added',
                                                'High', widgets)

        if btnName == "make_fav6_btn":
            username = widgets.user_name.text()
            Outputs.update_myfavourites(self, username, widgets.output_image_6.pixmap(), "Image", widgets)
            widgets.make_fav6_btn.hide()
            widgets.remove_fav6_btn.show()
            User_Profile.update_recent_activity(self, username, 'Favourite Added',
                                                'High', widgets)

        if btnName == "remove_fav1_btn":
            username = widgets.user_name.text()
            Outputs.remove_favourite(self,username,widgets.output_image_1.pixmap(),widgets)
            widgets.remove_fav1_btn.hide()
            widgets.make_fav1_btn.show()
            User_Profile.update_recent_activity(self, username, 'Favourite Removed',
                                                'High', widgets)

        if btnName == "remove_fav2_btn":
            username = widgets.user_name.text()
            Outputs.remove_favourite(self, username, widgets.output_image_2.pixmap(), widgets)
            widgets.remove_fav2_btn.hide()
            widgets.make_fav2_btn.show()
            User_Profile.update_recent_activity(self, username, 'Favourite Removed',
                                                'High', widgets)

        if btnName == "remove_fav3_btn":
            username = widgets.user_name.text()
            Outputs.remove_favourite(self, username, widgets.output_image_3.pixmap(), widgets)
            widgets.remove_fav3_btn.hide()
            widgets.make_fav3_btn.show()
            User_Profile.update_recent_activity(self, username, 'Favourite Removed',
                                                'High', widgets)

        if btnName == "remove_fav4_btn":
            username = widgets.user_name.text()
            Outputs.remove_favourite(self, username, widgets.output_image_4.pixmap(), widgets)
            widgets.remove_fav4_btn.hide()
            widgets.make_fav4_btn.show()
            User_Profile.update_recent_activity(self, username, 'Favourite Removed',
                                                'High', widgets)

        if btnName == "remove_fav5_btn":
            username = widgets.user_name.text()
            Outputs.remove_favourite(self, username, widgets.output_image_5.pixmap(), widgets)
            widgets.remove_fav5_btn.hide()
            widgets.make_fav5_btn.show()
            User_Profile.update_recent_activity(self, username["name"], 'Favourite Removed',
                                                'High', widgets)

        if btnName == "remove_fav6_btn":
            username = widgets.user_name.text()
            Outputs.remove_favourite(self, username, widgets.output_image_6.pixmap(), widgets)
            widgets.remove_fav6_btn.hide()
            widgets.make_fav6_btn.show()
            User_Profile.update_recent_activity(self, username, 'Favourite Removed',
                                                'High', widgets)

        if btnName == "outputs_list_view_btn":
            outputs_load_status = Outputs.load_output_images_list(self, widgets)
            if outputs_load_status == "output loaded success":
                widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
                username = widgets.user_name.text()
                Outputs.load_favourite_btns(self, username, widgets)
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.generated_images_page)
                widgets.generated_images_stackedWidget.setCurrentWidget(widgets.output_list_view_page)
                widgets.outputs_thumb_view_btn.show()
                widgets.outputs_list_view_btn.hide()

            elif outputs_load_status == "no outputs":
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.generated_images_page)
                widgets.generated_images_stackedWidget.setCurrentWidget(widgets.no_outputs_page)
                widgets.outputs_thumb_view_btn.hide()
                widgets.outputs_list_view_btn.hide()

        if btnName == "outputs_thumb_view_btn":
            outputs_load_status = Outputs.load_output_images_thumbs(self, widgets)
            if outputs_load_status == "output loaded success":
                widgets.stackedWidget_5.setCurrentWidget(widgets.content_page)
                username = widgets.user_name.text()
                Outputs.load_favourite_btns(self, username, widgets)
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.generated_images_page)
                widgets.generated_images_stackedWidget.setCurrentWidget(widgets.output_thumbs_view_page)
                widgets.outputs_thumb_view_btn.hide()
                widgets.outputs_list_view_btn.show()
            elif outputs_load_status == "no outputs":
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.generated_images_page)
                widgets.generated_images_stackedWidget.setCurrentWidget(widgets.no_outputs_page)
                widgets.outputs_thumb_view_btn.hide()
                widgets.outputs_list_view_btn.hide()

        if btnName == "open_favourite_btn":
            User_Profile.open_favourite(self,widgets)

        if btnName == "open_output_list_img_btn":
            Outputs.open_output_list_image(self,widgets)

        if btnName == "update_algo_btn":
            widgets.update_algo_widget.raise_()

        if btnName == "update_algo_ok_btn":
            key = widgets.admin_key.text()
            match_result = User_Profile.match_admin_secret_key(self,key)
            if match_result == 'Key Found':
                user = widgets.user_name.text()
                widgets.key_match_error.setText("")
                widgets.update_algo_widget.lower()
                User_Profile.update_recent_activity(self, user, "Started Algo Update",'High', widgets)
                Gan_Model.update_algo(self)
                User_Profile.update_recent_activity(self, user, "Ended Algo Update",'High', widgets)
            elif match_result == 'Key Not Found':
                widgets.key_match_error.setText("Key Not Found")

        if btnName == "update_algo_cancel_btn":
            widgets.update_algo_widget.lower()

        if btnName == "customize_image_btn":
            self.resized_image_331 = Image_Customization.choose_image(self, widgets, 331, 331)[0]
            self.customized_image_331 = self.resized_image_331
            self.resized_image_array_331 = Image_Customization.choose_image(self, widgets, 331, 331)[2]
            self.original_image = Image_Customization.choose_image(self,widgets,251,251)[1]
            self.customized_image = self.original_image
            self.original_image_array = Image_Customization.choose_image(self, widgets,251,251)[3]
            widgets.stackedWidget_content_pages.setCurrentWidget(widgets.image_customization)
            widgets.selected_image.setPixmap(QtGui.QPixmap(self.customized_image_331))

        if btnName == "reset_changes_image_btn":
            self.rotation_process = False
            self.resized_image_331 = Image_Customization.choose_image(self, widgets, 331, 331)[0]
            self.customized_image_331 = self.resized_image_331
            self.resized_image_array_331 = Image_Customization.choose_image(self, widgets, 331, 331)[2]
            self.original_image = Image_Customization.choose_image(self, widgets, 251, 251)[1]
            self.customized_image = self.original_image
            self.original_image_array = Image_Customization.choose_image(self, widgets, 251, 251)[3]
            widgets.img_cutom_widget.raise_()
            widgets.changes_reset_notification.raise_()

        if btnName == "changes_reset_ok_btn":
            widgets.stackedWidget_img_cutom.setCurrentWidget(widgets.img_custom_home)
            widgets.selected_image.setPixmap(QtGui.QPixmap(self.customized_image_331))
            widgets.img_cutom_widget.lower()
            widgets.changes_reset_notification.lower()

        if btnName == "apply_effects_btn":
            widgets.stackedWidget_img_cutom.setCurrentWidget(widgets.img_filters)
            widgets.selected_image_filter_2.setPixmap(QtGui.QPixmap(self.resized_image_331))

        if btnName == "mean_filter_btn":
            Image_Customization.apply_filters(self, "mean_filter",widgets)

        if btnName == "median_filter_btn":
            Image_Customization.apply_filters(self, "median_filter",widgets)

        if btnName == "gaussian_filter_btn":
            Image_Customization.apply_filters(self, "gaussian_filter", widgets)

        if btnName == "bilateral_filter_btn":
            Image_Customization.apply_filters(self, "bilateral_filter", widgets)

        if btnName == "contrast_image_btn":
            widgets.stackedWidget_img_cutom.setCurrentWidget(widgets.img_contrast)
            widgets.selected_image_filter.setPixmap(QtGui.QPixmap(self.resized_image_331))

        if btnName == "half_brightness_btn":
            Image_Customization.apply_contrast_to_images(self, "brightness","half", widgets)

        if btnName == "double_brightness_btn":
            Image_Customization.apply_contrast_to_images(self, "brightness","double", widgets)

        if btnName == "zero_sharpness_btn":
            Image_Customization.apply_contrast_to_images(self, "sharpness","half", widgets)

        if btnName == "double_sharpness_btn":
            Image_Customization.apply_contrast_to_images(self, "sharpness","double", widgets)

        if btnName == "half_contrast_btn":
            Image_Customization.apply_contrast_to_images(self, "contrast","half", widgets)

        if btnName == "double_contrast_btn":
            Image_Customization.apply_contrast_to_images(self, "contrast","double", widgets)

        if btnName == "half_color_btn":
            Image_Customization.apply_contrast_to_images(self, "color","half", widgets)

        if btnName == "double_color_btn":
            Image_Customization.apply_contrast_to_images(self, "color","double", widgets)

        if btnName == "style_image_btn":
            widgets.stackedWidget_img_cutom.setCurrentWidget(widgets.img_styling)
            widgets.selected_image_content.setPixmap(widgets.selected_image.pixmap())
            widgets.selected_style_image.setPixmap(widgets.selected_image.pixmap())

        if btnName == "select_style_img_btn":
            Image_Customization.select_style_image(self,widgets)

        if btnName == "draw_image_btn":
            widgets.stackedWidget_img_cutom.setCurrentWidget(widgets.draw_on_image)
            widgets.selected_image_filter_6.setPixmap(QtGui.QPixmap(self.resized_image_331))

        if btnName == "use_pen_btn":
            threading.Thread(target=DrawWindow.setmap,args=[self,"pen"]).start()
            window = DrawWindow()
            window.show()

        if btnName == "use_brush_btn":
            threading.Thread(target=DrawWindow.setmap, args=[self, "brush"]).start()
            window = DrawWindow()
            window.show()

        if btnName == "crop_image_btn":
            widgets.stackedWidget_img_cutom.setCurrentWidget(widgets.crop_image)
            widgets.selected_image_filter_5.setPixmap(QtGui.QPixmap(self.resized_image_331))

        if btnName == "apply_crop_btn":
            threading.Thread(target=Image_Customization.crop_image,args=[self, widgets]).start()

        if btnName == "translate_image_btn":
            widgets.stackedWidget_img_cutom.setCurrentWidget(widgets.image_translation)

        if btnName == "edge_detect_image_btn":
            widgets.stackedWidget_img_cutom.setCurrentWidget(widgets.edge_detection)
            widgets.selected_image_filter_3.setPixmap(QtGui.QPixmap(self.resized_image_331))

        if btnName == "detect_edges_2_btn":
            Image_Customization.detect_edges(self,"sigma-2",widgets)

        if btnName == "detect_edges_5_btn":
            Image_Customization.detect_edges(self, "sigma-5", widgets)

        if btnName == "detect_rough_edges_btn":
            Image_Customization.detect_edges(self, "rough", widgets)

        if btnName == "rotate_image_btn":
            widgets.stackedWidget_img_cutom.setCurrentWidget(widgets.rotate_image)
            widgets.selected_image_filter_4.setPixmap(QtGui.QPixmap(self.resized_image_331))
            self.rotation_process = True
            threading.Thread(target=Image_Customization.rotate_image,
                             args=[self,widgets]).start()

        if btnName == "save_changes_image_btn":
            Image_Customization.save_changes_on_image(self,widgets)

        if btnName == "store_image_btn":
            Image_Customization.store_customized_image(self,widgets)

        if btnName == "changes_success_ok_btn":
            widgets.img_cutom_widget.lower()
            widgets.changes_success_notification.lower()

        if btnName == "store_success_ok_btn":
            widgets.img_cutom_widget.lower()
            widgets.store_success_notification.lower()

        if btnName == "open_cutomized_image_btn":
            MainWindow.open_image(self, QtGui.QPixmap(self.original_image))

        if btnName == "open_cutomized_image_btn_2":
            MainWindow.open_image(self, QtGui.QPixmap(self.customized_image))

        if btnName == "open_cutomized_image_btn_3":
            MainWindow.open_image(self, QtGui.QPixmap(self.customized_image))

        if btnName == "open_cutomized_image_btn_4":
            Image_Customization.select_mask_image(self,widgets)

        if btnName == "open_cutomized_image_btn_5":
            MainWindow.open_image(self, QtGui.QPixmap(self.customized_image))

        if btnName == "open_cutomized_image_btn_6":
            MainWindow.open_image(self, QtGui.QPixmap(self.customized_image))

        if btnName == "open_cutomized_image_btn_7":
            MainWindow.open_image(self, QtGui.QPixmap(self.customized_image))

        if btnName == "open_cutomized_image_btn_8":
            MainWindow.open_image(self, QtGui.QPixmap(self.customized_image))

        if btnName == "apply_mask_btn":
            widgets.style_img_result.setPixmap(QtGui.QPixmap(self.customized_image_331))
            widgets.style_result_label.raise_()
            widgets.style_img_result_cross_btn.raise_()
            widgets.style_img_result.raise_()
            widgets.style_img_result_btn.raise_()
            widgets.bitwise_not_btn.raise_()
            widgets.blacknwhite_btn.raise_()
            widgets.bitwise_or_btn.raise_()
            widgets.bitwise_and_btn.raise_()
            widgets.bitwise_xor_btn.raise_()

        if btnName == "bitwise_or_btn":
            Image_Customization.apply_mask(self,"or",widgets)

        if btnName == "bitwise_and_btn":
            Image_Customization.apply_mask(self, "and", widgets)

        if btnName == "bitwise_xor_btn":
            Image_Customization.apply_mask(self, "xor", widgets)

        if btnName == "bitwise_not_btn":
            Image_Customization.apply_mask(self, "not", widgets)

        if btnName == "blacknwhite_btn":
            Image_Customization.apply_mask(self, "black_white", widgets)

        if btnName == "blend_image_btn":
            widgets.style_result_label.raise_()
            widgets.style_img_result_cross_btn.raise_()
            widgets.style_img_result.raise_()
            widgets.style_img_result_btn.raise_()
            widgets.blend_image_slider.raise_()
            widgets.label_291.raise_()
            widgets.label_290.raise_()
            self.blending = True
            threading.Thread(target=Image_Customization.blend_images,
                             args=[self, widgets]).start()

        if btnName == "style_img_result_btn":
            MainWindow.open_image(self, QtGui.QPixmap(self.customized_image))

        if btnName == "style_img_result_cross_btn":
            self.blending = False
            self.blender_image_331 = self.customized_image_331
            self.blender_image = self.customized_image
            self.mask_image_331 = self.customized_image_331
            self.mask_image = self.customized_image
            self.customized_image_331 = self.resized_image_331
            self.customized_image = self.original_image
            widgets.style_img_result_cross_btn.lower()
            widgets.style_img_result.lower()
            widgets.style_img_result_btn.lower()
            widgets.blend_image_slider.lower()
            widgets.label_291.lower()
            widgets.label_290.lower()
            widgets.style_result_label.lower()
            widgets.bitwise_or_btn.lower()
            widgets.bitwise_and_btn.lower()
            widgets.bitwise_xor_btn.lower()
            widgets.bitwise_not_btn.lower()
            widgets.blacknwhite_btn.lower()

        if btnName == "translated_image_btn":
            MainWindow.open_image(self, QtGui.QPixmap(self.customized_image))

        if btnName == "translate_new_btn":
            self.translation_process = True
            widgets.stackedWidget_content_pages.setCurrentWidget(widgets.stylegan_page)
            widgets.stackedWidget_stylegan.setCurrentWidget(widgets.google_account_page)

        if btnName == "apply_translation_btn":
            self.translation_process = True
            widgets.stackedWidget_content_pages.setCurrentWidget(widgets.stylegan_page)
            widgets.stackedWidget_stylegan.setCurrentWidget(widgets.google_account_page)

        if btnName == "back_to_img_custom_btn":
            if widgets.stackedWidget_img_cutom.currentWidget() == widgets.img_custom_home:
                widgets.stackedWidget_content_pages.setCurrentWidget(widgets.generated_images_page)
            else:
                self.rotation_process = False
                widgets.stackedWidget_img_cutom.setCurrentWidget(widgets.img_custom_home)
                widgets.selected_image.setPixmap(QtGui.QPixmap(self.resized_image_331))
                self.customized_image_331 = self.resized_image_331
                self.customized_image = self.original_image

        # Print Pressed Button
        print(f'Button "{btnName}" pressed!')

    # Resizing the Events
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # Mouse Click Events Settings
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

# MAIN Function of the Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
