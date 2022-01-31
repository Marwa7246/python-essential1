# Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, or returns None if any of the arguments is invalid.

# Use the previously written and tested functions. Add some test cases to the code. This test is only a beginning.

def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False    
    elif year % 4 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
#
# Write your new code here.
#
    list_month =[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year >= 1549:
        if month != 2 and month in range(1, 13):
            return list_month[month-1]
        elif month == 2:
            if is_year_leap(year):
                return list_month[1]
            else:
                return list_month[1] -1 
        else:
            return
    else:
        return





def day_of_year(year, month, day):
#
# Write your new code here.
    # print(year, month, day)
    if month in range(1,13) and year >= 1549:
        month_length = days_in_month(year, month)
        if day > month_length:
            return
        else:
            days = day
            for ele in range(1,month-1):
                days += days_in_month(year, ele)
            return days
    else:
        return        


print(day_of_year(2000, 12, 31))
print(day_of_year(2001, 12, 31))
print(day_of_year(2000, 11, 31))