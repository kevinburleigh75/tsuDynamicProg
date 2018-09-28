import sys
import time

def fib(nn):
    def fib_inner(nn, memo):
        if memo[nn] is None:
            if nn == 0:
                result = 0
            elif nn == 1:
                result = 1
            else:
                result = fib_inner(nn-1,memo) + fib_inner(nn-2,memo)
            memo[nn] = result
        return memo[nn]

    memo = [None]*(nn+1)
    return fib_inner(nn, memo)

if __name__ == '__main__':
    lo_nn = int(sys.argv[1])
    hi_nn = int(sys.argv[2])

    start = time.time()

    for nn in range(lo_nn,hi_nn+1):
        print('{:>3d}: {}'.format(nn,fib(nn)))

    elapsed = time.time() - start
    print('elapsed = {:1.3e}'.format(elapsed))
