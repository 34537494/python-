global answer
def devide(num1,num2):
    global answer
    if num1 == 0 or num2 == 0:
        answer = 0
        #排除某个数就是0
    elif num1>num2:
        #先比较大小，大除以小
        num3 = num1%num2
        if num3 == 0:
            #余数为0则输出小的那个数为最大公约数
            answer = min(num1,num2)
        else:
            #否则继续进行循环
            devide(num3,num2)
    else:
        #比较大小的另一种情况
        num3 = num2%num1
        if num3 == 0:
            answer = min(num1,num2)
        else:
            devide(num3,num2)

def getnumber():
    global answer
    userdata = input('''请输入需要求最大公约数的数字:
    格式如（num1,num2,……,numn）''')
    #获取用户原始数据
    number = userdata[1:(len(userdata)-1)].split(',')
    #从第二个到倒数第二个（除去括号）以逗号切片
    number = list(map(int, number))
    #string转换为int
    devide(number[0],number[1])
    for i in range(1,len(number)-1):
        if answer != 1 or 0:
            devide(answer,number[i])
        #将上一次得到的最大公约数与下一个数进行计算
        else:
            break
        #若最大公约数为0或者1，直接结束，不用进行后续计算
    print(answer)
        
def main():
    getnumber()
    #主函数，调用方法

main()


'''
程序功能要求：
"""
辗转相除法：辗转相除法是求两个自然数的最大公约数的一种方法，也叫欧几里德算法。
例如，求（319，377）：
∵ 319÷377=0（余319）
∴（319，377）=（377，319）；
∵ 377÷319=1（余58）
∴（377，319）=（319，58）；
∵ 319÷58=5（余29）
∴ （319，58）=（58，29）；
∵ 58÷29=2（余0）
∴ （58，29）= 29；
∴ （319，377）=29。
可以写成右边的格式。
用辗转相除法求几个数的最大公约数，可以先求出其中任意两个数的最大公约数，
再求这个最大公约数与第三个数的最大公约数，依次求下去，直到最后一个数为止。最后所得的那个最大公约数，就是所有这些数的最大公约数。
"""
用辗转相除法求多个整数的最小公倍数
提示：要求用户输入用逗号分开的多个整数
可以预习后面内容，使用函数来实现
'''