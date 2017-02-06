#!/usr/bin/env python3  
#coding: utf-8  
import smtplib 
from email.mime.text import MIMEText 

username = 'wangwei0609@gmail.com'# 用户名 
password = '' # 密码 

sender = 'wangwei0609@gmail.com' # 发件人邮箱 
receiver = 'wangwei0609@gmail.com' # 收件人邮箱 
subject = 'python email test' 
mail_content = '<html><h1>你好</h1></html>' # email内容 
msg = MIMEText(mail_content,'html','utf-8') 
msg['Subject'] = subject 

mail_server = 'smtp.gmail.com' 
mail_server_port = 587 
server = smtplib.SMTP(mail_server, mail_server_port) 
server.set_debuglevel(1) # 调试模式 

server.starttls() 
server.ehlo() 
server.login(username, password) 
server.sendmail(sender, receiver, msg.as_string()) 
server.quit()