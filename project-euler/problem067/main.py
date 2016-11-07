class Node:

    def __init__(self, value):
        self.highest_value = value
        self.value = value


def get_maximum_path_sum():
    tree = create_tree()
    number_of_levels = len(tree)
    for i in range(0, number_of_levels - 1):
        number_of_elements = len(tree[i])
        for y in range(0, number_of_elements):
            value = tree[i][y].highest_value + tree[i + 1][y].value
            if tree[i + 1][y].highest_value < value:
                tree[i + 1][y].highest_value = value
            value = tree[i][y].highest_value + tree[i + 1][y + 1].value
            if tree[i + 1][y + 1].highest_value < value:
                tree[i + 1][y + 1].highest_value = value

    number_of_elements = len(tree[-1])
    highest_value = 0
    for i in range(0, number_of_elements):
        if highest_value < tree[-1][i].highest_value:
            highest_value = tree[-1][i].highest_value
    return highest_value


def create_tree():
    tree = []
    with open("numbers.txt", "r") as f:
        for line in f:
            numbers = line.split(' ')
            number_of_numbers = len(numbers)
            tree.append([])
            for i in range(0, number_of_numbers):
                tree[-1].append(Node(int(numbers[i])))
    return tree

if __name__ == "__main__":
    answer = get_maximum_path_sum()
    print(answer)

