
def a(input):
    count = 0
    prev = 0
    for line in input:
        if prev and line > prev:
            count += 1
        prev = line
    return count

def compare(a, b, c, d):
    print('a:{a} b:{b} c:{c} d:{d}')

def b(input):
    count = 0
    for index, number in enumerate(input):
        if index >= 3 and number > input[index-3]:
            count += 1
    return count

with open('input.txt', 'r') as input:
    numbers = list(map(int, input))
    result = a(numbers)
    print('result of a:')
    print(result)
    result = b(numbers)
    print('result of b:')
    print(result)
