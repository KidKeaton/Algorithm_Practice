a = int(input())

def primeNumber(a):                 
  for i in range (2, a):          #1과 자기자신을 제외한 range 
    if a % i ==0:
      return False 
  return True
  
print (primeNumber(a))

