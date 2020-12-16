import numpy as np
import matplotlib.pyplot as plt
import csv

with open("resource/date_price benz.csv", encoding='utf-8') as r_file:
    # типизированный символ разделения в  файле ","
    file_reader = csv.reader(r_file, delimiter=",")
    count = 0
    h = 1
    # дата
    dateArray = []

    #  массив X
    valueOXArray = []
    # массив y
    valueOYArray = []

    # Читаем файл
    for row in file_reader:
        if count > 0:
            try:
                valueOYArray.append(round(float(row[1]), 2))
                dateArray.append(row[0][:-6])
                valueOXArray.append(count * h)
                count += 1
            except:
                print('Предупреждение о неверном типе ' + row[1])
        else:
            count += 1

    k = 0.5  # теор. k
    b = 2  # теор. b
    mx = 0
    for val in valueOXArray:
        mx += val
    my = 0
    for val in valueOYArray:
        my += val

    mx = mx / count-2
    my = my / count-2

    a2 = np.dot(valueOXArray, valueOXArray) / count-2
    a11 = np.dot(valueOXArray, valueOYArray) / count-2
    kk = (a11 - mx * my) / (a2 - mx ** 2)
    bb = my - kk * mx
    ff = np.array([kk * z + bb for z in valueOXArray])
    fig, ax = plt.subplots(2, 1)
    ax[1].bar(dateArray, valueOYArray,color = 'red')
    ax[0].plot(valueOXArray, valueOYArray,color = 'blue')
    ax[0].plot(ff,color = 'red')
    ax[1].set_facecolor('white')
    ax[0].set_facecolor('white')
    ax[1].set_xlabel('Год')
    ax[1].set_ylabel('Стоимость')
    ax[0].set_xlabel('Год')
    ax[0].set_ylabel('Стоимось')
    plt.legend(['Стоимость'])





    fig.set_facecolor('white')
    fig.set_figwidth(17)  # ширина граффиков
    fig.set_figheight(12)  # высота граффиков
    plt.show()

