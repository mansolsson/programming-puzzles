if __name__ == "__main__":
    cache = [-1, 1]
    result = 1
    longest = 1

    for i in range(2, 1000000):
        number = i
        length = 0
        while(number != 1):
            if number < len(cache):
                length += cache[number]
                number = 1
            elif number % 2 == 0:
                number //= 2
                length += 1
            else:
                number = (number * 3 + 1) // 2
                length += 2
        cache.append(length)
        if longest < length:
            longest = length
            result = i
    print(result)
