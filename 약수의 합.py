def sumDiv(a):
  return sum([i for i in range(1, a) if a % i == 0])
          
a = int(input())
print (sumDiv(a))
          
#or 

def sumDiv(a):
  return (a + sum([i for i in range(1,(a//2)+1) if a % i == 0]))

a = int(input())
print (sumDiv(a))

# range를 a/2로 줄이고 a를 sum에 따로 더해줌
