import math
 
cur =input('int only::')
number = int(cur)
 
def trial_division(target):
    dest = int(math.sqrt(target))
 
    for i in range(2,dest):
        if target % i == 0:
            print(str(target) + 'は合成数！')
            return
    print(str(target) + 'は素数！')
 
trial_division(number)