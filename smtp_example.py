import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login("sender email", "sender password")

message = "test_message"

s.sendmail("sender email", "receiver email", message)

s.quit()