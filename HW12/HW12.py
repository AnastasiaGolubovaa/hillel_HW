def is_power_of_two(number):
    if number <= 0:
        return 'no'
    elif number == 1:
        return 'yes'
    else:
        while number % 2 == 0:
            number //= 2
        return 'yes' if number == 1 else 'no'
print(is_power_of_two(256))
print(is_power_of_two(12))
print(is_power_of_two(16))



