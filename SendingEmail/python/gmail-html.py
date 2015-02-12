#!/usr/bin/env python
# A program to send an email with gmail
import smtplib,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Gmail:
  def __init__(self,username,password):
    try:
      self.server = smtplib.SMTP('smtp.gmail.com', 587)
      self.server.ehlo()
      self.server.starttls()
      self.server.login(username,password)
    except Exception as e:
      print "Something went wrong when sending the email %s: %s" % (fromaddr,e)
      print e

  def cleanup(self):
    self.server.quit()

  def send(self,fromaddr, toaddr, email_subject, fileName):
    # Build the email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = email_subject
    msg['From'] = fromaddr
    msg['To'] = toaddr

    # Read the HTML file
    file = open(fileName, 'r')
    html = file.read()
    file.close()

    # Attach the HTML to the message
    body = MIMEText(html, 'html')
    msg.attach(body)

    # Send the email
    try:
      self.server.sendmail(fromaddr, toaddr, msg.as_string())
      print "email sent: %s" % toaddr
    except Exception as e:
      print "Something went wrong %s" % e
      
#-------------------------------------------------

# Open the connection
#username = 'emailthemagpi@gmail.com'
username = 'whbqcd1@gmail.com'
#password = '*********'
password = '******'
g = Gmail(username,password)

# Email header
#fromaddr = 'emailthemagpi@gmail.com'
fromaddr = 'whbqcd1@gmail.com'
#toaddrs  = 'whbqcd1@gmail.com'
#msg = 'This is a text message...'
msgSubject = 'Glasgow Raspberry Pi day : 17/01/2015'

# Input file names
#fileName='test-emails2.txt'
#fileName='scottish-secondary-schools-email.txt'
#fileName='english-secondary-schools-email.txt'
#fileName='welsh-secondary-schools-email.txt'
#fileName='rest_7.txt'
fileName='/home/wbell/Documents/raspberrypi/raspberrypi-day/2015-01-17/GlasgowSchools-emails.txt'
#fileName='2.txt'

# Open email address file
inFile = open(fileName, "r" )

htmlMsg='/home/wbell/Documents/raspberrypi/raspberrypi-day/2015-01-17/schools-email.html'

# Loop over all files
for toaddrs in inFile:
  toaddrs = toaddrs.rstrip()
  print toaddrs
  g.send(fromaddr, toaddrs, msgSubject, htmlMsg)
  time.sleep(1)
inFile.close()

# Close the connection
g.cleanup()
