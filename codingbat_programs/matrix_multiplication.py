# Program to multiply two matrices using nested loops

X = [
    [1, 2],
    [3, 4]
    ]
Y = [
    [1,1],
    [1,5]
    ]
result = [[0,0],[0,0]]


for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for row in result:
    print(row)
