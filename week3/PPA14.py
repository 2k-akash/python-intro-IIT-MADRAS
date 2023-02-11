#coprime or not

import math
n = int(input())
m = int(input())
if math.gcd(m,n) == 1:
    print("Coprime")
else:
    print('Not Coprime')