from datetime import datetime, timedelta

date_text = input("Enter the birthday date: ")
date_object = datetime.strptime(date_text, "%d-%m-%Y")
addition = timedelta(days = 1000)
date = date_object + addition
print(date.strftime("%d-%m-%Y"))