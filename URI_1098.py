i = 0
j_start = 1
j_end = j_start + 3
while i <= 2:
    for j in range(j_start, j_end, 1):
        if ((j + i)*10)%10 == 0:
            print("I={} J={}".format(round(i), round(j + i)))
        else:
            print("I={} J={}".format(round(i, 1), round(j + i, 1)))

    i += 0.2
