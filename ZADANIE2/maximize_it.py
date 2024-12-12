from itertools import product


def maximize_expression(K, M, lists):
    combinations = product(*lists)

    max_value = 0
    for combination in combinations:
        current_value = sum(x ** 2 for x in combination) % M
        max_value = max(max_value, current_value)

    return max_value


if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
