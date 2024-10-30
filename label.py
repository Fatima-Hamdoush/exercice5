n = int(input("Please enter a number to display the first n Fibonacci numbers:"))
sum =1
sum_1 =0
#lzm hon sum_1 take the  old value of  sum 
print(sum_1,sum,end=" ")
for (i) in range (n):
    
    sum = sum+sum_1
    sum_1 =sum - sum_1
    print(sum ,end=" ")
