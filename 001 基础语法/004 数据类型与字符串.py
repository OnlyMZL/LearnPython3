
# -1-python中数有四种类型：整数、长整数、浮点数和复数。
#       整数    如 1
i=1
print(i)
#       长整数  是比较大的整数
i=35894657863475
print(i)
#       浮点数  如 1.23、3E-2
#       复数    如 1 + 2j、 1.1 + 2.2j


#-2-字符串
#   python中单引号和双引号使用完全相同。
str1='单引号'
str2="双引号"
print(str1,str2)
#   使用三引号('''或""")可以指定一个多行字符串。
str3='''多行
字符串'''
print(str3)
#   转义符 '\'
str4="123\n456"
print(str4)
#   自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
str5=r"这个\n不会换行"
print(str5)

#   python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
#   字符串是不可变的。
#   按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
str6="this " "is " "string"
print(str6)