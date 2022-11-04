

def F():

    X = int(input('введите число'))
    if X == 0:
        return 1
    else:
        for i in range(1, X):
            X = X*i
        return X


print(F())
