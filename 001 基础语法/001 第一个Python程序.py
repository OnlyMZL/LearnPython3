#-*- coding:UTF-8 -*-

print("hello world")

if True:
    print("True!")

if False:
    print("False!")

if True:
    print("true")
else:
    print("false")

#Python通常一行写完一条语句，但如果语句很长，可以用反斜线（\）来实现多行语句

item_one=1
item_two=2
item_three=3
total=item_one+\
    item_two+\
    item_three
print(total)