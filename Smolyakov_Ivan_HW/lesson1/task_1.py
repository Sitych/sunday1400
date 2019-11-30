A = int(input())
for i in range(A):
    print('%s%s' % (' ' * (A-i-1), '*' * (i*2+1)))
