def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = change_to_binary(num)
        answer.append(1 if is_valid(bin_num) else 0)
    return answer


def change_to_binary(num):
    binary_str = bin(num)[2:]
    length = len(binary_str)
    height = 1
    while (2 ** height - 1) < length:
        height += 1
    size = 2 ** height - 1
    add_zeros = size - length
    return "0" * add_zeros + binary_str


def is_valid(s):
    stack = [s]

    while stack:
        node = stack.pop()
        mid = len(node) // 2
        root = node[mid]
        left = node[:mid]
        right = node[mid + 1:]

        if root == '0' and ('1' in left or '1' in right):
            return False

        if len(left) > 1:
            stack.append(left)
        if len(right) > 1:
            stack.append(right)

    return True
