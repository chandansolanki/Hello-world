# Determine whether a number is Prime Number or not.

a = int(input("Enter a number: "))
p=1
if abs(a) > 1:
    for i in range(2, a):
        if (a % i) == 0:
            p=0
            break  
elif frac(a) > 0 :
        print(a, "is not a integer number")  
        break
else:
     print(a, "is not a prime number") 
 
if p == 0:
     print(a, "is not a prime number")   
else:
      print(a, "is a prime number")    

      
  