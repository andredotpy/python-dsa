def print_items(n: int) -> None:
    for i in range(n):
        print(i)


def print_items_drop_contants(n: int) -> None:
    for i in range(n):
        print(i)
    
    # even though this is O(n), it is still a constant
    # so we drop it
    # and it becomes O(n) not O(n + n)
    for j in range(n):
        print(j)