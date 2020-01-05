def largest_prime_factor(number):

    factor = number

    counter = 2

    while counter <= factor ** 0.5:
        if factor % counter == 0:
            factor = factor / counter
            counter -= 1
        counter += 1

    if factor >= 2:
        return factor
