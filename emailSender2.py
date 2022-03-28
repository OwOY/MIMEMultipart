import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mako.template import Template

def send_email(sender, receivers, subject, FCTID, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    receivers = receivers if isinstance(receivers, list) else [receivers]
    msg['To'] = ','.join(receivers)
    msg['Subject'] = subject

    mail_template = Template(filename=f'./mail_template/notify.html')
    # body > df.to_html()
    mail_body = mail_template.render(FCTID = FCTID, body=body)
    
    content = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(content)

    with smtplib.SMTP(host="10.2.1.70", port=25) as smtp:  # 設定SMTP伺服器
        try:
            smtp.sendmail(sender, receivers, msg.as_string())  # 寄送郵件
        except Exception as e:
            print("Error message: ", e)
            

if __name__ == '__main__':
    send_email('david.yang@wiadvance.com', 'david.yang@wiadvance.com', 'test')
