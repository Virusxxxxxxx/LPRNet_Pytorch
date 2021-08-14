import csv
from matplotlib import pyplot as plt

filename = 'loss.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)  # 表头
    x = []
    y = []
    for row in reader:
        x.append(row[0])
        y.append(row[1])
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(x, y, c='red')
plt.title(filename, fontsize=24)
plt.xlabel('epoch', fontsize=16)
plt.ylabel("Loss", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
