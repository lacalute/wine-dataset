# import neccessary libraries
import csv
import numpy as np
import matplotlib.pyplot as plt

# open csv file
with open('winequality-red.csv') as f:
    reader = csv.reader(f)
    x = list(reader)

# the creating new big array with data, without 3D structure
d = []
i = 0 
while i < len(x):
    x[i][0] = x[i][0].split(";")
    d.append(x[i][0])
    i = i + 1

titles = d[0]
d.pop(0)

# indexes
# let's imagine 1 is 0 (index I meant)
# 1 - fixed acidity
# 2 - volatile acidity
# 3 - citric acid
# 4 - residual sugar
# 5 - chlorides
# 6 - free sulfur dioxide
# 7 - total sulfur dioxide
# 8 - density
# 9 - pH
# 10 - sulphates
# 11 - alcohol
# 12 - quality (score between 0 and 10)

# the main func, which collect data by index and visualize them
status = True
print("0 - fixed acidity\n1 - volatile acidity\n2 - citric acid\n3 - residual sugar\n4 - chlorides\n5 - free sulfur dioxide\n6 - total sulfur dioxide\n7 - density\n8 - pH\n9 - sulphates\n10 - alcohol\n11 - quality (score between 0 and 10)")
while status:
    try:
        ask_x = int(input('Choose the data on the x axis -> '))
        ask_y = int(input('Choose the data on the y axis -> '))
        def program(index_x, index_y):
            x_set = []
            y_set = []
            z = 0 
            while z < len(d):
                x_set.append(float(d[z][index_x]))
                y_set.append(float(d[z][index_y]))
                z = z + 1
            # on this step we've got the data for plotting

            def plotting():
                plt.style.use('ggplot')
                plt.scatter(x_set, y_set)
                plt.title(f'Compare {titles[index_x]} with {titles[index_y]}')
                plt.xlabel(titles[index_x])
                plt.ylabel(titles[index_y])
                plt.show()
            plotting()
        program(ask_x, ask_y)
        status = False

    except ValueError:
        print('Wrong data, again please')
# simple statistic programm by Lacalute !!!