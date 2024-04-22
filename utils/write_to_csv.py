import csv

# Варіант №7
x_train = [[43, 16], [5, 44], [24, 50], [41, 49], [28, 40], [49, 20], [5, 20], [31, 32], [11, 38]]
y_train = [1, -1, -1, -1, 1, -1, 1, -1, 1]

with open('train_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Feature1', 'Feature2', 'Label'])
    for x, y in zip(x_train, y_train):
        writer.writerow(x + [y])