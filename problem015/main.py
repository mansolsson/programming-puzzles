import math


def get_lattice_paths(height, width):
    return math.factorial(height + width) // \
           (math.factorial((height + width) - height) * math.factorial(height))

if __name__ == '__main__':
    answer = get_lattice_paths(20, 20)
    print(answer)
