a = int(input())
for i in range(a):
    fff = list(map(int, input().split()))
    print("Неделя", i+1, "-", sum(fff), "км")