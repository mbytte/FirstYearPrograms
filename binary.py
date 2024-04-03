#program 1.3.7 p77

#imports
import sys 
import stdio

#getting the input from the terminal
n = int(sys.argv[1])

#Compute v as the largest power of 2 <= n. 
v = 1 #max binary powerw
while v <= (n // 2): #
    v *= 2
    
#Cast out powers of 2 in decreasing order. 
while v > 0: #making sure that it there is still part of the number left to convert
    if n < v: #checks if the n is smaller than the base power
       stdio.write(0) 
    else: 
      stdio.write(1) 
      n -= v 
    v //= 2 #Divide v by 2 (integer division)

#outputting a new line
stdio.writeln()