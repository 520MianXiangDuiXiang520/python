# 每天一道python题 
## [题目来源于‘zhangben’的GitHub](https://github.com/zhangben6/show-me-the-code)
###  第 0000 题：
* 时间：12/12  
* 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
* 类似于图中效果
![头像](http://i.imgur.com/sg2dkuY.png?1)
* 使用PIL完成图片处理
### 第 0001 题：
* 时间12/13 
* 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
* [随机数可以参考博客](https://www.jb51.net/article/130368.htm)
### 第 0002 题
* 12/14
* 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。
* ![picture](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/1.jpg)
### 第 0003 题
* 12/14
* 任一个英文的纯文本文件（我用了[小王子英文版全文](https://pan.baidu.com/s/11mRRl)），统计其中的单词出现的个数。
* ![picture](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/0003.jpg)
### 第0004 题
* 12/14
* 你有一个目录，放了你一个月的日记（我用了《星球大战》原文），都是 txt，为了避免分词的问题，假设内容都是英文，请统计出每篇日记中出现次数最多的词。
* ![picture](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/0004.jpg)
### 第 0005 题
* 12/15
* 爬取**豆瓣Top250**
* ![picture](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/0005.jpg)
### 第 0006 题
* 12/15
* 你有一个目录，装了很多照片（昨天爬的豆瓣海报），把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
* ![picture](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/0006.jpg)
*  ![picture](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/0006-1.jpg)
### 第 0007 题
* 12/16
* 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
*  ![picture](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/0007.jpg)
### 第 0008 题
* 12/17
* 你有一个HTML页面，找出他的正文和链接
### 第 0009 题
* 12/17
*  使用 Python 生成类似于下图中的**字母验证码图片**
* ![字母验证码](http://i.imgur.com/aVhbegV.jpg)
* [python PIL 模块参考](https://blog.csdn.net/guduruyu/article/details/71213717)
* ![效果](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/0009.png)
### 第 0010 题
* 12/18
* 敏感词文本文件 0010.txt，里面的内容为以下内容，当用户输入敏感词语时，用*替换
```text
牛比
牛逼
你娘
你妈
吃屎
```
运行结果
```text
C:\Users\lenovo\AppData\Local\Programs\Python\Python37\python.exe E:/PYthon/pythonday/pythonday/0010.py
shuru吃屎吧哈哈哈你妈
Building prefix dict from the default dictionary ...
Loading model from cache C:\Users\lenovo\AppData\Local\Temp\jieba.cache
*吧哈哈哈*
Loading model cost 0.704 seconds.
Prefix dict has been built succesfully.

Process finished with exit code 0
```
### 第 0011 题
* 12/19
* 在一段长文本中寻找某个字符串第一次出现的位置
* KMP算法
### 第 0012 题
* 12/21
* 用 Python 写一个爬图片的程序 [全是小姐姐 -_-!](https://pixabay.com/zh/photos/girl/?image_type=photo)
* ![errar](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/0012.png)
### 第 0013 题
* 12/22
* 纯文本文件 0013.txt为学生信息, 里面的内容（包括花括号）如下所示
```txt
{
        "1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
```
请将上述内容写到 0013.xlsx 文件中
* 关键：xlsx文件的读写
* ![errar](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/0013.jpg)
### 第 0014 题
* 12/27
> 抓了a,b,c,d四名犯罪嫌疑人，其中有一人是小偷，审讯中：  
a说我不是小偷；
b说c是小偷；
c说小偷肯定是d；
d说c胡说！
其中有三个人说的是实话，一个人说的是假话，请编程推断谁是小偷
### 第 0015 题
* 2019/1/1
* 今天元旦，开心一下，2019，去爱，去努力
* 在python中运行以下代码
```python
import antigravity
```
:heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart::heart:
![errar](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/0015.jpg)
### 第 0016 题
* 2019/1/6
* 老式挂钟会在整点的报时，响铃的次数和时间相等。我们设计一个在电脑上运行的报时器。
* 功能描述：运行后，在每一个整点长响一声，半个整点短响两声。实现睡眠模式，晚上十二点到早上五点不响铃。
### 第 0017 题
* 2019/1/7
* 再 0016 的基础上增加显示时间的功能，使它更像一块表
![errar](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/0017.jpg)
### 第 0018 题
* 2019/1/7
* 好多人只是假装在努力，为了让自己真实，做一个计时器，记录下自己每天学习的真实时间
![errar](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/0018.jpg)
### 第 0019 题
* 2019/1/16
* 今天发现一个好玩的库，itchat 用来实现微信接口，我有一个大胆的想法...
![404](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/001901.jpg)
![404](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/001902.jpg)
![404](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/001903.jpg)
![404](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/001904.jpg)
### 第 0020 题
使用python Web 框架，搭建一个 todolist 应用
![404](https://github.com/520MianXiangDuiXiang520/python/blob/master/imc/ToDoList.gif)
[代码位置](https://github.com/520MianXiangDuiXiang520/Django/tree/db_todolist)
### 第 0021 题
 纯文本文件 0021.txt, 里面的内容（包括方括号），将其导入到xls文件中
 ```text
[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]
```
### 第 0022 题
在圆周率前一百万位中能不能找到自己的生日？？
```text

按20190203的格式输入生日：
199985
您的生日在圆周率前1000000位中出现 2 次
第一次出现在 535589 到 535595 位

Process finished with exit code 0

顺便统计了一下各个数字出现的次数，发现5出现最多，，，虽然没什么意义

0 : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (99959次)
1 : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (99758次)
2 : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (100026次)
3 : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (100230次)
4 : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (100230次)
5 : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (100359次)
6 : @@@@@@@@@@@@@@@@@@@@@@@@@@@@  (99548次)
7 : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (99800次)
8 : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (99985次)
9 : @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  (100106次)

```
