# -*- coding: utf-8 -*-
import datetime
import smtplib
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# 設置收件人信箱
username = 'test@gmail.com'


# password = ''
# sender = 'test@gmail.com'


class EmailSender():

    def __init__(self, sender, receiver, subject, ):
        '''
        初始化郵件發送對象
        :param receiver: 收件人：list -['xxx@gmail.com','xxxx@yahoo.com.tw']
        :param subject: 標題
        '''
        self.receiver = receiver
        self.msg = MIMEMultipart('mixed')
        # 下面的主題，寄件人，收件人，日期是顯示在郵件上的。
        self.msg['Subject'] = subject
        self.msg['From'] = sender
        # 若收件人為多個，則用；分隔
        self.msg['To'] = ";".join(receiver)
        self.msg['Date'] = '{}'.format(datetime.datetime.now())

    def add_text(self, text_plain):
        '''
        构造文字内容
        :param text_plain: 字符串文件 可以使用回车换行等符号
        :return:
        '''
        text_plain = MIMEText(text_plain, 'plain', 'utf-8')
        self.msg.attach(text_plain)

    def add_img(self, img_name, sendimagefile):
        '''
        发送图片
        示例:
            sendimagefile = open(img_path, 'rb').read()
            send_img('ima_name',sendimagefile)
        :param imgname: 图片路径
        :return:
        '''

        image = MIMEImage(sendimagefile)
        image.add_header('Content-ID', '<image1>')
        image["Content-Disposition"] = 'attachment; filename="{}"'.format(img_name)
        self.msg.attach(image)

    def add_html(self, html):
        '''
        发送html
        :param html: html文件
        :return:
        '''
        text_html = MIMEText(html, 'html', 'utf-8')
        text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
        self.msg.attach(text_html)

    def add_html_content(self, html):
        '''
        發送html格式文件
        :param html: html文件
        :return:
        '''
        text_html = MIMEText(html, 'html', 'utf-8')
        self.msg.attach(text_html)
        
    def add_file(self, filename, sendfile):
        '''
        發送附件
          sendfile = open(r'xxxx.xls', 'rb').read()
          add_file('file_name',sendfile)
        :param filename: 附件名稱
        :param sendfile: 附件文件
        :return:
        '''

        text_att = MIMEText(sendfile, 'base64', 'utf-8')
        text_att["Content-Type"] = 'application/octet-stream'
        text_att.add_header('Content-Disposition', 'attachment', filename=filename)
        self.msg.attach(text_att)

    def send(self):
        # 發送郵件SMTP
        smtp = smtplib.SMTP('10.41.22.108', 25)
        # smtp.connect()
        # smtp.starttls()
        # smtp.login(username, None)
        smtp.sendmail(sender, self.receiver, self.msg.as_string())
        smtp.quit()

if __name__ == '__main__':
    em_obj = EmailSender(['test@gmail.com'], '測試測試')
    em_obj.add_text('testest')
    em_obj.send()
