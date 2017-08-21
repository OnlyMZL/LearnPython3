

#Python通常一行写完一条语句，但如果语句很长，可以用反斜线（\）来实现多行语句

item_one=1
item_two=2
item_three=3
total=item_one+\
    item_two+\
    item_three
print(total)


# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：

total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total)

#同一行显示多条语句
#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys;  x='runoob';  print(sys.version)