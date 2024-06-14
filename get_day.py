d_week = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 0: "Sun"}
n_day_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

week_day = 1 # Monday, 2024/01/01
count = 0


for month, day in n_day_month.items():
    for date in range(1, day+1):
        if month == 10 and date == 11:
            break
        print(f'2024-{month}-{date} {d_week[week_day]}')
        week_day += 1
        count += 1
        # check if week_day == 7 => let it become 0
        if week_day % 7 == 0:
            week_day = 0

    if month == 10:
        break


print(count)