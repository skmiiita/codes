def count_setnumbits(n):
    if n < 0:
        n = ~n + 1
    count = 0
    while(n >=1):
        count = count + n % 2
        n = n>>1

    return count
BITS = 32
def getMSB(n):
    msb = 1 << (BITS - 1)

    return n & msb

print (getMSB(8))
print (count_setnumbits(-5))