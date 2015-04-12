def find_pythagorean_triplet(sought_triplet_sum):
    a_max = sought_triplet_sum // 3 + 1
    for a in range(1, a_max):
        b_max = (sought_triplet_sum - a) // 2 + 1
        for b in range(a + 1, b_max):
            c = sought_triplet_sum - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return -1

if __name__ == "__main__":
    answer = find_pythagorean_triplet(1000)
    print(answer)
