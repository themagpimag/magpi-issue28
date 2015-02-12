#!/usr/bin/env python
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
      print "Something went wrong when sending the email %s: %s" % (fromAddr,e)
      print e

  def cleanup(self):
    self.server.quit()

  def send(self,fromAddr, toAddr, emailSubject, htmlFileName):
    # Build the email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = emailSubject
    msg['From'] = fromAddr
    msg['To'] = toAddr

    # Read the HTML file
    htmlFile = open(htmlFileName, 'r')
    html = htmlFile.read()
    htmlFile.close()

    # Attach the HTML to the message
    body = MIMEText(html, 'html')
    msg.attach(body)

    # Send the email
    try:
      self.server.sendmail(fromAddr, toAddr, msg.as_string())
      print "email sent: %s" % toAddr
    except Exception as e:
      print "Something went wrong %s" % e

username = 'sending@gmail.com'
password = '******'  # The sending account password
fromAddr = 'sending@gmail.com'  # Sending email address
msgSubject = 'Glasgow Raspberry Pi day : 17/01/2015' # Subject
addressFile='local-schools.txt' # Column of input addresses
htmlMsg='schools-email.html' # HTML file to send

g = Gmail(username,password)  # Open the connection to the gmail server
addresses = open(addressFile, "r" )  # Open email address file
for toAddr in addresses:  # Loop over address list
  toAddr = toAddr.rstrip()  # Remove new line from the end of address
  g.send(fromAddr, toAddr, msgSubject, htmlMsg)  # Send HTML message
  time.sleep(1) # Pause to avoid overloading connection to Gmail server
addresses.close()  # Close the address list file
g.cleanup()  # Close the connection to gmail server
