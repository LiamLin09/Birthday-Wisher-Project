
from datetime import datetime
import pandas
import random
import smtplib

MY_EMIAL = 'appbreweryinfo@gmail.com'
MY_PASSWORD = 'abcd1234'

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv('birthdays.csv')
birthday_dict = {(data.row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f'Letter_templates/letter_{random.randint(1, 3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP('stmp.gmail.com')as connection:
        connection.starttls()
        connection.login(MY_EMIAL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMIAL,
                            to_addrs=birthday_person['email'],
                            msg=f"Subject: Happy Birthday\n\n{contents}")




