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

# Style_Gan_Model Class
# ///////////////////////////////////////////////////////////////
class Style_Gan_Model(MainWindow):

    driver = None
    verify_acc = False
    login_fail = False
    login_success = False
    process1_running = False
    process2_running = False

    def login_status(self,widgets):
        while (True):
            if Style_Gan_Model.login_success:
                # prompt the successful login notification
                widgets.login_success_notification_2.raise_()
                self.google_dots_loading.stop()
                widgets.login_loading_label.lower()
                break
            elif Style_Gan_Model.login_fail:
                widgets.login_fail_message_2.setText("Username or password is incorrect!")
                widgets.login_fail_notification_2.raise_()
                self.google_dots_loading.stop()
                widgets.login_loading_label.lower()
                global login_fail;
                Style_Gan_Model.login_fail = False
                break

    def sign_up_google_account(self):
        # link to sign up google account
        webbrowser.open('https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fwww.google.com%2F&hl=en&dsh=S889484839%3A1632033490050369&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')

    def check_exists(selector, value):
        try:
            if selector == "ID":
                Style_Gan_Model.driver.find_element(By.ID,value)
            elif selector == "XPATH":
                Style_Gan_Model.driver.find_element(By.XPATH,value)
        except NoSuchElementException:
            return False
        return True

    def sign_in_google_account(self, GMAIL, PASSWORD,widgets):

            chrome_options = uc.ChromeOptions()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--profile-directory=Default")
            #chrome_options.add_argument("--ignore-certificate-errors")
            #chrome_options.add_argument('--no-sandbox')
            #chrome_options.add_argument("--disable-plugins-discovery")
            chrome_options.add_argument("--window-size=500,500")
            chrome_options.add_argument("--window-position=980,980");
            #chrome_options.add_argument("--incognito")
            chrome_options.add_argument("user_agent=DN")

            try:
                global driver;
                Style_Gan_Model.driver = uc.Chrome(options=chrome_options)
                Style_Gan_Model.driver.delete_all_cookies()
                Style_Gan_Model.driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
                time.sleep(2)
                handle_of_the_window = Style_Gan_Model.driver.current_window_handle
                Style_Gan_Model.driver.minimize_window()
                WebDriverWait(Style_Gan_Model.driver, 5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"))).send_keys(GMAIL)
                WebDriverWait(Style_Gan_Model.driver, 5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"))).send_keys(Keys.RETURN)
                #Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(GMAIL)
                #Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(Keys.RETURN)
                time.sleep(3)
                # enter google password
                Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
                time.sleep(0.5)
                WebDriverWait(Style_Gan_Model.driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"))).send_keys(PASSWORD)
                WebDriverWait(Style_Gan_Model.driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"))).send_keys(Keys.RETURN)
                Style_Gan_Model.driver.minimize_window()
                time.sleep(5)
                Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
                time.sleep(0.5)
                if Style_Gan_Model.check_exists("XPATH","/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[5]/div"):
                    Style_Gan_Model.driver.minimize_window()
                    global verify_acc;
                    Style_Gan_Model.verify_acc = True
                    time.sleep(2)
                    Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
                    time.sleep(0.5)
                    verify_gaccount = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[5]/div")
                    verify_gaccount.click()
                    Style_Gan_Model.driver.minimize_window()
                    widgets.google_verify_code_widget_resend_btn.hide()
                    widgets.verify_code_error.hide()
                    widgets.google_verify_code_widget.raise_()
                Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
                time.sleep(0.5)
                password_error = Style_Gan_Model.check_exists("XPATH","/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div[2]/span")
                print(password_error)
                Style_Gan_Model.driver.minimize_window()
                if password_error:
                    global login_fail;
                    Style_Gan_Model.login_fail = True
                    Style_Gan_Model.driver.close()
                    widgets.login_loading_label.lower()
                # g-auth page
                if (Style_Gan_Model.verify_acc == False) and (password_error == False):
                    Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
                    time.sleep(0.5)
                    Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/a")
                    Style_Gan_Model.driver.minimize_window()
                    global login_success;
                    Style_Gan_Model.login_success = True
            except:
                global login_fail;
                Style_Gan_Model.login_fail = True
                Style_Gan_Model.driver.close()
                return

    def verify_code(self,code,widgets):
        handle_of_the_window = Style_Gan_Model.driver.current_window_handle
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(code)
        Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(Keys.RETURN)
        time.sleep(3)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        if Style_Gan_Model.check_exists("XPATH","/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[2]/div"):
            print("Wrong code entered")
            widgets.verify_code_error.show()
            time.sleep(2)
            Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
            time.sleep(0.5)
            input_gaccount = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div/div[1]/input")
            input_gaccount.click()
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/a")
        global login_success;
        Style_Gan_Model.login_success = True
        widgets.google_verify_code_widget.lower()

    def sign_in_google_colab(self):
        pass

    def useGPU(self):
        pass

    def use_Pretrainined_Model(self):
        pass

    def mount_gdrive(self):
        pass

    def run_style_gan1(self,images_size,dataset,widgets):
        global driver;
        global process1_running;
        Style_Gan_Model.process1_running = True
        widgets.progress_number.display(0)
        widgets.genrated_images_count_stylegan1.display(0)
        widgets.stylegan1_hours.display(0)
        widgets.stylegan1_minutes.display(0)
        widgets.style_gan_plabel.setPixmap('')
        # Start time of run
        start_time = time.time()
        handle_of_the_window = Style_Gan_Model.driver.current_window_handle
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        Style_Gan_Model.driver.get("https://colab.research.google.com/drive/1yv2bTNRuEXk59Vq_-Yav41JOb1-FfS4J?usp=sharing")

        time.sleep(3)
        size = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div/div/div[2]/div[12]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]/div[43]/span/span[2]")
        size.click()
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.BACK_SPACE).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.BACK_SPACE).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(str(images_size)).perform()
        time.sleep(3)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        network_ = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[12]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]/div[30]/span/span")
        network_.click()
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(dataset).perform()

        time.sleep(3)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        runtime_butn = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[7]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/div/div/div[1]")
        runtime_butn.click()
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        run_all = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[13]/div[1]/div/span")
        run_all.click()

        time.sleep(2)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(1)
        if Style_Gan_Model.check_exists("ID", "ok"):
            print("found")
            time.sleep(2)
            Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
            time.sleep(1)
            run_anyway = Style_Gan_Model.driver.find_element(By.ID,"ok")
            run_anyway.click()

        while (True):
            Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
            time.sleep(0.5)
            if Style_Gan_Model.check_exists("XPATH",'/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div/div/div[2]/div[13]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/iframe'):
                iframe = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div/div/div[2]/div[13]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/iframe")
                Style_Gan_Model.driver.switch_to.frame(iframe)
                print("iframe found")
                break
        widgets.style_gan_plabel.raise_()
        widgets.loading_label_dst.setMovie(self.tick_gif)

        widgets.style_gan_plabel.setMovie(self.dst_gif)
        widgets.progress_number.raise_()
        gen_img_units = int(100 / int(images_size));
        images_generated = 0
        #widgets.stylegan1_progressBar.setMaximum(100)
        while ((images_generated) != int(images_size)):
            if Style_Gan_Model.check_exists("XPATH", "/html/body/div[2]/progress"):
                progress = Style_Gan_Model.driver.find_element(By.XPATH,"/html/body/div[2]/progress")
                max = progress.get_attribute("max")
                value = progress.get_attribute("value")
                progress_percent = int((int(value) / int(max)) * 100)
                images_generated = int(progress_percent / gen_img_units)
                widgets.progress_number.display(int(progress_percent))
                widgets.genrated_images_count_stylegan1.display(images_generated)

                # Updating training time
                training_time_in_secs = float(time.time() - start_time)
                secs = training_time_in_secs % (24 * 3600)
                training_time_in_hours = secs // 3600
                secs %= 3600
                training_time_in_minutes = secs // 60
                widgets.stylegan1_hours.display(training_time_in_hours)
                widgets.stylegan1_minutes.display(training_time_in_minutes)
                #print("progress = " + str(progress_percent) + " %")
                #print("images genrated " + str(images_generated))
        widgets.progress_number.lower()
        widgets.loading_label_dst.setPixmap(self.tick)
        widgets.style_gan_plabel.setPixmap(self.tick)
        self.dst_gif.stop()
        self.tick_gif.stop()
        time.sleep(3)
        # Switching driver settings to default browser window
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.4)
        Style_Gan_Model.driver.switch_to.default_content()
        if Style_Gan_Model.check_exists("XPATH", "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div/div/div[2]/div[13]/div[2]/div[2]/div[2]/div[2]/div[1]/div/iron-icon[1]"):
            Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
            time.sleep(0.4)
            Style_Gan_Model.driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div/div/div[2]/div[13]/div[2]/div[2]/div[2]/div[2]/div[1]/div/iron-icon[1]").click()

        global process1_running;
        Style_Gan_Model.process1_running = False

    def store_stylegan1_outputs(self):
        if Style_Gan_Model.process1_running == True:
            print("process in progress...")
        elif os.path.exists('C:\\Users\\SYS\\Downloads\\AI images\\content\\stylegan\\images\\'):
            subprocess.Popen(r'explorer /open,"C:\Users\SYS\Downloads\AI images\content\stylegan\images\"')
        else:
            with zipfile.ZipFile("C:\\Users\\SYS\\Downloads\\stylegan1-Images.zip", 'r') as zip_ref:
                zip_ref.extractall("C:\\Users\\SYS\\Downloads\\AI images")
            time.sleep(2)
            os.remove("C:\\Users\\SYS\\Downloads\\stylegan1-Images.zip")
            subprocess.Popen(r'explorer /open,"C:\Users\SYS\Downloads\AI images\content\stylegan\images\"')

    def run_style_gan2(self,starting_image_index, last_image_index,dataset,widgets):
        global driver;
        global process2_running;
        Style_Gan_Model.process2_running = True
        widgets.progress_number_2.display(0)
        widgets.genrated_images_count_stylegan2.display(0)
        widgets.stylegan2_hours.display(0)
        widgets.stylegan2_minutes.display(0)
        widgets.style_gan_plabel_2.setPixmap('')
        # Start time of run
        start_time = time.time()
        handle_of_the_window = Style_Gan_Model.driver.current_window_handle
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        # Opens a new tab and switches to new tab
        #Style_Gan_Model.driver.switch_to.new_window('tab')
        Style_Gan_Model.driver.get("https://colab.research.google.com/drive/1lUJdcFmPPaY6ZsMyF2cuO7LRC5H2XxH_?usp=sharing")
        time.sleep(3)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        first_img_no = Style_Gan_Model.driver.find_element(By.XPATH,
            "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[8]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]/div[1]/span/span")
        first_img_no.click()
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(str(starting_image_index)).perform()
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        last_img_no = Style_Gan_Model.driver.find_element(By.XPATH,
            "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[8]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]/div[2]/span/span")
        last_img_no.click()
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(str(last_image_index)).perform()
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        network = Style_Gan_Model.driver.find_element(By.XPATH,
            "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[8]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]/div[3]/span/span")
        network.click()
        dataset = f'''"{dataset}"'''
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(Keys.ARROW_RIGHT).perform()
        # ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.SEPARATOR).key_up(Keys.CONTROL).key_up(Keys.RETURN).perform()
        ActionChains(Style_Gan_Model.driver).send_keys(dataset).perform()
        time.sleep(3)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        runtime_butn = Style_Gan_Model.driver.find_element(By.XPATH,
            "/html/body/div[7]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/div/div/div[1]")
        runtime_butn.click()
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
            run_anyway = Style_Gan_Model.driver.find_element(By.ID,"ok")
            run_anyway.click()

        while (True):
            Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
            time.sleep(0.5)
            if Style_Gan_Model.check_exists("XPATH",
                            '/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[10]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/iframe'):
                iframe = Style_Gan_Model.driver.find_element(By.XPATH,
                    "/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[10]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/iframe")
                Style_Gan_Model.driver.switch_to.frame(iframe)
                print("iframe found")
                break

        widgets.style_gan_plabel_2.raise_()
        widgets.loading_label_dst_2.setMovie(self.tick_gif_2)

        widgets.style_gan_plabel_2.setMovie(self.dst_gif_2)
        widgets.progress_number_2.raise_()

        images_size = int(int(last_image_index) - int(starting_image_index))
        gen_img_units = int(100 / images_size);
        images_generated = 0
        while (images_generated != images_size):
            if Style_Gan_Model.check_exists("XPATH", "/html/body/div[2]/progress"):
                progress = Style_Gan_Model.driver.find_element_by_xpath("/html/body/div[2]/progress")
                max = progress.get_attribute("max")
                value = progress.get_attribute("value")
                progress_percent = int((int(value) / int(max)) * 100)
                images_generated = int(progress_percent / gen_img_units)
                widgets.progress_number_2.display(int(progress_percent))
                widgets.genrated_images_count_stylegan2.display(images_generated)

                # Updating training time
                training_time_in_secs = float(time.time() - start_time)
                secs = training_time_in_secs % (24 * 3600)
                training_time_in_hours = secs // 3600
                secs %= 3600
                training_time_in_minutes = secs // 60
                widgets.stylegan2_hours.display(training_time_in_hours)
                widgets.stylegan2_minutes.display(training_time_in_minutes)

        widgets.progress_number_2.lower()
        widgets.loading_label_dst_2.setPixmap(self.tick_2)
        widgets.style_gan_plabel_2.setPixmap(self.tick_2)
        self.dst_gif_2.stop()
        self.tick_gif_2.stop()
        time.sleep(3)
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        # Switching driver settings to default browser window
        Style_Gan_Model.driver.switch_to.default_content()
        Style_Gan_Model.driver.switch_to.window(handle_of_the_window)
        time.sleep(0.5)
        Style_Gan_Model.driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[10]/div[2]/div[2]/div[2]/div[2]/div[1]/div/iron-icon[1]").click()
        global process2_running;
        Style_Gan_Model.process2_running = False

    def store_stylegan2_outputs(self):
        if Style_Gan_Model.process2_running == True:
            print("process in progress...")
        elif os.path.exists('C:\\Users\\SYS\\Downloads\\AI Images\\content\\results\\00000-generate-images\\'):
            subprocess.Popen(r'explorer /open,"C:\Users\SYS\Downloads\AI Images\content\results\00000-generate-images\"')
        else:
            with zipfile.ZipFile("C:\\Users\\SYS\\Downloads\\stylegan2-Images.zip", 'r') as zip_ref:
                zip_ref.extractall("C:\\Users\\SYS\\Downloads\\AI images")
            time.sleep(2)
            os.remove("C:\\Users\\SYS\\Downloads\\stylegan2-Images.zip")
            subprocess.Popen(r'explorer /open,"C:\Users\SYS\Downloads\AI Images\content\results\00000-generate-images\"')
            Style_Gan_Model.store_style2_output_images(self)

    def download_from_gdrive(self):
        pass

    def selected_dataset(self,widgets):
        if widgets.selected_dst_style1.currentText() == "human":
            dataset = "ffhq_network"
        elif widgets.selected_dst_style1.currentText() == "celebrity":
            dataset = "celeba_network"
        elif widgets.selected_dst_style1.currentText() == "cats":
            dataset = "cats_network"
        elif widgets.selected_dst_style1.currentText() == "cars":
            dataset = "cars_network"
        elif widgets.selected_dst_style1.currentText() == "bedrooms":
            dataset = "bedrooms_network"
        return dataset

    def selected_dataset_2(self,widgets):
        if widgets.selected_dst_style2.currentText() == "anime":
            dataset = "anime"
        elif widgets.selected_dst_style1.currentText() == "human":
            dataset = "human"
        elif widgets.selected_dst_style1.currentText() == "cat":
            dataset = "cat"
        elif widgets.selected_dst_style1.currentText() == "car":
            dataset = "car"
        elif widgets.selected_dst_style1.currentText() == "church":
            dataset = "church"
        elif widgets.selected_dst_style1.currentText() == "horse":
            dataset = "horse"
        return dataset

    def store_style1_output_images(self):
        # Using try/except blocks for exception handling
        # try block
        try:
            # Getting images names
            images_name = []
            for file in glob.glob("C:/Users/SYS/Downloads/AI images/content/stylegan/images/*.png"):
                f_name = file.rpartition('\\')[-1]
                images_name.append(f_name)

            # Getting images data from the output folder
            images = [cv2.imread(file) for file in glob.glob("C:/Users/SYS/Downloads/AI images/content/stylegan/images/*.png")]
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

    def store_style2_output_images(self):
        # Using try/except blocks for exception handling
        # try block
        try:
            # Getting images names
            images_name = []
            for file in glob.glob("C:/Users/SYS/Downloads/AI images/content/results/00000-generate-images/seed*.png"):
                f_name = file.rpartition('\\')[-1]
                images_name.append(f_name)

            # Getting images data from the output folder
            images = [cv2.imread(file) for file in glob.glob("C:/Users/SYS/Downloads/AI images/content/results/00000-generate-images/seed*.png")]
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

    def refresh_with_alert(driver):

        # wrap this in try / except so the whole code does not fail if alert is not present
        try:
            # attempt to refresh
            driver.refresh()

            # wait until alert is present
            WebDriverWait(driver, 3).until(EC.alert_is_present())

            # switch to alert and accept it
            driver.switch_to.alert.accept()

        except TimeoutException:
            print("No alert was present.")


