import csv
import numpy as np
import matplotlib.pyplot as plt

with open('winequality-red.csv') as f:
    reader = csv.reader(f)

    x = list(reader)
    x.pop(0)

y = []
i = 0 
while i < len(x):
    x[i][0] = x[i][0].split(";")
    y.append(x[i][0])
    i = i + 1




ph = []
qualities = []
z = 0 
while z < len(y):
    ph.append(y[z][4])
    qualities.append(y[z][11])
    z = z + 1



ph_data = [float(q) for q in ph]



ger = {3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
lis = list(ger.keys())

qu = [int(po) for po in qualities]

def sort():
    counter = 0
    while counter < len(lis):
        af = 0
        while af < len(ph_data):
            if qu[af] == lis[counter]:
                ger[lis[counter]].append(ph_data[af])
                af = af + 1
            else:
                af = af + 1
        counter = counter + 1
    
    
sort()



ph_finale = []
h = 0
while h < len(lis):
    ph_finale.append(sum(ger[lis[h]]) / len(ger[lis[h]]))
    h = h + 1


print(ph_finale)

def plotting():
    plt.style.use('ggplot')
    plt.xlabel('Качество (от 1 до 10)')
    plt.ylabel('Хлориды')
    plt.title('Красное вино')
    plt.bar(lis, ph_finale,label=lis)
    plt.show()

plotting()