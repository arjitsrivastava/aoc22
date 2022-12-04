def part1():
    f = open('day_4_input.txt').readlines()
    total_count = 0
    for i in range(len(f)):
        pair = f[i].strip().split(',')
        first_half = pair[0].split('-')
        second_half = pair[1].split('-')

        first_range, second_range = set(), set()

        for i in range(int(first_half[0]), int(first_half[1]) + 1):
            first_range.add(i)
        for i in range(int(second_half[0]), int(second_half[1]) + 1):
            second_range.add(i)
        if first_range.issubset(second_range) or (first_range).issuperset(second_range):
            total_count += 1
    print(total_count)


def part2():
    f = open('day_4_input.txt').readlines()
    total_count = 0
    for i in range(len(f)):
        pair = f[i].strip().split(',')
        first_half = pair[0].split('-')
        second_half = pair[1].split('-')

        first_range, second_range = set(), set()
        for i in range(int(first_half[0]), int(first_half[1]) + 1):
            first_range.add(i)
        for i in range(int(second_half[0]), int(second_half[1]) + 1):
            second_range.add(i)
        if len((first_range & second_range)) > 0:
            total_count += 1
    print(total_count)


if __name__ == "__main__":
    part1()
    part2()
