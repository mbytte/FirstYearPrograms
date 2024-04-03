#program 1.2.5 p35

#imports
import sys 
import stdio

#getting the input from the terminal
year = int(sys.argv[1])
isLeapYear = (year % 4 == 0) #will output a boolean

#checking if it is a leap year or not --> the value of isLeap year will change beforehand which is whhy you need another check after thaat
isLeapYear = isLeapYear and ((year % 100) != 0) #if it is a leap year, it is not a leap year if it is divisible by 100
isLeapYear = isLeapYear or ((year % 400) == 0) #if it is a leap year, it is a leap year if it is divisible by 400

#output
stdio.writeln(isLeapYear)