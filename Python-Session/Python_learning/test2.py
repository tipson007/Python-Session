

def gym_routine(workout):
    if workout >= 4:
        print("That's a good week session")
    else:
        print("You need to work harder")
user_input = int(input("Enter the number of workout days: "))
print(gym_routine(user_input))



