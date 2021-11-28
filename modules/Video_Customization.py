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

# Imports from MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *

# Video_Customization Class
# ///////////////////////////////////////////////////////////////
class Video_Customization(MainWindow):

    def choose_images(self,widgets):
        # path = "C://Users//SYS//Downloads//AI Images//"
        # files = QFileDialog.getOpenFileNames(
        #     self, "Select the file to add", path, "source File (*.png *.jpeg)",
        #     options=QFileDialog.DontUseNativeDialog
        # )
        widgets.seleted_db_images_widget.raise_()
        # clearing all the rows of the generated images table Widget
        widgets.tableWidget_generated_images_selection.setRowCount(0)
        # setting starting row position
        rowPosition = 0
        # for every output document present in the database
        for output in output_images.find():
            # Inserting the first row in the Qtable Widget
            widgets.tableWidget_generated_images_selection.insertRow(rowPosition)
            # load image from the pickle module
            image = pickle.loads(output["image"])
            # destructing height, width and channel variables from the shape property of the image
            height, width, channel = image.shape
            # setting bytes per line
            bytesPerLine = 3 * width
            # generating a rgbSwapped Qimage from the image data
            qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            # Converting Qimage to pixmap
            pix = QtGui.QPixmap(qImg)
            # Converting the output item pixmap data to Qicon for Qtable list view
            i = PySide6.QtGui.QIcon(pix)
            image_icon = QTableWidgetItem()
            image_icon.setIcon(i)
            # Set Output item data in the table row according to specified columns
            widgets.tableWidget_generated_images_selection.setItem(rowPosition, 0, QTableWidgetItem(image_icon))
            widgets.tableWidget_generated_images_selection.setItem(rowPosition, 1, QTableWidgetItem(output["name"]))
            widgets.tableWidget_generated_images_selection.setItem(rowPosition, 2, QTableWidgetItem(output["generated_at"]))
            # increment rowPosition
            rowPosition = rowPosition + 1

    def set_selected_images(self,widgets):
        seleted_images = widgets.tableWidget_generated_images_selection.selectionModel().selectedRows()
        print(seleted_images)
        for ix in seleted_images:
            print(ix.row())

        widgets.no_images_selected.lower()
        # clearing all the rows of the generated images table Widget
        widgets.tableWidget_selected_images_for_videos.setRowCount(0)
        # setting starting row position
        rowPosition = 0

        for selected_image in seleted_images:

            image_icon = widgets.tableWidget_generated_images_selection.item(selected_image.row(), 0)
            image_name = widgets.tableWidget_generated_images_selection.item(selected_image.row(), 1)
            print(image_icon)
            print(image_name)
            widgets.tableWidget_selected_images_for_videos.insertRow(rowPosition)

            widgets.tableWidget_selected_images_for_videos.setItem(rowPosition, 0, QTableWidgetItem(image_icon))
            widgets.tableWidget_selected_images_for_videos.setItem(rowPosition, 1, QTableWidgetItem(image_name))
            # increment rowPosition
            rowPosition = rowPosition + 1

    def open_selected_list_image(self, widgets):
        # set initial counter
        i = 0
        # Using try/except blocks for exception handling
        # try block
        try:
            # for every output document present in the database of the specified user
            for gen_image in output_images.find({"name": {'$regex': ".png$"}}):
                # checking if the current output is selected in the Qtable list
                if (widgets.tableWidget_selected_images_for_videos.item(i, 0)).isSelected():
                    # load image from the pickle module
                    image = pickle.loads(gen_image["image"])
                    # destructing height, width and channel variables from the shape property of the image
                    height, width, channel = image.shape
                    # setting bytes per line
                    bytesPerLine = 3 * width
                    # generating a rgbSwapped Qimage from the image data
                    qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                    # Converting Qimage to pixmap
                    pix = QtGui.QPixmap(qImg)
                    # calling function to open the image on CV2 viewer
                    MainWindow.open_image(self, pix)
                    # break the loop
                    break
                # incrementing the counter
                i = i + 1
        # except block
        except:
            pass

    def create_video(self,widgets):

        # first take all selected images
        # retrieve all selected images from database
        # put in numpy array
        # set initial counter
        i = 0
        images_names = []
        images = []
        # Using try/except blocks for exception handling

        # for every output document present in the database of the specified user
        for gen_image in output_images.find({"name": {'$regex': ".png$"}}):

            # checking if the current output is selected in the Qtable list
            for i in range(widgets.tableWidget_selected_images_for_videos.rowCount()):
                if (widgets.tableWidget_selected_images_for_videos.item(i, 1)).text() == gen_image["name"]:
                    name = widgets.tableWidget_selected_images_for_videos.item(i, 1).text()

                    # # load image from the pickle module
                    image = pickle.loads(gen_image["image"])
                    exists = name in images_names
                    if (exists == False):
                        print(name)
                    images.append(image)
                    # break the loop
                    break

        # pass through pymovie function
        video_name = 'video.avi'

        frame = images[0]
        height, width, layers = frame.shape

        video = cv2.VideoWriter(video_name, 0, 1, (width, height))

        # save video
        for image in images:
            video.write(image)

        # save video to database


    def view_video(self,widgets):

        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # create videowidget object
        videowidget = QVideoWidget()

        # create open button
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)

        # create button for playing
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        # create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        # create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0, 0, 0, 0)

        # set widgets to the hbox layout
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)

        # create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)

        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(videowidget)

        # media player signals
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def flip_video(self):
        pass

    def change_video_fps(self):
        pass

    def reverse_video(self):
        pass

    def get_frames(self):
        pass

    def crop_video(self):
        pass

    def apply_effects(self):
        pass

    def rotate_video(self):
        pass

    def save_changes_to_video(self):
        pass

    def reset_changes_to_video(self):
        pass

    def export_video(self):
        pass