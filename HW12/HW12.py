def is_power_of_two(number):
    if number == 1:
        return 'yes'
    elif number % 2 == 1 or number == 0:
        return 'no'
    else:
        return is_power_of_two(number // 2)

print(is_power_of_two(256))
print(is_power_of_two(12))
print(is_power_of_two(16))







