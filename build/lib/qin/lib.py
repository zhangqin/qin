#!/usr/bin/env python
# coding=utf-8
# author: b0lu
# mail: b0lu_xyz@163.com
import smtplib  
from base64 import b64encode 
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  

sender = 'b0lu_xyz@163.com'  
receiver = 'b0lu_xyz@163.com'  

smtpserver = 'smtp.163.com'  
username = 'b0lu_xyz@163.com'  


'''
发送邮件内容获取
'''
def get_msg(subject, plain="best with by b0lu", html = None, image = None, attach = None ):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = '=?%s?B?%s?=' % ('utf-8',b64encode(subject))  
    #msg['Subject'] = subject

    text = "骚年，\n"+plain
    plain_text = MIMEText(text, 'plain', 'utf-8')  
    msg.attach(plain_text)
    '''
    HTML格式的内容
    '''
    if html is not None:
        html_text = MIMEText(html, 'html', 'utf-8')
        msg.attach(html_text)
    #图片内容
    elif image is not None:
        if isinstance(image, list):
            for img in image:
                image = MIMEImage(open(img,'rb').read())
                image.add_header('Content-ID','<image1>')
                msg.attach(image)
        else: 
            image = MIMEImage(open(image,'rb').read())
            image.add_header('Content-ID','<image1>')
            msg.attach(image)
    #附件内容
    elif attach is not None:
        if isinstance(attach, list):
            for filename in attach:
                att = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')  
                att["Content-Type"] = 'application/octet-stream'  
                att["Content-Disposition"] = 'attachment; filename="1.jpg"'  
                msg.attach(att)
        else:
            att = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')  
            att["Content-Type"] = 'application/octet-stream'  
            att["Content-Disposition"] = 'attachment; filename="1.jpg"'  
            msg.attach(att)
    #返回邮件内容
    return msg.as_string()

def send_mail(password, subject, **kargs):
    smtp = smtplib.SMTP()  
    smtp.connect('smtp.163.com')  
    smtp.login(username, password)  
    msg = get_msg(subject, **kargs)
    smtp.sendmail(sender, receiver, msg)  
    smtp.quit()  

