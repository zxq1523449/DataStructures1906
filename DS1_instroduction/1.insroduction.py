'''
    如果 a+b+c=1000,且 a^2+b^2=c^2（a，b，c 为自然数），如何求出所有a、b、c可能的组合？
    a b c 取值氛围0-1000
'''
import time
start_time = time.time()
for a in range(0,1001):
    for b in range(0,1001):
        for c in range(0,1001):
            if a+b+c == 1000 and a**2+b**2 == c**2:
                print("a=%d,b=%d,c=%d"%(a,b,c))
            
end_time = time.time()
print("耗时%s"%(end_time-start_time))

# 减少循环
import time
start_time = time.time()

for a in range(0,1001):
    for b in range(0,1001):
        c=1000-a-b
        if a**2+b**2==c**2:
            print("a=%d,b=%d,c=%d"%(a,b,c))

end_time = time.time()
print("耗时%s"%(end_time-start_time))











'''
    计算1-5000的和
    高斯算法
    普通算法
'''
'''
    练习：编写函数求出列表中的最小值。
    要求：函数1:O（n^2） 两两比较
         函数2：O（n）  

'''