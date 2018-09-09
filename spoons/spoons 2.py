'''
Problem 2
Solution algorithm in Python:
'''
# retrieve the inputs in decimal values
a = int(input('a: '))
b = int(input('b: '))

# print in binary the inputs to see with more detail the inputs
print("a binary: {0:b}".format(a))
print("b binary: {0:b}".format(b))

# check if a < b
if a > b:
    print('a isn\'t < b')
    exit()

# Calculation start here
i = a + 1 # create aux var i to receive the a + 1
result = a # result var receive the a number

# while loop calculate until i is igual b (Loop = O(n))
# iterate thru i + 1 until b
while i <= b:
    result = result & i # calculate bitwise & for result and i
    i = i + 1 # incremnt i to the next calculation

# return the response
print("result: %d" % result) # response in decimal
print("result binary: {0:b}".format(result)) # response in binary to see more details


'''
solution notes:

Example 1:
a 5 = 101
b 7 = 111
b > a
c(a, b) = 101 & 110 & 111 = 100 (4)
                 5        6       7
c(a, b) = 111 & 110 & 101 = 100 (4)
                 7       6        5
c(a, b) = 101 ^ 111 = 010 (5)
                5         7

111 & 010 = 010

Example 2:
a 5 = 101
b 6 = 110
b > a
c(a, b) = 101 & 110 = 100 (4)
                 5        6

Example 3:
a 4 = 100
b 6 = 110
b > a
c(a, b) = 100 & 101 & 110 = 100 (4)
                 4        5        6
c(a, b) = 100 & 110 = 100 (4)
                 4        6

Example 4:
a 7 = 0111
b 9 = 1001
b > a
c(a, b) = 0111 & 1000 & 1001 = 0000 (0)
                 7          8          9
'''
