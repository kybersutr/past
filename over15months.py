import matplotlib.pyplot as plt
import scipy.stats as st
import os
import csv
import time

months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for file in os.listdir("./data"):
    if file == "souhrn.csv":
        continue
    with open(f"./data/{file}") as f:
        csv_reader = csv.reader(f, delimiter=";")
        line_count = 0
        total = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                total += int(row[4])
                if row[2] == "A+":
                    date = time.strptime(row[1], '%Y-%m-%d %H:%M:%S')
                    month = date.tm_mon
                    months[month - 1] += int(row[4])
        print(file, total)

print(months)
print(sum(months))

for i in range(12):
    months[i] = months[i]/18

month_nums = [x for x in range(1, 13)]

plt.bar(range(1,13), months)
plt.title("Průměrný počet knih vypůjčených dospělými v jednotlivých měsících")
plt.xticks(month_nums)
plt.xlabel("Měsíc")
plt.ylabel("Počet vypůjčených knih")
plt.show()

print(st.chisquare(months))