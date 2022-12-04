def part1():
    """
    A --> Rock <-- X +1
    B --> Paper <-- Y +2
    C --> Scissors <-- Z +3
    Loss: 0, Draw: 3, Win: 6
    :return:
    """
    f = open('day_2_input.txt').readlines()
    current_score, total_score = 0, 0
    for i in range(len(f)):
        current_match = f[i].strip()
        if current_match[0] == 'A':
            if current_match[2] == 'X':
                current_score += 1 + 3
                total_score += current_score
                current_score = 0
            if current_match[2] == 'Y':
                current_score += 2 + 6
                total_score += current_score
                current_score = 0
            if current_match[2] == 'Z':
                current_score += 3 + 0
                total_score += current_score
                current_score = 0
        elif current_match[0] == 'B':
            if current_match[2] == 'X':
                current_score += 1 + 0
                total_score += current_score
                current_score = 0
            if current_match[2] == 'Y':
                current_score += 2 + 3
                total_score += current_score
                current_score = 0
            if current_match[2] == 'Z':
                current_score += 3 + 6
                total_score += current_score
                current_score = 0
        elif current_match[0] == 'C':
            if current_match[2] == 'X':
                current_score += 1 + 6
                total_score += current_score
                current_score = 0
            if current_match[2] == 'Y':
                current_score += 2 + 0
                total_score += current_score
                current_score = 0
            if current_match[2] == 'Z':
                current_score += 3 + 3
                total_score += current_score
                current_score = 0
    print(total_score)


def part2():
    f = open('day_2_input.txt').readlines()
    current_score, total_score = 0, 0
    for i in range(len(f)):
        current_match = str(f[i].splitlines()[0])
        if current_match == 'A X':
            total_score += 0 + 3
        elif current_match == 'B X':
            total_score += 0 + 1
        elif current_match == 'C X':
            total_score += 0 + 2
        elif current_match == 'A Y':
            total_score += 3 + 1
        elif current_match == 'B Y':
            total_score += 3 + 2
        elif current_match == 'C Y':
            total_score += 3 + 3
        elif current_match == 'A Z':
            total_score += 6 + 2
        elif current_match == 'B Z':
            total_score += 6 + 3
        elif current_match == 'C Z':
            total_score += 6 + 1
    print(total_score)


if __name__ == "__main__":
    part1()
    part2()
