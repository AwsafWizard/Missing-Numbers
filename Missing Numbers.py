
k = int(input())
l1 = [int(i) for i in input().split()]

m = int(input())
l2 = [int(i) for i in input().split()]

done = []
ans = []

for x in l2:

    if x not in done:

        if l1.count(x) != l2.count(x):
            ans.append(x)

        done.append(x)

ans = sorted(ans)
ans = [str(i) for i in ans]

print(" ".join(ans))
