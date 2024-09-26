def factorial(n):
    """Calculates the factorial of a given number.

    Args:
        n: The number for which to calculate the factorial.

    Returns:
        The factorial of n.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numbers = input("Enter numbers separated by commas: ")
number_list = [int(num) for num in numbers.split(",")]

factorials = [factorial(num) for num in number_list]

print(", ".join(str(factorial) for factorial in factorials))