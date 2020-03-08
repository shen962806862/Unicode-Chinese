# Unicode-Chinese
一个实现Unicode与中文相互转换的小软件

<b>Version 1.1.0</b>

练手的小东西。<br />
刚巧最近玩阴阳师的时候接触到一位大哥写的御魂hub网站，里面通过对json文件的解析来实现一些计算，这让我对json产生了兴趣。<br /><br />
于是今天下午尝试着将Unicode与字符串相互转换的功能集成在小软件里。<br /><br />
2.0版本打算尝试实现txt文件与json文件的相互转换√ <br />

![Version 1.1.0](/1.1/UI.png)

<b>Version 2.0.0</b>

新增功能：<br /><br />
1.实现了json文件的解析并以txt文件的形式保存。<br /><br />
2.实现了一定格式下的txt文件转换为json文件<br /><br />
```python
{   #大括号顶格
   key1：value1  #键值对，一定要有冒号，不需要引号，顶格与否随意
   key2：value2
   key3：value3
}
```
3.通过选取文件路径方式输入文件，自动锁定输出目录为输入文件所在目录<br /><br />
4.优化UI，实现了窗口自适应以及滚动条自动跟随至文本末<br />

![Version 2.0.0](/2.0/UI.png)
