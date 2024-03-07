import numpy as np

# Створення першого варіанту даних
# TODO import from file
x_train_1 = np.array([[10, 50], [20, 30], [25, 30], [20, 60], [15, 70], [40, 40], [30, 45], [20, 45], [40, 30], [7, 35]])
y_train_1 = np.array([-1, 1, 1, -1, -1, 1, 1, -1, 1, -1])

# Створення додаткових варіантів даних
additional_datasets = []

for i in range(2, 16):
    x_train_additional = np.random.randint(5, 51, size=(10, 2))
    y_train_additional = np.random.choice([-1, 1], size=10)
    
    # Видалення перетину з першим варіантом
    intersect_indices = np.where(np.isin(x_train_additional, x_train_1).all(axis=1))[0]
    if len(intersect_indices) > 0:
        x_train_additional = np.delete(x_train_additional, intersect_indices, axis=0)
        y_train_additional = np.delete(y_train_additional, intersect_indices)
    
    additional_datasets.append((x_train_additional, y_train_additional))

# Виведення всіх даних
print("Перший варіант:")
print("x_train_1:")
print(x_train_1)
print("y_train_1:")
print(y_train_1)
print()

for i, (x_train_additional, y_train_additional) in enumerate(additional_datasets, start=2):
    print(f"Варіант {i}:")
    print(f"x_train_{i}:")
    print(x_train_additional)
    print(f"y_train_{i}:")
    print(y_train_additional)
    print()