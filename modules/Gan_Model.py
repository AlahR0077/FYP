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

# Gan_Model Class
# ///////////////////////////////////////////////////////////////
class Gan_Model(MainWindow):

    # Function to Train the GAN Model Against the provided Dataset
    # ///////////////////////////////////////////////////////////////
    def train_model(self, widgets):
        # Showing the model training progress page
        widgets.stackedWidget_model_training.setCurrentWidget(widgets.model_progress_page)
        #
        # opening browser on the background
        #chrome_options.add_argument("--headless")

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
        sign_in_butn = driver.find_element_by_xpath("/html/body/main/div[1]/div[1]/div/form/div[2]/div[3]/button")
        sign_in_butn.click()
        # Redirecting to generate-realistic-human-face-using-gan edit page
        driver.get('https://www.kaggle.com/aiimages/generate-realistic-human-face-using-gan/edit')

        # Clicking the session btn to start the session
        time.sleep(3)
        session_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/button[1]")
        session_btn.click()
        time.sleep(3)

        # Clicking the settings tab to display
        settings_down_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/button")

        #settings_down_btn = driver.find_element_by_css_selector(
         #   "#site-content > div.AppView--16eb2j.kMYsPa > div.App_Body--16c8j4p.lpnlFZ > div.Sidebar_Body--14r4g35.krYMPd > div > div:nth-child(2) > div > div:nth-child(2) > div > div.SidebarPane_ChevronWrapper--qm9hj3.jkhhYy > button")
        settings_down_btn.click()
        time.sleep(1)

        # Clicking the Accelerator button to use the GPU for the model training process
        accelerator_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div/button")
        accelerator_btn.click()
        time.sleep(2)

        # Clicking the GPU button to train the model perfectly
        gpu_btn = driver.find_element_by_xpath("/html/body/div[12]/div/div[2]")
        time.sleep(1)
        gpu_btn.click()
        time.sleep(1)
        turn_on_gpu_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div[2]/div[4]/div[1]/div/div[2]/button[2]/span")
        turn_on_gpu_btn.click()

        # Clicking the RUN GAN algorithm on kaggle
        run_all_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[1]/button[7]")

        # Checking if the session is LIVE
        green_signal = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div/div/div/div/div[1]/button/div[1]/div[1]/i")

        # if not, wait for the active session
        while green_signal.get_attribute("color") != "#42E3BB":
            time.sleep(1)
        time.sleep(5)

        # Checking if the RUN button is enabled/disabled
        if run_all_btn.is_selected() == False:
            run_all_btn.click()

        # Printing the training start status
        print("training has been started!")

        # Start time of training
        start_time = time.time()

        # Iframe for the kaggle code notebook
        iframe = driver.find_element_by_tag_name('iframe')

        # Switching driver settings to Iframe
        driver.switch_to.frame(iframe)

        # Settings the maximum values of the components accordingly
        widgets.training_progressBar.setMaximum(150)
        widgets.total_epochs.display(150)

        # While the training is on going, get the processing stats
        while (True):
            try:
                # Getting the dataset processing stats
                c = WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div[3]/div[2]/div[3]/div[2]/div[2]/div[8]/div[3]/div[2]/div/div[2]/pre")))
                dataset_progress_number = (c.text).split('%')[0]
                if dataset_progress_number != "100":
                    widgets.dataset_processing_bar.setValue(int(dataset_progress_number) + 1)
                    if widgets.dataset_processing_bar.value() > 75:
                        widgets.dataset_processing_bar.setStyleSheet(
                            "QProgressBar"
                            "{"
                            "color : black;"
                            "}"
                            "QProgressBar"
                            "{"
                            "font: 700 12pt 'Segoe UI';"
                            "}"
                        )

                # Getting the training processing stats, (i.e. epoch, trainining time and output images count)
                d = WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div[3]/div[2]/div[3]/div[2]/div[2]/div[26]/div[3]/div[2]/div/div[2]/pre")))
                d = (d.text).splitlines()
                d = d[-1]
                print(d)

                # Updating outputs count
                if d.startswith("o") == True:
                    output_imgs_count = d.partition("output:")[2]
                    print(output_imgs_count)
                    widgets.genrated_images_count.display(output_imgs_count)
                elif d.startswith("o") == False:
                    # Updating epochs
                    epoch_number = d
                    widgets.training_progressBar.setValue(int(epoch_number) + 1)
                    widgets.epoch.display(int(epoch_number) + 1)
                    if widgets.training_progressBar.value() > 5000:
                        widgets.training_progressBar.setStyleSheet(
                            "QProgressBar"
                            "{"
                            "color : black;"
                            "}"
                            "QProgressBar"
                            "{"
                            "font: 700 12pt 'Segoe UI';"
                            "}"
                        )

                # Updating training time
                training_time_in_secs = float(time.time() - start_time)
                secs = training_time_in_secs % (24 * 3600)
                training_time_in_hours = secs // 3600
                secs %= 3600
                training_time_in_minutes = secs // 60
                widgets.hours_2.display(training_time_in_hours)
                widgets.minutes.display(training_time_in_minutes)

                # If the training approches the last epoch
                if (epoch_number == str(widgets.total_epochs.intValue() - 1)):
                    # Exit While loop
                    break
            # if any exceptions occur
            except:
                continue

        # Calculating final output count
        widgets.genrated_images_count.display(widgets.genrated_images_count.intValue() + 1)

        # Switching driver settings to default browser window
        driver.switch_to.default_content()
        time.sleep(5)

        # Refreshing the output folders on kaggle site
        dataset_show = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[3]")
        dataset_show.click()
        refresh_btn_ = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/ul/div/div[4]/div/div[2]/div[1]/i")
        #refresh_btn_ = driver.find_element_by_css_selector(
         #   "#site-content > div.AppView-sc-16eb2j.kDpcJw > div.App_Body-sc-16c8j4p.hxOBfv > div.Sidebar_Body-sc-14r4g35.dEilyb > div > div:nth-child(2) > div > div:nth-child(1) > div.SidebarPane_ItemBody-sc-tqtqts.jKIbPu > div > div:nth-child(2) > ul > ul > div > div.sc-pRrUz.dQnepB > div > div.sc-pYNsO.YWalf > div.sc-pByoR.eHxtff > i")
        ActionChains(driver).move_to_element(refresh_btn_).click().perform()
        output_fold = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id='site-content']/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/ul/div/div[3]")))
        output_fold.click()
        time.sleep(1)
        ActionChains(driver).reset_actions()
        output_fold2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id='site-content']/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/ul/ul/ul/div/div[3]")))
        ActionChains(driver).move_to_element(output_fold2).double_click().perform()
        time.sleep(2)

        # Getting the access to output generated images
        im = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/ul/ul/ul/ul")
        images = im.find_elements_by_class_name("sc-oUaSW.fZWUHt")

        # Fetching the list of all generated images and downloading them to local machine
        for img in images:
            ActionChains(driver).move_to_element(img).perform()
            g = img.find_element_by_class_name("sc-fzoyTs.sc-fzoNJl.sc-pIvhh.chEDYu")
            time.sleep(1)
            more_acbtn = img.find_elements_by_class_name("sc-pByoR.eHxtff")
            ActionChains(driver).move_to_element(more_acbtn[1]).click().perform()
            time.sleep(1)
            d_btn = img.find_element_by_class_name("mdc-list.mdc-menu__items.mdc-list")
            d_btn.click()
            time.sleep(1)
            print(g.text)
            ActionChains(driver).reset_actions()

        # Resetting the kaggle site settings
        time.sleep(1)
        settings_down_btn.click()
        output_fold2.click()
        output_fold.click()
        session_btn.click()
        time.sleep(5)

        # Closing the chrome driver
        driver.close()
        print(Gan_Model.store_output_images(self))
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

    # Function to Store Output Images in the database using the output folder on the local drive
    # ///////////////////////////////////////////////////////////////
    def store_output_images(self):
        # Using try/except blocks for exception handling
        # try block
        try:

            # Getting images names
            images_name = []
            for file in glob.glob("C:/Users/SYS/Downloads/AI Images/generated*.png"):
                f_name = file.rpartition('\\')[-1]
                images_name.append(f_name)

            # Getting images data from the output folder
            images = [cv2.imread(file) for file in glob.glob("C:/Users/SYS/Downloads/AI Images/generated*.png")]
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