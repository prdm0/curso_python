import time
import math
import functools

def tempo(nano):
    def _tempo(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if nano:
                t0 = time.perf_counter_ns()
            else:
                t0 = time.time()
            func(*args, **kwargs)
            if nano:
                return time.perf_counter_ns() - t0
            else:
                return time.time() - t0
        return wrapper
    return _tempo
         
@tempo(nano=False)
def teste():
    """Aqui é uma docstring
    qualquer... bla bla bla
    """
    for i in range(int(5e7)):
        math.asinh(float(i))

# Note que se não houvesse @functools.wraps(func), então
# teste.__doc__ não iria retorna a sua docstring.
teste()