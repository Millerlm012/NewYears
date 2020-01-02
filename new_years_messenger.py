# sends out some sort of message at the new year
from datetime import *
import smtplib
import time

current_time = datetime.now()

current_hour_sec = current_time.hour * 3600
current_min_sec = current_time.minute * 60
current_sec = current_time.second
midnight = 86400

total_sec = current_hour_sec + current_min_sec + current_sec

time_till_midnight = midnight - total_sec

print(time_till_midnight)

# sleep until midnight
time.sleep(time_till_midnight)

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login('millerlm012@gmail.com', 'Heyitsme#16')

# Send text message through SMS gateway of destination number
message = 'Happy New Year! - I was extremely bored so I programmed a bot to send you this text a couple hours ago...'
email = 'millerlm012@gmail.com'

server.sendmail(email, '5633797111@vtext.com', message)
server.sendmail(email, '5632020704@vtext.com', message)
server.sendmail(email, '5633796178@vtext.com', message)
server.sendmail(email, '5635688860@vtext.com', message)
server.sendmail(email, '5634199425@vtext.com', message)
server.sendmail(email, '5634196470@email.uscc.net', message)

server.quit()

print('new years texts have been sent')

