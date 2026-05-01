def bad_function(x):
    temp = 10
    print("debug info")

    total = 0

    for i in range(x):
        total += i

    for j in range(x):
        total += j

    for k in range(x):
        total += k

    return total