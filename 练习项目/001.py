def Calc(number):
    if number%2 == 0:  
            print('number / 2')
            return number / 2
    elif number%2 == 1:  
        print('3 * ' + str(number) + ' + 1')
        return 3*number+1

print('this is a Collatz array program. Type exit to exit.')
quitFlag = ''  #用户是否要继续计算的标记
conExit = ''   #退出程序的标记

while conExit!='exit':
    print("Do you want to Continue? yes or no")
    quitFlag = input()
    if quitFlag == 'yes':
        try:
            print('Input an INT number!')
            Num = int(input())
            while True:
                Num = Calc(Num)
                if Num == 1:
                    print(Num)
                    break
        except ValueError:
            print('Please input INT number')
    elif quitFlag == 'no':
        print('Program Exited.')
        conExit = 'exit'