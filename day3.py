def part1():
    all_alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    f = open('day_3_input.txt').readlines()
    total_diff = 0
    for i in range(len(f)):
        current_str = f[i].strip()
        len_current_str = len(current_str)
        first_half, second_half = \
            current_str[:len_current_str // 2], current_str[len_current_str // 2:len_current_str]
        common_one = list((set(first_half) & set(second_half)))
        for j in range(len(all_alphabets)):
            if all_alphabets[j] == common_one[0]:
                total_diff += j + 1
    print(total_diff)


def part2():
    all_alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    f = open('day_3_input.txt').readlines()
    total_diff = 0
    for i in range(0, len(f), 3):
        str1, str2, str3 = f[i].strip(), f[i + 1].strip(), f[i + 2].strip()
        common_one = list(set(str1) & set(str2) & set(str3))
        for j in range(len(all_alphabets)):
            if all_alphabets[j] == common_one[0]:
                total_diff += j + 1
    print(total_diff)


if __name__ == "__main__":
    part1()
    part2()
