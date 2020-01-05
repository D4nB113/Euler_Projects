def evenfibonacchinumbers(number):

    fibarr = [1, 2]
    fibsum = 0

    while fibsum < number:
        fibarr[0], fibarr[1] = fibarr[1], fibarr[0] + fibarr[1]
        if fibarr[1] % 2 == 0:
            fibsum += fibarr[1]

    print("Total sum: ", fibarr[1])
