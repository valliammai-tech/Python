# Question 4) - Using filter and lambdas. your function will take an Integer X,Y followed by an Array.
#               You must take all numbers from the Array which is either;
#                 -> (divisible by X or divisible by Y) OR (leaves remainder <= 10 when divided by X or divided by Y)


def func4(div1, div2, array):
    return list(filter(lambda x: x % div1 <= 10 or x % div2 <= 10, array))
