def irish_weather(temp):
    if temp >= 24:
        print(" That's extreme for ireland: ")
    elif temp  <= -10:
        print("Russia Vibes, That's definitely not Irish weather: ")
    else:
        print("Now that's what we call the norms: ")

user_input = float(input("Enter temperature: "))
print(irish_weather(user_input))


