total_working_days = int(input("Enter total number of working days: "))
days_absent = int(input("Enter total number of days absent: "))

days_attended = total_working_days - days_absent
attendance_percentage = (days_attended / total_working_days) * 100

print("Attendance Percentage:", round(attendance_percentage, 2), "%")

if attendance_percentage >= 75:
    print("Eligible to sit in the exam.")
else:
    print("Not eligible to sit in the exam.")