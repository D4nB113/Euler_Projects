fibArr = [1, 2]

fibSum = 0

while fibSum < 4000000:
    fibArr[0], fibArr[1] = fibArr[1], fibArr[0] + fibArr[1]
    if fibArr[1] % 2 == 0:
        fibSum += fibArr[1]

print("Total sum: ", fibArr[1])
