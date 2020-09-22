# 零宽文字混淆器

一个在字符串中随机加入随机数量零宽字符的混淆器。

随手写出来练手用的小工具。

![image](https://user-images.githubusercontent.com/21986859/93933527-545eed00-fd11-11ea-98f6-1212f8dd7ca1.png)

## 用法

1. 在 “输入文字” 输入框输入想要混淆的文字
1. （可选）：调整最大分隔字符数量
   1. 最大分隔字符数量代表两个字符之间最多能被插入多少个随机零宽字符
1. 点击 “混淆” 在 “输出文字” 中生成混淆的字符

## 原理

在字符之间插入随机数量的随机零宽字符。字符库如下：

- ~~'\u200B',  # zero-width space~~ 在某些情况下还是会显示出宽度
- '\u200C',  # zero-width non-joiner
- '\u200D',  # zero-width joiner
- '\u2060',  # word joiner
- '\uFEFF',  # zero-width no-break space
