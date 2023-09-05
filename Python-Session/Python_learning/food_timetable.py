#create a food daily food time table

import random
import sys
import pandas
import time
import os

while True:
    if os.path.exists("files/weekly_meal_planner.csv"):
        data = pandas.read_csv("files/weekly_meal_planner.csv")
        print(data)
    else:
        print("file does not exist")
    time.sleep(3)


