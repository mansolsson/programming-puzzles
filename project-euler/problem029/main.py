def get_nr_of_distinct_powers(start, end):
    numbers = []
    for i in range(start, end + 1):
        for y in range(start, end + 1):
            numbers.append(i ** y)
    return len(set(numbers))

if __name__ == "__main__":
    answer = get_nr_of_distinct_powers(2, 100)
    print(answer)
