import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

from langchain_core.tools import BaseTool


class InvalidEmailPasswordException(Exception):
	pass


class EmailSender(BaseTool):
	name: str = "Tool to send an email"
	"""
	 If the parameter type is not described, parameters in the following format may be entered when passing parameters, causing execution exceptions.
	{
		"action": "Tool to count how many words appear in a sentence",
		"action_input": {
			"text": {
				"title": "山重水复疑无路，柳暗花明又一村"
			}
		}
	}
	"""
	description: str = (
		"Use this tool when you are asked to send an email"
		"{'subject':email subject, string type parameter}"
		"{'send_to':email address to send to, string type parameter}"
		"{'from_name':user name who send the email, string type parameter}"
		"{'content':email body, string type parameter}"
	)

	def _run(self, subject, send_to, from_name, content):
		from_email = "joezhang7788@126.com"
		smtp_server = "smtp.126.com"
		smtp_port = 465
		login_user = "joezhang7788@126.com"

		invalid_password = "INVALID_PASSWORD"
		login_password = os.getenv("EMAIL_LOGIN_TOKEN_126", invalid_password)  # expires in 180 days
		if login_password == invalid_password:
			raise InvalidEmailPasswordException
		try:
			# 创建MIMEMultipart对象，用于构建邮件
			message = MIMEMultipart()
			message['From'] = formataddr((from_name, from_email))
			message['To'] = send_to  # 将收件人列表拼接为字符串
			message['Subject'] = subject

			# 添加邮件内容
			message.attach(MIMEText(content, 'plain', 'utf-8'))

			# 连接SMTP服务器并发送邮件
			server = smtplib.SMTP_SSL(smtp_server, smtp_port)  # 使用SSL加密连接
			server.login(login_user, login_password)

			# 收件人包括主送和抄送
			recipients = send_to

			# 发送邮件
			server.sendmail(from_email, recipients, message.as_string())
			server.quit()
			return "Email sent successfully."
		except Exception as e:
			return f"Failed to send email: {e}"


if __name__ == '__main__':
	# 调用方法示例
	subject = "Test Email2"
	send_to = "woxiaoxinxin@gmail.com"
	content = "This is a test email sent from Python."

	print(EmailSender()._run(subject, send_to, 'Li lei', content))
