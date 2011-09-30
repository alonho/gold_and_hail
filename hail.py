def cached(func):
    func.cache = {} # make it reachable from outside if needed
    def decorated(arg):
        try:
            return func.cache[arg]
        except KeyError:
            func.cache[arg] = func(arg)
        return func.cache[arg]
    return decorated

@cached
def hail(n):
    if n == 1:
        return [1]
    return [n] + hail(3 * n + 1 if n & 1 else n // 2)

RANGE = 2**20

def main_iter():
    for i in xrange(2, RANGE, 2):
        yield i, hail(i)

def main_verbose():
    for n, h in main_iter():
        print n, h

def main_silent():
    for _ in main_iter(): pass

if __name__ == '__main__':
    main_silent()
