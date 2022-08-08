import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
import os
import csv
import time

children_books = [0 for _ in range(18)]
total_books = [0 for _ in range(18)]

for file in os.listdir("./data"):
    if file == "souhrn.csv":
        continue
    with open(f"./data/{file}") as f:
        csv_reader = csv.reader(f, delimiter=";")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[2] == "A+":
                    year = int(((file.split('.'))[0]))
                    index = year - 1998
                    total_books[index] += int(row[4])
                elif row[2] == "A-":
                    year = int(((file.split('.'))[0]))
                    index = year - 1998
                    children_books[index] += int(row[4])
                    total_books[index] += int(row[4])
                else:
                    pass


ratios = [0 for _ in range(18)]

for i in range(18):
    ratios[i] = children_books[i]/total_books[i]

years = [x for x in range(1998, 2016)]

x = np.array(years)
y = np.array(ratios)

plt.plot(x, y, 'o')
plt.title("Poměr knih vypůjčených dětmi mladšími 15 let")
plt.xlabel("Rok")
plt.ylabel("Poměr knih vypůjčených dětmi")

a, b, c = np.polyfit(x, y, 2)
m, t = np.polyfit(x,y,1)

plt.plot(x, a*(x**2) + b*x + c)
plt.plot(x, m*x + t)
plt.xticks(years)
plt.show()