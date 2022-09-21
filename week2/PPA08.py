'''Accept two positions as input: start and end.
Print YES if a bishop at start can move to end in exactly one move.
Print NO otherwise.
Note that a bishop can only move along diagonals.'''


start = input()
end = input()
s = 'ABCDEFGH'
a=(abs(s.index(start[0])-s.index(end[0])))
b=abs(int(start[1])- int(end[1]))
if (a==b):
 print('YES')
else:
 print('NO')