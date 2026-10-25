#mehmet ali aslan - 20253005005

from functools import wraps,lru_cache

def say(func):
    @wraps(func)    
    def sarmalayici(*args,**kwargs):
        sarmalayici.cagri += 1
        return func(*args,**kwargs)

    sarmalayici.cagri = 0
    return sarmalayici

@say
def fib1(a): #özyinelemeli fibonacci
    if a < 2: 
        return a
    
    return (fib1(a-1)+fib1(a-2)) 

@say
@lru_cache
def fib2(a):
    if a < 2: 
        return a
    
    return (fib2(a-1)+fib2(a-2))

@lru_cache(maxsize=None)
@say
def fib3(a):
    if a < 2:
        return a

    return (fib3(a - 1) + fib3(a - 2))

fib1(20)
print("Yalnızca @say                  :", fib1.cagri)

fib2(20)
print("@say üstte, @lru_cache altta   :", fib2.cagri)

fib3(20)
print("@lru_cache üstte, @say altta   :", fib3.__wrapped__.cagri)

