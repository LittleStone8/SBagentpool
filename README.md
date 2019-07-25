# SBagentpool

- [x] 没必要在意是否已经存在了的
# Python 屎上最走心的代理池 项目

------
## ———— 善待每一个代理



### 直接谈一下项目吧，不聊技术：

#### 1）首先先说代理的存储方式
储存在redis中<br>
所有代理的信息都只存放在一个有序集合（SortedSet），一个哈希表(Hash)，一个链表（List）中。<br>
有序集合：存放分数低于100分的代理，按分数排序，分数越低越优质。<br>
哈希表：存放代理的详细信息。<br>
链表：存放分数高于100分（确认死得透透）的代理。<br>

#### 2）无脑的代理抓取
肯定是抓免费的嘛<br>
目前已加入西刺代理，快代理，66代理，站大爷这几个代理来源网站。<br>
抓取手段也集成了requests请求，urllib.request请求，还有selenium模拟浏览器抓取，走的是谷歌的内核。<br>
肯定是优先使用代理去抓取代理嘛，获取已有线程池里的十个最优质的代理去请求抓取数据。<br>
如果使用某个代理抓取失败了，会适当的对该代理做出加分处理，使其适当下沉起到自调节的作用。<br>
当然，如何使得其适当的下沉，避免劣质代理占据高位，优质代理没办法被使用，这其实是我觉得最难的东西，而且花费的时间也最多，后面说。<br>

#### 3）勤勤恳恳的调度器
调度器嘛，线程池的集合。<br>
主要工作是安排一系列任务的有序执行，例如多少时间间隔发起一次对某个代理的抓取，什么时候代理池该check一波等等。<br>
项目中所有的任务都是在调度器的线程池里跑的<br>
为什么要搞多个线程池？很容易理解嘛，就跟为什么要区分快车道和慢车道一样。比如同样是抓取代理，requests方式和selenium方式的速度就不是一个量级的，放在一起就很难受。<br>
还有另外一层就是'道不同，不相为谋'的意思。比如线程池的自净机制是每时每刻都在发生的，而抓取代理池是隔一段时间才执行。放在一起也是添堵。<br>
该项目里的线程池都自适应扩充的线程池，优先使用空闲的线程，没有空闲线程再创建，然后就是调用方法的参数传入，回调处理全部都有，模板代码没什么好说的。<br>
线程安全，为什么玩一下py的锁我故意在项目里搞了几个全局的计数变量，通过RLock()的方式保证计数的线程安全。<br>
别跟我说什么排他锁阻塞线程了.....我知道我知道<br>















- [x] 持续集成中
## 交流
* 作者：小石头
* QQ：262627160
