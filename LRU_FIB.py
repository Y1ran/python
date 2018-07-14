def fibonacci_tail(n, res, tmp):
    if n == 0:
        return res
    else:
        return fibonacci_tail(n-1,tmp, res+ tmp)
    
def fibonacci_iter(n):
    a, b = 0 ,1
    for _ in range(n):
        a , b = a + b , a
    return a
@lru_cache()
def fibonacci_cache(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cache(n - 1) + fibonacci_cache( n - 2)

@functools.lru_cache()
def fibonacci_cache(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cache(n - 1) + fibonacci_cache( n - 2)
def fibonacci_org(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cache(n - 1) + fibonacci_cache( n - 2)
def fibonacci_org(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_org(n - 1) + fibonacci_org( n - 2)
time(fibonacci_org(10))
%timeit
%%timeit
fibonacci_org(10)



num_list=[5,10,20,30,40,50]
for num in num_list:
    start_time=time.time()
    print (fibonacci_org(num))
    end_time=time.time()
    print (fibonacci_tail(num,0,1))
    end_time2=time.time()
    print( fibonacci_iter(num))
    end_time3=time.time()
    print( fibonacci_cache(num))
    end_time4=time.time()
    print ('正在求解的斐波那契数字下标为%s' % num)
    print ('直接递归耗时为 ：', end_time-start_time)
    print ('尾递归调用耗时为：', end_time2-end_time)
    print ('直接使用循环耗时为：', end_time3-end_time2)
    print ('使用CACHE缓冲耗时为：', end_time4-end_time3)