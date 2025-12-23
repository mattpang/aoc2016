  
for i in range(2**13):
    if '101010101010' in str(bin(i)):
        print(i)
        break


a = i - 2572

# the asm code simplifies down to: 
d = a + 2572 
# while True: but don't care about this loop. 
# Just need to make d+a a 101010101010 in binary that is the smallest
a = d
while a != 0:
    b = a % 2
    a //= 2
    print(b,end='')
print()
print(i-2572)