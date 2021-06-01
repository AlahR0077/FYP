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

# Datasets Class
# ///////////////////////////////////////////////////////////////
class Datasets(MainWindow):

    # Function to Load Datasets Thumbnails
    # ///////////////////////////////////////////////////////////////
    def load_datasets_thumbs(self, widgets):
        # set initial counter
        i = 1
        # for every dataset document present in the database
        for document in datasets.find():
            # Using try/except for exception handling (if any)
            try:
                # load image from the pickle module
                image = pickle.loads(document["thumbnail"])
                # destructing height, width and channel variables from the shape property of the image
                height, width, channel = image.shape
                # setting bytes per line
                bytesPerLine = 3 * width
                # generating a rgbSwapped Qimage from the image data
                qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                # Converting Qimage to pixmap
                pix = QtGui.QPixmap(qImg)
            # except block
            except:
                # get image bytes data from the database
                image = document["thumbnail"]
                # converting bytes data to pixmap for displaying image as a Qwidget
                pix = MainWindow.convert_bytes_to_pixmap(self, image)
            # if counter is set to 1
            if i == 1:
                # set the human dataset thumbnail
                widgets.human_thumbnail.setPixmap(pix)
                widgets.human_thumbnail_2.setPixmap(pix)
            elif i == 2:
                # set the anime dataset thumbnail
                widgets.anime_thumbnail.setPixmap(pix)
                widgets.anime_thumbnail_2.setPixmap(pix)
            elif i == 3:
                # set the flower dataset thumbnail
                widgets.flower_thumbnail.setPixmap(pix)
                widgets.flower_thumbnail_2.setPixmap(pix)
            # incrementing the counter
            i = i + 1
        return


    # Function to Load Human Dataset Images
    # ///////////////////////////////////////////////////////////////
    def load_human_dataset_imgs(self, widgets):
        # finding human dataset document in the database collection
        human_doc = datasets.find_one({"name": "human"})
        # set initial counter
        i = 1
        # for every image in images Array
        for img in human_doc["images"]:
            # load image from the pickle module
            image = pickle.loads(img)
            # destructing height, width and channel variables from the shape property of the image
            height, width, channel = image.shape
            # setting bytes per line
            bytesPerLine = 3 * width
            # generating a rgbSwapped Qimage from the image data
            qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            # Converting Qimage to pixmap
            pix = QtGui.QPixmap(qImg)
            # if counter is set to 1
            if i == 1:
                # set human_image_1 to view
                widgets.human_image_1.setPixmap(pix)
            elif i == 2:
                # set human_image_2 to view
                widgets.human_image_2.setPixmap(pix)
            elif i == 3:
                # set human_image_3 to view
                widgets.human_image_3.setPixmap(pix)
            elif i == 4:
                # set human_image_4 to view
                widgets.human_image_4.setPixmap(pix)
            elif i == 5:
                # set human_image_5 to view
                widgets.human_image_5.setPixmap(pix)
            elif i == 6:
                # set human_image_6 to view
                widgets.human_image_6.setPixmap(pix)
            # incrementing the counter
            i = i + 1
        return


    # Function to Load Anime Dataset Images
    # ///////////////////////////////////////////////////////////////
    def load_anime_dataset_imgs(self, widgets):
        # finding anime dataset document in the database collection
        anime_doc = datasets.find_one({"name": "anime"})
        # set initial counter
        i = 1
        # for every image in images Array
        for img in anime_doc["images"]:
            # load image from the pickle module
            image = pickle.loads(img)
            # destructing height, width and channel variables from the shape property of the image
            height, width, channel = image.shape
            # setting bytes per line
            bytesPerLine = 3 * width
            # generating a rgbSwapped Qimage from the image data
            qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            # Converting Qimage to pixmap
            pix = QtGui.QPixmap(qImg)
            # if counter is set to 1
            if i == 1:
                # set anime_image_1 to view
                widgets.anime_image_1.setPixmap(pix)
            elif i == 2:
                # set anime_image_2 to view
                widgets.anime_image_2.setPixmap(pix)
            elif i == 3:
                # set anime_image_3 to view
                widgets.anime_image_3.setPixmap(pix)
            elif i == 4:
                # set anime_image_4 to view
                widgets.anime_image_4.setPixmap(pix)
            elif i == 5:
                # set anime_image_5 to view
                widgets.anime_image_5.setPixmap(pix)
            elif i == 6:
                # set anime_image_6 to view
                widgets.anime_image_6.setPixmap(pix)
            # incrementing the counter
            i = i + 1
        return


    # Function to Load Flower Dataset Images
    # ///////////////////////////////////////////////////////////////
    def load_flower_dataset_imgs(self, widgets):
        # finding flower dataset document in the database collection
        flower_doc = datasets.find_one({"name": "flower"})
        # set initial counter
        i = 1
        # for every image in images Array
        for img in flower_doc["images"]:
            # load image from the pickle module
            image = pickle.loads(img)
            # destructing height, width and channel variables from the shape property of the image
            height, width, channel = image.shape
            # setting bytes per line
            bytesPerLine = 3 * width
            # generating a rgbSwapped Qimage from the image data
            qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            # Converting Qimage to pixmap
            pix = QtGui.QPixmap(qImg)
            # if counter is set to 1
            if i == 1:
                # set flower_image_1 to view
                widgets.flower_image_1.setPixmap(pix)
            elif i == 2:
                # set flower_image_2 to view
                widgets.flower_image_2.setPixmap(pix)
            elif i == 3:
                # set flower_image_3 to view
                widgets.flower_image_3.setPixmap(pix)
            elif i == 4:
                # set flower_image_4 to view
                widgets.flower_image_4.setPixmap(pix)
            elif i == 5:
                # set flower_image_5 to view
                widgets.flower_image_5.setPixmap(pix)
            elif i == 6:
                # set flower_image_6 to view
                widgets.flower_image_6.setPixmap(pix)
            # incrementing the counter
            i = i + 1
        return


    # Function to Create a New Custom Dataset
    # ///////////////////////////////////////////////////////////////
    def create_dataset(self, widgets):
        # getting the new dataset name
        dataset_name = widgets.new_dtset_name.text()
        # getting the uploaded images of the new dataset to store in the database
        image_0_pix = widgets.new_dst_u_image_0.pixmap()
        image_1_pix = widgets.new_dst_u_image_1.pixmap()
        image_2_pix = widgets.new_dst_u_image_2.pixmap()
        image_3_pix = widgets.new_dst_u_image_3.pixmap()
        image_4_pix = widgets.new_dst_u_image_4.pixmap()
        image_5_pix = widgets.new_dst_u_image_5.pixmap()
        # getting the new database size
        dataset_size = str(widgets.select_dst_size.currentText())
        # if the dataset name already exists => throw an error
        if dataset_name == "" or datasets.find_one({"name": dataset_name}) != None:
            # return not created
            return "dataset not created"
        # converting the pixmap data of images to bytes form for the database storage purpose
        image_0 = MainWindow.convert_pixmap_to_bytes(self, image_0_pix)
        image_1 = MainWindow.convert_pixmap_to_bytes(self, image_1_pix)
        image_2 = MainWindow.convert_pixmap_to_bytes(self, image_2_pix)
        image_3 = MainWindow.convert_pixmap_to_bytes(self, image_3_pix)
        image_4 = MainWindow.convert_pixmap_to_bytes(self, image_4_pix)
        image_5 = MainWindow.convert_pixmap_to_bytes(self, image_5_pix)
        # inserting the new database document in the database
        datasets.insert_one({"name": dataset_name, "thumbnail": image_0, "size": dataset_size, "images": []})
        # updating new dataset images in the images Array
        datasets.update_many({"name": dataset_name},
                             {"$set": {"images": [image_0, image_1, image_2, image_3, image_4, image_5]}})
        # return created
        return "dataset created"


    # Function to Load a Newly Created Dataset
    # ///////////////////////////////////////////////////////////////
    def load_new_dataset(self, widgets):
        # Using try/catch for any exceptions
        # try block
        try:
            # sorting the dataset documents in reverse to get newly created dataset document
            new_doc = datasets.find().sort("_id", -1).limit(1)
            # getting the newly created dataset document
            for doc in new_doc:
                # setting the labels text with the new dataset name
                widgets.new_dataset_name.setText(doc["name"])
                widgets.label_new_dataset.setText(doc["name"])
                widgets.label_new_dataset_2.setText(doc["name"])
                # set initial counter
                i = 1
                # for every image in images Array
                for img in doc["images"]:
                    # converting the bytes data to pixmap for displaying the results on PyQt Widget
                    pix = MainWindow.convert_bytes_to_pixmap(self, img)
                    # if counter is set to 1
                    if i == 1:
                        # setting the widgets with new dataset thumbnail
                        widgets.new_datset_thumbnail.setPixmap(pix)
                        widgets.new_datset_thumbnail_2.setPixmap(pix)
                        # set new_dst_image_1 to view
                        widgets.new_dst_image_1.setPixmap(pix)
                    # if counter is set to 2
                    elif i == 2:
                        # set new_dst_image_2 to view
                        widgets.new_dst_image_2.setPixmap(pix)
                    # if counter is set to 3
                    elif i == 3:
                        # set new_dst_image_3 to view
                        widgets.new_dst_image_3.setPixmap(pix)
                    # if counter is set to 4
                    elif i == 4:
                        # set new_dst_image_4 to view
                        widgets.new_dst_image_4.setPixmap(pix)
                    # if counter is set to 5
                    elif i == 5:
                        # set new_dst_image_5 to view
                        widgets.new_dst_image_5.setPixmap(pix)
                    # if counter is set to 6
                    elif i == 6:
                        # set new_dst_image_6 to view
                        widgets.new_dst_image_6.setPixmap(pix)
                    # incrementing the counter
                    i = i + 1
            # return loaded
            return 'new dataset loaded'
        # except block
        except:
            # return not loaded
            return 'new dataset not loaded'


    # Function to Add Image to a Dataset
    # ///////////////////////////////////////////////////////////////
    def add_image_to_dataset(self, widgets):
        # getting the pixmap of the new image to be added
        pix = widgets.new_dst_image_6.pixmap()
        # converting the new image pixmap data to bytes form for the database storage purpose
        new_image = MainWindow.convert_pixmap_to_bytes(self, pix)
        # sorting the dataset documents in reverse to get newly created dataset document
        new_doc = datasets.find().sort("_id", -1).limit(1)
        # try block
        try:
            # getting the newly created dataset document
            for doc in new_doc:
                # add the new image in images Array of the document
                datasets.update_one({"name": doc["name"]}, {"$push": {"images": new_image}})
                # break the loop
                break
            # return added
            return 'image added'
        # except block
        except:
            # return not added
            return 'image not added'


    # Function to Delete the Created Dataset
    # ///////////////////////////////////////////////////////////////
    def delete_new_dataset(self):
        # sorting the dataset documents in reverse to get newly created dataset document
        new_doc = datasets.find().sort("_id", -1).limit(1)
        # try block
        try:
            # getting the newly created dataset document
            for doc in new_doc:
                # delete the new created dataset document
                datasets.delete_one({"name": doc["name"]})
                # break the loop
                break
            # return deleted
            return 'dataset deleted'
        # except block
        except:
            # return unable to delete
            return 'unable to delete'

    # Function to Search the Created Dataset
    # ///////////////////////////////////////////////////////////////
    def search_dataset(self, dataset_name, widgets):
        # finding the dataset doc in the database by the specified name
        dataset_doc = datasets.find_one({"name": dataset_name})
        # if the document exists
        if dataset_doc != None:
            # converting the thumbnail bytes data to pixmap form for displaying it on a QWidget
            dst_thumb = MainWindow.convert_bytes_to_pixmap(self, dataset_doc["thumbnail"])
            # getting the dataset name
            dst_name = dataset_doc["name"]
            # getting the dataset size
            dst_size = dataset_doc["size"]
            # setting the Searched dataset thumbnail to searched widget
            widgets.searched_dst_thumbnail.setPixmap(dst_thumb)
            widgets.searched_dst_thumbnail_2.setPixmap(dst_thumb)
            # setting the searched dataset name to searched widget
            widgets.searched_dst_name.setText(dst_name)
            widgets.searched_dst_name_2.setText(dst_name)
            # setting the searched dataset size to searched widget
            widgets.searched_dst_size.setText(dst_size)
            widgets.searched_dst_size_2.setText(dst_size)
            # return search success
            return "dst search success"
        # if the dataset document doesn't exists
        elif dataset_doc == None:
            # return search fail
            return "dst search fail"


    # Function to Load the Searched Dataset
    # ///////////////////////////////////////////////////////////////
    def load_searched_dataset(self, widgets):
        # getting the name of the searched dataset
        dst_name = widgets.searched_dst_name.text()
        # setting the dataset name label on searched dataset page with the searched dataset name
        widgets.new_dataset_name_2.setText(dst_name)
        # finding the searched dataset document with the dataset name
        dst_doc = datasets.find_one({"name": dst_name})
        # try block
        try:
            # set initial counter
            i = 1
            # getting the images from the dataset document
            for img in dst_doc:
                # converting the IMAGE bytes data to pixmap form for displaying it on a QWidget
                pix = MainWindow.convert_bytes_to_pixmap(self, img)
                # if counter is set to 1
                if i == 1:
                    # setting the first image of searched dataset
                    widgets.new_dst_image_7.setPixmap(pix)
                elif i == 2:
                    # setting the second image of searched dataset
                    widgets.new_dst_image_8.setPixmap(pix)
                elif i == 3:
                    # setting the third image of searched dataset
                    widgets.new_dst_image_9.setPixmap(pix)
                elif i == 4:
                    # setting the fourth image of searched dataset
                    widgets.new_dst_image_10.setPixmap(pix)
                elif i == 5:
                    # setting the fifth image of searched dataset
                    widgets.new_dst_image_11.setPixmap(pix)
                elif i == 6:
                    # setting the sixth image of searched dataset
                    widgets.new_dst_image_12.setPixmap(pix)
                # incrementing the counter
                i = i + 1
            return
        # except block
        except:
            return


    # Function to Add Image to a Searched Dataset
    # ///////////////////////////////////////////////////////////////
    def add_image_to_searched_dataset(self, widgets):
        # getting the pixmap of the new image to be added
        pix = widgets.new_dst_image_12.pixmap()
        # converting the new image pixmap data to bytes form for the database storage purpose
        new_image = MainWindow.convert_pixmap_to_bytes(self, pix)
        # getting the searched dataset name
        dst_name = widgets.searched_dst_name.text()
        # try block
        try:
            # add the new image in images Array of the document
            datasets.update_one({"name": dst_name}, {"$push": {"images": new_image}})
            # return added
            return 'image added'
        # except block
        except:
            # return not added
            return 'image not added'


    # Function to Delete the Searched Dataset
    # ///////////////////////////////////////////////////////////////
    def delete_searched_dataset(self, widgets):
        # getting the searched dataset name
        dst_name = widgets.searched_dst_name.text()
        # try/except block for catching exceptions
        try:
            # delete the seached dataset document from the dataset database collection
            datasets.delete_one({"name": dst_name})
            # return deleted
            return 'dataset deleted'
        # except block
        except:
            # unable to delete
            return 'unable to delete'


    # Function to Activate the Dataset Search for every 6 seconds delay
    # ///////////////////////////////////////////////////////////////
    def dataset_search_activate(self, widgets):
        # if the datasets page is open
        if (
                widgets.datsets_stackedWidget.currentWidget() == widgets.create_dataset_page and widgets.stackedWidget_content_pages.currentWidget() == widgets.datasets_page) or (
                widgets.stackedWidget_model_training.currentWidget() == widgets.select_dataset_page and widgets.stackedWidget_content_pages.currentWidget() == widgets.model_training_page):
            # if the dataset search text is not empty
            if widgets.search_dataset.text() != "" or widgets.search_dataset_2.text() != "":
                # if searching dataset in the first dataset page
                if widgets.search_dataset.text() != "":
                    # calling the search function with entered dataset name to be searched
                    dst_search_1 = Datasets.search_dataset(self, widgets.search_dataset.text(), widgets)
                    # if search success is returned
                    if dst_search_1 == "dst search success":
                        # setting the input to "" after performing search
                        widgets.search_dataset.setText("")
                        # raise the found dataset widget
                        widgets.dataset_found_widget.raise_()
                        return
                    # if search fail is returned
                    elif dst_search_1 == "dst search fail":
                        # setting the input to "" after performing search
                        widgets.search_dataset.setText("")
                        # raise the not found dataset widget
                        widgets.dataset_not_found_widget.raise_()
                        return
                # if searching dataset in the second dataset page
                elif widgets.search_dataset_2.text() != "":
                    # calling the search function with entered dataset name to be searched
                    dst_search_2 = Datasets.search_dataset(self, widgets.search_dataset_2.text(), widgets)
                    # if search success is returned
                    if dst_search_2 == "dst search success":
                        # setting the input to "" after performing search
                        widgets.search_dataset_2.setText("")
                        # raise the found dataset widget
                        widgets.dataset_found_widget_2.raise_()
                        return
                    # if search fail is returned
                    elif dst_search_2 == "dst search fail":
                        # setting the input to "" after performing search
                        widgets.search_dataset_2.setText("")
                        # raise the not found dataset widget
                        widgets.dataset_not_found_widget_2.raise_()
                        return
                # printing searching message on the console
                print("searching...")
            # if the dataset search text is empty
            elif widgets.search_dataset.text() == "":
                # printing not searching message on the console
                print("not searching...")