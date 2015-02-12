#!/usr/bin/env python
# A program to send an email with gmail
import smtplib
from email.mime.text import MIMEText

def sendGmail(fromAddr, toAddr, username, password, 
              emailBody, emailSubject):          

  # Build the email
  msg = MIMEText(emailBody)
  msg['Subject'] = emailSubject
  msg['From'] = fromAddr
  msg['To'] = toAddr

  try:
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromAddr, toAddr, msg.as_string())  
    server.quit()
    print "email sent: %s" % fromAddr
  except Exception as e:
    print "Something went wrong when sending the email %s" % fromAddr
    print e

fromAddr = 'emailthemagpi@gmail.com'
toAddr  = 'whbqcd1@gmail.com'
msg = 'This is a text message...'
msgSubject = 'Test message'
username = 'emailthemagpi@gmail.com'
password = '*********'

sendGmail(fromAddr, toAddr, username, password, msg, msgSubject)
