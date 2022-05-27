


import datetime

hours = 480
lesson_l = 4
days = int(hours/lesson_l)

course_date_list = []
no_course_date_list = [datetime.date(2022, 5, 4), datetime.date(2022, 5, 11),
                       datetime.date(2022, 7, 6), datetime.date(2022, 8, 15),
                       datetime.date(2022, 11, 1), datetime.date(2022, 11, 2)]

lesson_date = datetime.date(2022, 4, 28)

while len(course_date_list) < days:
    weekday = lesson_date.isoweekday()
    if weekday in (1,2,3,4):
        if lesson_date in no_course_date_list:
            lesson_date = lesson_date + datetime.timedelta(days=1)
        else:
            course_date_list.append(lesson_date)
            lesson_date = lesson_date + datetime.timedelta(days=1)
    else:
        lesson_date = lesson_date + datetime.timedelta(days=3)

for day in course_date_list:
    print(day.strftime("%Y - %B - %d"))