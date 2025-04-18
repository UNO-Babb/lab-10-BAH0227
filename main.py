#MatPlot.py
#Name:
#Date:
#Assignment:

import cars
import pandas
import matplotlib.pyplot as plt
car = cars.get_car()

#print(car[0]["Engine Information"]["Engine Statistics"]["Horsepower"])
#print(car[0]["Identification"]["Model Year"])
mpgs = []
horsepowers = []
for carmodel in car:
    mpg = carmodel["Fuel Information"]["City mpg"]
    horsepower = carmodel["Engine Information"]["Engine Statistics"]["Horsepower"]
    mpgs.append(mpg)
    horsepowers.append(horsepower)
    #print(year, horsepower)

df = pandas.DataFrame({"MPG": mpgs,
                        "Horsepower": horsepowers})

print(df)
df.plot(kind = 'scatter', x = 'Horsepower', y = 'MPG')
plt.savefig("output")