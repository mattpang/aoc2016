import heapq

grid = dict()
num = 10

start = (1, 1)
dest = (7, 4)

num = 1358
dest = (31, 39)

for x in range(max(dest) + 10):
    for y in range(max(dest) + 10):
        tmp = (x * x + 3 * x + 2 * x * y + y + y * y) + num
        isspace = sum([1 for x in str(bin(tmp)) if x == "1"]) % 2 == 0
        if isspace:
            grid[(x, y)] = 0
        else:
            grid[(x, y)] = 1


def main(part2=False):
    # then do standard A* maze solver or brute force it

    stack = []

    heapq.heappush(stack, [0, [start]])

    been = set()
    been.add(start)

    while True:
        dist, route = heapq.heappop(stack)
        if part2:
            if dist == 50:
                return been
        current_pos = route[-1]

        if not part2:
            if tuple(current_pos) == dest:
                print(len(route) - 1)
                break

        # udlf only
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            next_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if grid.get(next_pos) == 0 and next_pos not in route:
                new_route = [dist + 1, route + [next_pos]]
                if dist <= 50:
                    been.add(next_pos)

                heapq.heappush(stack, new_route)


main()
been = main(part2=True)
print(len(been))
