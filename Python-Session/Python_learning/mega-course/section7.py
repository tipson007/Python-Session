##for loop

#convert to fahrenheight--
# (0degree celcius * 9/5) + 32 =  32degree fahrenheight

def conv_to_fahrenheight(celcius):
    return celcius * 9/5 + 32

monday_temperatures = [3, 4, 1, 31, 23, -1, 0]

for temperature in monday_temperatures:
    print(conv_to_fahrenheight(temperature))

##while loop

# username = ''

# while username != "pypy":
  #  username = input("Enter username: ")


while True:
    username = input("Enter username: ")
    if username == 'sam':
        break
    else:
        continue

#You can combine a dictionary for loop with string formatting to create text containing information from the dictionary:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))


#Another (better) way to do it::

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))
#