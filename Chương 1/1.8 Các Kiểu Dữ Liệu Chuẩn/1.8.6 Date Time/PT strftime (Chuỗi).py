# Xu ly thoi gian trong Python

import datetime

# Lay thoi gian hien tai
current_time = datetime.datetime.now()

print("Thoi gian hien tai:", current_time)

# Dinh dang lai thoi gian thanh chuoi
formatted_time = current_time.strftime("%d/%m/%Y %H:%M:%S")

print("Thoi gian da dinh dang:", formatted_time)
