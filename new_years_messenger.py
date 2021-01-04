# sends out text message on new years day when the program is ran new years eve before 00:00 / midnight

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

server.login('example@gmail.com', 'examplePassword')

# Send text message through SMS gateway of destination number
message = 'Happy New Year! - I was extremely bored so I programmed a bot to send you this text a couple hours ago...'
email = 'example@gmail.com'

server.sendmail(email, 'xxx-xxx-xxxx@vtext.com', message)

server.quit()

print('new years texts have been sent')

