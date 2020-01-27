flowers = {
    "iris_setosa": {
        "sepal_length": [3.6, 4.9, 4.8, 4.7],
        "sepal_width": [2.9, 3.3, 3.2, 3.1],
        "petal_length": [1.3, 1.2, 1.5, 1.4],
    },
    "iris_virginica": {
        "sepal_length": [7.2, 7.0, 7.9],
         "sepal_width": [3.1, 2.7, 2.8],
        "petal_length": [5.5, 5.5, 6.5],
    },
    "iris_versicolor": {
        "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
         "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
        "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8],
    },
}
sepalLengthAll = 0
sepalLengthCount = 0
sepalWidthAll = 0
sepalWidthCount = 0
petalLengthAll = 0
petalLengthCount = 0

for keys, value in flowers.items():
    for keys1,value1 in value.items():
        if keys1 == 'sepal_length':
            for i in value1:
                sepalLengthAll = sepalLengthAll + i
                sepalLengthCount = sepalLengthCount +1
        if keys1 == 'sepal_width':
            for i in value1:
                sepalWidthAll = sepalWidthAll + i
                sepalWidthCount = sepalWidthCount +1
        if keys1 == 'petal_length':
            for i in value1:
                petalLengthAll = petalLengthAll + i
                petalLengthCount = petalLengthCount +1

print('sepalLengthAll', sepalLengthAll/sepalLengthCount)
print('sepalWidthAll', sepalWidthAll/sepalWidthCount)
print('sepalWidthAll', petalLengthAll/petalLengthCount)