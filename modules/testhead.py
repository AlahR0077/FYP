import re

import undetected_chromedriver.v2 as uc
from selenium.common.exceptions import NoSuchElementException
import threading
import zipfile
import subprocess
import random,time,os,sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

GMAIL = 'syedawaisk'
PASSWORD = 'jameskazmi1'

chrome_options = uc.ChromeOptions()

chrome_options.add_argument("--disable-extensions")

chrome_options.add_argument("--disable-popup-blocking")

chrome_options.add_argument("--profile-directory=Default")
# chrome_options.add_argument("--ignore-certificate-errors")

chrome_options.add_argument("--disable-plugins-discovery")

# chrome_options.add_argument("--incognito")

chrome_options.add_argument("user_agent=DN")
# chrome_options.add_argument("--headless")

driver = uc.Chrome(options=chrome_options)
driver.delete_all_cookies()

login_success = False
def google_login():

    driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(GMAIL)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(Keys.RETURN)
    time.sleep(3)

    # enter google password
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(PASSWORD)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(Keys.RETURN)
    time.sleep(3)
    def check_exists(selector, value):
        try:
            if selector == "ID":
                driver.find_element_by_id(value)
            elif selector == "XPATH":
                driver.find_element_by_xpath(value)
        except NoSuchElementException:
            return False
        return True

    if check_exists("XPATH", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[5]/div"):
        print("found")
        time.sleep(2)
        verify_gaccount = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[5]/div")
        verify_gaccount.click()

    elif check_exists("XPATH", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button"):
        time.sleep(2)
        verify_gaccount = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
        verify_gaccount.click()

    time.sleep(4)
    global login_success;
    login_success = True
    time.sleep(1000)

def verify_code(code):
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(code)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(Keys.RETURN)
    time.sleep(3)
    def check_exists(selector, value):
        try:
            if selector == "ID":
                driver.find_element_by_id(value)
            elif selector == "XPATH":
                driver.find_element_by_xpath(value)
        except NoSuchElementException:
            return False
        return True

    if check_exists("XPATH", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[2]/div"):
        print("Wrong code entered")
        time.sleep(2)
        input_gaccount = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div/div[1]/input")
        input_gaccount.click()


def generate_images(images_size,dataset):
    driver.get("https://colab.research.google.com/drive/1vetN2gygCFT10i4dhlalDRSlSfCmkRzR#scrollTo=EKlzPpXYzh_Y")

    time.sleep(7)

    runtime_butn = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]")
    runtime_butn.click()
    time.sleep(2)
    run_all = driver.find_element_by_xpath("/html/body/div[13]/div[1]/div/span")
    run_all.click()

    time.sleep(2)

    def check_exists(selector, value):
        try:
            if selector == "ID":
                driver.find_element_by_id(value)
            elif selector == "XPATH":
                driver.find_element_by_xpath(value)
        except NoSuchElementException:
            return False
        return True

    if check_exists("ID", "ok"):
        print("found")
        time.sleep(2)
        run_anyway = driver.find_element_by_id("ok")
        run_anyway.click()

    while (True):
        if check_exists("XPATH",'/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[14]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/iframe'):
            iframe = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[14]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/iframe")
            driver.switch_to.frame(iframe)
            print("iframe found")
            break
    time.sleep(3)
    while (True):
        if check_exists("XPATH",'/html/body/div/div/div/div/input'):
            content_img = driver.find_element_by_xpath("/html/body/div/div/div/div/input")
            print("bc found")
            ActionChains(driver).move_to_element(content_img).perform()
            ActionChains(driver).click(content_img).perform()
            break

    while (True):
        if check_exists("XPATH",'/html/body/div/div/div[1]/div/output/li/span[1]'):
            content_img_name = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/output/li/span[1]")
            c_name = content_img_name.text
            print("name found")
            break
    time.sleep(2)
    while (True):
        if driver.find_element_by_xpath("/html/body/div/div/div[1]/div/output/li/span[3]").text == "100% done":
            break
        percentage = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/output/li/span[3]").text
        print(percentage)
        time.sleep(0.5)
    # Switching driver settings to default browser window
    driver.switch_to.default_content()
    while (True):
        if check_exists("XPATH",'/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[15]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/iframe'):
            iframe = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[15]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/iframe")
            driver.switch_to.frame(iframe)
            print("iframe 2 found")
            break
    time.sleep(3)
    while (True):
        if check_exists("XPATH",'/html/body/div/div/div/div/input'):
            style_img = driver.find_element_by_xpath("/html/body/div/div/div/div/input")
            print("bc 2 found")
            ActionChains(driver).click(style_img).perform()
            #ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
            break
    while (True):
        if check_exists("XPATH",'/html/body/div/div/div[1]/div/output/li/span[1]'):
            style_img_name = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/output/li/span[1]")
            s_name = style_img_name.text
            print("name 2 found")
            break


    while (True):
        if check_exists("XPATH","/html/body/div/div/div[1]/div/output/li/span[3]"):
            # Switching driver settings to default browser window
            driver.switch_to.default_content()
            driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[14]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]/div[2]").click()
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[14]/div[1]/colab-cell-toolbar/paper-icon-button[8]").click()
            print("del")
            break

    cname = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[15]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]/div[1]/span/span")
    cname.click()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(c_name).perform()
    time.sleep(1)
    sname = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[15]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]/div[2]/span/span")
    sname.click()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    ActionChains(driver).send_keys(s_name).perform()

    driver.switch_to.frame(iframe)
    while (True):
        if driver.find_element_by_xpath("/html/body/div/div/div[1]/div/output/li/span[3]").text == "100% done":
            # Switching driver settings to default browser window
            driver.switch_to.default_content()
            driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[14]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]").click()
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[14]/div[1]/colab-cell-toolbar/paper-icon-button[8]").click()
            print("del--2")
            break
        percentage = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/output/li/span[3]").text
        print(percentage)
        time.sleep(0.5)
    time.sleep(5)
    runtime_butn = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]")
    runtime_butn.click()
    time.sleep(2)
    run_all = driver.find_element_by_xpath("/html/body/div[13]/div[1]/div/span")
    run_all.click()
    time.sleep(2)
    while (True):
        if check_exists("XPATH","/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[59]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/iframe"):
            iframe = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[59]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/iframe")
            driver.switch_to.frame(iframe)
            break

    while (True):
        if check_exists("XPATH","/html/body/div/div/div[2]/div/pre"):
            try:
                progress_1 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/pre").text
            except:
                pass
            print(progress_1)
            time.sleep(1)
            if re.search("1000",progress_1):
                break
    time.sleep(1)
    driver.switch_to.default_content()
    while (True):
        if check_exists("XPATH","/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[77]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/iframe"):
            iframe = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[77]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/iframe")
            driver.switch_to.frame(iframe)
            break

    while (True):
        if check_exists("XPATH", "/html/body/div/div/div[2]/div/pre"):
            try:
                progress_2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/pre").text
            except:
                pass
            print(progress_2)
            time.sleep(1)
            if re.search("1000", progress_2):
                break
    time.sleep(1)
    driver.switch_to.default_content()
    while (True):
        if check_exists("XPATH","/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[79]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/iframe"):
            iframe = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[79]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/iframe")
            driver.switch_to.frame(iframe)
            break

    progress_percent = 0
    while (progress_percent != 100):
        if check_exists("XPATH", "/html/body/div[2]/progress"):
            progress = driver.find_element_by_xpath("/html/body/div[2]/progress")
            max = progress.get_attribute("max")
            value = progress.get_attribute("value")
            progress_percent = int((int(value) / int(max)) * 100)
            print("progress = " + str(progress_percent) + " %")

    # Switching driver settings to default browser window
    driver.switch_to.default_content()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[80]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]").click()
    ActionChains(driver).send_keys('!rm ''"{content_img_name}"''').perform()
    ActionChains(driver).send_keys(Keys.RETURN).perform()
    ActionChains(driver).send_keys('!rm ''"{style_img_name}"''').perform()
    ActionChains(driver).send_keys(Keys.RETURN).perform()
    ActionChains(driver).send_keys('!rm ''"{file_name}"''').perform()
    driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/colab-tab-layout-container/colab-tab/div/colab-shaded-scroller/div/div[1]/div/div[2]/div[80]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button").click()

    time.sleep(500)
    t4.start()

def extract_images():
    with zipfile.ZipFile("C:\\Users\\SYS\\Downloads\\stylegan1-Images.zip", 'r') as zip_ref:
        zip_ref.extractall("C:\\Users\\SYS\\Downloads\\AI images")
    time.sleep(2)
    os.remove("C:\\Users\\SYS\\Downloads\\stylegan1-Images.zip")
    subprocess.Popen(r'explorer /open,"C:\Users\SYS\Downloads\AI images\content\stylegan\images\"')

def print_hi():
    while(True):
        global login_success;
        if (login_success):
            print("login_success")
            t3.start()
            break

t1 = threading.Thread(target=google_login)
t2 = threading.Thread(target=print_hi)
t3 = threading.Thread(target=generate_images,args=[5,"ffhq_network"]) #ffhq_network #celeba_network #cats_network #cars_network #bedrooms_network
t4 = threading.Thread(target=extract_images)
t1.start()
t2.start()

