a = int(input())

for i in range (1, a+1):
  if i % 3 == 0:
    print('X',end=' ')
  else:
    print(i, end=' ')
    
#가로 출력을 위해 end를 넣어줌
