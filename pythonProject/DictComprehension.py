def func3(div, **arrays):
    nos = 0
    for arr in arrays.values():
        iterr = 0
        for i in arr:
            if i % div == 0:
                iterr = iterr + 1
        print({nos: iterr})
        nos = nos + 1
