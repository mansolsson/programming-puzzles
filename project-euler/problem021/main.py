import sys
sys.path.insert(0, "../")
import pemath


def get_sum_of_amicable_number(limit):
    sum_of_divisors = [0, 0]
    for i in range(2, limit + 1):
        sum_of_divisors.append(sum(pemath.get_divisors(i)) - i)

    sum_of_amicable_nrs = 0
    for i in range(2, limit + 1):
        if sum_of_divisors[i] < limit and sum_of_divisors[sum_of_divisors[i]] == i \
                and sum_of_divisors[i] != i:
            sum_of_amicable_nrs += sum_of_divisors[i]
    return sum_of_amicable_nrs

if __name__ == "__main__":
    answer = get_sum_of_amicable_number(10000)
    print(answer)
