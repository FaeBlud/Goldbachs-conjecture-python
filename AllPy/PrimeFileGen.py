upper = 999999999999

f = open("primenumbers.txt", "w")


for num in range(0, upper):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           numfin = str(num)
           f.write(numfin + "\n")

f.close()
