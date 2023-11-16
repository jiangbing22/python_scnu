def is_narcissistic(num):
    num_str = str(num)
    power = len(num_str)
    digits = map(int, num_str)
    powered = sum(map(lambda x: x ** power, digits))
    return powered == num

narcissistic_3_digits = [num for num in range(100, 1000) if is_narcissistic(num)]
narcissistic_4_digits = [num for num in range(1000, 10000) if is_narcissistic(num)]
narcissistic_5_digits = [num for num in range(10000, 100000) if is_narcissistic(num)]

print("3位水仙花数:", narcissistic_3_digits)
print("4位水仙花数:", narcissistic_4_digits)
print("5位水仙花数:", narcissistic_5_digits)
