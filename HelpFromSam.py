def helpFromSam(target):
    currScore = 1

    while currScore * 2 < target:
        currScore *= 2

    return target - currScore + 1


if __name__ == "__main__":
    A = int(input())

    print(helpFromSam(A))
