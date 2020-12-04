import operator
import functools
from typing import List

lines: List[str] = [line.strip() for line in open("day3_1.txt").readlines()]


def run_slope(lines: List[str], right: int = 3, down: int = 1) -> int:

    line_length: int = len(lines[0])

    horizontal = 0
    vertical = 0
    tally = 0

    while True:
        horizontal += right
        if horizontal >= line_length:
            horizontal -= line_length  # it wraps
        vertical += down
        try:
            tally += int(lines[vertical][horizontal] == '#')
        except IndexError:
            break

    return tally


if __name__ == "__main__":
    print("Part 1:", run_slope(lines, 3, 1))
    print("Part 2:", functools.reduce(operator.mul, [run_slope(
        lines, r, d) for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]))
