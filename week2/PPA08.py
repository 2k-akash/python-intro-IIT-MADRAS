'''Accept two positions as input: start and end.
Print YES if a bishop at start can move to end in exactly one move.
Print NO otherwise.
Note that a bishop can only move along diagonals.


start = input()
end = input()
s = 'ABCDEFGH'
a=(abs(s.index(start[0])-s.index(end[0])))
b=abs(int(start[1])- int(end[1]))
if (a==b):
 print('YES')
else:
 print('NO')'''

start, end = input(),input()
pos = 'ABCDEFGH'
start_horiz,start_vert = pos.index(start[0]),int(start[1])
end_horiz , end_vert = pos.index(end[0]), int(end[1])
if abs(start_horiz - end_horiz) == abs(start_vert - end_vert):
 print("YES")
else:
 print("NO")