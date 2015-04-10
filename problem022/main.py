import string

def getNames():
    names = ""
    with open("p022_names.txt", "r") as f:
        names = f.read()
    sortedNames = names.replace("\"", "").split(',')
    sortedNames.sort()
    return sortedNames


def getNameScore(name):
    nameScore = 0
    for character in name:
        nameScore += string.ascii_uppercase.index(character) + 1
    return nameScore


if __name__ == "__main__":
    names = getNames()
    numberOfNames = len(names)
    sumOfNameScores = 0
    for i in range(0, numberOfNames):
        sumOfNameScores += getNameScore(names[i]) * (i + 1)
    print(sumOfNameScores)