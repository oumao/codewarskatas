def perimeter_squares(n):
    fibs = [0, 1]
    for i in range(2, n+2):
        fibs.append(fibs[i-1] + fibs[i-2])
    return sum(fibs)*4
print(perimeter_squares(5))