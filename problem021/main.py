def getSumOfDivisors(number):
    divisors = []
    if number % 2 == 0:
        inc = 1
    else:
        inc = 2

    stop = number // 2
    i = 1
    while i < stop:
        if number % i == 0:
            stop = number // i
            if stop == i:
                divisors.append(stop)
            else:
                divisors.append(stop)
                divisors.append(i)
        i += inc

    return sum(divisors) - number

if __name__ == "__main__":
    sumOfDivisors = [0, 0]
    for i in range(2, 10001):
        sumOfDivisors.append(getSumOfDivisors(i))

    sumOfAmicableNrs = 0
    for i in range(2, 10001):
        if sumOfDivisors[i] < 10000 and sumOfDivisors[sumOfDivisors[i]] == i \
           and sumOfDivisors[i] != i:
            sumOfAmicableNrs += sumOfDivisors[i]
    print(sumOfAmicableNrs)
