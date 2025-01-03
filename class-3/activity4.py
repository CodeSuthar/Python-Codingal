from datetime import datetime
import pytz
import calendar

# Define timezones
GMT = pytz.timezone('GMT')
EST = pytz.timezone('US/Eastern')
CST = pytz.timezone('US/Central')
MST = pytz.timezone('US/Mountain')
IST = pytz.timezone('Asia/Kolkata')

# Function to get current time in a timezone
def get_time(timezone):
    return datetime.now(timezone).strftime('%H:%M:%S')

# Function to get current date in a timezone
def get_date(timezone):
    return datetime.now(timezone).strftime('%Y-%m-%d')

while True:
    print("\nChoose Option:")
    print("1. Get today's date")
    print("2. Get current time")
    print("3. Get current time and date")
    print("4. Get calendar of the month")
    print("5. Get calendar of the year")
    print("6. Exit")
    option = int(input("Enter your choice: "))

    if option == 1:
        print("\nToday's Date:")
        print('GMT:', get_date(GMT))
        print('EST:', get_date(EST))
        print('CST:', get_date(CST))
        print('MST:', get_date(MST))
        print('IST:', get_date(IST))

    elif option == 2:
        print("\nCurrent Time:")
        print('GMT:', get_time(GMT))
        print('EST:', get_time(EST))
        print('CST:', get_time(CST))
        print('MST:', get_time(MST))
        print('IST:', get_time(IST))

    elif option == 3:
        print("\nCurrent Time and Date:")
        print('GMT:', get_time(GMT) + ' ' + get_date(GMT))
        print('EST:', get_time(EST) + ' ' + get_date(EST))
        print('CST:', get_time(CST) + ' ' + get_date(CST))
        print('MST:', get_time(MST) + ' ' + get_date(MST))
        print('IST:', get_time(IST) + ' ' + get_date(IST))

    elif option == 4:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))
        print("\nCalendar for", calendar.month_name[month], year)
        print(calendar.month(year, month))

    elif option == 5:
        year = int(input("Enter the year: "))
        print("\nCalendar for the year", year)
        print(calendar.TextCalendar().formatyear(year))

    elif option == 6:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")