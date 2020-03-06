本文涉及 cd, ls, pwd, mkdir, rmdir, rm, chmod 等基本操作。

**cd 指令，在电脑文件中游走**

cd (change Directory），切换文件夹。

➜ ~ pwd \#显示当前路径

/Users/zy1996

➜ ~ cd Documents \#切换文件夹到

➜ Documents pwd \#绝度路径

/Users/zy1996/Documents

➜ Documents cd /Users/zy1996/Downloads \#切换到指定的绝对路径

➜ Downloads \#到啦！

**ls指令，看看所在文件夹下都有啥？**

ls 就是 list 的缩写，就是列出你所在文件夹下的文件们

➜ Downloads ls \#列出 Downloads 文件夹下的文件

file1 file2 file3 file4 file5

➜ Downloads ls -l \#输出更多信息，l 就是 long 的缩写，下面输出了文件权限，用户名，文件大小，文件名

total 0

-rw-r--r-- 1 zy1996 staff 0 3 6 11:43 file1

-rw-r--r-- 1 zy1996 staff 0 3 6 11:43 file2

-rw-r--r-- 1 zy1996 staff 0 3 6 11:43 file3

-rw-r--r-- 1 zy1996 staff 0 3 6 11:43 file4

-rw-r--r-- 1 zy1996 staff 0 3 6 11:43 file5

➜ Downloads ls -a \#a 是 all 的缩写，展示文件夹下所有的文件，包括隐藏文件

. .. .DS\_Store file1 file2 file3 file4 file5

➜ Downloads ls -lh \#l是 lang 的缩写，h 是 human 的缩写，说白了，就是给输出给人看的东西

total 0

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:43 file1

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:43 file2

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:43 file3

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:43 file4

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:43 file5

**touch 创建文件(不能创建文件夹，mkdir 用来创建文件夹）**

➜ Downloads touch file6.py \#新建 file6.py

➜ Downloads ls \#显示当前文件夹文件

file1 file2 file3 file4 file5 file6.py

**cp 复制**

cp(copy)，顾名思义。常用操作为：

copy oldfile newfile \#copy 旧文件到新文件

➜ Downloads cp file1 folder1/ 复制 file1到

➜ Downloads ls

file1 file1copy file2 file3 file4 file5 file6.py folder1

➜ Downloads cd folder1

➜ folder1 ls

file1

➜ Downloads cp folder2 folder3 \#复制文件夹

cp: folder2 is a directory (not copied). \#文件夹不能这么复制

➜ Downloads cp -r folder2 folder3 \#文件夹需要加上-r

➜ Downloads cd folder3

➜ folder3 ls

folder2

➜ folder3

**mv 移动，也就是剪切**

➜ Downloads ls \#查看 Downloads 文件夹内的文件们

file1 file1copy file2 file3 file5 file6.py folder1 folder2

➜ Downloads mv file5 folder2 \#在 Downloads 文件夹下把 file5 移动到 folder2 文件夹下

➜ Downloads ls \#移动完毕查看 Downloads，确实没有file5 了

file1 file1copy file2 file3 file6.py folder1 folder2

➜ Downloads cd folder2/ \#切入 folder2 文件夹

➜ folder2 ls \#查看 folder2 文件夹内文件们 确实有 file5 文件

file5

**mkdir 创建文件夹 make directory**

➜ Downloads mkdir folder3 \#在 Downloads 文件夹下创建 folder3 文件夹

➜ Downloads ls \#list 一下发现 folder3 文件夹已创建

file1 file1copy file2 file3 file6.py folder1 folder2 folder3

➜ Downloads mkdir folder3/folder3\_1\#在 folder3 文件夹下再创建一个文件夹

➜ Downloads cd folder3 \#切换至 folder3 文件夹

➜ folder3 ls\#查看 folder3 确实有新文件夹

folder3\_1

**rmdir 移除文件夹 remove directory**

➜ folder3 rmdir folder3\_1 \#remove文件夹

➜ folder3 ls \#查看文件 list

➜ folder3

**rm, remove文件**

➜ Downloads ls \#查看文件 list

file1 file1copy file2 file3 file6.py folder1 folder2 folder3

➜ Downloads rm file1copy \#remove 文件 file1copy

➜ Downloads ls\#再次查看文件 list 验证是否删除成功

file1 file2 file3 file6.py folder1 folder2 folder3

加-i

➜ Downloads rm -i file2

remove file2? y

➜ Downloads ls

file1 file3 file6.py folder1 folder2 folder3

➜ Downloads ls

total 0

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:43 file1

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:43 file3

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:55 file6.py

drwxr-xr-x 6 zy1996 staff 192B 3 6 14:44 folder1

drwxr-xr-x 3 zy1996 staff 96B 3 6 14:46 folder2

drwxr-xr-x 2 zy1996 staff 64B 3 6 15:01 folder3

➜ Downloads rmdir folder1\#删除文件夹

rmdir: folder1: Directory not empty\#报错不能删，因为文件夹不为空

➜ Downloads rm -r folder1 \#递归地删除 folder1 里所有文件

➜ Downloads ls \#发现 folder1 已删除

total 16

-rw-r--r--@ 1 zy1996 staff 6.0K 3 6 12:41 .DS\_Store

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:43 file1

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:43 file3

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:55 file6.py

drwxr-xr-x 3 zy1996 staff 96B 3 6 14:46 folder2

drwxr-xr-x 2 zy1996 staff 64B 3 6 15:01 folder3

**文件权限管理 chmod(change mode)**

[![Linux 文件权限](resources/C300905B53F288F10A124D1F38C8A1EA.png "Linux 文件权限")](https://morvanzhou.github.io/static/results/linux-basic/03-01-02.png)

➜ Downloads ls -l \#查看文件们的状态，观察 file1 ，user 有 read，write 权限，没有 execute 权限

total 16

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:43 file1

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:43 file3

-rw-r--r-- 1 zy1996 staff 46B 3 6 15:20 file6.py

-rw-r--r-- 1 zy1996 staff 23B 3 6 15:19 file7.py

drwxr-xr-x 3 zy1996 staff 96B 3 6 14:46 folder2

drwxr-xr-x 3 zy1996 staff 96B 3 6 15:13 folder3

drwxr-xr-x 2 zy1996 staff 64B 3 6 15:23 qutiansong

案例：给所有 all 增加 x 权限

➜ Downloads chmod a+x 03-01-02.png

➜ Downloads ll

total 64

-rwxr-xr-x@ 1 zy1996 staff 23K 3 5 11:00 03-01-02.png

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:43 file1

-rw-r--r-- 1 zy1996 staff 0B 3 6 11:43 file3

-rw-r--r-- 1 zy1996 staff 46B 3 6 15:20 file6.py

-rw-r--r-- 1 zy1996 staff 69B 3 6 15:28 file7.py

drwxr-xr-x 3 zy1996 staff 96B 3 6 14:46 folder2

drwxr-xr-x 3 zy1996 staff 96B 3 6 15:13 folder3

drwxr-xr-x 2 zy1996 staff 64B 3 6 15:23 qutiansong

通常的修改形式是

$ chmod [谁][怎么修改] [哪个文件]


[举个最简单的例子, 现在的 `t1.py` 是 `----rw-r--`, 如果我们想让你(user)有读的能力. 下面这样改就行了.

    u+r t1.py
    * ```
    $ chmod u+r t1.py
    $ ls -l
    -r--rw-r-- 1 morvan morvan 34 Oct 12 09:51 t1.py
    ```

这里的 `u+r` 很形象, User + read, 给 t1.py 这个修改. 所以我们的修改形式就能总结出下面这样.

[谁]

* `u`: 对于 User 修改
* `g`: 对于 Group 修改
* `o`: 对于 Others 修改
* `a`: (all) 对于所有人修改

[怎么修改]

* `+`, `-`, `=`: 作用的形式, 加上, 减掉, 等于某些权限
* `r`, `w`, `x` 或者多个权限一起, 比如 `rx`
* [哪个文件]
* 施加操作的文件, 可以为多个
