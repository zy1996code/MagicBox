基于 Python 语言的常见字符串操作实例

**len 函数：获取字符串长度**

\>\>\> a = ‘01234’ \#从 0 计数位开始

\>\>\> len(a)

5

\>\>\> a = ‘01234,6789' \#标点符号也占位

\>\>\> len(a)

10

\>\>\> len(['zy1996','zy2020’])\#判断列表中有多少元素

2

**切片操作（slice)操作**

a[start: end: step)

\>\>\> a = ‘01234,6789'

\>\>\> a[2:6:1] \#取[2,6)，步长为 1

'234,'

\>\>\> a[2:6:2]\#取[2,6)，步长为 2

'24'

\>\>\>

**加乘等法**

加法：字符串拼接

\>\>\> a = 'Hello'

\>\>\> b = ' World!’\#注意这里有空格

\>\>\> a+b

'Hello World!'

\>\>\>

乘法：字符串重复

\>\>\> c = a+b

\>\>\> c

'Hello World!'

\>\>\> c \*3

'Hello World!Hello World!Hello World!'

\>\>\>

判断字符串内容是否相等

\>\>\> a = 'Hello'

\>\>\> d = "hello"

\>\>\> a == d

False

\>\>\> d = "Hello"

\>\>\> a == d

True \#说明单等号和双等号一样

**判断字符串中是否包含某个子字符串(in)**

\>\>\> 'h' in a

False

\>\>\> 'H' in a

True

\#对大小写的区分

**strip 函数去掉首尾的字符**

\>\>\> e = '01234543210'

\>\>\> e.strip('012’)\#去掉 0，1，2 这三个字符

'34543'

\>\>\> e = '012345012210543210'

\>\>\> e.strip('012')

‘345012210543'\#只去掉首尾的 0，1，2

\>\>\> e = ' 012345012210543210 ‘\#带空格

\>\>\> e.strip()\#去掉首尾的空格

'012345012210543210'

**isalpha(), isdigit(), isalnum()判断字母数字及其组合**

\>\>\> f = '012345689abcdefg'

\>\>\> f.isalpha()

False

\>\>\> f.isdigit()

False

\>\>\> f.isalnum()

True

**split(‘分割依据’）分割函数**

\>\>\> g = 'Happy birthday, zy1996!'

\>\>\> g.split(' ‘)\#按照空格分割

['Happy', 'birthday,', 'zy1996!’]

join 函数

\>\>\> '-'.join(['Happy','birthday','zy1996’])

'Happy-birthday-zy1996'

**upper(), lower(), swapcase()大小写**

\>\>\> h = 'Zy1996'

\>\>\> h.upper()

'ZY1996'

\>\>\> h.upper()

'ZY1996'

\>\>\> h = 'Zy1996'

\>\>\> h.lower()

'zy1996'

\>\>\> h

'Zy1996'

\>\>\> h.swapcase()

'zY1996'

**replace（’被替换的 x’，’替换成 y‘）函数**

\>\>\> 'Happy birthday, zy1996!'.replace('zy1996’, 'zy2020')

'Happy birthday, zy2020!'