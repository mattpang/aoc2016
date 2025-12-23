from collections import deque

def run(n, part2=False):
    q = deque()

    for i in range(1, n + 1):
        q.append([i, 1])

    while len(q) > 0:
        try:
            if part2:
                next = int(len(q) // 2)
                n_elf, n_gifts = q[next]
                del q[next]

            elf, gifts = q.popleft()
            if not part2:
                n_elf, n_gifts = q.popleft()

            q.append([elf, gifts + n_gifts])
        except IndexError:
            break

    print(elf)


def pt2(n=30000):
    top = deque()
    bottom = deque()

    for i in range(1, n + 1):
        if i < (n // 2) + 1:
            top.append(i)
        else:
            bottom.append(i)

    while top and bottom:
        if len(top) > len(bottom):
            top.pop()
        else:
            bottom.pop()

        bottom.appendleft(top.popleft())
        top.append(bottom.pop())

    print(top[0] or bottom[0])


run(n=3001330)

#  this is very slow. try and do some speed ups first.
# run(n=3001330, part2=True)
pt2(n=3001330)
