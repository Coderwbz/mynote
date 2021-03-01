# python 使用print语句来输出内容  print 内置函数
#  print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# sep 参数用来表示输出，每个值之间使用哪种字符作为分隔，默认使用空格作为分隔符
# end 当执行完一个print语句以后，接下来要输出的字符。默认以\n 表示换行
# 可以输出数字
print(520)
print(98.5)
# 可以输出字符串
print("helloworld")
print("are you ok")
# 含有运算符的表达式
print(9+1)
# 将数据输出到文件中
fp=open('D:/text.txt','a+')
# a+如果文件不存在就创建，存在就在文件内容的后面继续追加。每次运行都在后面追加一次
print('helloworld' ,file=fp)
fp.close()



