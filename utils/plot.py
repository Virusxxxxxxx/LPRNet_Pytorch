import csv
import matplotlib.pyplot as plt


def plotChart(filename, saveDir):
    file = saveDir + '/' + filename + ".csv"
    with open(file) as f:
        reader = csv.reader(f)
        head_row = next(reader)  # 表头
        x = []
        y = []
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))

    fig = plt.figure(dpi=128, figsize=(10, 6))
    ln1 = plt.plot(x, y, "r")
    plt.title(filename, fontsize=24)
    plt.grid()
    plt.savefig(saveDir + '/' + filename + ".png")


if __name__ == '__main__':
    plotChart("acc", "../runs/train/exp/")

