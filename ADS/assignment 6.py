#create a list, store values from 1..10 in it and print values
i =[1,2,3,4,5,6,7,8,9,10]
print(i)

#find sum of all numbers in a list
arr = [1,2,3,4,5,6,7,8,10]
s = 0
for i in arr:
  s += i
print(s)

#sum of even numbers in a list
arr = [1,2,3,4,5,6,7,8,10]
s = 0
for i in arr:
  if i%2==0:
   s += i
print(s)

#sum of odd numbers in a list
arr = [1,2,3,4,5,6,7,8,9,10]
s=0
for i in arr:
  if(i%2!= 0):
   s += i
print(s)

#add all prime number in a list
arr = [1,2,3,4,5,6,7,8,9,10]
s = 0
for i in arr:
  
  #this checks prime 
  count = 0 #if count is 0 then  i is prime, otherwise it is not prime
  for j in range(2,i):
    if i%j == 0:
      #if a number is not prime count will be 1
      count = 1
      break
    #add the number to s only if count is 0
  if count == 0 and i != 1:
    s+=i
  print (s)
