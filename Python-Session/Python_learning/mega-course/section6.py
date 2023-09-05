#user_input = input("Enter your name:  ")
##python 2
#message = "hello %s"  % user_input
##python 3
#message = f"hello  {user_input}"
#print(message)

name = input("enter your name:  ")
surname = input("enter your  surname: ")
when = "today"

#message = "hello  %s %s" % (name, surname)
message = f"hello {name} {surname}. What's up{when}"
print(message)
