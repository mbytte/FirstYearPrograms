#program 1.3.9 p81

#imports
import sys 
import stdio

#Getting the input from the terminal
n = int(sys.argv[1])

#smallest prime factor
factor = 2 

#
while factor*factor <= n: 
    while (n % factor) == 0: 
        #Cast out and write factor. 
        n //= factor 
        stdio.write(str(factor) + ' ') 
    factor += 1 
    #Any factors of n are greater than or equal to factor.

#gets the last number that was used as a factor
if n > 1: 
    stdio.write(n) 
stdio.writeln()