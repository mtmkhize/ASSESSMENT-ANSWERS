import re

def is_date_format_correct(date_string):
    date_format = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    return bool(date_format.match(date_string))

print(is_date_format_correct("2022-01-01")) # True
print(is_date_format_correct("2022/01/01")) # False
print(is_date_format_correct("2022-01-1")) # False 

    
# This function uses the re (regular expression) module to check 
#if the input string matches the pattern YYYY-MM-DD. 
#The regular expression ^\d{4}-\d{2}-\d{2}$ matches strings that start (^) with 4 digits
#(\d{4}), followed by a hyphen (-), then 2 digits (\d{2}), 
#another hyphen (-), and finally 2 digits (\d{2}) at the end ($) of the string



Question 2 

def skip_number():
    for i in range(1, 11):
        if i == 6:
            continue
        else:
            print(i, end=',')

# Call the function
skip_number()

#The continue statement is used in the if block to skip the current iteration
#of the loop when i is equal to 6, so that number 6 is not printed. 
#The end parameter in the print function is set to ',' 
#to print all the numbers on the same line, separated by commas.

Question 3

import datetime
import calendar

def compute_prev_date(dates_list):
    prev_dates = []
    for date_str in dates_list:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        prev_date = date - datetime.timedelta(days=1)
        prev_date_str = prev_date.strftime("%d %b %Y")
        prev_dates.append(prev_date_str)
    return prev_dates


    dates = ["2022-01-01", "2022-02-28", "2022-03-01"]
print(compute_prev_date(dates)) # ['31 Dec 2021', '27 Feb 2022', '28 Feb 2022']

#This function uses the datetime module to convert the date strings in the
# input list dates_list to datetime objects, subtracts one day from each datetime 
#object using the timedelta class, and then converts the resulting datetime objects 
#back to strings using the strftime method. The %b format code in the strftime method 
#is used to represent the abbreviated month name.

Question 4

def main():
    try:
        qty = fetch_quantity()
        cost = fetch_cost()
        cost_per_quantity = cost/qty
    except Exception as e:
        if "fetch_quantity" in str(e):
            print(e)
            return
        else:
            pass
    # rest of the code

def fetch_quantity():
    # implementation

def fetch_cost():
    # implementation

#In this code, the main function is wrapped in a try-except block to handle exceptions that 
#might be raised from either of the two functions, fetch_quantity and fetch_cost. 
#If an exception is raised from fetch_quantity, the exception is printed and the 
#program terminates immediately by returning from the main function. 
#If an exception is raised from fetch_cost, the exception is simply ignored and the 
#program continues to the next step. The rest of the code outside of the try-except 
#block remains unchanged

Question 6 

class TestMath:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def test_add(self):
        return self.x + self.y

    def test_subtract(self):
        return self.x - self.y

    def test_multiply(self):
        return self.x * self.y

#In this updated version, the class has a constructor __init__ that accepts x and y as 
#arguments and stores them as instance variables self.x and self.y. 
#This eliminates the need to repeat the same values of x and y in every method. 
#The three methods test_add, test_subtract, and test_multiply no longer accept arguments 
#and instead use the instance variables self.x and self.y in their calculations. 
#This results in more concise and maintainable code, as any changes to the values of x and y can be
# made in a single place, in the constructor.






Question 5 

from django.http import JsonResponse

def get_params(request):
    name = request.GET.get('name', '')
    surname = request.GET.get('surname', '')
    return JsonResponse({'name': name, 'surname': surname})

    #In this implementation, the request.GET dictionary is used to retrieve the name and surname parameters from the query string of the URL. 
    #The get method is used with a default value of '' to return an empty string if either name or 
    #surname is not present in the query string. 
    #The values of name and surname are then returned as a JSON response using the JsonResponse 
    #class from the django.http module

