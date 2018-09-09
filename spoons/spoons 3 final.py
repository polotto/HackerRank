# receive N space separed values, X[N] array
# x_i = input('Enter X:\n').split()
x_i = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split()
# convert x_i to a list of integers
x = list(map(int, x_i))

# ans receive the first value of X,
# so, the loop will start in position 1
ans = x[0]
# Loop throught the X array until the N-1,
# this will avoid index out of range.
# To achieve the complexity O(N) (worst case),
# we need solve using only one loop.
for n in range(1, len(x) - 1):
    # Calculate the XOR of the sub set.
    # XOR is calculated between previous result,
    # actual X and the next X (X[n+1]).
    # this cam be done because:
    # (X[0] XOR X[1]) ... (X[n-1] XOR X[n]) = f(X)
    ans = x[n] ^ x[n+1] ^ ans

# print the answer
print(ans)
