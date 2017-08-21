#保留字即关键字，我们不能把它们用作任何标识符名称。
#Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字

import keyword

keyWords=keyword.kwlist
for kw in keyWords:
    print(kw)
    

# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
# 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
# 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']