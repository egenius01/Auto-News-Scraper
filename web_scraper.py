import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()

content = ""


def extract_news(url):
    print("Extracting Hacker News Stories...")
    cnt = ""
    cnt += "<b>HN TOP STORIES:</b>\n" + "<br />" + "-" * 50 + "<br>"
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    for i, tag in enumerate(
        soup.find_all("td", attrs={"class": "title", "valign": ""})
    ):
        cnt += (
            (f"{str(i + 1)}  :: {tag.text}" + "\n" + "<br>")
            if tag.text != "More"
            else ""
        )
        return cnt


cnt = extract_news("https://news.ycombinator.com/")
content += cnt
content += "<br>---------<br>"
content += "<br><br>End of Mesage"

# sending the email

print("composing email")

# email details

SERVER = "smtp.gmail.com"
PORT = 587
FROM = "omoragbonemmanuel@gmail.com"
TO = "omoragbonemmanuel@gmail.com"
PASS = "Password"  # email id's password

# message body
msg = MIMEMultipart()

msg["Subject"] = f"Top News Updates[Automated Email] {str(now.day)} - {str(now.year)}"
msg["From"] = FROM
msg["To"] = TO
msg.attach(MIMEText(content, "html"))
print(msg.as_string())

# GOOGLE STOPPED ALLOWING LESS SECURE APPS
# print("Initiating Server...")

# server = smtplib.SMTP(SERVER, PORT)
# server.set_debuglevel(1)
# server.ehlo()
# server.starttls()
# server.login(FROM, PASS)
# server.sendmail(FROM, TO, msg.as_string())
print("Email Sent...")

# server.quit()
