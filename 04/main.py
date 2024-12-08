num_cards = [1 for n in range(212)]

def task1():
    input_file = open("input.txt")
    total_score = 0
    for n, line in enumerate(input_file.readlines()):
        tag, numbers = line.split(':')
        wining_numbers, present_numbers = numbers.split('|')
        wining_numbers = [int(n) for n in wining_numbers.split(' ') if len(n) > 0]
        present_numbers = [int(n) for n in present_numbers.split(' ') if len(n) > 0]
        intersection = list(set(wining_numbers) & set(present_numbers))
        if len(intersection) > 0:
            total_score += 2**(len(intersection)-1)
            for i in range(n+1, n+len(intersection)+1):
                if i < len(num_cards):
                    num_cards[i] += num_cards[n]
    return total_score

def task2():
    return sum(num_cards)

if __name__ == '__main__':
    print(task1())
    print(task2())