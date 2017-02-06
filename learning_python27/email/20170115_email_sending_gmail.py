#!/usr/bin/env python3  
#coding: utf-8  
import smtplib

fromaddr = 'wangwei0609@gmail.com'
toaddrs  = 'wangwei0609@gmail.comm'
msg = 'There was a terrible error that occured and I wanted you to know!'


# Credentials (if needed)
username = 'wangwei0609@gmail.com'
password = ''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()