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
* ![效果](http://tie.027cgb.com/150_612828/0009.png)
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
```python
C:\Users\lenovo\AppData\Local\Programs\Python\Python37\python.exe E:/PYthon/pythonday/pythonday/0010.py
shuru吃屎吧哈哈哈你妈
Building prefix dict from the default dictionary ...
Loading model from cache C:\Users\lenovo\AppData\Local\Temp\jieba.cache
*吧哈哈哈*
Loading model cost 0.704 seconds.
Prefix dict has been built succesfully.

Process finished with exit code 0
```
