import sys
import time

def fib(nn):
    def fib_inner(nn, old_1, old_2):
        if nn == 0:
            return old_2
        if nn == 1:
            return old_1
        return fib_inner(nn-1, old_1+old_2, old_1)

    return fib_inner(nn, 1, 0)


if __name__ == '__main__':
    lo_nn = int(sys.argv[1])
    hi_nn = int(sys.argv[2])

    start = time.time()

    for nn in range(lo_nn,hi_nn+1):
        print('{:>3d}: {}'.format(nn,fib(nn)))

    elapsed = time.time() - start
    print('elapsed = {:1.3e}'.format(elapsed))
