# Enter your code here. Read input from STDIN. Print output to STDOUT
d = divmod(int(input()), int(input()))
print(*d, d, sep='\n')