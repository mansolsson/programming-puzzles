def get_sum_of_multiples(limit):
    sum_of_multiplies = 0
    for i in range(3, limit):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiplies += i
    return sum_of_multiplies

if __name__ == "__main__":
    answer = get_sum_of_multiples(1000)
    print(answer)
