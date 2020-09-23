# 零宽文字混淆器

一个在字符串中随机加入随机数量零宽字符的混淆器，可以在不损害文字可读性的情况下绕过众多自动屏蔽/审核系统。

随手写出来的小工具。

虽然我没有参考其他项目的实现方式，但是目前应该已经有很多类似的项目能够达到该软件类似的效果了，所以该项目无疑是在造轮子。因此，相较于实际使用这个工具来混淆文字，我认为该工具更大的价值在于普及这种无损可读性绕过审核的思路。虽然目前该策略对于大多数自动审核屏蔽的平台都有效，但是只要平台忽略零宽字符就能够反制这种策略。希望该项目能抛砖引玉，引领更优秀的不损害文字本身可读性的审核绕过方案出现。如果我后续想到更好的方案也会继续加入进这个轮子里。

![image](https://user-images.githubusercontent.com/21986859/93933527-545eed00-fd11-11ea-98f6-1212f8dd7ca1.png)

## 用法

1. 在 “输入文字” 输入框输入想要混淆的文字
1. （可选）：调整最大分隔字符数量
   1. 最大分隔字符数量代表两个字符之间最多能被插入多少个随机零宽字符
1. 点击 “混淆” 在 “输出文字” 中生成混淆的字符

## 原理

在字符之间插入随机数量的随机零宽字符。字符库如下：

- ~~'\u200B',  # zero-width space~~
  - 在某些情况下还是会显示出宽度
- '\u200C',  # zero-width non-joiner
- '\u200D',  # zero-width joiner
- '\u2060',  # word joiner
- '\uFEFF',  # zero-width no-break space
  - 某些平台（例如 Twitter）不支持该字符

## 免责声明

请不要将该技术运用于违法违规用途。没错，咱求生欲很强。
