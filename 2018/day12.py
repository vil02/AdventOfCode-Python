def get_rules():
    rule_lines = [
        line.strip().split(" => ") for line in open("input/day12.txt").readlines()
    ]
    rules = {k: v for (k, v) in rule_lines}
    return rules


def iterate_rows(
    initial: str, iterations: int, rules: dict, buffer_l: int, buffer_r: int, debug=True
) -> str:
    row = ("." * buffer_l) + initial + ("." * buffer_r)
    for i in range(iterations):
        if debug:
            print(i, row)
        next_row = ".."
        for j in range(len(row) - 4):
            if row[j : j + 5] in rules:
                next_row += rules[row[j : j + 5]]
            else:
                next_row += "."
        next_row += ".."
        row = next_row
        print(get_row_sum(row))

    if debug:
        print(iterations, row)
    return row


def get_row_sum(row):
    sum_i = 0
    for i in range(len(row)):
        if row[i] == "#":
            sum_i += i
    return sum_i


def puzzles():
    row = "#.####...##..#....#####.##.......##.#..###.#####.###.##.###.###.#...#...##.#.##.#...#..#.##..##.#.##"
    rules = get_rules()

    # puzzle 1
    left_buffer = 20
    right_buffer = 40
    row = iterate_rows(row, 20, rules, buffer_l=left_buffer, buffer_r=right_buffer)
    row_sum = get_row_sum(row[left_buffer:])
    print("20 iterations:", row_sum)

    # puzzle 2
    # visually after 71+ rows a gliding pattern emerges
    # every row adds a sum of 72
    left_buffer = 20
    right_buffer = 100
    row = iterate_rows(row, 100, rules, buffer_l=left_buffer, buffer_r=right_buffer)
    row_sum = get_row_sum(row[left_buffer:])
    print("100 iterations:", row_sum)
    # 90 - 8574
    print("after 50 bill:", (50000000000 - 101) * 72 + 12102)


if __name__ == "__main__":
    puzzles()
