days = int(input("Enter number of days: "))

hours = days*24

minutes = hours*60

seconds = minutes*60


hours1 = days//24

minutes_in_hours = days%24

minutes = minutes_in_hours

print("That is equivalent to", hours, "hours \nor", minutes,"minutes \nor ", seconds, "seconds")