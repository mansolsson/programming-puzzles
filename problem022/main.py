import string


def get_sum_of_all_name_scores():
    names = get_names()
    number_of_names = len(names)
    sum_of_name_scores = 0
    for i in range(0, number_of_names):
        sum_of_name_scores += get_name_score(names[i]) * (i + 1)
    return sum_of_name_scores


def get_names():
    with open("p022_names.txt", "r") as file:
        names = file.read()
    sorted_names = names.replace("\"", "").split(',')
    sorted_names.sort()
    return sorted_names


def get_name_score(name):
    name_score = 0
    for character in name:
        name_score += string.ascii_uppercase.index(character) + 1
    return name_score


if __name__ == "__main__":
    answer = get_sum_of_all_name_scores()
    print(answer)
