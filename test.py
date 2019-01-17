def outter1(func1): #func1=wrapper2的内存地址
    print('加载了outter1')
    print(func1)
    def wrapper1(*args,**kwargs):
        print('执行了wrapper1')
        res1=func1(*args,**kwargs)
        return res1
    return wrapper1

def outter2(func2): #func2=wrapper3的内存地址
    print('加载了outter2')
    def wrapper2(*args,**kwargs):
        print('执行了wrapper2')
        res2=func2(*args,**kwargs)
        return res2
    return wrapper2

def outter3(func3): # func3=最原始的那个index的内存地址
    print('加载了outter3')
    def wrapper3(*args,**kwargs):
        print('执行了wrapper3')
        res3=func3(*args,**kwargs)
        return res3
    return wrapper3



@outter1 # outter1(wrapper2的内存地址)======>index=wrapper1的内存地址
@outter2 # outter2(wrapper3的内存地址)======>wrapper2的内存地址
@outter3 # outter3(最原始的那个index的内存地址)===>wrapper3的内存地址
def index():
    print('from index')

print('======================================================')
index()