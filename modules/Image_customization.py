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
import time

from main import *
from modules.Style_Gan_Model import Style_Gan_Model

# Image_Customization Class
# ///////////////////////////////////////////////////////////////
class Image_Customization(MainWindow):

    def choose_image(self,widgets,x,y):
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
                    original_image = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                    if int(image.shape[0]) < 1000:
                        res = cv2.resize(image, dsize=(int(image.shape[1] * 0.5), int(image.shape[0] * 0.5)), interpolation=cv2.INTER_CUBIC)
                    else:
                        res = cv2.resize(image, dsize=(x, y), interpolation=cv2.INTER_CUBIC)
                    # destructing height, width and channel varables from the shape property of the image
                    height, width, channel = res.shape
                    # setting bytes per line
                    bytesPerLine = 3 * width
                    # generating a rgbSwapped Qimage from the image data
                    resized_image = QImage(res.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                    # break the loop
                    break

                # incrementing the counter
                i = i + 1
            return resized_image,original_image,res,image
        # except block
        except:
            return ''

    def apply_filters(self,filter,widgets):

        resized_image_array_331 = MainWindow.QImageToCvMat(self, self.customized_image_331)
        original_image_array = MainWindow.QImageToCvMat(self, self.customized_image)

        if filter == "mean_filter":
            filter_img_331 = cv2.blur(resized_image_array_331, (5, 5))
            filter_img = cv2.blur(original_image_array, (5, 5))

        elif filter == "gaussian_filter":
            filter_img_331 = cv2.GaussianBlur(resized_image_array_331, (3, 3), 1, 1)
            filter_img = cv2.GaussianBlur(original_image_array, (3, 3), 1, 1)

        elif filter == "bilateral_filter":
            filter_img_331 = cv2.bilateralFilter(resized_image_array_331, 9, 75, 75)
            filter_img = cv2.bilateralFilter(original_image_array, 9, 75, 75)

        elif filter == "median_filter":
            filter_img_331 = cv2.medianBlur(resized_image_array_331, 5)
            filter_img = cv2.medianBlur(original_image_array, 5)

        height, width, channel = filter_img_331.shape
        # setting bytes per line
        bytesPerLine = 3 * width
        # generating a rgbSwapped Qimage from the image data
        self.customized_image_331 = QImage(filter_img_331.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        # setting bytes per line
        height, width, channel = filter_img.shape
        # setting bytes per line
        bytesPerLine = 3 * width
        self.customized_image = QImage(filter_img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        widgets.selected_image_filter_2.setPixmap(QtGui.QPixmap(self.customized_image_331))

    def apply_contrast_to_images(self,effect,intensity,widgets):

        resized_image_array_331 = MainWindow.QImageToCvMat(self, self.customized_image_331)
        original_image_array = MainWindow.QImageToCvMat(self, self.customized_image)

        img = cv2.cvtColor(resized_image_array_331, cv2.COLOR_BGR2RGB)
        img_2 = cv2.cvtColor(original_image_array, cv2.COLOR_BGR2RGB)

        im_pil = Image.fromarray(img)
        im_pil_2 = Image.fromarray(img_2)

        if effect == "brightness":
            converter = ImageEnhance.Brightness(im_pil)
            converter_2 = ImageEnhance.Brightness(im_pil_2)

        elif effect == "sharpness":
            converter = ImageEnhance.Sharpness(im_pil)
            converter_2 = ImageEnhance.Sharpness(im_pil_2)

        elif effect == "contrast":
            converter = ImageEnhance.Contrast(im_pil)
            converter_2 = ImageEnhance.Contrast(im_pil_2)

        elif effect == "color":
            converter = ImageEnhance.Color(im_pil)
            converter_2 = ImageEnhance.Color(im_pil_2)

        if intensity == "half":
                hb = converter.enhance(0.5)
                hb_2 = converter_2.enhance(0.5)

        elif intensity == "double":
                hb = converter.enhance(2)
                hb_2 = converter_2.enhance(2)


        numpy_image = numpy.array(hb)
        opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)

        numpy_image_2 = numpy.array(hb_2)
        opencv_image_2 = cv2.cvtColor(numpy_image_2, cv2.COLOR_RGB2BGR)

        height, width, channel = opencv_image.shape
        # setting bytes per line
        bytesPerLine = 3 * width
        # generating a rgbSwapped Qimage from the image data
        self.customized_image_331 = QImage(opencv_image.data, width, height, bytesPerLine,
                                           QImage.Format_RGB888).rgbSwapped()
        # setting bytes per line
        height, width, channel = opencv_image_2.shape
        # setting bytes per line
        bytesPerLine = 3 * width
        self.customized_image = QImage(opencv_image_2.data, width, height, bytesPerLine,
                                       QImage.Format_RGB888).rgbSwapped()
        widgets.selected_image_filter.setPixmap(QtGui.QPixmap(self.customized_image_331))

    def select_style_image(self, widgets):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Image files (*.jpg *.png)")
        imagePath = fname[0]
        if imagePath != "":
            self.blender_image_array = cv2.imread(imagePath)
            self.blender_image_array_331 = cv2.resize(self.blender_image_array, dsize=(331, 331),
                                                      interpolation=cv2.INTER_CUBIC)
            # destructing height, width and channel varables from the shape property of the image
            height, width, channel = self.blender_image_array_331.shape
            # setting bytes per line
            bytesPerLine = 3 * width
            # generating a rgbSwapped Qimage from the image data
            self.blender_image_331 = QImage(self.blender_image_array_331.data, width, height, bytesPerLine,
                                            QImage.Format_RGB888).rgbSwapped()
            # converting file data to pixmap
            pixmap = QPixmap(self.blender_image_331)
            widgets.selected_style_image.setPixmap(pixmap)

    def detect_edges(self, intensity , widgets):

        resized_image_array_331 = MainWindow.QImageToCvMat(self, self.customized_image_331)
        original_image_array = MainWindow.QImageToCvMat(self, self.customized_image)
        im = resized_image_array_331
        im_2 = original_image_array

        if intensity == "sigma-2":
            edges = cv2.Canny(image=im, threshold1=100, threshold2=200)
            edges_2 = cv2.Canny(image=im_2, threshold1=100, threshold2=200)
        elif intensity == "sigma-5":
            edges = cv2.Canny(image=im, threshold1=200, threshold2=220)
            edges_2 = cv2.Canny(image=im_2, threshold1=200, threshold2=220)
        elif intensity == "rough":
            edges = cv2.Canny(image=im, threshold1=60, threshold2=90)
            edges_2 = cv2.Canny(image=im_2, threshold1=60, threshold2=90)

        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        edges_2 = cv2.cvtColor(edges_2, cv2.COLOR_GRAY2BGR)

        height, width, channel = edges.shape
        # setting bytes per line
        bytesPerLine = 3 * width
        # generating a rgbSwapped Qimage from the image data
        self.customized_image_331 = QImage(edges.data, width, height, bytesPerLine,
                                           QImage.Format_RGB888).rgbSwapped()
        # setting bytes per line
        height, width, channel = edges_2.shape
        # setting bytes per line
        bytesPerLine = 3 * width
        self.customized_image = QImage(edges_2.data, width, height, bytesPerLine,
                                       QImage.Format_RGB888).rgbSwapped()
        widgets.selected_image_filter_3.setPixmap(QtGui.QPixmap(self.customized_image_331))

    def save_changes_on_image(self, widgets):
        self.rotation_process = False
        self.original_image = self.customized_image
        self.resized_image_331 = self.customized_image_331
        self.customized_image = self.original_image
        self.customized_image_331 = self.resized_image_331
        widgets.img_cutom_widget.raise_()
        widgets.changes_success_notification.raise_()

    def store_customized_image(self,widgets):
        images = []
        for gen_image in output_images.find({"name": {'$regex': "^new"}}):
            try:
                images.append(str(gen_image["name"]))
            except:
                pass
        custom_image = len(images)
        new_image_array = MainWindow.QImageToCvMat(self, self.customized_image)
        # Getting local machine time
        t = time.localtime()
        # Formatting time
        current_time = time.strftime("%H:%M:%S", t)
        # Getting current date
        now = datetime.now()
        # Formatting date
        date = now.strftime("%d/%m/%Y");
        # Getting datetime both
        date_time = current_time + " " + date
        # convert numpy array to Binary, store record in mongodb
        rec = Binary(pickle.dumps(new_image_array, protocol=custom_image % 6))
        # storing the output image in the database collection with date time stamp
        output_images.insert_one(
            {"image": rec, "name": f"new_customized_image_{custom_image}.png", "generated_at": date_time})
        widgets.img_cutom_widget.raise_()
        widgets.store_success_notification.raise_()

    def select_mask_image(self, widgets):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Image files (*.jpg *.png)")
        imagePath = fname[0]
        if imagePath != "":
            self.mask_image_array = cv2.imread(imagePath)
            self.mask_image_array_331 = cv2.resize(self.mask_image_array, dsize=(331, 331),
                                                   interpolation=cv2.INTER_CUBIC)
            # destructing height, width and channel varables from the shape property of the image
            height, width, channel = self.mask_image_array_331.shape
            # setting bytes per line
            bytesPerLine = 3 * width
            # generating a rgbSwapped Qimage from the image data
            self.mask_image_331 = QImage(self.mask_image_array_331.data, width, height, bytesPerLine,
                                         QImage.Format_RGB888).rgbSwapped()
            # converting file data to pixmap
            pixmap = QPixmap(self.mask_image_331)
            widgets.selected_image_content.setPixmap(pixmap)

    def draw_on_image(self,widgets):

        self.last_x, self.last_y = None, None

        def mouseMoveEvent(self, e):
            if self.last_x is None:  # First event.
                self.last_x = e.x()
                self.last_y = e.y()
                return  # Ignore the first time.

            painter = QtGui.QPainter(widgets.selected_image_filter_6.pixmap())
            painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
            painter.end()
            self.update()

            # Update the origin for next time.
            self.last_x = e.x()
            self.last_y = e.y()

        def mouseReleaseEvent(self, e):
            self.last_x = None
            self.last_y = None

    def rotate_image(self,widgets):
        widgets.rotate_image_slider.setValue(0)
        resized_image_array_331 = MainWindow.QImageToCvMat(self, self.customized_image_331)
        original_image_array = MainWindow.QImageToCvMat(self, self.customized_image)
        im = resized_image_array_331
        im_2 = original_image_array
        while self.rotation_process:

            # Shape of image in terms of pixels.
            (rows, cols) = im.shape[:2]
            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), int(widgets.rotate_image_slider.value()), 1)
            res = cv2.warpAffine(im, M, (cols, rows))

            (rows, cols) = im_2.shape[:2]
            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), int(widgets.rotate_image_slider.value()), 1)
            res_2 = cv2.warpAffine(im_2, M, (cols, rows))

            height, width, channel = res.shape
            # setting bytes per line
            bytesPerLine = 3 * width
            # generating a rgbSwapped Qimage from the image data
            self.customized_image_331 = QImage(res.data, width, height, bytesPerLine,
                                               QImage.Format_RGB888).rgbSwapped()
            # setting bytes per line
            height, width, channel = res_2.shape
            # setting bytes per line
            bytesPerLine = 3 * width
            self.customized_image = QImage(res_2.data, width, height, bytesPerLine,
                                           QImage.Format_RGB888).rgbSwapped()
            widgets.selected_image_filter_4.setPixmap(QtGui.QPixmap(self.customized_image_331))
            time.sleep(0.02)

    cropping = False
    cropping_done = False
    customized_image_331 = None
    customized_image = None
    x_start, y_start, x_end, y_end = 0, 0, 0, 0

    def crop_image(self, widgets):
        global cropping_done
        Image_Customization.cropping_done = False
        original_image_array = MainWindow.QImageToCvMat(self, self.customized_image)
        image = original_image_array
        oriImage = image.copy()

        def mouse_crop(event, x, y, flags, param):
            # grab references to the global variables
            global x_start, y_start, x_end, y_end, cropping, cropping_done, customized_image_331, customized_image
            # if the left mouse button was DOWN, start RECORDING
            # (x, y) coordinates and indicate that cropping is being
            if event == cv2.EVENT_LBUTTONDOWN:
                Image_Customization.x_start, Image_Customization.y_start, Image_Customization.x_end, Image_Customization.y_end = x, y, x, y
                Image_Customization.cropping = True
            # Mouse is Moving
            elif event == cv2.EVENT_MOUSEMOVE:
                if Image_Customization.cropping == True:
                    Image_Customization.x_end, Image_Customization.y_end = x, y
            # if the left mouse button was released
            elif event == cv2.EVENT_LBUTTONUP:
                # record the ending (x, y) coordinates
                Image_Customization.x_end, Image_Customization.y_end = x, y
                Image_Customization.cropping = False  # cropping is finished
                refPoint = [(Image_Customization.x_start, Image_Customization.y_start), (Image_Customization.x_end, Image_Customization.y_end)]
                if len(refPoint) == 2:  # when two points were found
                    Image_Customization.cropping_done = True
                    # close all open windows
                    cv2.destroyAllWindows()
                    roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
                    res = cv2.resize(roi, dsize=(int(roi.shape[1] * 0.5), int(roi.shape[0] * 0.5)), interpolation=cv2.INTER_CUBIC)
                    res_2 = cv2.resize(roi, dsize=(roi.shape[1], roi.shape[0]), interpolation=cv2.INTER_CUBIC)
                    height, width, channel = res.shape
                    # setting bytes per line
                    bytesPerLine = 3 * width
                    # generating a rgbSwapped Qimage from the image data
                    Image_Customization.customized_image_331 = QImage(res.data, width, height, bytesPerLine,QImage.Format_RGB888).rgbSwapped()
                    height, width, channel = res_2.shape
                    # setting bytes per line
                    bytesPerLine = 3 * width
                    Image_Customization.customized_image = QImage(res_2.data, width, height, bytesPerLine,QImage.Format_RGB888).rgbSwapped()
                    widgets.selected_image_filter_5.setPixmap(QtGui.QPixmap(Image_Customization.customized_image_331))

        cv2.namedWindow("image")
        cv2.setMouseCallback("image", mouse_crop)
        while Image_Customization.cropping_done == False:
            i = image.copy()
            if not Image_Customization.cropping:
                cv2.imshow("image", image)
            elif Image_Customization.cropping:
                cv2.rectangle(i, (Image_Customization.x_start, Image_Customization.y_start), (Image_Customization.x_end, Image_Customization.y_end), (255, 0, 0), 2)
                cv2.imshow("image", i)
            cv2.waitKey(1)
        self.customized_image = Image_Customization.customized_image
        self.customized_image_331 = Image_Customization.customized_image_331
        # close all open windows
        cv2.destroyAllWindows()

    def blend_images(self,widgets):
        widgets.blend_image_slider.setValue(0)
        resized_image_array_331 = MainWindow.QImageToCvMat(self, self.customized_image_331)
        original_image_array = MainWindow.QImageToCvMat(self, self.customized_image)

        while self.blending == True:
            try:
                alpha = int(widgets.blend_image_slider.value()) / 100
                beta = (1.0 - alpha)

                res = cv2.addWeighted(resized_image_array_331, alpha, self.blender_image_array_331, beta, 0.0);
                res_2 = cv2.addWeighted(original_image_array, alpha, self.blender_image_array, beta, 0.0);

                height, width, channel = res.shape
                # setting bytes per line
                bytesPerLine = 3 * width
                # generating a rgbSwapped Qimage from the image data
                self.customized_image_331 = QImage(res.data, width, height, bytesPerLine,
                                                   QImage.Format_RGB888).rgbSwapped()
                # setting bytes per line
                height, width, channel = res_2.shape
                # setting bytes per line
                bytesPerLine = 3 * width
                self.customized_image = QImage(res_2.data, width, height, bytesPerLine,
                                               QImage.Format_RGB888).rgbSwapped()
                widgets.style_img_result.setPixmap(QtGui.QPixmap(self.customized_image_331))
            except:
                pass
            time.sleep(0.06)
        return

    def apply_mask(self,opt,widgets):

        # getting the image
        image = MainWindow.QImageToCvMat(self, self.customized_image_331)
        image_2 = MainWindow.QImageToCvMat(self, self.customized_image)

        if opt == "black_white":
            self.customized_image_331 = self.customized_image_331.convertToFormat(QImage.Format_Mono);
            self.customized_image = self.customized_image.convertToFormat(QImage.Format_Mono);
            widgets.style_img_result.setPixmap(QtGui.QPixmap(self.customized_image_331))
            return

        elif opt == "or":
            # cv2.bitwise_or is applied over the image inputs with applied parameters
            try:
                dest = cv2.bitwise_or(self.mask_image_array_331, image, mask=None)
                dest_2 = cv2.bitwise_or(self.mask_image_array, image_2, mask=None)
            except:
                dest = cv2.bitwise_or(image,image, mask=None)
                dest_2 = cv2.bitwise_or(image_2,image_2, mask=None)
        elif opt == "and":
            # cv2.bitwise_and is applied over the image inputs with applied parameters

            try:
                dest = cv2.bitwise_and(self.mask_image_array_331, image, mask=None)
                dest_2 = cv2.bitwise_and(self.mask_image_array, image_2, mask=None)
            except:
                dest = cv2.bitwise_and(image,image, mask=None)
                dest_2 = cv2.bitwise_and(image_2,image_2, mask=None)
        elif opt == "xor":
            # cv2.bitwise_xor is applied over the image inputs with applied parameters
            #dest = cv2.bitwise_xor(self.mask_image_array_331, image, mask=None)
            #dest_2 = cv2.bitwise_xor(self.mask_image_array, image_2, mask=None)
            try:
                dest = cv2.bitwise_xor(self.mask_image_array_331,image, mask=None)
                dest_2 = cv2.bitwise_xor(self.mask_image_array,image_2, mask=None)
            except:
                dest = cv2.bitwise_xor(image,image, mask=None)
                dest_2 = cv2.bitwise_xor(image_2,image_2, mask=None)

        elif opt == "not":
            # cv2.bitwise_not is applied over the image inputs with applied parameters
            try:
                dest = cv2.bitwise_not(self.mask_image_array_331, mask=None)
                dest_2 = cv2.bitwise_not(self.mask_image_array, mask=None)
            except:
                dest = cv2.bitwise_not(image, mask=None)
                dest_2 = cv2.bitwise_not(image_2, mask=None)

        height, width, channel= dest.shape
        # setting bytes per line
        bytesPerLine =  3 * width
        # generating a rgbSwapped Qimage from the image data
        self.customized_image_331 = QImage(dest.data, width, height, bytesPerLine,
                                           QImage.Format_RGB888).rgbSwapped()

        # setting bytes per line
        height, width, channel= dest_2.shape
        # setting bytes per line
        bytesPerLine = 3 * width
        self.customized_image = QImage(dest_2.data, width, height, bytesPerLine,
                                       QImage.Format_RGB888).rgbSwapped()

        widgets.style_img_result.setPixmap(QtGui.QPixmap(self.customized_image_331))

    def translate_images(self,widgets):
        widgets.style_gan_plabel_5.setPixmap('')
        handle_of_the_window = Style_Gan_Model.driver.current_window_handle
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        Style_Gan_Model.driver.get("https://colab.research.google.com/drive/1vetN2gygCFT10i4dhlalDRSlSfCmkRzR#scrollTo=EKlzPpXYzh_Y")

        time.sleep(7)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        while(True):
            if Style_Gan_Model.check_exists("XPATH","/html/body/div[7]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]"):
                runtime_butn = Style_Gan_Model.driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]")
                runtime_butn.click()
                break
        time.sleep(2)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        run_all = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[13]/div[1]/div/span")
        run_all.click()
        time.sleep(2)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        if Style_Gan_Model.check_exists("ID", "ok"):
            print("found")
            time.sleep(2)
            Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
            time.sleep(0.5)
            run_anyway = Style_Gan_Model.driver.find_element(By.ID,"ok")
            run_anyway.click()

        while (True):
            Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
            time.sleep(0.5)
            if Style_Gan_Model.check_exists("XPATH",'/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[14]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/iframe'):
                iframe = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[14]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/iframe")
                Style_Gan_Model.driver.switch_to.frame(iframe)
                print("iframe found")
                break
        time.sleep(3)
        while (True):
            if Style_Gan_Model.check_exists("XPATH",'/html/body/div/div/div/div/input'):
                content_img = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div/div/div/div/input")
                ActionChains(Style_Gan_Model.driver).move_to_element(content_img).perform()
                ActionChains(Style_Gan_Model.driver).click(content_img).perform()
                break

        while (True):
            if Style_Gan_Model.check_exists("XPATH", '/html/body/div/div/div[1]/div/output/li/span[1]'):
                content_img_name = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/output/li/span[1]")
                c_name = content_img_name.text
                print("name found")
                break
        time.sleep(2)
        while (True):
            if Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/output/li/span[3]").text == "100% done":
                break
            percentage = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/output/li/span[3]").text
            print(percentage)
            widgets.label_127.setText(f'<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; color:#ff0000;">NOTE: </span><span style=" font-size:14pt;">Uploading the &quot;</span><span style=" font-size:14pt; font-weight:700; font-style:italic;">Content Image</span><span style=" font-size:14pt;">&quot; {percentage} </span></p></body></html>')
            time.sleep(0.5)

        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        # Switching driver settings to default browser window
        Style_Gan_Model.driver.switch_to.default_content()
        while (True):
            Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
            time.sleep(0.5)
            if Style_Gan_Model.check_exists("XPATH",
                            '/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[15]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/iframe'):
                iframe = Style_Gan_Model.driver.find_element(By.XPATH,
                    "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[15]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/iframe")
                Style_Gan_Model.driver.switch_to.frame(iframe)
                print("iframe 2 found")
                break
        time.sleep(3)
        while (True):
            if Style_Gan_Model.check_exists("XPATH", '/html/body/div/div/div/div/input'):
                style_img = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div/div/div/div/input")
                ActionChains(Style_Gan_Model.driver).move_to_element(style_img).perform()
                ActionChains(Style_Gan_Model.driver).click(style_img).perform()
                break
        while (True):
            if Style_Gan_Model.check_exists("XPATH", '/html/body/div/div/div[1]/div/output/li/span[1]'):
                style_img_name = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/output/li/span[1]")
                s_name = style_img_name.text
                print("name 2 found")
                break

        while (True):
            if Style_Gan_Model.check_exists("XPATH", "/html/body/div/div/div[1]/div/output/li/span[3]"):
                # Switching driver settings to default browser window
                Style_Gan_Model.driver.switch_to.default_content()
                Style_Gan_Model.driver.find_element(By.XPATH,
                    "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[14]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]/div[2]").click()
                time.sleep(2)
                Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
                time.sleep(0.5)
                Style_Gan_Model.driver.find_element(By.XPATH,
                    "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[14]/div[1]/colab-cell-toolbar/paper-icon-button[8]").click()
                print("del")
                break

        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        cname = Style_Gan_Model.driver.find_element(By.XPATH,
            "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[15]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]/div[1]/span/span")
        cname.click()
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(c_name).perform()
        time.sleep(1)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        sname = Style_Gan_Model.driver.find_element(By.XPATH,
            "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[15]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]/div[2]/span/span")
        sname.click()
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(s_name).perform()

        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        widgets.label_127.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; color:#ff0000;">NOTE: </span><span style=" font-size:14pt;">First Select the &quot;</span><span style=" font-size:14pt; font-weight:700; font-style:italic;">Content Image</span><span style=" font-size:14pt;">&quot; then the &quot;</span><span style=" font-size:14pt; font-weight:700; font-style:italic;">Style Image</span><span style=" font-size:14pt;">&quot;!</span></p></body></html>')
        Style_Gan_Model.driver.switch_to.frame(iframe)

        while (True):
            if Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/output/li/span[3]").text == "100% done":
                # Switching driver settings to default browser window
                Style_Gan_Model.driver.switch_to.default_content()
                Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
                time.sleep(0.3)
                Style_Gan_Model.driver.find_element(By.XPATH,
                    "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[14]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]").click()
                time.sleep(2)
                Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
                time.sleep(0.3)
                Style_Gan_Model.driver.find_element(By.XPATH,
                    "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[14]/div[1]/colab-cell-toolbar/paper-icon-button[8]").click()
                print("del--2")
                break

            percentage = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/output/li/span[3]").text
            widgets.label_127.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; color:#ff0000;">NOTE: </span><span style=" font-size:14pt;">Uploading the &quot;</span><span style=" font-size:14pt; font-weight:700; font-style:italic;">Style Image</span><span style=" font-size:14pt;">&quot; {percentage} </span></p></body></html>')
            time.sleep(0.5)
        time.sleep(5)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        runtime_butn = Style_Gan_Model.driver.find_element(By.XPATH,
            "/html/body/div[7]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]")
        runtime_butn.click()
        time.sleep(2)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        run_all = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[13]/div[1]/div/span")
        run_all.click()
        time.sleep(2)
        while (True):
            Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
            time.sleep(0.5)
            if Style_Gan_Model.check_exists("XPATH",
                            "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[59]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/iframe"):
                iframe = Style_Gan_Model.driver.find_element(By.XPATH,
                    "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[59]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/iframe")
                Style_Gan_Model.driver.switch_to.frame(iframe)
                break
        widgets.label_127.setText(
            '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; color:#ff0000;">NOTE: </span><span style=" font-size:14pt;">Phase 1 of the process is in progress ... </span></p></body></html>')

        while (True):
            if Style_Gan_Model.check_exists("XPATH", "/html/body/div/div/div[2]/div/pre"):
                try:
                    progress_1 = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/pre").text
                except:
                    pass
                widgets.phase1_label.setText(
                    f'<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; color:#ff0000;">NOTE: </span><span style=" font-size:14pt;">{progress_1} </span></p></body></html>')

                time.sleep(1)
                if re.search("1000", progress_1):
                    break
        widgets.style_gan_plabel_4.setMovie(self.tick_gif)
        widgets.style_gan_plabel_5.setMovie(self.dst_gif)
        widgets.phase1_label.lower()
        widgets.label_127.setText(
            '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; color:#ff0000;">NOTE: </span><span style=" font-size:14pt;">Phase 2 of the process is in progress ... </span></p></body></html>')

        time.sleep(1)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        Style_Gan_Model.driver.switch_to.default_content()
        while (True):
            if Style_Gan_Model.check_exists("XPATH",
                            "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[77]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/iframe"):
                iframe = Style_Gan_Model.driver.find_element(By.XPATH,
                    "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[77]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/iframe")
                Style_Gan_Model.driver.switch_to.frame(iframe)
                break

        while (True):
            if Style_Gan_Model.check_exists("XPATH", "/html/body/div/div/div[2]/div/pre"):
                try:
                    progress_2 = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/pre").text
                except:
                    pass
                widgets.phase2_label.setText(
                    f'<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; color:#ff0000;">NOTE: </span><span style=" font-size:14pt;">{progress_2} </span></p></body></html>')
                time.sleep(1)
                if re.search("1000", progress_2):
                    break
        widgets.style_gan_plabel_5.setMovie(self.tick_gif)
        time.sleep(1)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        Style_Gan_Model.driver.switch_to.default_content()
        while (True):
            if Style_Gan_Model.check_exists("XPATH",
                            "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[79]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/iframe"):
                iframe = Style_Gan_Model.driver.find_element(By.XPATH,
                    "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[79]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/iframe")
                Style_Gan_Model.driver.switch_to.frame(iframe)
                break
        widgets.phase2_label.lower()
        self.tick_gif.stop()
        self.dst_gif.stop()
        widgets.style_gan_plabel_4.setPixmap(self.tick)
        widgets.style_gan_plabel_5.setPixmap(self.tick)
        progress_percent = 0
        while (progress_percent != 100):
            if Style_Gan_Model.check_exists("XPATH", "/html/body/div[2]/progress"):
                progress = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[2]/progress")
                max = progress.get_attribute("max")
                value = progress.get_attribute("value")
                progress_percent = int((int(value) / int(max)) * 100)
                x = "Downloading Translated Image Progress = " + str(progress_percent) + " %"
                widgets.label_127.setText(
                    f'<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; color:#ff0000;">NOTE: </span><span style=" font-size:14pt;">{x} </span></p></body></html>')

        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        # Switching driver settings to default browser window
        Style_Gan_Model.driver.switch_to.default_content()
        time.sleep(5)
        Style_Gan_Model.driver.find_element(By.XPATH,
            "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[80]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]").click()
        ActionChains(Style_Gan_Model.driver).send_keys('!rm ''"{content_img_name}"''').perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.RETURN).perform()
        ActionChains(Style_Gan_Model.driver).send_keys('!rm ''"{style_img_name}"''').perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.RETURN).perform()
        ActionChains(Style_Gan_Model.driver).send_keys('!rm ''"{file_name}"''').perform()
        Style_Gan_Model.driver.find_element(By.XPATH,
            "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[80]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button").click()

        Image_Customization.store_translated_image(self)

        for gen_image in output_images.find({"name": "stylized-image.png"}):
                # load image from the pickle module
                image = pickle.loads(gen_image["image"])
                # destructing height, width and channel varables from the shape property of the image
                height, width, channel = image.shape
                # setting bytes per line
                bytesPerLine = 3 * width
                # generating a rgbSwapped Qimage from the image data
                qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

                res = cv2.resize(image, dsize=(181, 191), interpolation=cv2.INTER_CUBIC)
                # destructing height, width and channel varables from the shape property of the image
                height, width, channel = res.shape
                # setting bytes per line
                bytesPerLine = 3 * width
                # generating a rgbSwapped Qimage from the image data
                resized_image = QImage(res.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                widgets.translated_image.setPixmap(resized_image)
                self.customized_image = qImg


        widgets.stackedWidget_img_cutom.setCurrentWidget(widgets.image_translation_result)

        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        runtime_butn = Style_Gan_Model.driver.find_element(By.XPATH,
                                                           "/html/body/div[7]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]")
        runtime_butn.click()
        time.sleep(2)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        manage_sess = Style_Gan_Model.driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/div/div/div[1]")
        manage_sess.click()
        time.sleep(2)
        terminate_sess = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/colab-dialog/paper-dialog/colab-sessions-dialog//div[2]/div[2]/div[2]/colab-session/div[5]")
        ActionChains(Style_Gan_Model.driver).move_to_element(terminate_sess).perform()
        ActionChains(Style_Gan_Model.driver).click(terminate_sess).perform()
        time.sleep(5)
        Style_Gan_Model.driver.close()
        self.translation_process = False

    def store_translated_image(self):
        # Using try/except blocks for exception handling
        # try block
        try:
            # Getting images names
            images_name = []
            for file in glob.glob("C:/Users/SYS/Downloads/stylized-image.png"):
                f_name = file.rpartition('\\')[-1]
                images_name.append(f_name)

            # Getting images data from the output folder
            images = [cv2.imread(file) for file in glob.glob("C:/Users/SYS/Downloads/stylized-image.png")]
            print(len(images))

            # Getting local machine time
            t = time.localtime()
            # Formatting time
            current_time = time.strftime("%H:%M:%S", t)
            # Getting current date
            now = datetime.now()
            # Formatting date
            date = now.strftime("%d/%m/%Y");
            # Getting datetime both
            date_time = current_time + " " + date

            # Iterating through the total images
            for i in range(len(images)):
                # convert numpy array to Binary, store record in mongodb
                rec = Binary(pickle.dumps(images[i], protocol=i % 6))
                # storing the output image in the database collection with date time stamp
                output_images.insert_one({"image": rec, "name": images_name[i], "generated_at": date_time})
            # return stored success
            return "outputs stored success"
        # except block
        except:
            return "outputs stored failure"