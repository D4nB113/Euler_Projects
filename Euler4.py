def is_palindrome(number):
    number = str(number)

    number_rev = number[::-1]

    if number == number_rev:
        return True
    return False


a_max, b_max = 0, 0

for a in range(999, 99, -1):
    for b in range(999, 99, -1):
        if (a * b) < (a_max * b_max):
            break
        if is_palindrome(a * b):
            a_max, b_max = a, b

print("Palindrome: ", a_max, "x", b_max, " = ", a_max*b_max)