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
import os
import time

from main import *

# Gan_Model Class
# ///////////////////////////////////////////////////////////////
class Gan_Model(MainWindow):

    driver = None
    training = False
    # Function to Train the GAN Model Against the provided Dataset
    # ///////////////////////////////////////////////////////////////
    def train_model(self, widgets):

        Gan_Model.training = True
        widgets.azure_label.setMovie(self.azure_gif)

        widgets.total_epochs.display(widgets.set_epoch_number.currentText())
        # opening browser on the background
        #chrome_options.add_argument("--headless")

        # Creating a Chrome driver instance
        Gan_Model.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)

        # Load kaggle gan model training page
        Gan_Model.driver.get(
            'https://ml.azure.com/compute/list?wsid=/subscriptions/1bfb53aa-2de8-4774-be73-30f4dd005819/resourcegroups/Fyp_resource/workspaces/Fyp_machine_learning_workspace&tid=75df096c-8b72-48e4-9b91-cbf79d87ee3a')
        while (True):
            try:
                email = Gan_Model.driver.find_element(By.XPATH,
                                            "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]")
                email.send_keys("SP18-BCS-154@isbstudent.comsats.edu.pk")
                break
            except:
                pass

        ActionChains(Gan_Model.driver).send_keys(Keys.RETURN).perform()

        while (True):
            try:
                password = Gan_Model.driver.find_element(By.XPATH,
                                               "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input")
                password.send_keys("7310643")
                break
            except:
                pass

        ActionChains(Gan_Model.driver).send_keys(Keys.RETURN).perform()

        while (True):
            try:
                Gan_Model.driver.find_element(By.XPATH,
                                    "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input").click()
                break
            except:
                pass

        while (True):
            try:
                Gan_Model.driver.find_element(By.XPATH,
                                    "/html/body/div/div/div/div[2]/div[2]/main/div/div[3]/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]").click()
                time.sleep(1)
                Gan_Model.driver.find_element(By.XPATH,
                                    "/html/body/div/div/div/div[2]/div[2]/main/div/div[3]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[3]/button").click()
                break
            except:
                try:
                    Gan_Model.driver.find_element(By.XPATH,
                                        "/html/body/div/div/div/div[2]/div[2]/main/div/div[3]/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[3]/div/a[2]")
                    break
                except:
                    pass

        while (True):
            try:
                Gan_Model.driver.find_element(By.XPATH,
                                    "/html/body/div/div/div/div[2]/div[2]/main/div/div[3]/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[3]/div/a[2]")
                time.sleep(1)
                Gan_Model.driver.get(
                    "https://ganmodelgpuinstance.eastus.instances.azureml.ms/notebooks/Users/SP18-BCS-154/Gan_model.ipynb")
                print("Compute instance started!")
                widgets.status_label.setText(f'<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; font-style:italic;">Compute instance started!</span></body></html>')
                break
            except:
                print("Compute instance starting....")

        while (True):
            try:
                Gan_Model.driver.find_element(By.XPATH,
                                    "/html/body/div[4]/div/div/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div/div[6]/div[1]/div/div/div/div[5]/pre").click()
                time.sleep(1)
                ActionChains(Gan_Model.driver).send_keys("dst_name = " + self.training_gan_dataset).perform()
                break
            except:
                pass

        widgets.azure_label.lower()
        self.azure_gif.stop()
        widgets.loading_label_dst_3.setMovie(self.dst_gif)
        widgets.progress_number_3.raise_()

        while (True):
            try:
                Gan_Model.driver.find_element(By.XPATH,
                                    "/html/body/div[4]/div/div/div[1]/div[1]/div[4]/div[1]/div[2]/div[2]/div/div[6]/div[1]/div/div/div/div[5]/pre").click()
                time.sleep(1)
                ActionChains(Gan_Model.driver).send_keys("epochs = " + widgets.set_epoch_number.currentText()).perform()
                break
            except:
                pass

        while (True):
            try:
                run = Gan_Model.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div[5]/button[4]")
                time.sleep(1)
                ActionChains(Gan_Model.driver).move_to_element(run).perform()
                time.sleep(1)
                ActionChains(Gan_Model.driver).click(run).perform()
                time.sleep(3)
                try:
                    Gan_Model.driver.find_element(By.XPATH, "/html/body/div[8]/div/div/div[3]/button[2]").click()
                    break
                except:
                    pass
                break
            except:
                pass

        print("training has been started!")
        widgets.status_label.setText(
            f'<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; font-style:italic;">training has been started!</span></body></html>')

        # Start time of training
        start_time = time.time()

        # While the training is on going, get the processing stats
        while (True):
            try:
                # Getting the dataset processing stats
                c = Gan_Model.driver.find_element(By.XPATH,
                                        "/html/body/div[4]/div/div/div[1]/div[1]/div[5]/div[2]/div[2]/div/div[3]/pre")

                dataset_progress_number = (c.text).split('%')[0]
                widgets.progress_number_3.display(int(dataset_progress_number))
                widgets.status_label.setText(
                    f'<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; font-style:italic;">Processing Dataset ...</span></body></html>')
                if int(dataset_progress_number) == 100:
                    break
            # if any exceptions occur
            except:
                pass

        widgets.loading_label_dst_3.setMovie(self.tick_gif)
        widgets.progress_number_3.lower()

        widgets.loading_label_dst_4.setMovie(self.dst_gif)
        widgets.progress_number_4.raise_()

        # While the training is on going, get the processing stats
        while (True):
            try:

                # Getting the dataset processing stats
                c = Gan_Model.driver.find_element(By.XPATH,
                                        "/html/body/div[4]/div/div/div[1]/div[1]/div[16]/div[2]/div[2]/div/div[3]/pre")
                image_progress_number = (c.text).split('%')[0]

                if int(image_progress_number) != 100:
                    pass
                    widgets.progress_number_4.display(int(image_progress_number))
                    total_epochs = int(widgets.set_epoch_number.currentText())
                    epoch = int((int(image_progress_number) / 100) * total_epochs)
                    widgets.epoch.display(epoch)
                    output_imgs_count = int(epoch / 49)
                    widgets.genrated_images_count.display(output_imgs_count)

                    # Updating training time
                    training_time_in_secs = float(time.time() - start_time)
                    secs = training_time_in_secs % (24 * 3600)
                    training_time_in_hours = secs // 3600
                    secs %= 3600
                    training_time_in_minutes = secs // 60
                    widgets.hours_2.display(training_time_in_hours)
                    widgets.minutes.display(training_time_in_minutes)
                    widgets.status_label.setText(
                        f'<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; font-style:italic;">Training the GAN Model ...</span></body></html>')
                elif int(image_progress_number) == 100:
                    widgets.progress_number_4.display(int(image_progress_number))
                    total_epochs = int(widgets.set_epoch_number.currentText())
                    epoch = int((int(image_progress_number) / 100) * total_epochs)
                    widgets.epoch.display(epoch)
                    widgets.status_label.setText(
                        f'<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:700; font-style:italic;">Finalizing ...</span></body></html>')
                    break
            # if any exceptions occur
            except:
                pass

        widgets.progress_number_4.lower()
        widgets.loading_label_dst_3.setPixmap(self.tick)
        widgets.loading_label_dst_4.setPixmap(self.tick)
        self.dst_gif.stop()
        self.tick_gif.stop()
        handle_of_the_window = Gan_Model.driver.current_window_handle
        while (True):
            try:
                Gan_Model.driver.find_element(By.XPATH,
                                    "/html/body/div[4]/div/div/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div/div[6]/div[1]/div/div/div/div[5]/pre").click()

                i=0
                j=0
                for i in range(10):
                    ActionChains(Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
                for j in range(30):
                    ActionChains(Gan_Model.driver).send_keys(Keys.BACKSPACE).perform()
                break
            except:
                pass

        while (True):
            try:
                Gan_Model.driver.find_element(By.XPATH,
                                    "/html/body/div[4]/div/div/div[1]/div[1]/div[4]/div[1]/div[2]/div[2]/div/div[6]/div[1]/div/div/div/div[5]/pre").click()
                i = 0
                j = 0
                for i in range(10):
                    ActionChains(Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
                for j in range(30):
                    ActionChains(Gan_Model.driver).send_keys(Keys.BACKSPACE).perform()
                break
            except:
                pass

        time.sleep(2)
        Gan_Model.driver.switch_to.window(handle_of_the_window)
        down_path = f"C:\\Users\\{USER_NAME}\\Downloads\\AI images\\results.zip"
        while (True):
            if (os.path.exists(down_path)):
                time.sleep(3)
                Gan_Model.store_gan_outputs(self)
                break
            else:
                pass

        time.sleep(2)
        Gan_Model.driver.switch_to.window(handle_of_the_window)
        Gan_Model.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div[1]/button").click()
        time.sleep(2)
        Gan_Model.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div[5]/button[2]").click()

        while (True):
            try:
                Gan_Model.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div/div/div/ul/li[5]").click()
                clrr = Gan_Model.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div/div/div/ul/li[5]/ul/li[11]/a")
                ActionChains(Gan_Model.driver).move_to_element(clrr).perform()
                time.sleep(1)
                clr_btn = Gan_Model.driver.find_element(By.XPATH,
                                              "/html/body/div[3]/div[3]/div[1]/div/div/div/ul/li[5]/ul/li[11]/ul/li[3]")
                ActionChains(Gan_Model.driver).move_to_element(clr_btn).perform()
                time.sleep(1)
                ActionChains(Gan_Model.driver).click(clr_btn).perform()
                break
            except:
                pass

        time.sleep(3)
        Gan_Model.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div[1]/button").click()
        handle_of_the_window = Gan_Model.driver.current_window_handle
        Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(3)
        Gan_Model.driver.close()
        # opening browser on the background
        # chrome_options.add_argument("--headless")

        # Creating a Chrome driver instance
        Gan_Model.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
        Gan_Model.driver.get(
            "https://ml.azure.com/compute/list?wsid=/subscriptions/1bfb53aa-2de8-4774-be73-30f4dd005819/resourcegroups/Fyp_resource/workspaces/Fyp_machine_learning_workspace&tid=75df096c-8b72-48e4-9b91-cbf79d87ee3a")
        while (True):
            try:
                email = Gan_Model.driver.find_element(By.XPATH,
                                                      "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]")
                email.send_keys("SP18-BCS-154@isbstudent.comsats.edu.pk")
                break
            except:
                pass

        ActionChains(Gan_Model.driver).send_keys(Keys.RETURN).perform()

        while (True):
            try:
                password = Gan_Model.driver.find_element(By.XPATH,
                                                         "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input")
                password.send_keys("7310643")
                break
            except:
                pass

        ActionChains(Gan_Model.driver).send_keys(Keys.RETURN).perform()

        while (True):
            try:
                Gan_Model.driver.find_element(By.XPATH,
                                              "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input").click()
                break
            except:
                pass

        time.sleep(4)
        while (True):
            try:
                Gan_Model.driver.find_element(By.XPATH,
                                              "/html/body/div/div/div/div[2]/div[2]/main/div/div[3]/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]").click()
                time.sleep(1)
                Gan_Model.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[2]/main/div/div[3]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[4]/button").click()
                break
            except:
                pass
        time.sleep(3)
        widgets.status_label.lower()
        Gan_Model.driver.close()
        return

    # Function to Update the GAN Algorithm
    # ////////////////////////////////////////////////////////////////////////////////////////
    def update_algo(self):

        # Creating a Chrome driver instance
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
        # Load kaggle gan model training page
        driver.get('https://www.kaggle.com/account/login?phase=emailSignIn&returnUrl=%2F')
        # Putting user email login details for kaggle account
        email = driver.find_element_by_name("email")
        email.send_keys("aiimagestoolkit@gmail.com")
        # Putting user password login details for kaggle account
        password = driver.find_element_by_name("password")
        password.send_keys("kazmi12!")
        # Clicking sign in btn
        sign_in_butn = driver.find_element_by_class_name("sc-psCJM.mBUMG")
        sign_in_butn.click()
        # Redirecting to generate-realistic-human-face-using-gan edit page
        driver.get('https://www.kaggle.com/aiimages/generate-realistic-human-face-using-gan/edit')
        return

    def store_gan_outputs(self):
        while (True):
            try:
                with zipfile.ZipFile(f"C:\\Users\\{USER_NAME}\\Downloads\\AI images\\results.zip", 'r') as zip_ref:
                    zip_ref.extractall(f"C:\\Users\\{USER_NAME}\\Downloads\\AI images\\results")
                break
            except:
                pass
        time.sleep(2)
        os.remove(f"C:\\Users\\{USER_NAME}\\Downloads\\AI images\\results.zip")

    # Function to Store Output Images in the database using the output folder on the local drive
    # ///////////////////////////////////////////////////////////////
    def store_output_images(self):
        # Using try/except blocks for exception handling
        # try block
        try:
            # Getting images names
            images_name = []
            for file in glob.glob(f"C:/Users/{USER_NAME}/Downloads/AI Images/results/generated*.png"):
                f_name = file.rpartition('\\')[-1]
                images_name.append(f_name)

            # Getting images data from the output folder
            images = [cv2.imread(file) for file in glob.glob(f"C:/Users/{USER_NAME}/Downloads/AI Images/results/generated*.png")]
            print(len(images))

            # Getting local machine time
            t = time.localtime()
            # Formatting time
            current_time = time.strftime("%H:%M:%S", t)
            # Getting current date
            now = datetime.now()
            # Formatting date
            date = now.strftime("%d/%m/%Y")
            # Getting datetime both
            date_time = current_time + " " + date

            # Iterating through the total images
            for i in range(len(images)):
                # convert numpy array to Binary, store record in mongodb
                rec = Binary(pickle.dumps(images[i], protocol=i % 6))
                # storing the output image in the database collection with date time stamp
                output_images.insert_one({"image": rec, "name": images_name[i], "generated_at": date_time})
            # return stored success
            os.rmdir(f"C:\\Users\\{USER_NAME}\\Downloads\\AI images\\results")
            return "outputs stored success"
        # except block
        except:
            return "outputs stored failure"