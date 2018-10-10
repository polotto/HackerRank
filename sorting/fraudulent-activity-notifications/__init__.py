import os
import math

def median(arr):
    aux = sorted(arr)
    n = len(aux)
    half = math.floor(n/2)
    # print(aux,n,half)
    if n % 2 == 0:
        return (aux[half] + aux[half + 1]) / 2
    else:
        return aux[half]

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notifications = 0
    initial_day = 0
    last_day = d
    while last_day < len(expenditure): 
        med = median(expenditure[initial_day:last_day])
        # print(expenditure[last_day], med, 2 * med)
        if expenditure[last_day] >= 2 * med:
            notifications += 1
        initial_day += 1
        last_day += 1
    
    return notifications

if __name__ == '__main__':
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input/input01.txt'), 'r')
    
    nd = fptr_input.readline().split()
    n = int(nd[0])
    d = int(nd[1])

    expenditure = list(map(int, fptr_input.readline().rstrip().split()))
    result = activityNotifications(expenditure, d)
    print(result)
    fptr.write(str(result) + '\n')
    fptr.close()