# Enter your code here. Read input from STDIN. Print output to STDOUT

import math 
ab = float(input())
bc = float(input())
ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac/2.0
mc = bm

b = mc
c = bm
a = bc

angel_b_radian = math.acos(a / (2*b))
angel_b_degree = int(round((180*angel_b_radian)/math.pi))
degree=chr(176) 
output_str = str(angel_b_degree)+str(degree)
print(output_str)