def a(input):
    x = 0
    depth = 0
    for line in input:
        cmd,dist_str = line.split()
        dist = int(dist_str)
        if cmd == 'up':
            depth -= dist
        elif cmd == 'down':
            depth += dist
        else:
            x += dist

    print(x)
    print(depth)
    print(x * depth)

def b(input):
    x = 0
    depth = 0
    aim = 0
    for line in input:
        cmd,dist_str = line.split()
        dist = int(dist_str)
        if cmd == 'up':
            aim -= dist
        elif cmd == 'down':
            aim += dist
        else:
            x += dist
            depth += aim * dist

    print(x)
    print(depth)
    print(x * depth)


with open('02/input.txt', 'r') as input:
    b(input)
