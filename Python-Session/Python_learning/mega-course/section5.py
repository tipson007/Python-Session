def mean(value):
    #interpreter checks if the type of the list is a dictionary
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
       the_mean = sum(value) / len(value)
    
    return the_mean

monday_temperatures = [1,10.0, 10.0,10.0,20]
student_grades = {"ben": 1.3, "john": 7.1, "sam": 8.9}

print(mean(monday_temperatures))
##

#def foo(password):
 #   if len(password) >= 8:
  #      return True
   # else:
    #    return False
