import numpy as np
import matplotlib.pyplot as plt

malelen = []
maleweigh = []
femalelen = []
femaleweigh = []

incToCm = 2.54
poundToKg = 0.454

gender = np.genfromtxt("weight-height(1).csv", delimiter=",", dtype=str, skip_header=1, usecols=0, deletechars="'")
lenght = np.genfromtxt("weight-height(1).csv", delimiter=",", dtype=float, skip_header=1, usecols=1)
weight = np.genfromtxt("weight-height(1).csv", delimiter=",", dtype=float, skip_header=1, usecols=2)

gender = np.char.strip(gender, '"')

for i in range(len(lenght)):
    lenght[i] = lenght[i] * incToCm

for i in range(len(weight)):
    weight[i] = weight[i] * poundToKg

#data separation
for i in range(len(gender)):
    if gender[i] == "Male":
        malelen.append(lenght[i])
        maleweigh.append(weight[i])
    else:
        femalelen.append(lenght[i])
        femaleweigh.append(weight[i])

#len
yAllLen = [np.mean(lenght), np.median(lenght), np.std(lenght), np.var(lenght)]
yMalelen = [np.mean(malelen), np.median(malelen), np.std(malelen), np.var(malelen)]
yFemaleLen = [np.mean(femalelen), np.median(femalelen), np.std(femalelen), np.var(femalelen)]

#weight
yAllweight = [np.mean(weight), np.median(weight), np.std(weight), np.var(weight)]
yMaleweight = [np.mean(maleweigh), np.median(maleweigh), np.std(maleweigh), np.var(maleweigh)]
yFemaleWeight = [np.mean(femaleweigh), np.median(femaleweigh), np.std(femaleweigh), np.var(femaleweigh)]

print(f"Students mean height (cm): {yAllLen[0]}")
print(f"Students median height(cm): {yAllLen[1]}")
print(f"Students standard dev height(cm): {yAllLen[2]}")
print(f"Students variance height(cm): {yAllLen[3]}")
print()

print(f"Male mean height(cm): {yMalelen[0]}")
print(f"Male median height(cm):{yMalelen[1]}")
print(f"Male standard dev height(cm): {yMalelen[2]}")
print(f"Male variance height(cm): {yMalelen[3]}")
print()

print(f"Female mean height(cm): {yFemaleLen[0]}")
print(f"Female median height(cm): {yFemaleLen[1]}")
print(f"Female standard dev height(cm): {yFemaleLen[2]}")
print(f"Female variance height(cm): {yFemaleLen[3]}")
print()
print()

print(f"Students mean weight (kg): {yAllweight[0]}")
print(f"Students median weight(kg): {yAllweight[1]}")
print(f"Students standard dev weight(kg): {yAllweight[2]}")
print(f"Students variance weight(kg): {yAllweight[3]}")
print()

print(f"Male mean weight(kg): {yMaleweight[0]}")
print(f"Male median weight(kg):{yMaleweight[1]}")
print(f"Male standard dev weight(kg): {yMaleweight[2]}")
print(f"Male variance weight(kg): {yMaleweight[3]}")
print()

print(f"Female mean weight(kg): {yFemaleWeight[0]}")
print(f"Female median weight(kg): {yFemaleWeight[1]}")
print(f"Female standard dev weight(kg): {yFemaleWeight[2]}")
print(f"Female variance weight(kg): {yFemaleWeight[3]}")



plt.hist(lenght, 10)
plt.title("all subject height")
plt.ylabel("cm")
plt.show()

plt.hist(malelen, 10)
plt.title("male height")
plt.ylabel("cm")
plt.show()

plt.hist(femalelen, 10)
plt.title("female height")
plt.ylabel("cm")
plt.show()

