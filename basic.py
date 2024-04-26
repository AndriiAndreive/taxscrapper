import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from selenium import webdriver
import base64

# Configure Chrome options for headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration

# Initialize Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage you want to take a screenshot of
driver.get('https://www.example.com')

# Take a screenshot as a binary data
screenshot_binary = driver.get_screenshot_as_png()

# Encode the binary data to Base64
screenshot_base64 = base64.b64encode(screenshot_binary).decode('utf-8')

# Close the browser
driver.quit()

# Email configuration
sender_email = 'mahroos.two@gmail.com'
receiver_email = 'andreievandrii71@gmail.com'
subject = 'Screenshot from Selenium'
body = 'Screenshot attached.'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'mahroos.two@gmail.com'
smtp_password = 'Bronze833!'

# Create a multipart message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the screenshot as a MIMEBase object
attachment = MIMEBase('application', 'octet-stream')
attachment.set_payload(screenshot_binary)
encoders.encode_base64(attachment)
attachment.add_header('Content-Disposition', f'attachment; filename=screenshot.png')
msg.attach(attachment)

# Add the body text to the email
msg.attach(MIMEText(body, 'plain'))

# Create an SMTP session
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print('Email sent successfully')
