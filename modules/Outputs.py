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

# Outputs Class
# ///////////////////////////////////////////////////////////////
class Outputs(MainWindow):

    # Function to remove a specified Favourite item from the database
    # ///////////////////////////////////////////////////////////////
    def remove_favourite(self, user_name, item,widgets):
        # try block
        try:
            # Converting favourite item from pixmap to bytes data for database query retrieval
            item_in_bytes = MainWindow.convert_pixmap_to_bytes(self,item)
            # deleting the favourite item from the database
            users_favourites.delete_one({"user_name": user_name, "item" : item_in_bytes})
            # clearing the favourites table widget
            widgets.tableWidget_my_favourites.setRowCount(0)
            # reloading the updated favourite docs from the database
            User_Profile.load_myfavourites(self,user_name,widgets)
            print ("favourite removed successfully")
            return
        # except block
        except:
            print("favourite unable to be removed")
            return

    # Function to update the Favourite items in the database by adding a favourite
    # ///////////////////////////////////////////////////////////////
    def update_myfavourites(self, user_name, item, category,widgets):
        # getting the current date
        now = datetime.now()
        # formatting the date
        date = now.strftime("%d/%m/%Y");
        # try block
        try:
            # Converting favourite item from pixmap to bytes data for database storage purpose
            item_in_bytes = MainWindow.convert_pixmap_to_bytes(self,item)
            # Converting the favourite item pixmap data to Qicon for Qtable list view
            i = PySide6.QtGui.QIcon(item)
            item_icon =  QTableWidgetItem()
            item_icon.setIcon(i)
            # inserting the specified favourite of a specified user item in the database
            users_favourites.insert_one({"user_name": user_name, "item": item_in_bytes , "category" : category, "favourite_since": date})
            # Counting the table rows
            rowPosition = widgets.tableWidget_my_favourites.rowCount()
            # Insert new row in the table
            widgets.tableWidget_my_favourites.insertRow(rowPosition)
            # Set Favourite data in the table row according to specified columns
            widgets.tableWidget_my_favourites.setItem(rowPosition, 0, QTableWidgetItem(item_icon))
            widgets.tableWidget_my_favourites.setItem(rowPosition, 1, QTableWidgetItem(category))
            widgets.tableWidget_my_favourites.setItem(rowPosition, 2, QTableWidgetItem(date))
            print ("favourites updated successfully")
            return
        # except block
        except:
            print("favourite unable to be updated")
            return

    # Function to load the Make/Remove Favourite Buttons
    # ///////////////////////////////////////////////////////////////
    def load_favourite_btns(self, user_name,widgets):
        # Initially show all the Make Favourite Buttons with the outputs
        widgets.make_fav1_btn.show()
        widgets.make_fav2_btn.show()
        widgets.make_fav3_btn.show()
        widgets.make_fav4_btn.show()
        widgets.make_fav5_btn.show()
        widgets.make_fav6_btn.show()
        # Using Try/Except Blocks for catching Exceptions (if Any)
        try:
            try:
                # output_image_1 pixmap data to bytes for database query
                output_image_1 = MainWindow.convert_pixmap_to_bytes(self, widgets.output_image_1.pixmap())
            except:
                pass

            try:
                # output_image_2 pixmap data to bytes for database query
                output_image_2 = MainWindow.convert_pixmap_to_bytes(self, widgets.output_image_2.pixmap())
            except:
                pass
            try:
                # output_image_3 pixmap data to bytes for database query
                output_image_3 = MainWindow.convert_pixmap_to_bytes(self, widgets.output_image_3.pixmap())
            except:
                pass
            try:
                # output_image_4 pixmap data to bytes for database query
                output_image_4 = MainWindow.convert_pixmap_to_bytes(self, widgets.output_image_4.pixmap())
            except:
                pass
            try:
                # output_image_5 pixmap data to bytes for database query
                output_image_5 = MainWindow.convert_pixmap_to_bytes(self, widgets.output_image_5.pixmap())
            except:
                pass
            try:
                # output_image_6 pixmap data to bytes for database query
                output_image_6 = MainWindow.convert_pixmap_to_bytes(self, widgets.output_image_6.pixmap())
            except:
                pass

            # finding all the favourites docs of the current User
            for favourite in users_favourites.find({"user_name": user_name}):
                # getting the favourite item
                item = favourite["item"]
                # Using Try/Except Blocks for catching Exceptions (if Any)
                try:
                    # if output_image_1 is already set to favourites
                    if output_image_1 == item:
                        # hide make favourite button
                        widgets.make_fav1_btn.hide()
                        # show remove favourite button
                        widgets.remove_fav1_btn.show()
                except:
                    pass
                try:
                    # if output_image_2 is already set to favourites
                    if output_image_2 == item:
                        # hide make favourite button
                        widgets.make_fav2_btn.hide()
                        # show remove favourite button
                        widgets.remove_fav2_btn.show()
                except:
                    pass
                try:
                    # if output_image_3 is already set to favourites
                    if output_image_3 == item:
                        # hide make favourite button
                        widgets.make_fav3_btn.hide()
                        # show remove favourite button
                        widgets.remove_fav3_btn.show()
                except:
                    pass
                try:
                    # if output_image_4 is already set to favourites
                    if output_image_4 == item:
                        # hide make favourite button
                        widgets.make_fav4_btn.hide()
                        # show remove favourite button
                        widgets.remove_fav4_btn.show()
                except:
                    pass
                try:
                    # if output_image_5 is already set to favourites
                    if output_image_5 == item:
                        # hide make favourite button
                        widgets.make_fav5_btn.hide()
                        # show remove favourite button
                        widgets.remove_fav5_btn.show()
                except:
                    pass
                try:
                    # if output_image_6 is already set to favourites
                    if output_image_6 == item:
                        # hide make favourite button
                        widgets.make_fav6_btn.hide()
                        # show remove favourite button
                        widgets.remove_fav6_btn.show()
                except:
                    pass
            # printing success message on console
            print ("favourite btns loaded successfully")
            return
        except:
            # printing fail message on console
            print("favourite btns not loaded successfully")
            return

    # Function to load the Output Images Thumbnails
    # ///////////////////////////////////////////////////////////////
    def load_output_images_thumbs(self,widgets):
        # set counter
        i=1
        # checking if the outputs images are empty or not
        if output_images.find_one({"name": {'$regex':".png$"}}) == None:
                # return if no outputs are present in the database
                return "no outputs"
        # for every output document present in the database
        for document in output_images.find():
            # load image from the pickle module
            image = pickle.loads(document["image"])
            # destructing height, width and channel varables from the shape property of the image
            height, width, channel = image.shape
            # setting bytes per line
            bytesPerLine = 3 * width
            # generating a rgbSwapped Qimage from the image data
            qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            # Converting Qimage to pixmap
            pix = QtGui.QPixmap(qImg)
            # if counter is 1
            if i==1:
                # setting output_image_1 thumbnail
                widgets.output_image_1.setPixmap(pix)
            elif i == 2:
                # setting output_image_2 thumbnail
                widgets.output_image_2.setPixmap(pix)
            elif i == 3:
                # setting output_image_3 thumbnail
                widgets.output_image_3.setPixmap(pix)
            elif i == 4:
                # setting output_image_4 thumbnail
                widgets.output_image_4.setPixmap(pix)
            elif i == 5:
                # setting output_image_5 thumbnail
                widgets.output_image_5.setPixmap(pix)
            elif i == 6:
                # setting output_image_6 thumbnail
                widgets.output_image_6.setPixmap(pix)
            # incrementing counter
            i=i+1
        # returning load success
        return "output loaded success"

    # Function to load the Output Images List View in Qtable
    # ///////////////////////////////////////////////////////////////
    def load_output_images_list(self,widgets):
        # set initial counter
        i=1
        # checking if the outputs images are empty or not
        if output_images.find_one({"name": {'$regex':".png$"}}) == None:
            # return if no outputs are present in the database
            return "no outputs"
        # clearing all the rows of the generated images table Widget
        widgets.tableWidget_generated_images.setRowCount(0)
        # setting starting row position
        rowPosition = 0
        # for every output document present in the database
        for output in output_images.find():
            # Inserting the first row in the Qtable Widget
            widgets.tableWidget_generated_images.insertRow(rowPosition)
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
            widgets.tableWidget_generated_images.setItem(rowPosition, 0, QTableWidgetItem(image_icon))
            widgets.tableWidget_generated_images.setItem(rowPosition, 1, QTableWidgetItem(output["name"]))
            widgets.tableWidget_generated_images.setItem(rowPosition, 2, QTableWidgetItem(output["generated_at"]))
            # increment rowPosition
            rowPosition = rowPosition + 1
        # printing success message on console
        print("output loaded success")
        # return success message
        return "output loaded success"

    # Function to Open the Output Folder having the results
    # ///////////////////////////////////////////////////////////////
    def open_output_folder(self):

        # setting output folder path
        path = "C://Users//SYS//Downloads//AI Images//"
        # openning folder using os module
        path = os.path.realpath(path)
        os.startfile(path)
        return


    # Function to Open Output Image from the Selected Qtable list on the CV2 image Viewer
    # ////////////////////////////////////////////////////////////////////////////////////////
    def open_output_list_image(self, widgets):
        # set initial counter
        i = 0
        # Using try/except blocks for exception handling
        # try block
        try:
            # for every output document present in the database of the specified user
            for gen_image in output_images.find({"name": {'$regex': ".png$"}}):
                # checking if the current output is selected in the Qtable list
                if (widgets.tableWidget_generated_images.item(i, 0)).isSelected():
                    # load image from the pickle module
                    image = pickle.loads(gen_image["image"])
                    # destructing height, width and channel varables from the shape property of the image
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

