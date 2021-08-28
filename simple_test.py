#Ignore this file 
#You can use this to test if your email account is working
#Did you disable enable less secure apps access?

import smtplib

#Sender email
email = "example@gmail.com"
#Sender password
pw = "examplepassword"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(email,pw)
server.sendmail(email, email, msg="Subject: Hello there\n\n Hello there!")
server.close()
