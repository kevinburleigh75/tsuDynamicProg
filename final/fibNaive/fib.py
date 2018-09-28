import sys
import time

def fib(nn):
    if nn == 0:
        return 0
    if nn == 1:
        return 1
    return fib(nn-1) + fib(nn-2)

if __name__ == '__main__':
    lo_nn = int(sys.argv[1])
    hi_nn = int(sys.argv[2])

    start = time.time()

    for nn in range(lo_nn,hi_nn+1):
        print('{:>3d}: {}'.format(nn,fib(nn)))

    elapsed = time.time() - start
    print('elapsed = {:1.3e}'.format(elapsed))
