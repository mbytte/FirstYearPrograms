#exercise 1.3.11 p90
n = 123456789 
m = 0 

#infinite loop because n will never equal 0
while n != 0: 
    m = (10 * m) + (n % 10) 
    n /= 10

#not possible to know what the values of the values are because the loop will never end
print(m)
print(n)