import os

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    N  = len(arr)
    arr_s = sorted(arr)
    abs_diff = 10**9
    for i in range(N-1):
        abs_diff = min(abs(arr_s[i]-arr_s[i+1]), abs_diff)

    return abs_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()