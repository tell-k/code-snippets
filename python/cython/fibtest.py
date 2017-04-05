import fib
import cyfib
from benchmarker import Benchmarker

N = 30


with Benchmarker(10, cycle=1) as bench:

    @bench('normal fib')
    def _(bm):
        for _ in bm:
             fib.fib(N)

#    @bench('cython fib')
#    def _(bm):
#        for _ in bm:
#             cyfib.fib(N)
#
#    @bench('cython fib_int')
#    def _(bm):
#        for _ in bm:
#             cyfib.fib_int(N)

    @bench('cython fib_cdef')
    def _(bm):
        for _ in bm:
             cyfib.fib_cdef(N)

#    @bench('cython fib_cpdef')
#    def _(bm):
#        for _ in bm:
#             cyfib.fib_cpdef(N)

#    @bench('normal fib2')
#    def _(bm):
#        for _ in bm:
#             fib.fib2(N)
#
#    @bench('cython fib2')
#    def _(bm):
#        for _ in bm:
#             cyfib.fib2(N)
#
#    @bench('cython fib2_int')
#    def _(bm):
#        for _ in bm:
#             cyfib.fib2_int(N)
#
#    @bench('cython fib2_cdef')
#    def _(bm):
#        for _ in bm:
#             cyfib.fib2_cdef(N)
#
#    @bench('cython fib2_cpdef')
#    def _(bm):
#        for _ in bm:
#             cyfib.fib2_cpdef(N)
