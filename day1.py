def part1():
    f = open('day_2_input.txt').readlines()
    highest_calories = 0
    current_calories = 0
    for i in range(len(f)):
        if f[i] == '\n':
            highest_calories = max(highest_calories, current_calories)
            current_calories = 0
        else:
            current_calories += int(f[i])
    print(highest_calories)


def part2():
    f = open('day_2_input.txt').readlines()
    current_calories = 0
    all_calories = []
    for i in range(len(f)):
        if f[i] == '\n':
            all_calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(f[i])
    all_calories = sorted(all_calories)[::-1]
    print(all_calories[0] + all_calories[1] + all_calories[2])


if __name__ == "__main__":
    part1()
    part2()
