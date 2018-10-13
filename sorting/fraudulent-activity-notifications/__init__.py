import os
import math
from timeit import default_timer as timer
import bisect

def median(aux, half, even):
    if  even: # made a median of 2 central elements
        return (aux[half] + aux[half + 1]) / 2
    else: # return central element
        return aux[half]

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notifications = 0 # number of notificatons
    initial_day = 0 # initial counting day index
    last_day = d # last day index, the day that will check if we will have some notification

    median_arr = sorted(expenditure[initial_day:last_day]) # initial median array for bisect
    # the following vars don't change in the future, so they need be computaded one time
    n_median = len(median_arr) # len of median array will be fixed
    half = math.ceil(n_median/2) - 1 # half element postion in the median array, the ceil round up the element
    even = True if n_median % 2 == 0 else False # check with the median array have a num of elem even or odd
    
    n = len(expenditure) # the length of the exp array
    while last_day < n:
        med = median(median_arr, half, even) # calculate the median
        last_day_exp = expenditure[last_day] # get the last day expenditure
        if last_day_exp >= 2 * med: # check if have some notification
            notifications += 1
        j = bisect.bisect_left(median_arr, expenditure[initial_day]) # get the postition of the exp. of the initial day
        del median_arr[j] # remove the element to keep the median_arr with the same length
        bisect.insort(median_arr, last_day_exp) # insert the actual last day exp. that will be part of the median in the next loop
        # increment the days
        initial_day += 1
        last_day += 1
    
    return notifications # return the num of notifications

if __name__ == '__main__':
    start = timer()

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
    print(timer() - start)