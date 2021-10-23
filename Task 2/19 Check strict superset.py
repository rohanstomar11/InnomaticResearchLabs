# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
n = int(input())
check = True
for i in range(n):
    s = set(input().split())
    if (s&A != s) or (s==A):
        check = False
        break
print(check)
