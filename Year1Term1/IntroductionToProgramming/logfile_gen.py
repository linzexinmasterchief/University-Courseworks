import random


def generate_time(start_time = (1970, 1, 1), end_time = (1970, 1, 1), amount = 0):
    time_array = []
    total_days = (end_time[0] - start_time[0]) * 365 + (end_time[1] - start_time[1]) * 30 + (end_time[2] - start_time[2])
    day_step = total_days // amount
    count = 0
    i = 0
    while i < total_days:
        y = start_time[0] + i // 365
        m = (start_time[1] + 1 + i) % 12
        d = i % 28 + 1
        time_array.append([str(y) + "/" + str(m) + "/" + str(d), str(y) + "/" + str(m) + "/" + str(random.randint(d, 29))])
        i += random.randint(0, day_step)
    time_array.sort()
    return time_array

f_a = open("logfile.txt", 'w')

f_b = open("database.txt","r")
database_arr = f_b.readlines()
f_b.close()

log_arr = []
for record in database_arr:
    # [:-1] removes the last \n character in record_arr
    record_arr = record.split(',')[:-1]
    date = record_arr[-2]
    day, month, year = date.split("/")
    time_list = generate_time((int(year), int(month), int(day)), (2020, 1, 1), random.randint(5, 30))
    for time in time_list:
        log_arr.append(time[0] + "," + time[1] + "," + record_arr[0] + ",\n")
log_arr.sort()
f_a.writelines(log_arr)
f_a.close()