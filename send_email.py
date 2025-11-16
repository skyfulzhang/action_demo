# -*- coding: utf-8 -*-
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from set_log import logger
from read_config import read_config_yaml

# 发送邮件
def send_email(email_name,email_content):
    try:
        logger.info('发送邮件 - Start')
        # 读取yaml配置文件
        data = read_config_yaml()
        emil_address = data['EMAIL_ADDRESS']
        emil_password = data['EMAIL_PASSWORD']
        sender = data['SENDER']
        receiver = data['RECEIVER']
        # 邮箱地址
        EMAIL_ADDRESS = emil_address
        # SMTP的授权码(QQ邮箱设置里）
        EMAIL_PASSWORD = emil_password
        """
        在smtplib中，如果您将context设置为None，这意味着您的SMTP连接将不会使用SSL/TLS加密，即使目标SMTP服务器支持它。这可能会导致您发送的邮件的安全性受到威胁，因为它们可能会在网络传输过程中被拦截或篡改。
        如果您想确保SMTP连接的安全性，我建议您将context参数设置为一个有效的SSLContext对象，以便启用SSL/TLS加密。您也可以考虑使用其他方法（如STARTTLS命令）来启用SMTP连接的加密。
        """
        context = ssl.create_default_context()
        # 邮件的标题
        subject = email_name
        # 创建 SMTP 客户端对象并发送邮件
        with smtplib.SMTP_SSL("smtp.qq.com", 465, context = context) as smtp :
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            # 遍历收件人
            for recipient in receiver :
                # 创建一个新的邮件
                msg = MIMEMultipart()
                msg['Subject'] = subject
                msg['From'] = sender
                msg['To'] = recipient
                # 添加邮件内容 plain代表纯文本
                msg.attach(MIMEText(email_content, 'plain'))
                # 发送邮件
                smtp.sendmail(sender, recipient, msg.as_string())
        logger.info('发送邮件 - success {0} {1}'.format('、'.join(receiver),email_name))
    except Exception as e :
        logger.error('发送邮件 - Failed')
        logger.error(f"{e}")
    finally:
        logger.info('发送邮件 - End')

# if __name__ == "__main__":
#     send_email(email_name = '邮件标题', email_content = '邮件内容部分')
