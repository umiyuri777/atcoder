import sys

def main(lines):
    n, m = map(int, lines[0].split())
    reserved = set(map(int, lines[1].split()))
    q = int(lines[2])
    query = [list(map(int, lines[i + 3].split())) for i in range(q)]

    not_reserved = [num for num in range(1, n + 1) if num not in reserved]

    near = []

    for nr in not_reserved:
        while len(near) < nr:
            near.append(nr)

    for l, r in query:
        if near[l - 1] <= r:
            print(near[l - 1])
        else:
            print(-1)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)