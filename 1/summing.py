def sum_numbers(numbers=None):
    numbers_to_sum = range(1, 101) if numbers is None else numbers
    return sum(numbers_to_sum)
