##dictionary

student_grades = {"ben": 1.3, "john": 7.1, "sam": 8.9}

for grades in student_grades.values():
    print(grades)
    
phone_numbers = {"sam smith": "+0136763445", "becca higgins": "+7864373453"}

for key, values in phone_numbers.items():
    print("{} has a phone number:  {}" .format(key, values))


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key, values  in phone_numbers.items():
    #python 2 formatting
    print("%s: %s "  % (key, values))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for values in phone_numbers.values():
    #replacing strings
    print(values.replace( "+",  "00"))

#append the first item of weekend to workdays
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])