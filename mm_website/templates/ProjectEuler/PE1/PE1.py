# Method 1 - Brute Force
sum = 0
for i in range(1,1000):
  if ((i%3==0) or (i%5==0)):
    sum += i

print(sum)

# Method 2 - Subsets
sumA = 0; sumB = 0; sumC = 0;

for i in range(1,(999 // 3)+1):
  sumA += i*3

for i in range(1,(999 // 5)+1):
  sumB += i*5

for i in range(1,(999 // 15)+1):
  sumC += i*15

print(sumA + sumB - sumC)
