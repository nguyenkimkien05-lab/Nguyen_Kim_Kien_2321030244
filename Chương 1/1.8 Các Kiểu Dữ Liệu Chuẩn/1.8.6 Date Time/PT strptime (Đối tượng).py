# Chuyen doi chuoi sang datetime trong Python

from datetime import datetime

# Chuoi ngay thang
date_string = "25/12/2024"

# Chuyen chuoi thanh doi tuong datetime
converted_date = datetime.strptime(date_string, "%d/%m/%Y")

print(converted_date)
