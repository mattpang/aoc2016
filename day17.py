import heapq
import hashlib

grid_size = 4
start = (0, 0)
target = (3, 3)
# can only go UDLR

directions = {"D": (0, 1), "L": (-1, 0), "R": (1, 0), "U": (0, -1)}


def solve(code, part2=False):
    # doors can open up again if you visited them before.
    # code = 'qzthpkfp'
    stack = [[0, code, start]]

    if part2:
        heapq.heapify(stack)
        # stack is going to be: steps, seq , pos
        heapq._heapify_max(stack)

    biggest = 0

    while len(stack) > 0:
        if part2:
            steps, seq, pos = heapq._heappop_max(stack)
        else:
            steps, seq, pos = heapq.heappop(stack)

        if pos == target:
            if part2:
                if steps > biggest:
                    biggest = steps
                continue
            else:
                print(seq.replace(code, ""))
                break

        up, down, left, right = hashlib.md5(seq.encode()).hexdigest()[:4]
        # door is only open for these chars
        allowed = "bcdef"
        if up in allowed and (pos[1] - 1) >= 0:
            heapq.heappush(stack, [steps + 1, seq + "U", (pos[0], pos[1] - 1)])
        if down in allowed and (pos[1] + 1) <= 3:
            heapq.heappush(stack, [steps + 1, seq + "D", (pos[0], pos[1] + 1)])
        if left in allowed and (pos[0] - 1) >= 0:
            heapq.heappush(stack, [steps + 1, seq + "L", (pos[0] - 1, pos[1])])
        if right in allowed and (pos[0] + 1) <= 3:
            heapq.heappush(stack, [steps + 1, seq + "R", (pos[0] + 1, pos[1])])

    if part2:
        print(biggest)


solve(code="qzthpkfp")
solve(code="qzthpkfp", part2=True)
