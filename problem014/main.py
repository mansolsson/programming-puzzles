def get_longest_collatz_sequence(limit):
    collatz_length_cache = [-1]
    longest_collatz_sequence = 0
    number_producing_longest_sequence = 0

    for i in range(1, limit):
        number = i
        length = 1
        while number != 1:
            if number < len(collatz_length_cache):
                length += collatz_length_cache[number]
                number = 1
            elif number % 2 == 0:
                number //= 2
                length += 1
            else:
                number = (number * 3 + 1) // 2
                length += 2
        collatz_length_cache.append(length)
        if longest_collatz_sequence < length:
            longest_collatz_sequence = length
            number_producing_longest_sequence = i
    return number_producing_longest_sequence

if __name__ == "__main__":
    answer = get_longest_collatz_sequence(1000000)
    print(answer)
