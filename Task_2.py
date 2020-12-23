time = 0
while time <= 0:
    time = int(input ('Введите время в секнудах '))
print('Введенное время в секундах',time)
time_hour = time // 3600
time -= time_hour * 3600
if time_hour < 10:
    time_hour = '0' + str(time_hour)
time_minute = time // 60
time -= time_minute * 60
if time_minute < 10:
    time_minute = '0' + str(time_minute)
if time < 10:
    time = '0' + str(time)
print(f"{time_hour}:{time_minute}:{time}")