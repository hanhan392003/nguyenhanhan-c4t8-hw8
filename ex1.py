for y in range(5):
    for x in range(5):
        if y == 1 and ( x == 0 or x== 4):
            print(" ", end= " ")
        else:
            print("x", end = " ")
    print()