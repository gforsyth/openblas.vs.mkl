import numpy
import pickle
import sys
import timeit
import os

def matmatmult(A,B):
    A.dot(B)

def saveresult(runtime):
    try:
        pkl = open('results_'+sys.argv[1]+'.pkl','rb')
        results = pickle.load(pkl)
        pkl.close()
    except:
        results = {}

    pkl = open('results_'+sys.argv[1]+'.pkl','wb')
    reskey = sys.argv[1]+'_threads_' + os.environ[sys.argv[2]]
    try:
        results[reskey] += [runtime]
    except:
        results[reskey] = [runtime]

    print(results)
    pickle.dump(results,pkl)
    pkl.close()

def runtimeit(t):
    for i in range(1, 10):
        number = 10**i
        try:
            x = t.timeit(number)
        except:
            t.print_exc()
            return 1

        if verbose:
            print("%d loops -> %.*g secs" % (number, precision, x))
        if x >= 0.2:
            break

    repeat = 3
    try:
        r = t.repeat(repeat, number)
    except:
        t.print_exc()
        return 1

    best = min(r)
    if verbose:
        print("raw times:", " ".join(["%.*g" % (precision, x) for x in r]))
    print("%d loops," % number, end=' ')
    usec = best * 1e6 / number
    if usec < 1000:
        print("best of %d: %.*g usec per loop" % (repeat, precision, usec))
    else:
        msec = usec / 1000
        if msec < 1000:
            print("best of %d: %.*g msec per loop" % (repeat, precision, msec))
        else:
            sec = msec / 1000
            print("best of %d: %.*g sec per loop" % (repeat, precision, sec))

    saveresult(usec)

if __name__ == '__main__':
    print(os.environ[sys.argv[2]])
    for dim in [500, 1000, 2000]:
        A = numpy.random.random((dim,dim))
        B = numpy.random.random((dim,dim))
        
        precision = 3
        verbose = False
        t = timeit.Timer("matmatmult(A,B)", setup="from __main__ import matmatmult;import numpy;A = numpy.random.random(({},{}));B = numpy.random.random(({},{}))".format(dim,dim,dim,dim))
        
        print("Running matmatmult for {}x{}".format(dim,dim))
        runtimeit(t)
