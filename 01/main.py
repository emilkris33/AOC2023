

def task1():
    input_file = open("input.txt")
    sum = 0
    for line in input_file.readlines():
        for c in line:
            if c in "0123456789":
                first = c
                break
        for c in line[::-1]:
            if c in "0123456789":
                last = c
                break
        sum += int(first + last)
    return sum


def getDigit(text, pos):
    if text[pos] in "0123456789":
        return text[pos]
    if text[pos:pos+3] == "one":
        return "1"
    if text[pos:pos+3] == "two":
        return "2"
    if text[pos:pos+5] == "three":
        return "3"
    if text[pos:pos+4] == "four":
        return "4"
    if text[pos:pos+4] == "five":
        return "5"
    if text[pos:pos+3] == "six":
        return "6"
    if text[pos:pos+5] == "seven":
        return "7"
    if text[pos:pos+5] == "eight":
        return "8"
    if text[pos:pos+4] == "nine":
        return "9"
    return None

def task2():
    input_file = open("input.txt")
    sum = 0
    for line in input_file.readlines():
        for c in range(len(line)):
            d = getDigit(line, c)
            if d is not None:
                first = d
                break
        for c in range(len(line)):
            d = getDigit(line, len(line) - c - 1)
            if d is not None:
                last = d
                break
        sum += int(first + last)
    return sum

if __name__ == '__main__':
    print(task1())
    print(task2())