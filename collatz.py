# Richella O'Driscoll 12.02.2018
#Collatz Conjuncture Exercise

n = int(input("Enter integer:"))

while n!=1:

    if n % 2 ==0: #this is an even number
        n = n/2

        print (n) #this is an odd number

    else:

        n = (n * 3) + 1

        print (n) 
        
        PS C:\Users\riche\Desktop\Collatz> python collatz.py
Enter integer:14
7.0
22.0
11.0
34.0
17.0
52.0
26.0
13.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
1.0
