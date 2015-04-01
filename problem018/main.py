class Node:

    def __init__(self, value):
        self.highestValue = value
        self.value = value


def createTree():
    tree = []
    numbers = []
    with open("numbers.txt", "r") as f:
        for line in f:
            numbers = line.split(' ')
            numberOfNumbers = len(numbers)
            tree.append([])
            for i in range(0, numberOfNumbers):
                tree[-1].append(Node(int(numbers[i])))
    return tree

if __name__ == "__main__":
    tree = createTree()
    numberOfLevels = len(tree)
    for i in range(0, numberOfLevels - 1):
        numberOfElements = len(tree[i])
        for y in range(0, numberOfElements):
            value = tree[i][y].highestValue + tree[i + 1][y].value
            if(tree[i + 1][y].highestValue < value):
                tree[i + 1][y].highestValue = value
            value = tree[i][y].highestValue + tree[i + 1][y + 1].value
            if(tree[i + 1][y + 1].highestValue < value):
                tree[i + 1][y + 1].highestValue = value

    numberOfElements = len(tree[-1])
    highestValue = 0
    for i in range(0, numberOfElements):
        if(highestValue < tree[-1][i].highestValue):
            highestValue = tree[-1][i].highestValue
    print(highestValue)
