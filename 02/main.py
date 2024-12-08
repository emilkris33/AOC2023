
def task1():
    input_file = open("input.txt")
    possible_sum = 0
    for line in input_file.readlines():
        tag, rounds = line.split(':')
        game_id = int(tag[5:])
        rounds = rounds.split(';')
        for round in rounds:
            pulls = round.split(',')
            for pull in pulls:
                pull = pull.strip()
                space_pos = pull.find(' ')
                number = int(pull[:space_pos])
                color = pull[space_pos+1:]
                if color == "red" and number > 12:
                    break
                if color == "green" and number > 13:
                    break
                if color == "blue" and number > 14:
                    break
            else:
                continue
            break
        else:
            possible_sum += game_id
    return possible_sum


def task2():
    input_file = open("input.txt")
    power = 0
    for line in input_file.readlines():
        tag, rounds = line.split(':')
        rounds = rounds.split(';')
        min_red = 0
        min_green = 0
        min_blue = 0
        for round in rounds:
            pulls = round.split(',')
            for pull in pulls:
                pull = pull.strip()
                space_pos = pull.find(' ')
                number = int(pull[:space_pos])
                color = pull[space_pos + 1:]
                if color == "red" and number > min_red:
                    min_red = number
                if color == "green" and number > min_green:
                    min_green = number
                if color == "blue" and number > min_blue:
                    min_blue = number
        power += min_red * min_green * min_blue
    return power

if __name__ == '__main__':
    print(task1())
    print(task2())