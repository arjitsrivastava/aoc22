"""
            [G] [W]         [Q]
[Z]         [Q] [M]     [J] [F]
[V]         [V] [S] [F] [N] [R]
[T]         [F] [C] [H] [F] [W] [P]
[B] [L]     [L] [J] [C] [V] [D] [V]
[J] [V] [F] [N] [T] [T] [C] [Z] [W]
[G] [R] [Q] [H] [Q] [W] [Z] [G] [B]
[R] [J] [S] [Z] [R] [S] [D] [L] [J]
 1   2   3   4   5   6   7   8   9
"""


def get_hardcoded_list() -> list:
    hardcoded_list = [[], ['Z', 'V', 'T', 'B', 'J', 'G', 'R'], ['L', 'V', 'R', 'J'], ['F', 'Q', 'S'],
                      ['G', 'Q', 'V', 'F', 'L', 'N', 'H', 'Z'], ['W', 'M', 'S', 'C', 'J', 'T', 'Q', 'R'],
                      ['F', 'H', 'C', 'T', 'W', 'S'], ['J', 'N', 'F', 'V', 'C', 'Z', 'D'],
                      ['Q', 'F', 'R', 'W', 'D', 'Z', 'G', 'L'], ['P', 'V', 'W', 'B', 'J']]
    return hardcoded_list


def get_test_list():
    hardcoded_list = [[], ['N', 'Z'], ['D', 'C', 'M'], ['P']]
    return hardcoded_list


def part1():
    # hardcoded_list = get_test_list()
    hardcoded_list = get_hardcoded_list()

    f = open('day_5_input_modified.txt').readlines()
    for i in range(len(f)):
        s = f[i].strip().split(' ')
        s_int = list(map(int, s))

        for j in range(s_int[0]):
            to_pop = hardcoded_list[s_int[1]].pop(0)
            hardcoded_list[s_int[2]].insert(0, to_pop)

    for i in range(1, len(hardcoded_list)):
        print(hardcoded_list[i][0]),


def part2():
    # hardcoded_list = get_test_list()
    hardcoded_list = get_hardcoded_list()

    f = open('day_5_input_modified.txt').readlines()
    for i in range(len(f)):
        s = f[i].strip().split(' ')
        s_int = list(map(int, s))

        to_pop = []
        for j in range(s_int[0]):
            to_pop.append(hardcoded_list[s_int[1]].pop(0))
        hardcoded_list[s_int[2]] = to_pop + hardcoded_list[s_int[2]]

    for i in range(1, len(hardcoded_list)):
        print(hardcoded_list[i][0]),


if __name__ == "__main__":
    part1()
    part2()
