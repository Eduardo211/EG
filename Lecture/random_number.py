import random

for i in range(1000):
    myNumber = random.randint(0, 100)
    print(myNumber)

i=0
while True:
    myNumber = random.randint(0,100)
    i+=1
    if (i==1000):
        break