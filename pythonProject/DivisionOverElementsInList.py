def func4(div1, div2, array):
    return list(filter(lambda x: x % div1 <= 10 or x % div2 <= 10, array))
