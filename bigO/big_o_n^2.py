def print_items(n: int) -> None:
    for i in range(n):
        for j in range(n):
            print(i, j)


print_items(10)


def print_items_drop_non_dominants(n: int) -> None:
    for i in range(n):
        for j in range(n):
            print(i, j)
    # even though this is O(n), it's not the dominant term
    # so we drop it
    # and it becomes O(n^2) not O(n + n^2)
    for k in range(n):
        print(k)
