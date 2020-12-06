from typing import List, Tuple

codes = [l.strip() for l in open('day5.txt').readlines()]


def halve(row, letter) -> List[int]:
    '''do one piece of the binary retrieval'''
    if letter in ("F", "L"):
        return row[:len(row)//2]
    if letter in ("B", "R"):
        return row[len(row)//2:]
    raise TypeError(f"{letter} is invalid")


def decode(code) -> Tuple[int, int]:
    '''get the row + seat numbers for one code'''
    row = list(range(128))
    seat = list(range(8))

    rowcode = code[:7]
    seatcode = code[7:]

    for letter in rowcode: # for each letter in the code
        row = halve(row, letter) # cut row in half (front/back)
    row = row[0] # the num we're left with is the row

    for letter in seatcode: # do the same with the seats
        seat = halve(seat, letter)
    seat = seat[0]

    return row, seat


def calc_id(code) -> int:
    '''return the seat id for one ticket code'''
    row, seat = decode(code)
    return (row * 8) + seat


print("part 1: highest code =", max(
    [(code, calc_id(code)) for code in codes], key=lambda x: x[1]))

calc_codes = [calc_id(code) for code in codes]
print("part 2: your seat id = ", list(
    filter(lambda x: x+1 not in calc_codes, calc_codes))[0]+1 )
