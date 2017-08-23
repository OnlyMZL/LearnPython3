
#生成数列前num项
def fib(num):
    a, b = 0, 1
    while num>0:
        print(b, end = ', ')
        a, b = b, a+b
        num = num - 1
    print()

if __name__=='__main__':
    flagPlay = ''
    while True:
        print('是否继续生成数列？ y/n')
        flagPlay = input()
        if flagPlay == 'y':
            num = int(input('请指定要输出数列前多少项：'))
            try:
                fib(int(num))
            except :
                print("请输入一个正整数！！！")
        elif flagPlay == 'n':
            print('退出成功！')
            break
        else:
            print('请输入 y 或 n')