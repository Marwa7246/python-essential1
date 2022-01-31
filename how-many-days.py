# our task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given month/year pair (while only February is sensitive to the year value, your function should be universal).

# The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.

# Of course, you can (and should) use the previously written and tested function (LAB 4.3.1.6). It may be very helpful. We encourage you to use a list filled with the months' lengths. You can create it inside the function - this trick will significantly shorten the code.

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




    # list_length = [28, 29, 30, 31]
    # if month in [1,3,5,7,8,10,12]:
    #     return list_length[3]
    # elif month in [4,6,8,11]:
    #     return list_length[2]
    # elif month == 2:
    #     if is_year_leap(year):
    #         return list_length[1]
    #     else:
    #         return list_length[0]
    # else:
    #     return

test_years = [1900, 2000, 2016, 1987, 1]
test_months = [2, 2, 1, 11, 13]
test_results = [28, 29, 31, 30, None]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")