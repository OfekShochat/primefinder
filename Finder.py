import math
from tqdm import tqdm
import time

pd = 4809328409238549024859084509348
p = 0
bar = ">"
"""for r in range(1, 20):
  if r > 20 / 10 * p:
    bar = "=" + bar
    print(bar + str(r) + "  " + str(len(bar) - 1) + "                                ",end="\r" )
    p += 1
  time.sleep(0.5)"""
primes = []
def find(startpower):
    for n in range(startpower, startpower + 100):
        number = (2 ** n)
        print("number: ", (2**n - 1))
        numbefore = int(number - 1)
        #with tqdm(total=int(2**n - 1)) as pbar:
        st = time.time()
        precentagecheck = 1
        bar = "+"
        times = 100
        for num in range(2,int(number - 1)):
          if ((2**n - 1) % (num)) == 0:
            print(str(number - 1) + " is not a prime number... " + str(num) + " times " + str((number - 1) // num) + " is " + str(number - 1))
            break
            if num == int(number - 2):
              print("prime number found!!! " + str(2**n - 1))
              primes.append(2**n - 1)
              print(primes)
            #pbar.update(1)
        
          if time.time() - st > 1:
            est = ((number - 1) / (num - numbefore)) / (86400)
            print(str(num - numbefore) + " nums/s   " + str(num / ((number - 1) / 100)) + " " + f'{est:.3f}' + " days left                   ", end="\r")
            st = time.time()
            numbefore = num
          if num > int((number -1) / 1000 * precentagecheck):
            bar = "=" + bar
            precentagecheck += 1
            times -= 1
find(10)
print(primes)
for prime in primes:
    open("./primes.txt", "a").write(str(int(prime)) + "\n")
