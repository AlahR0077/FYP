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

# PySide Package Import
# ///////////////////////////////////////////////////////////////
import PySide6
from PySide6 import QtCore

# Imports from MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *

# AppFunctions Class
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):

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
        self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")

    # Function for the User Login
    # ///////////////////////////////////////////////////////////////
    def login(self, username, password):

        # Finding the User in the Database
        exists = users.find_one({"name": username})

        # If User Exists in the Database
        if exists:

            # Decrypting the Hashed Passsword and Matching
            if bcrypt.hashpw(password.encode('utf-8'), exists['password']) == exists['password']:
                return 'Logged successfully'

            # Wrong Password
            return 'The password is incorrect!'

        # If User Doesn't Exist in the Database
        return "The user doesn't exists!"

    # Function for the User Logout
    # ///////////////////////////////////////////////////////////////
    def logout(self, username):

        # Finding the User in the Database
        exists = users.find_one({"name": username})

        # If User Exists in the Database
        if exists:
            return 'Logged out successfully'

        # If User Doesn't Exist in the Database
        return "The user doesn't exists!"

    # Function for the User Registration
    # ///////////////////////////////////////////////////////////////
    def register(self, username, email, password, confirm_password,profile_image):

        # Setting User Name Acceptable Pattern
        username_pattern = '[a-zA-Z][a-zA-Z0-9]{3,7}$'

        # Setting a Boolean Variable for User Name Match With the Acceptable Name Pattern
        u_result = re.match(username_pattern, username)

        # If User Name Not Matches the Acceptable Name Pattern
        if u_result is None:
            return "Username Search Unsuccessful"

        # If User Name is Already Registered in the Database
        already_exists = users.find_one({"name": username})
        if already_exists:
            return 'The user already exists!'

        # Setting Email Acceptable Pattern
        email_pattern = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

        # Setting a Boolean Variable for Email Match With the Acceptable Email Pattern
        e_result = re.match(email_pattern, email)

        # If User Email Not Matches the Acceptable Email Pattern
        if e_result is None:
            return "Email Search Unsuccessful"

        # Setting Password Acceptable Pattern
        password_pattern = '^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,15}$'

        # Setting a Boolean Variable for Password Match With the Acceptable Password Pattern
        p_result = re.match(password_pattern, password)

        # If User Password Not Matches the Acceptable Password Pattern
        if p_result is None:
            return "Password Search Unsuccessful"

        # If User Password Not Matches the Confirmed Password Field
        if password != confirm_password:
            return "Pass Confirmed Unsuccessful"

        # Converting the Profile Picture Data to Bytes for Database Storage
        profile_pic = AppFunctions.convert_pixmap_to_bytes(self, profile_image)

        # Encrypting the Password to Hashed Passsword for Hacker Attacks
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Storing the Correct Sign Up Form Data in the MongoDB Database
        users.insert_one({"name": username, "email": email, "password": hash_password, "profile_pic" : profile_pic, "verified_account": False})

        # Return registration success message
        return 'Registered successfully'

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
        if pixmap_bytes=="":
            return "./images/images/LogoW.png"

        # Using QByteArray
        ba = QtCore.QByteArray(pixmap_bytes)
        pixmap = QtGui.QPixmap()
        ok = pixmap.loadFromData(ba, "PNG")
        assert ok
        print(type(pixmap))
        #  return converted data in pixmap form
        return pixmap

    # Function for Finding User By Email Address
    # ///////////////////////////////////////////////////////////////
    def find_user_by_email(self, email):

        #  finding user by email in the database
        user = users.find_one({"email": email})

        #  if the user found in the database
        if user:
            # return User document
            return user
        #  if the user not found in the database
        return "The user doesn't exists!"

    # Function for Finding User By Name
    # ///////////////////////////////////////////////////////////////
    def find_user_by_name(self, name):

        #  finding user by name in the database
        user = users.find_one({"name": name})

        #  if the user found in the database
        if user:
            # return User document
            return user
        #  if the user not found in the database
        return "The user doesn't exists!"

    # Function for Sending the forgotten User Credentials by Email
    # ///////////////////////////////////////////////////////////////
    def send_user_details_to_email(self, email):

        # creating an instance of EmailMessage() Class
        msg = EmailMessage()

        # setting Email Subject and Sender and Receiver Address
        msg['subject'] = "AI Images: Forgot Credentials"
        msg['From'] = host_user
        msg['To'] = email
        # setting Email Content
        msg.set_content('Remember your credentials!')
        # setting HTML Email Template
        html = """\
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
         <head> 
          <meta charset="UTF-8"> 
          <meta content="width=device-width, initial-scale=1" name="viewport"> 
          <meta name="x-apple-disable-message-reformatting"> 
          <meta http-equiv="X-UA-Compatible" content="IE=edge"> 
          <meta content="telephone=no" name="format-detection"> 
          <title>New message</title> 
          <!--[if (mso 16)]>
            <style type="text/css">
            a {text-decoration: none;}
            </style>
            <![endif]--> 
          <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]--> 
          <!--[if gte mso 9]>
        <xml>
            <o:OfficeDocumentSettings>
            <o:AllowPNG></o:AllowPNG>
            <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
        </xml>
        <![endif]--> 
          <style type="text/css">
        #outlook a {
        	padding:0;
        }
        .ExternalClass {
        	width:100%;
        }
        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
        	line-height:100%;
        }
        .es-button {
        	mso-style-priority:100!important;
        	text-decoration:none!important;
        }
        a[x-apple-data-detectors] {
        	color:inherit!important;
        	text-decoration:none!important;
        	font-size:inherit!important;
        	font-family:inherit!important;
        	font-weight:inherit!important;
        	line-height:inherit!important;
        }
        .es-desk-hidden {
        	display:none;
        	float:left;
        	overflow:hidden;
        	width:0;
        	max-height:0;
        	line-height:0;
        	mso-hide:all;
        }
        [data-ogsb] .es-button {
        	border-width:0!important;
        	padding:6px 25px 6px 25px!important;
        }
        @media only screen and (max-width:600px) {p, ul li, ol li, a { line-height:150%!important } h1 { font-size:30px!important; text-align:center; line-height:120%!important } h2 { font-size:26px!important; text-align:center; line-height:120%!important } h3 { font-size:20px!important; text-align:center; line-height:120%!important } .es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a { font-size:30px!important } .es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a { font-size:26px!important } .es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a { font-size:20px!important } .es-menu td a { font-size:16px!important } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:16px!important } .es-content-body p, .es-content-body ul li, .es-content-body ol li, .es-content-body a { font-size:16px!important } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:16px!important } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:12px!important } *[class="gmail-fix"] { display:none!important } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 { text-align:center!important } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right!important } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left!important } .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img { display:inline!important } .es-button-border { display:inline-block!important } a.es-button, button.es-button { font-size:20px!important; display:inline-block!important; border-width:6px 25px 6px 25px!important } .es-btn-fw { border-width:10px 0px!important; text-align:center!important } .es-adaptive table, .es-btn-fw, .es-btn-fw-brdr, .es-left, .es-right { width:100%!important } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%!important; max-width:600px!important } .es-adapt-td { display:block!important; width:100%!important } .adapt-img { width:100%!important; height:auto!important } .es-m-p0 { padding:0px!important } .es-m-p0r { padding-right:0px!important } .es-m-p0l { padding-left:0px!important } .es-m-p0t { padding-top:0px!important } .es-m-p0b { padding-bottom:0!important } .es-m-p20b { padding-bottom:20px!important } .es-mobile-hidden, .es-hidden { display:none!important } tr.es-desk-hidden, td.es-desk-hidden, table.es-desk-hidden { width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important } tr.es-desk-hidden { display:table-row!important } table.es-desk-hidden { display:table!important } td.es-desk-menu-hidden { display:table-cell!important } .es-menu td { width:1%!important } table.es-table-not-adapt, .esd-block-html table { width:auto!important } table.es-social { display:inline-block!important } table.es-social td { display:inline-block!important } }
        </style>
         </head>
         <body style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
          <div class="es-wrapper-color" style="background-color:#FFFFFF">
           <!--[if gte mso 9]>
        			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
        				<v:fill type="tile" color="#ffffff"></v:fill>
        			</v:background>
        		<![endif]-->
           <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top">
             <tr style="border-collapse:collapse">
              <td valign="top" style="padding:0;Margin:0">
               <table class="es-content" align="center" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
                 <tr style="border-collapse:collapse">
                  <td align="center" style="padding:0;Margin:0">
                   <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;border-top:1px solid transparent;border-right:1px solid transparent;border-left:1px solid transparent;width:700px;border-bottom:1px solid transparent" align="center" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
                     <tr style="border-collapse:collapse">
                      <td align="left" style="Margin:0;padding-top:20px;padding-bottom:40px;padding-left:40px;padding-right:40px">
                       <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                         <tr style="border-collapse:collapse">
                          <td align="left" style="padding:0;Margin:0;width:618px">
                           <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                             <tr style="border-collapse:collapse">
                              <td class="es-m-txt-c" align="center" style="padding:0;Margin:0;padding-bottom:5px;font-size:0px"><img src="https://pnchdt.stripocdn.email/content/guids/CABINET_c82d8daa906439489f01b6ac8e5a8e10/images/43101620675473411.png" alt="icon" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" title="icon" width="140" height="91"></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td align="center" style="padding:20px;Margin:0;font-size:0">
                               <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                 <tr style="border-collapse:collapse">
                                  <td style="padding:0;Margin:0;border-bottom:1px solid #CCCCCC;background:none;height:1px;width:100%;margin:0px"></td>
                                 </tr>
                               </table></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td class="es-m-txt-c" align="center" style="padding:0;Margin:0"><h2 style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#333333">Hey there!</h2></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td class="es-m-txt-c" align="center" style="padding:0;Margin:0;padding-top:15px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:24px;color:#333333;font-size:16px">We have received a request to remind you, your login credentials <br> Email : <strong>$code</strong></br> <br> User Name : <strong>$code_username</strong></br>. <br>If you want to change your password, please confirm by clicking the button below.</br></p></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td align="center" style="Margin:0;padding-left:10px;padding-right:10px;padding-bottom:15px;padding-top:20px"><span class="es-button-border" style="border-style:solid;border-color:#474745;background:#E22C1A;border-width:0px;display:inline-block;border-radius:20px;width:auto"><a href="mailto:awaiskfiverr@gmail.com?subject=NewPassword&body=By sending the confirmation message, your request for a new password will be received!" class="es-button" target="_blank" style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#EFEFEF;font-size:20px;border-style:solid;border-color:#E22C1A;border-width:6px 25px 6px 25px;display:inline-block;background:#E22C1A;border-radius:20px;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;font-weight:normal;font-style:normal;line-height:24px;width:auto;text-align:center;border-left-width:25px;border-right-width:25px">Set New Password</a></span></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td align="center" style="padding:20px;Margin:0;font-size:0">
                               <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                 <tr style="border-collapse:collapse">
                                  <td style="padding:0;Margin:0;border-bottom:1px solid #CCCCCC;background:none;height:1px;width:100%;margin:0px"></td>
                                 </tr>
                               </table></td>
                             </tr>
                           </table></td>
                         </tr>
                       </table></td>
                     </tr>
                   </table></td>
                 </tr>
               </table>
               <table class="es-content" align="center" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
                 <tr style="border-collapse:collapse">
                  <td align="center" style="padding:0;Margin:0">
                   <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:700px" align="center" cellspacing="0" cellpadding="0">
                     <tr style="border-collapse:collapse">
                      <td align="left" style="Margin:0;padding-left:20px;padding-right:20px;padding-top:30px;padding-bottom:30px">
                       <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                         <tr style="border-collapse:collapse">
                          <td align="center" valign="top" style="padding:0;Margin:0;width:660px">
                           <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                             <tr style="border-collapse:collapse">
                              <td align="center" style="padding:0;Margin:0;font-size:0px"><img class="adapt-img" src="https://pnchdt.stripocdn.email/content/guids/CABINET_c82d8daa906439489f01b6ac8e5a8e10/images/43101620675473411.png" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" height="142" width="219"></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td align="center" style="padding:0;Margin:0"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">@ AI IMAGES 2021</p></td>
                             </tr>
                           </table></td>
                         </tr>
                       </table></td>
                     </tr>
                   </table></td>
                 </tr>
               </table></td>
             </tr>
           </table>
          </div>
          <div style="position:absolute;left:-9999px;top:-9999px;margin:0px"></div>
         </body>
        </html>
        """
        # finding user by email
        user = AppFunctions.find_user_by_email(self, email)
        # setting message template and embedded variables
        mailmsg = Template(html).safe_substitute(code=email, code_username=user["name"])
        # setting mail message alternative
        msg.add_alternative(mailmsg, subtype="html")
        # sending email using SMTP Service
        smtp.send_message(msg)

    # Function for Sending Verification Email for Account Activation
    # ///////////////////////////////////////////////////////////////
    def send_verify_email_to_user_email(self, email):

        # creating an instance of EmailMessage() Class
        msg = EmailMessage()
        # setting Email Subject and Sender and Receiver Address
        msg['subject'] = "AI Images: Confirm Your Account"
        msg['From'] = host_user
        msg['To'] = email
        # setting Email Content
        msg.set_content('Confirm your email!')
        # setting HTML Email Template
        html = """\
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
         <head> 
          <meta charset="UTF-8"> 
          <meta content="width=device-width, initial-scale=1" name="viewport"> 
          <meta name="x-apple-disable-message-reformatting"> 
          <meta http-equiv="X-UA-Compatible" content="IE=edge"> 
          <meta content="telephone=no" name="format-detection"> 
          <title>New message</title> 
          <!--[if (mso 16)]>
            <style type="text/css">
            a {text-decoration: none;}
            </style>
            <![endif]--> 
          <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]--> 
          <!--[if gte mso 9]>
        <xml>
            <o:OfficeDocumentSettings>
            <o:AllowPNG></o:AllowPNG>
            <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
        </xml>
        <![endif]--> 
          <style type="text/css">
        #outlook a {
        	padding:0;
        }
        .ExternalClass {
        	width:100%;
        }
        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
        	line-height:100%;
        }
        .es-button {
        	mso-style-priority:100!important;
        	text-decoration:none!important;
        }
        a[x-apple-data-detectors] {
        	color:inherit!important;
        	text-decoration:none!important;
        	font-size:inherit!important;
        	font-family:inherit!important;
        	font-weight:inherit!important;
        	line-height:inherit!important;
        }
        .es-desk-hidden {
        	display:none;
        	float:left;
        	overflow:hidden;
        	width:0;
        	max-height:0;
        	line-height:0;
        	mso-hide:all;
        }
        [data-ogsb] .es-button {
        	border-width:0!important;
        	padding:6px 25px 6px 25px!important;
        }
        @media only screen and (max-width:600px) {p, ul li, ol li, a { line-height:150%!important } h1 { font-size:30px!important; text-align:center; line-height:120%!important } h2 { font-size:26px!important; text-align:center; line-height:120%!important } h3 { font-size:20px!important; text-align:center; line-height:120%!important } .es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a { font-size:30px!important } .es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a { font-size:26px!important } .es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a { font-size:20px!important } .es-menu td a { font-size:16px!important } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:16px!important } .es-content-body p, .es-content-body ul li, .es-content-body ol li, .es-content-body a { font-size:16px!important } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:16px!important } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:12px!important } *[class="gmail-fix"] { display:none!important } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 { text-align:center!important } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right!important } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left!important } .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img { display:inline!important } .es-button-border { display:inline-block!important } a.es-button, button.es-button { font-size:20px!important; display:inline-block!important; border-width:6px 25px 6px 25px!important } .es-btn-fw { border-width:10px 0px!important; text-align:center!important } .es-adaptive table, .es-btn-fw, .es-btn-fw-brdr, .es-left, .es-right { width:100%!important } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%!important; max-width:600px!important } .es-adapt-td { display:block!important; width:100%!important } .adapt-img { width:100%!important; height:auto!important } .es-m-p0 { padding:0px!important } .es-m-p0r { padding-right:0px!important } .es-m-p0l { padding-left:0px!important } .es-m-p0t { padding-top:0px!important } .es-m-p0b { padding-bottom:0!important } .es-m-p20b { padding-bottom:20px!important } .es-mobile-hidden, .es-hidden { display:none!important } tr.es-desk-hidden, td.es-desk-hidden, table.es-desk-hidden { width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important } tr.es-desk-hidden { display:table-row!important } table.es-desk-hidden { display:table!important } td.es-desk-menu-hidden { display:table-cell!important } .es-menu td { width:1%!important } table.es-table-not-adapt, .esd-block-html table { width:auto!important } table.es-social { display:inline-block!important } table.es-social td { display:inline-block!important } }
        </style>
         </head>
         <body style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
          <div class="es-wrapper-color" style="background-color:#FFFFFF">
           <!--[if gte mso 9]>
        			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
        				<v:fill type="tile" color="#ffffff"></v:fill>
        			</v:background>
        		<![endif]-->
           <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top">
             <tr style="border-collapse:collapse">
              <td valign="top" style="padding:0;Margin:0">
               <table class="es-content" align="center" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
                 <tr style="border-collapse:collapse">
                  <td align="center" style="padding:0;Margin:0">
                   <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;border-top:1px solid transparent;border-right:1px solid transparent;border-left:1px solid transparent;width:700px;border-bottom:1px solid transparent" align="center" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
                     <tr style="border-collapse:collapse">
                      <td align="left" style="Margin:0;padding-top:20px;padding-bottom:40px;padding-left:40px;padding-right:40px">
                       <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                         <tr style="border-collapse:collapse">
                          <td align="left" style="padding:0;Margin:0;width:618px">
                           <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                             <tr style="border-collapse:collapse">
                              <td class="es-m-txt-c" align="center" style="padding:0;Margin:0;padding-bottom:5px;font-size:0px"><img src="https://pnchdt.stripocdn.email/content/guids/CABINET_c82d8daa906439489f01b6ac8e5a8e10/images/43101620675473411.png" alt="icon" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" title="icon" width="140" height="91"></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td align="center" style="padding:20px;Margin:0;font-size:0">
                               <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                 <tr style="border-collapse:collapse">
                                  <td style="padding:0;Margin:0;border-bottom:1px solid #CCCCCC;background:none;height:1px;width:100%;margin:0px"></td>
                                 </tr>
                               </table></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td class="es-m-txt-c" align="center" style="padding:0;Margin:0"><h2 style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#333333">Hey there!</h2></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td class="es-m-txt-c" align="center" style="padding:0;Margin:0;padding-top:15px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:24px;color:#333333;font-size:16px">We have received a request to set your email to <strong>$code</strong>. If this is correct, please confirm by clicking the button below. If you don’t know why you got this email, please tell us straight away so we can fix this for you.</p></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td align="center" style="Margin:0;padding-left:10px;padding-right:10px;padding-bottom:15px;padding-top:20px"><span class="es-button-border" style="border-style:solid;border-color:#474745;background:#E22C1A;border-width:0px;display:inline-block;border-radius:20px;width:auto"><a href="mailto:awaiskfiverr@gmail.com?subject=ActivateMe&body=By sending the confirmation message, your account will be activated!" class="es-button" target="_blank" style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#EFEFEF;font-size:20px;border-style:solid;border-color:#E22C1A;border-width:6px 25px 6px 25px;display:inline-block;background:#E22C1A;border-radius:20px;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;font-weight:normal;font-style:normal;line-height:24px;width:auto;text-align:center;border-left-width:25px;border-right-width:25px">Confirm Email</a></span></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td align="center" style="padding:20px;Margin:0;font-size:0">
                               <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                 <tr style="border-collapse:collapse">
                                  <td style="padding:0;Margin:0;border-bottom:1px solid #CCCCCC;background:none;height:1px;width:100%;margin:0px"></td>
                                 </tr>
                               </table></td>
                             </tr>
                           </table></td>
                         </tr>
                       </table></td>
                     </tr>
                   </table></td>
                 </tr>
               </table>
               <table class="es-content" align="center" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
                 <tr style="border-collapse:collapse">
                  <td align="center" style="padding:0;Margin:0">
                   <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:700px" align="center" cellspacing="0" cellpadding="0">
                     <tr style="border-collapse:collapse">
                      <td align="left" style="Margin:0;padding-left:20px;padding-right:20px;padding-top:30px;padding-bottom:30px">
                       <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                         <tr style="border-collapse:collapse">
                          <td align="center" valign="top" style="padding:0;Margin:0;width:660px">
                           <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                             <tr style="border-collapse:collapse">
                              <td align="center" style="padding:0;Margin:0;font-size:0px"><img class="adapt-img" src="https://pnchdt.stripocdn.email/content/guids/CABINET_c82d8daa906439489f01b6ac8e5a8e10/images/43101620675473411.png" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" height="142" width="219"></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td align="center" style="padding:0;Margin:0"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">@ AI IMAGES 2021</p></td>
                             </tr>
                           </table></td>
                         </tr>
                       </table></td>
                     </tr>
                   </table></td>
                 </tr>
               </table></td>
             </tr>
           </table>
          </div>
          <div style="position:absolute;left:-9999px;top:-9999px;margin:0px"></div>
         </body>
        </html>
        """
        # setting message template and embedded variables
        mailmsg = Template(html).safe_substitute(code=email)
        # setting mail message alternative
        msg.add_alternative(mailmsg, subtype="html")
        # sending email using SMTP Service
        smtp.send_message(msg)

    # Function for Sending User Feedback
    # ///////////////////////////////////////////////////////////////
    def send_feedback(self, email, feedback):

        # creating an instance of EmailMessage() Class
        msg = EmailMessage()
        # setting Email Subject and Sender and Receiver Address
        msg['subject'] = "AI Images: User Feedback"
        msg['From'] = email
        msg['To'] = host_user
        # setting Email Content
        msg.set_content('User Feedback!')
        # setting HTML Email Template
        html = """\
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
         <head> 
          <meta charset="UTF-8"> 
          <meta content="width=device-width, initial-scale=1" name="viewport"> 
          <meta name="x-apple-disable-message-reformatting"> 
          <meta http-equiv="X-UA-Compatible" content="IE=edge"> 
          <meta content="telephone=no" name="format-detection"> 
          <title>New message</title> 
          <!--[if (mso 16)]>
            <style type="text/css">
            a {text-decoration: none;}
            </style>
            <![endif]--> 
          <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]--> 
          <!--[if gte mso 9]>
        <xml>
            <o:OfficeDocumentSettings>
            <o:AllowPNG></o:AllowPNG>
            <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
        </xml>
        <![endif]--> 
          <style type="text/css">
        #outlook a {
        	padding:0;
        }
        .ExternalClass {
        	width:100%;
        }
        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
        	line-height:100%;
        }
        .es-button {
        	mso-style-priority:100!important;
        	text-decoration:none!important;
        }
        a[x-apple-data-detectors] {
        	color:inherit!important;
        	text-decoration:none!important;
        	font-size:inherit!important;
        	font-family:inherit!important;
        	font-weight:inherit!important;
        	line-height:inherit!important;
        }
        .es-desk-hidden {
        	display:none;
        	float:left;
        	overflow:hidden;
        	width:0;
        	max-height:0;
        	line-height:0;
        	mso-hide:all;
        }
        [data-ogsb] .es-button {
        	border-width:0!important;
        	padding:6px 25px 6px 25px!important;
        }
        @media only screen and (max-width:600px) {p, ul li, ol li, a { line-height:150%!important } h1 { font-size:30px!important; text-align:center; line-height:120%!important } h2 { font-size:26px!important; text-align:center; line-height:120%!important } h3 { font-size:20px!important; text-align:center; line-height:120%!important } .es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a { font-size:30px!important } .es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a { font-size:26px!important } .es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a { font-size:20px!important } .es-menu td a { font-size:16px!important } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:16px!important } .es-content-body p, .es-content-body ul li, .es-content-body ol li, .es-content-body a { font-size:16px!important } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:16px!important } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:12px!important } *[class="gmail-fix"] { display:none!important } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 { text-align:center!important } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right!important } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left!important } .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img { display:inline!important } .es-button-border { display:inline-block!important } a.es-button, button.es-button { font-size:20px!important; display:inline-block!important; border-width:6px 25px 6px 25px!important } .es-btn-fw { border-width:10px 0px!important; text-align:center!important } .es-adaptive table, .es-btn-fw, .es-btn-fw-brdr, .es-left, .es-right { width:100%!important } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%!important; max-width:600px!important } .es-adapt-td { display:block!important; width:100%!important } .adapt-img { width:100%!important; height:auto!important } .es-m-p0 { padding:0px!important } .es-m-p0r { padding-right:0px!important } .es-m-p0l { padding-left:0px!important } .es-m-p0t { padding-top:0px!important } .es-m-p0b { padding-bottom:0!important } .es-m-p20b { padding-bottom:20px!important } .es-mobile-hidden, .es-hidden { display:none!important } tr.es-desk-hidden, td.es-desk-hidden, table.es-desk-hidden { width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important } tr.es-desk-hidden { display:table-row!important } table.es-desk-hidden { display:table!important } td.es-desk-menu-hidden { display:table-cell!important } .es-menu td { width:1%!important } table.es-table-not-adapt, .esd-block-html table { width:auto!important } table.es-social { display:inline-block!important } table.es-social td { display:inline-block!important } }
        </style>
         </head>
         <body style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
          <div class="es-wrapper-color" style="background-color:#FFFFFF">
           <!--[if gte mso 9]>
        			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
        				<v:fill type="tile" color="#ffffff"></v:fill>
        			</v:background>
        		<![endif]-->
           <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top">
             <tr style="border-collapse:collapse">
              <td valign="top" style="padding:0;Margin:0">
               <table class="es-content" align="center" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
                 <tr style="border-collapse:collapse">
                  <td align="center" style="padding:0;Margin:0">
                   <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;border-top:1px solid transparent;border-right:1px solid transparent;border-left:1px solid transparent;width:700px;border-bottom:1px solid transparent" align="center" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
                     <tr style="border-collapse:collapse">
                      <td align="left" style="Margin:0;padding-top:20px;padding-bottom:40px;padding-left:40px;padding-right:40px">
                       <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                         <tr style="border-collapse:collapse">
                          <td align="left" style="padding:0;Margin:0;width:618px">
                           <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                             <tr style="border-collapse:collapse">
                              <td class="es-m-txt-c" align="center" style="padding:0;Margin:0;padding-bottom:5px;font-size:0px"><img src="https://pnchdt.stripocdn.email/content/guids/CABINET_c82d8daa906439489f01b6ac8e5a8e10/images/43101620675473411.png" alt="icon" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" title="icon" width="140" height="91"></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td align="center" style="padding:20px;Margin:0;font-size:0">
                               <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                 <tr style="border-collapse:collapse">
                                  <td style="padding:0;Margin:0;border-bottom:1px solid #CCCCCC;background:none;height:1px;width:100%;margin:0px"></td>
                                 </tr>
                               </table></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td class="es-m-txt-c" align="center" style="padding:0;Margin:0"><h2 style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#333333">User Feedback!</h2><br><h3>User: $e_code</h3></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td class="es-m-txt-c" align="center" style="padding:0;Margin:0;padding-top:15px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:24px;color:#333333;font-size:16px"><strong>$code</strong></p></td>
                             </tr>
                             
                             <tr style="border-collapse:collapse">
                              <td align="center" style="padding:20px;Margin:0;font-size:0">
                               <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                 <tr style="border-collapse:collapse">
                                  <td style="padding:0;Margin:0;border-bottom:1px solid #CCCCCC;background:none;height:1px;width:100%;margin:0px"></td>
                                 </tr>
                               </table></td>
                             </tr>
                           </table></td>
                         </tr>
                       </table></td>
                     </tr>
                   </table></td>
                 </tr>
               </table>
               <table class="es-content" align="center" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
                 <tr style="border-collapse:collapse">
                  <td align="center" style="padding:0;Margin:0">
                   <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:700px" align="center" cellspacing="0" cellpadding="0">
                     <tr style="border-collapse:collapse">
                      <td align="left" style="Margin:0;padding-left:20px;padding-right:20px;padding-top:30px;padding-bottom:30px">
                       <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                         <tr style="border-collapse:collapse">
                          <td align="center" valign="top" style="padding:0;Margin:0;width:660px">
                           <table width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                             <tr style="border-collapse:collapse">
                              <td align="center" style="padding:0;Margin:0;font-size:0px"><img class="adapt-img" src="https://pnchdt.stripocdn.email/content/guids/CABINET_c82d8daa906439489f01b6ac8e5a8e10/images/43101620675473411.png" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" height="142" width="219"></td>
                             </tr>
                             <tr style="border-collapse:collapse">
                              <td align="center" style="padding:0;Margin:0"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">@ AI IMAGES 2021</p></td>
                             </tr>
                           </table></td>
                         </tr>
                       </table></td>
                     </tr>
                   </table></td>
                 </tr>
               </table></td>
             </tr>
           </table>
          </div>
          <div style="position:absolute;left:-9999px;top:-9999px;margin:0px"></div>
         </body>
        </html>
        """
        # setting message template and embedded variables
        mailmsg = Template(html).safe_substitute(code=feedback, e_code = email)
        # setting mail message alternative
        msg.add_alternative(mailmsg, subtype="html")
        # sending email using SMTP Service
        smtp.send_message(msg)

    # Function for Updating New User Password
    # ///////////////////////////////////////////////////////////////
    def update_new_password(self, new_password, confirm_new_password, email):

        # Setting Password Acceptable Pattern
        password_pattern = '^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,15}$'

        # Setting a Boolean Variable for Password Match With the Acceptable Password Pattern
        p_result = re.match(password_pattern, new_password)

        # If User Password Not Matches the Acceptable Password Pattern
        if p_result is None:
            return "Password Search Unsuccessful"

        # If User Password Not Matches the Confirmed Password Field
        if new_password != confirm_new_password:
            return "Pass Confirmed Unsuccessful"

        # Getting User email address from the email message template
        start = email.find("<") + len("<")
        end = email.find(">")
        substring = email[start:end]

        # Finding user by the email address
        user = AppFunctions.find_user_by_email(self, substring)
        # Encrpting the new Password to Prevent Hacker Access
        hash_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        # Updating new Hashed Password in the database
        users.update_one({"email": substring},{"$set": { "password": hash_password }})
        # returning the user name
        return (user["name"])

    # Function for Updating User Account Verification
    # ///////////////////////////////////////////////////////////////
    def update_account_verification(self, user_name):
        # Finding user name in the database and setting 'verfied_account' variable to TRUE
        users.update_one({"name": user_name},{"$set": { "verified_account": True }})
        return

    # Function for Updating User Profile Picture
    # ///////////////////////////////////////////////////////////////
    def update_profile_pic(self, user_name, profile_image):

        # Converting the picture data to bytes for database storage purpose
        profile_pic = AppFunctions.convert_pixmap_to_bytes(self, profile_image)

        # Updating the picture data in bytes in database
        users.update_one({"name": user_name},{"$set": { "profile_pic": profile_pic }})
        print ("pic updated successfully")
        return

    # Function for Removing User Profile Picture
    # ///////////////////////////////////////////////////////////////
    def remove_profile_pic(self, user_name):

        # Updating the picture field in the database to ''
        users.update_one({"name": user_name},{"$set": { "profile_pic": '' }})
        print ("pic removed successfully")
        return

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

    # Function for Deactivating the User Account (i.e. Deleting from the database)
    # ///////////////////////////////////////////////////////////////
    def deactivate_account(self, user_name):

        # findind and deleting the user from the database
        users.delete_one({"name": user_name})
        print ("Account deactivated successfully")
        return

    # Function for updating the User Logout Activity
    # ///////////////////////////////////////////////////////////////
    def update_logout_activity(self, user_name, activity, level):
        # getting local time i.e. machine time
        t = time.localtime()
        # formatting time
        current_time = time.strftime("%H:%M:%S", t)
        # getting the current date
        now = datetime.now()
        # formatting date
        date = now.strftime("%d/%m/%Y");
        # inserting the user logout activity data in the database with date and time of activity happening
        users_activity.insert_one({"user_name": user_name, "activity": activity , "date" : date, "time": current_time, "level": level})
        print ("logout activity updated successfully")
        return

    # Function for updating the User Activity
    # ///////////////////////////////////////////////////////////////
    def update_recent_activity(self, user_name, activity, level,widgets):
        # getting local time (i.e. machine time)
        t = time.localtime()
        # formatting time
        current_time = time.strftime("%H:%M:%S", t)
        # getting the current date
        now = datetime.now()
        # formatting date
        date = now.strftime("%d/%m/%Y");
        # inserting the user activity data in the database with date and time of activity happening
        users_activity.insert_one({"user_name": user_name, "activity": activity , "date" : date, "time": current_time, "level": level})
        # Updating the activity Table Widget on the user Dashboard

        # Counting the table rows
        rowPosition = widgets.tableWidget_recent_activity.rowCount()
        # Insert new row in the table
        widgets.tableWidget_recent_activity.insertRow(rowPosition)
        # Set Activity data in the table row according to specified columns
        widgets.tableWidget_recent_activity.setItem(rowPosition, 0, QTableWidgetItem(activity))
        widgets.tableWidget_recent_activity.setItem(rowPosition, 1, QTableWidgetItem(date))
        widgets.tableWidget_recent_activity.setItem(rowPosition, 2, QTableWidgetItem(current_time))
        widgets.tableWidget_recent_activity.setItem(rowPosition, 3, QTableWidgetItem(level))
        print ("activity updated successfully")
        return

    # Function for loading the User Activity
    # ///////////////////////////////////////////////////////////////
    def load_recent_activity(self, user_name,widgets):

        # getting all activity documents of the specified user from the database
        for activity in users_activity.find({"user_name": user_name}):
            # Counting the table rows
            rowPosition = widgets.tableWidget_recent_activity.rowCount()
            # Insert new row in the table
            widgets.tableWidget_recent_activity.insertRow(rowPosition)
            # Set Activity data in the table row according to specified columns
            widgets.tableWidget_recent_activity.setItem(rowPosition, 0, QTableWidgetItem(activity["activity"]))
            widgets.tableWidget_recent_activity.setItem(rowPosition, 1, QTableWidgetItem(activity["date"]))
            widgets.tableWidget_recent_activity.setItem(rowPosition, 2, QTableWidgetItem(activity["time"]))
            widgets.tableWidget_recent_activity.setItem(rowPosition, 3, QTableWidgetItem(activity["level"]))
        print ("activity loaded successfully")
        return

    # Function for clearing all the User Activity
    # ///////////////////////////////////////////////////////////////
    def clear_recent_activity_history(self, user_name,widgets):
        # deleting all the user activity documents in the database
        users_activity.delete_many({"user_name": user_name})
        # clearing user activity table data
        widgets.tableWidget_recent_activity.setRowCount(0)
        print ("recent activity history cleared successfully")
        return

    # Function for clearing all the User Favourite Items
    # ///////////////////////////////////////////////////////////////
    def clear_myfavourites_history(self, user_name,widgets):
        # deleting all the user favourite item documents in the database
        users_favourites.delete_many({"user_name": user_name})
        # clearing user favourites table data
        widgets.tableWidget_my_favourites.setRowCount(0)
        print ("myfavourites history cleared successfully")
        return

    # Function to remove a specified Favourite item from the database
    # ///////////////////////////////////////////////////////////////
    def remove_favourite(self, user_name, item,widgets):
        # try block
        try:
            # Converting favourite item from pixmap to bytes data for database query retrieval
            item_in_bytes = AppFunctions.convert_pixmap_to_bytes(self,item)
            # deleting the favourite item from the database
            users_favourites.delete_one({"user_name": user_name, "item" : item_in_bytes})
            # clearing the favourites table widget
            widgets.tableWidget_my_favourites.setRowCount(0)
            # reloading the updated favourite docs from the database
            AppFunctions.load_myfavourites(self,user_name,widgets)
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
            item_in_bytes = AppFunctions.convert_pixmap_to_bytes(self,item)
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

    # Function to load the Favourite items from the database to display results in the Qtable widget
    # ///////////////////////////////////////////////////////////////
    def load_myfavourites(self, user_name,widgets):
        # getting all favourite documents of the specified user from the database
        for favourite in users_favourites.find({"user_name": user_name}):
            # Counting the table rows
            rowPosition = widgets.tableWidget_my_favourites.rowCount()
            # Insert new row in the table
            widgets.tableWidget_my_favourites.insertRow(rowPosition)
            # Converting the bytes data to pixmap for displaying the item on Qtable list
            item = AppFunctions.convert_bytes_to_pixmap(self,favourite["item"])
            # Converting the favourite item pixmap data to Qicon for Qtable list view
            i = PySide6.QtGui.QIcon(item)
            item_icon = QTableWidgetItem()
            item_icon.setIcon(i)
            # Set Favourite data in the table row according to specified columns
            widgets.tableWidget_my_favourites.setItem(rowPosition, 0, QTableWidgetItem(item_icon))
            widgets.tableWidget_my_favourites.setItem(rowPosition, 1, QTableWidgetItem(favourite["category"]))
            widgets.tableWidget_my_favourites.setItem(rowPosition, 2, QTableWidgetItem(favourite["favourite_since"]))
        # printing message on console
        print ("favourites loaded successfully")
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
                output_image_1 = AppFunctions.convert_pixmap_to_bytes(self, widgets.output_image_1.pixmap())
            except:
                pass

            try:
                # output_image_2 pixmap data to bytes for database query
                output_image_2 = AppFunctions.convert_pixmap_to_bytes(self, widgets.output_image_2.pixmap())
            except:
                pass
            try:
                # output_image_3 pixmap data to bytes for database query
                output_image_3 = AppFunctions.convert_pixmap_to_bytes(self, widgets.output_image_3.pixmap())
            except:
                pass
            try:
                # output_image_4 pixmap data to bytes for database query
                output_image_4 = AppFunctions.convert_pixmap_to_bytes(self, widgets.output_image_4.pixmap())
            except:
                pass
            try:
                # output_image_5 pixmap data to bytes for database query
                output_image_5 = AppFunctions.convert_pixmap_to_bytes(self, widgets.output_image_5.pixmap())
            except:
                pass
            try:
                # output_image_6 pixmap data to bytes for database query
                output_image_6 = AppFunctions.convert_pixmap_to_bytes(self, widgets.output_image_6.pixmap())
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

    # Function to Open the Output Image in the CV2 viewer
    # ///////////////////////////////////////////////////////////////
    def open_image(self,image):

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

    # Function to Open the Output Folder having the results
    # ///////////////////////////////////////////////////////////////
    def open_output_folder(self):

        # setting output folder path
        path = "C://Users//SYS//Downloads//AI Images//"
        # openning folder using os module
        path = os.path.realpath(path)
        os.startfile(path)
        return

    # Function to Load Datasets Thumbnails
    # ///////////////////////////////////////////////////////////////
    def load_datasets_thumbs(self,widgets):

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
                pix = AppFunctions.convert_bytes_to_pixmap(self,image)
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
    def load_human_dataset_imgs(self,widgets):

        # finding human dataset document in the database collection
        human_doc = datasets.find_one({"name":"human"})
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
    def load_anime_dataset_imgs(self,widgets):

        # finding anime dataset document in the database collection
        anime_doc = datasets.find_one({"name":"anime"})
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
    def load_flower_dataset_imgs(self,widgets):

        # finding flower dataset document in the database collection
        flower_doc = datasets.find_one({"name":"flower"})
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
    def create_dataset(self,widgets):

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
        image_0 = AppFunctions.convert_pixmap_to_bytes(self,image_0_pix)
        image_1 = AppFunctions.convert_pixmap_to_bytes(self, image_1_pix)
        image_2 = AppFunctions.convert_pixmap_to_bytes(self, image_2_pix)
        image_3 = AppFunctions.convert_pixmap_to_bytes(self, image_3_pix)
        image_4 = AppFunctions.convert_pixmap_to_bytes(self, image_4_pix)
        image_5 = AppFunctions.convert_pixmap_to_bytes(self, image_5_pix)
        # inserting the new database document in the database
        datasets.insert_one({"name": dataset_name, "thumbnail": image_0, "size" : dataset_size, "images" : []})
        # updating new dataset images in the images Array
        datasets.update_many({"name": dataset_name}, {"$set": {"images": [image_0,image_1,image_2,image_3,image_4,image_5]}})
        # return created
        return "dataset created"

    # Function to Load a Newly Created Dataset
    # ///////////////////////////////////////////////////////////////
    def load_new_dataset(self,widgets):

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
                i=1
                # for every image in images Array
                for img in doc["images"]:
                    # converting the bytes data to pixmap for displaying the results on PyQt Widget
                    pix = AppFunctions.convert_bytes_to_pixmap(self,img)
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
    def add_image_to_dataset(self,widgets):

        # getting the pixmap of the new image to be added
        pix = widgets.new_dst_image_6.pixmap()
        # converting the new image pixmap data to bytes form for the database storage purpose
        new_image = AppFunctions.convert_pixmap_to_bytes(self, pix)
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
    def search_dataset(self,dataset_name,widgets):

        # finding the dataset doc in the database by the specified name
        dataset_doc = datasets.find_one({"name": dataset_name})
        # if the document exists
        if dataset_doc != None:
            # converting the thumbnail bytes data to pixmap form for displaying it on a QWidget
            dst_thumb = AppFunctions.convert_bytes_to_pixmap(self,dataset_doc["thumbnail"])
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
    def load_searched_dataset(self,widgets):
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
                pix = AppFunctions.convert_bytes_to_pixmap(self, img)
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
        new_image = AppFunctions.convert_pixmap_to_bytes(self, pix)
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
    def delete_searched_dataset(self,widgets):

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
        if (widgets.datsets_stackedWidget.currentWidget() == widgets.create_dataset_page and widgets.stackedWidget_content_pages.currentWidget() == widgets.datasets_page) or (widgets.stackedWidget_model_training.currentWidget() == widgets.select_dataset_page and widgets.stackedWidget_content_pages.currentWidget() == widgets.model_training_page):
                # if the dataset search text is not empty
                if widgets.search_dataset.text() != "" or widgets.search_dataset_2.text() != "":
                    # if searching dataset in the first dataset page
                    if widgets.search_dataset.text() != "":
                        # calling the search function with entered dataset name to be searched
                        dst_search_1 = AppFunctions.search_dataset(self, widgets.search_dataset.text(), widgets)
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
                        dst_search_2 = AppFunctions.search_dataset(self, widgets.search_dataset_2.text(), widgets)
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

    # Function to Train the GAN Model Against the provided Dataset
    # ///////////////////////////////////////////////////////////////
    def train_model(self,widgets):

        # Showing the model training progress page
        widgets.stackedWidget_model_training.setCurrentWidget(widgets.model_progress_page)

        # opening browser on the background
        chrome_options.add_argument("--headless")

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

        # Clicking the session btn to start the session
        time.sleep(3)
        session_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/button[1]")
        session_btn.click()
        time.sleep(3)

        # Clicking the settings tab to display
        settings_down_btn = driver.find_element_by_css_selector(
            "#site-content > div.AppView-sc-16eb2j.kDpcJw > div.App_Body-sc-16c8j4p.hxOBfv > div.Sidebar_Body-sc-14r4g35.dEilyb > div > div:nth-child(2) > div > div:nth-child(2) > div > div.SidebarPane_ChevronWrapper-sc-qm9hj3.yjdaM > button > span.MuiIconButton-label > i")
        settings_down_btn.click()
        time.sleep(1)

        # Clicking the Accelerator button to use the GPU for the model training process
        accelerator_btn = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div/button")
        accelerator_btn.click()
        time.sleep(2)

        # Clicking the GPU button to train the model perfectly
        gpu_btn = driver.find_element_by_xpath("/html/body/div[12]/div/div[2]")
        time.sleep(1)
        gpu_btn.click()
        time.sleep(1)
        turn_on_gpu_btn = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[5]/div[2]/div[4]/div[1]/div/div[2]/button[2]/span")
        turn_on_gpu_btn.click()

        # Clicking the RUN GAN algorithm on kaggle
        run_all_btn = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[1]/button[7]")

        # Checking if the session is LIVE
        green_signal = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div/div/div/div/div[1]/button/div[1]/div[1]/i")

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
        driver.switch_to_frame(iframe)

        # Settings the maximum values of the components accordingly
        widgets.training_progressBar.setMaximum(10000)
        widgets.total_epochs.display(10000)

        # While the training is on going, get the processing stats
        while (True):
            try:
                # Getting the dataset processing stats
                c = WebDriverWait(driver, 0.1).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "/html/body/div[4]/div[3]/div[2]/div[3]/div[2]/div[2]/div[8]/div[3]/div[2]/div/div[2]/pre")))
                dataset_progress_number = (c.text).split('%')[0]
                if dataset_progress_number != "100":
                    widgets.dataset_processing_bar.setValue(int(dataset_progress_number)+1)
                    if widgets.dataset_processing_bar.value() > 50:
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
                d = WebDriverWait(driver, 0.1).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "/html/body/div[4]/div[3]/div[2]/div[3]/div[2]/div[2]/div[26]/div[3]/div[2]/div/div[2]/pre")))
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
        widgets.genrated_images_count.display(widgets.genrated_images_count.intValue()+1)

        # Switching driver settings to default browser window
        driver.switch_to.default_content()
        time.sleep(5)

        # Refreshing the output folders on kaggle site
        dataset_show = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[3]")
        dataset_show.click()
        refresh_btn_ = driver.find_element_by_css_selector(
            "#site-content > div.AppView-sc-16eb2j.kDpcJw > div.App_Body-sc-16c8j4p.hxOBfv > div.Sidebar_Body-sc-14r4g35.dEilyb > div > div:nth-child(2) > div > div:nth-child(1) > div.SidebarPane_ItemBody-sc-tqtqts.jKIbPu > div > div:nth-child(2) > ul > ul > div > div.sc-pRrUz.dQnepB > div > div.sc-pYNsO.YWalf > div.sc-pByoR.eHxtff > i")
        ActionChains(driver).move_to_element(refresh_btn_).click().perform()
        output_fold = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//*[@id='site-content']/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/ul/div/div[3]")))
        output_fold.click()
        time.sleep(1)
        ActionChains(driver).reset_actions()
        output_fold2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//*[@id='site-content']/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/ul/ul/ul/div/div[3]")))
        ActionChains(driver).move_to_element(output_fold2).double_click().perform()
        time.sleep(2)

        # Getting the access to output generated images
        im = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[5]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/ul/ul/ul/ul")
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
        print(AppFunctions.store_output_images(self))
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
                rec = Binary(pickle.dumps(images[i], protocol=i%6))
                # storing the output image in the database collection with date time stamp
                output_images.insert_one({"image" : rec, "name" : images_name[i], "generated_at" : date_time})
            # return stored success
            return "outputs stored success"
        # except block
        except:
            return "outputs stored failure"

    # Function to Open Favourite Image from the Selected Qtable list on the CV2 image Viewer
    # ////////////////////////////////////////////////////////////////////////////////////////
    def open_favourite(self, widgets):
        # set initial counter
        i = 0
        # getting user name
        user_name = widgets.user_name.text()
        # Using try/except blocks for exception handling
        # try block
        try:
            # for every favourite document present in the database of the specified user
            for favourite in users_favourites.find({"user_name": user_name}):
                # checking if the current favourite is selected in the Qtable list
                if (widgets.tableWidget_my_favourites.item(i, 0)).isSelected():
                    # converting the image data to pixmap for displaying it on the UI
                    image = AppFunctions.convert_bytes_to_pixmap(self, favourite["item"])
                    # calling function to open the image on CV2 viewer
                    AppFunctions.open_image(self, image)
                    # break the loop
                    break
                # incrementing the counter
                i = i + 1
        # except block
        except:
            pass

    # Function to Open Output Image from the Selected Qtable list on the CV2 image Viewer
    # ////////////////////////////////////////////////////////////////////////////////////////
    def open_output_list_image(self, widgets):
        # set initial counter
        i = 0
        # Using try/except blocks for exception handling
        # try block
        try:
            # for every output document present in the database of the specified user
            for gen_image in output_images.find({"name": {'$regex':".png$"}}):
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
                    AppFunctions.open_image(self, pix)
                    # break the loop
                    break
                # incrementing the counter
                i = i + 1
        # except block
        except:
            pass

    # Function to Match the Admin Secret Key
    # ////////////////////////////////////////////////////////////////////////////////////////
    def match_admin_secret_key(self,key):
        # findind the secret key of the specified admin (i.e aiimages) in the database
        admin = admin_keys.find_one({"admin": "aiimages"})
        # if the entered secret key matches with the hashed key entered in the database
        if bcrypt.hashpw(key.encode('utf-8'), admin['secret_key']) == admin['secret_key']:
            # return key found
            return 'Key Found'
        # if the entered secret key not matches with the hashed key entered in the database
        else:
            # return key not found
            return 'Key Not Found'

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
