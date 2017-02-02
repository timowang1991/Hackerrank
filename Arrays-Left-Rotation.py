def array_left_rotation(a, n, k):
    i = len(a) - 1
    leftRot = k % len(a)

    tmp = a[i]
    trueOnce = True
    while i != len(a) - 1 or trueOnce:
        trueOnce = False
        while i - leftRot >= 0:
            a[i - leftRot], tmp = tmp, a[i - leftRot]
            i -= leftRot
        a[i - leftRot + len(a)], tmp = tmp, a[i - leftRot + len(a)]
        i = i - leftRot + len(a)
        if len(a) % k == 0:
            i -= 1
            tmp = a[i]
            if i <= len(a) - leftRot - 1:
                break

    return a

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))

print array_left_rotation([1,2,3,4,5,6,7,8], 8, 2)
