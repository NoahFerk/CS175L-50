#Noah Ferker
#CS175L
#Expense Pie chart

import matplotlib.pyplot as plt
import numpy as np

def main():
    try:
        expenses = open('expenses.txt','r')
    except IOError:
        print('file not found')
    accountant = []
    for line in expenses:
        line = line.strip('\n')
        accountant.append(line.split('\t'))
    expenses.close()
    label = []
    value = []
    for x in accountant:
        label.append(x[0])
        value.append(int(x[1]))

    y = np.array(value)

    plt.pie(y,labels = label)
    plt.show()

if __name__ == '__main__':
    main()
 
