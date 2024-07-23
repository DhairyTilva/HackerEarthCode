def minimum_steps(A, B):
    n = len(A)
    ans = 0
    flag = True

    while min(A) > -1:
        a = min(A)
        for i in range(n):
            if A[i] != a:
                A[i] -= B[i]
                ans += 1

        if len(set(A)) == 1:
            flag = False
            print(ans)
            break

    if flag:
        print(-1)

n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
minimum_steps(A, B)