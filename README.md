# SBagentpool

- [x] 没必要在意是否已经存在了的
# Python 屎上最不走心的代理池 项目

------
———— 最不专注抓取代理而专注于管理的 py代理池 项目



##
**直接谈一下项目吧，不聊技术（反正也没人看代码）：**

首先先说代理的存储方式吧，储存在redis中。

所有代理的信息都只存放在一个有序集合（SortedSet），一个哈希表(Hash)，一个链表（List）中。
有序集合：存放分数低于100分的代理，按分数排序，分数越低越优质。
哈希表：存放代理的详细信息。
链表：存放分数高于100分（确认死得透透）的代理。








- [x] 持续集成中
## 交流
* 作者：小石头
* QQ：262627160
