class calender:
    @staticmethod
    def april(day):
        april = int(day)
        if april == 1:
            return 'Friday: Odisha Day, April Fool''s Day'
        elif april >= 1 and april <= 2:
            return 'Saturday: Ugadi(Gudi Padwa), Ramadan Starts'
        elif april >= 2 and april <= 3:
            return 'Sunday'
        elif april >= 3 and april <= 4:
            return 'Monday'
        elif april >= 4 and april <= 5:
            return 'Tuesday'
        elif april >= 5 and april <= 6:
            return 'Wednesday'
        elif april >= 6 and april <= 7:
            return 'Thursday'
        elif april >= 7 and april <= 8:
            return 'Friday'
        elif april >= 8 and april <= 9:
            return 'Saturday'
        elif april >= 9 and april <= 10:
            return 'Sunday: Rama Navami'
        elif april >= 10 and april <= 11:
            return 'Monday'
        elif april >= 11 and april <= 12:
            return 'Tuesday'
        elif april >= 12 and april <= 13:
            return 'Wednesday'
        elif april >= 13 and april <= 14:
            return 'Thursday: Ambedkar Jayanti, Mahavir Jayanti, Vaisakhi, Tamil New Year'
        elif april >= 14 and april <= 15:
            return 'Friday: Good Friday'
        elif april >= 15 and april <= 16:
            return 'Saturday: Hanuman Jayanti'
        elif april >= 16 and april <= 17:
            return 'Sunday: Easter'
        elif april >= 17 and april <= 18:
            return 'Monday: World Heritage Day'
        elif april >= 18 and april <= 19:
            return 'Tuesday'
        elif april >= 19 and april <= 20:
            return 'Wednesday'
        elif april >= 20 and april <= 21:
            return 'Thursday: World Creativity and innovation Day'
        elif april >= 21 and april <= 22:
            return 'Friday'
        elif april >= 22 and april <= 23:
            return 'Saturday: English Language Day'
        elif april >= 23 and april <= 24:
            return 'Sunday'
        elif april >= 24 and april <= 25:
            return 'Monday'
        elif april >= 25 and april <= 26:
            return 'Tuesday'
        elif april >= 26 and april <= 27:
            return 'Wednesday'
        elif april >= 27 and april <= 28:
            return 'Thursday'
        elif april >= 28 and april <= 29:
            return "Friday: International Dance Day, 'Jumu''atul-wida"
        elif april >= 29 and april <= 30:
            return 'Saturday'


# Get Holidays of a month

def GetHolidaysofapril():
    H_count = 0
    month = calender()

    for day in range(1, 31):
        day_special = month.april(day)
        if len(day_special) > 9 or day_special == 'Sunday':
            if day in (1, 21, 31):
                print(str(day) + 'st', day_special)
            elif day in (2, 22):
                print(str(day) + 'nd', day_special)
            elif day in (3, 23):
                print(str(day) + 'rd', day_special)
            else:
                print(str(day) + 'th', day_special)

            H_count += 1
    print('Total Holidays in April are : {} '.format(H_count))
    return H_count


def GetWorkingDaysOofApril():
    w_count = 0
    month = calender()
    for day in range(1, 31):
        day_special = month.april(day)
        if len(day_special) <= 9 and day_special != 'Sunday':
            if day in (1, 21, 31):
                print(str(day) + 'st', day_special)
            elif day in (2, 22):
                print(str(day) + 'nd', day_special)
            elif day in (3, 23):
                print(str(day) + 'rd', day_special)
            else:
                print(str(day) + 'th', day_special)
            w_count += 1
    print('Total working days in April are : {} '.format(w_count))
    return w_count


if __name__ == '__main__':
    print("Holidays In april month are : ")

    h = GetHolidaysofapril()

    print('')
    print("Working Days in April are : ")
    w = GetWorkingDaysOofApril()

    print('')

    print('Total Days in april month are : {}'.format(w + h))

    input()
