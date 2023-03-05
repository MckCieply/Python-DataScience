import numpy as np
import matplotlib.pyplot as plt
names=np.array(["Basia", "Ania", "Grzesiek", "Elvira", "Katherine", "Thomas"])
heights=np.array([1.73, 1.61, 1.80, 1.58, 1.77, 1.90])# in metres
weights=np.array([61, 76, 78, 58, 57, 80])# in kilograms
bmis=weights / (heights*heights)
colors = []
for person in enumerate(names):
    thisPerson = person[0]
    if (bmis[thisPerson] <= 18.4):
        state = "underweight"
        colors.append("blue")
    elif (bmis[thisPerson] >= 18.4 and bmis[thisPerson] <= 24.9):
        state = "normal"
        colors.append("green")
    elif (bmis[thisPerson] >= 25 and bmis[thisPerson] <= 39.9):
        state = "overweight"
        colors.append("orange")
    elif (bmis[thisPerson] >= 40):
        state = "obese"
        colors.append("red")
    print(f"## {person[1]:<13}has BMI of {round(bmis[person[0]], 2)} which is {state}.")

plt.bar(names, bmis, color=colors)
plt.title("My friends' BMIs")
plt.xlabel("Name")
plt.ylabel("BMI Score")
plt.show()