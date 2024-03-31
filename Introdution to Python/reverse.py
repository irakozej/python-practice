def reverse(numbers):
    reversed_list = []
    for i in range(len(numbers)-1, -1, -1):
        reversed_list.append(numbers[i])
    return reversed_list