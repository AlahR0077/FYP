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

# User_Profile Class
# ///////////////////////////////////////////////////////////////
class User_Profile(MainWindow):

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
    def register(self, username, email, password, confirm_password, profile_image):

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
        profile_pic = MainWindow.convert_pixmap_to_bytes(self, profile_image)

        # Encrypting the Password to Hashed Passsword for Hacker Attacks
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Storing the Correct Sign Up Form Data in the MongoDB Database
        users.insert_one({"name": username, "email": email, "password": hash_password, "profile_pic": profile_pic,
                          "verified_account": False})

        # Return registration success message
        return 'Registered successfully'

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
        user = User_Profile.find_user_by_email(self, email)
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
        mailmsg = Template(html).safe_substitute(code=feedback, e_code=email)
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
        user = User_Profile.find_user_by_email(self, substring)
        # Encrpting the new Password to Prevent Hacker Access
        hash_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        # Updating new Hashed Password in the database
        users.update_one({"email": substring}, {"$set": {"password": hash_password}})
        # returning the user name
        return (user["name"])

    # Function for Updating User Account Verification
    # ///////////////////////////////////////////////////////////////
    def update_account_verification(self, user_name):
        # Finding user name in the database and setting 'verfied_account' variable to TRUE
        users.update_one({"name": user_name}, {"$set": {"verified_account": True}})
        return

    # Function for Updating User Profile Picture
    # ///////////////////////////////////////////////////////////////
    def update_profile_pic(self, user_name, profile_image):

        # Converting the picture data to bytes for database storage purpose
        profile_pic = MainWindow.convert_pixmap_to_bytes(self, profile_image)

        # Updating the picture data in bytes in database
        users.update_one({"name": user_name}, {"$set": {"profile_pic": profile_pic}})
        print("pic updated successfully")
        return

    # Function for Removing User Profile Picture
    # ///////////////////////////////////////////////////////////////
    def remove_profile_pic(self, user_name):

        # Updating the picture field in the database to ''
        users.update_one({"name": user_name}, {"$set": {"profile_pic": ''}})
        print("pic removed successfully")
        return

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
        users_activity.insert_one(
            {"user_name": user_name, "activity": activity, "date": date, "time": current_time, "level": level})
        print("logout activity updated successfully")
        return

    # Function for updating the User Activity
    # ///////////////////////////////////////////////////////////////
    def update_recent_activity(self, user_name, activity, level, widgets):
        # getting local time (i.e. machine time)
        t = time.localtime()
        # formatting time
        current_time = time.strftime("%H:%M:%S", t)
        # getting the current date
        now = datetime.now()
        # formatting date
        date = now.strftime("%d/%m/%Y");
        # inserting the user activity data in the database with date and time of activity happening
        users_activity.insert_one(
            {"user_name": user_name, "activity": activity, "date": date, "time": current_time, "level": level})
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
        print("activity updated successfully")
        return

    # Function for loading the User Activity
    # ///////////////////////////////////////////////////////////////
    def load_recent_activity(self, user_name, widgets):
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
        print("activity loaded successfully")
        return

    # Function for clearing all the User Activity
    # ///////////////////////////////////////////////////////////////
    def clear_recent_activity_history(self, user_name, widgets):
        # deleting all the user activity documents in the database
        users_activity.delete_many({"user_name": user_name})
        # clearing user activity table data
        widgets.tableWidget_recent_activity.setRowCount(0)
        print("recent activity history cleared successfully")
        return

    # Function for clearing all the User Favourite Items
    # ///////////////////////////////////////////////////////////////
    def clear_myfavourites_history(self, user_name, widgets):
        # deleting all the user favourite item documents in the database
        users_favourites.delete_many({"user_name": user_name})
        # clearing user favourites table data
        widgets.tableWidget_my_favourites.setRowCount(0)
        print("myfavourites history cleared successfully")
        return

    # Function to load the Favourite items from the database to display results in the Qtable widget
    # ///////////////////////////////////////////////////////////////
    def load_myfavourites(self, user_name, widgets):
        # getting all favourite documents of the specified user from the database
        for favourite in users_favourites.find({"user_name": user_name}):
            # Counting the table rows
            rowPosition = widgets.tableWidget_my_favourites.rowCount()
            # Insert new row in the table
            widgets.tableWidget_my_favourites.insertRow(rowPosition)
            # Converting the bytes data to pixmap for displaying the item on Qtable list
            item = MainWindow.convert_bytes_to_pixmap(self, favourite["item"])
            # Converting the favourite item pixmap data to Qicon for Qtable list view
            i = PySide6.QtGui.QIcon(item)
            item_icon = QTableWidgetItem()
            item_icon.setIcon(i)
            # Set Favourite data in the table row according to specified columns
            widgets.tableWidget_my_favourites.setItem(rowPosition, 0, QTableWidgetItem(item_icon))
            widgets.tableWidget_my_favourites.setItem(rowPosition, 1, QTableWidgetItem(favourite["category"]))
            widgets.tableWidget_my_favourites.setItem(rowPosition, 2,
                                                      QTableWidgetItem(favourite["favourite_since"]))
        # printing message on console
        print("favourites loaded successfully")
        return



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
                    image = MainWindow.convert_bytes_to_pixmap(self, favourite["item"])
                    # calling function to open the image on CV2 viewer
                    MainWindow.open_image(self, image)
                    # break the loop
                    break
                # incrementing the counter
                i = i + 1
        # except block
        except:
            pass

    # Function to Match the Admin Secret Key
    # ////////////////////////////////////////////////////////////////////////////////////////
    def match_admin_secret_key(self, key):
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