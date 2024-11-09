
# ВАШ КОД ТУТ

def rrange(begin= 0, end= 0, step= 1):
    if step > 0:
        if end <= begin:
            return []
        if begin < end:
            res = [begin] + rrange(begin + step, end, step)
            return res
    if step < 0:
        if end >= begin:
            return []
        if end < begin:
            res = [begin] + rrange(begin + step, end, step)
            return res


# ПЕРЕВІРКА

x = rrange(1, 10)
z = rrange(10, 1, 1)
y = rrange(10, 1, -1)
#print(x, y, z)

assert x == list(range(1, 10)), 'Failed test for simple range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
print('All tests good!')
