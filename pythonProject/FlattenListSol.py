def func2(lsta, lstb):
    flattenList = [j for i in lstb for j in lsta if j % i == 0]
    return list(set(filter(lambda x: flattenList.count(x) > 2, flattenList)))
