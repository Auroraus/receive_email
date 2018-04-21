# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 18:03:44 2017

@author: Administrator
"""
from email.mime.multipart import MIMEMultipart  
from email.mime.application import MIMEApplication  
from email.mime.text import MIMEText  
import smtplib

class send():
    def __init__(self,fro,psd,to,serve,subject,content):
       self.msg_from=fro                                #发送方邮箱
       self.passwd=psd                                   #填入发送方邮箱的授权码
       self.msg_to=to                                #收件人邮箱
                                
       self.subject=subject                                     #主
       
      
       self.content=content
       self.msg = MIMEText(self.content)
       self.msg['Subject'] = self.subject
       self.msg['From'] = self.msg_from
       self.msg['To'] = self.msg_to
       self.s=smtplib.SMTP_SSL(serve,465)
       self.s.login(self.msg_from, self.passwd)
       self.s.sendmail(self.msg_from, self.msg_to, self.msg.as_string())
       self.s.quit()
send('********@126.com','******','u********a@126.com',"smtp.126.com",'哈哈','哈哈')
