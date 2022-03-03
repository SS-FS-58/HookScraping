import csv
import numpy as np
from sklearn.linear_model import LinearRegression

datas = []
data_trans = []
with open("sub_Paper_box_data_1000_TiBa_7.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        datas.append(row)

    # data_trans = np.array(datas).transpose()
    # print(data_trans)
    length = len(datas)
    # length2 = len(datas[0])
    for num in range(1, length):
        datas[num][6] = float(datas[num][6]) / float(datas[num][2])
        datas[num][7] = float(datas[num][7]) / float(datas[num][2])
        datas[num][8] = float(datas[num][8]) / 1000
        datas[num][9] = float(datas[num][9]) / 1000
        datas[num][10] = float(datas[num][10]) / 2000
        datas[num][11] = float(datas[num][11]) / 2000
        datas[num][12] = float(datas[num][12]) / 3000
        datas[num][13] = float(datas[num][13]) / 3000
        datas[num][14] = float(datas[num][14]) / 4000
        datas[num][15] = float(datas[num][15]) / 4000

    # x = np.array(data_trans[0][1:]).reshape((-1, 1)).astype(np.float)
    # y = np.array(data_trans[1][1:]).astype(np.float)
    # # x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
    # # y = np.array([5, 20, 14, 32, 22, 38])
    # model = LinearRegression().fit(x, y)
    # r_sq = model.score(x, y)
    # print("coefficient of determination:", r_sq)
    # print("intercept:", model.intercept_)
    # print("slope:", model.coef_)

    # y_pred = model.predict(x)
    # print("predicted response:", y_pred, sep="\n")
    # for i in range(1, length - 3, 2):
    #     for j in range(1, length2):
    #         value = int(datas[length - i - 2][j]) - int(datas[length - i - 1][j])
    #         datas[length            - i - 1][j] = str(value)
with open("sub_Paper_box_data_1000_TiBa_7_analysis.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # writer.writerow(["number", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    for data in datas:
        writer.writerow(data)
