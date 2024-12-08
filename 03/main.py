grid = []
gears = {}

def task1():
    input_file = open("input.txt")
    output = 0
    for line in input_file.readlines():
        grid.append(list(line.strip()))
    for i in range(len(grid)):
        j = 0
        while j < len(grid[0]):
            if grid[i][j] not in "0123456789":
                j += 1
                continue
            j2 = j
            while j2 < len(grid[0]):
                if grid[i][j2] in "0123456789":
                    j2 += 1
                else:
                    break
            number = int(''.join(grid[i][j:j2]))
            for i_s in range(i-1,i+2):
                if not 0 <= i_s < 140:
                    continue
                for j_s in range(j-1,j2+1):
                    if not 0 <= j_s < 140:
                        continue
                    if grid[i_s][j_s] not in "0123456789.":
                        if grid[i_s][j_s] == '*':
                            gear_pos = str(i_s)+","+str(j_s)
                            if gear_pos not in gears:
                                gears[gear_pos] = []
                            gears[gear_pos].append(number)
                        break
                else:
                    continue
                output += number
                break
            j = j2+1
    return output

def task2():
    output = 0
    for gear in gears.values():
        if len(gear) == 2:
            output += gear[0] * gear[1]
    return output

if __name__ == '__main__':
    print(task1())
    print(task2())