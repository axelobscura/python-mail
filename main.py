#import smtplib

#my_email = "axelobscuras@gmail.com"
#password = "1x2l4bsc5r1s"

#with smtplib.SMTP("smtp.gmail.com") as connection:
    #connection.starttls()
    #connection.login(user=my_email, password=password)
    #connection.sendmail(
        #from_addr=my_email,
        #to_addrs="axosar@gmail.com",
        #msg="Subject:Hello...\n\nThis is the body"
    #)

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
print(now)
print(year)
print(month)

fecha_nacimiento = dt.datetime(year=1995, month=12, day=15)
print(fecha_nacimiento)