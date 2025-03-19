from datetime import datetime, timedelta
# functions of module datetime: get current time
cdt = datetime.now()
print(cdt)
# transform it into str
scdt = cdt.strftime("%Y-%m-%d")
scdt2 = cdt.strftime("heure: %H minutes: %M secondes: %S")
print(scdt, scdt2)
# parse str format time
time = "2025-09-09"
parsed_time = datetime.strptime(time, "%Y-%m-%d") # match only numeric characters
print(parsed_time, type(parsed_time))
# compare time 
date1 = datetime(2029, 1,1).date() # only show the date not time
date2 = datetime(2029,1,30).date()
diff = date2 - date1
print(f"the gap between {date1} and {date2} is {diff}")

future = cdt + timedelta(days=4)
print(future)

if date1 < date2:
    print(f"{date1} < {date2}")
else:
    print(f"{date1} > {date2}")

# show different part
print(cdt.year)
print(cdt.month)
print(cdt.day)
print(cdt.second)
