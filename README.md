# SBagentpool

- [x] 我不管反正这就是
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
线程安全，为了玩一下py的锁我故意在项目里搞了几个全局的计数变量，通过RLock()的方式保证计数的线程安全。<br>
别跟我说什么排他锁阻塞线程了.....我知道我知道<br>

#### 3）一脸懵逼的管理器
代理池管理，主要为两点，对使用中提供优质的代理;对自身代理的优胜劣汰，使代理池保持活性。<br>
第一个很容易就实现了，这也是为什么用redis存的原因，SortedSet天然有序，直接按分数最低的来取，就是最优质的了。<br>
怎么来给一个代理来打分，需要考量因素很多：地区，隐匿类型，验证时间，响应时间，爬取的时间，使用其请求的成功次数，具上一次使用其请求成功的间隔等等。
项目里用来参考的因素也使用了其中的几个吧。<br>
一直说的这个代理池的自调节。<br>
目前有项目里有四种不同的机制的共同作用使其保持活性：<br>
1)使用者对其打分，使用代理失败时，会对该代理进行加分处理，使其下沉。这样避免了获取最优质的代理时不是一层不变的，你不行，别人就顶上。<br>
2)常规轮询检查，这个是管理自身发起的对一定分数以下的代理进行检测，看是否还存活，一次检测是对五个不同的常用url进行请求，请求失败就加上固定的请求失败方，成功的话就用过响应时间来参考分数，响应时间越短越优质，分数就越低，位置就在越前面。<br>
3)较差轮询检查，面对的是分数较高的代理，轮询一些代理进行检测，打分规则与常规轮询检测也会有所区别，使其更容易'咸鱼翻身'。<br>
4)淘汰机制,对于代理池中的死得透透的代理从SortedSet移到List中。有的同学会问，为什么要去除死透了的代理，答案是如果不去除，代理中会越积越多，特别影响到自身的自净。为什么要移到list中而不是删除，为了避免再次抓到这个死透了的代理。<br>
为什么说这个项目会善待每一个代理呢，其实在其调节机制中有所展现。<br>
项目的自净调节机制会给一个代理很多很多次机会，只要这个代理成功请求一次，那么以前的'恩恩怨怨'就一笔购销。<br>
这里有必要说一下。一个代理是连续7天的没有一次请求成功，才会被放弃。<br>


### 以上也就是项目的全部东西了，最关键的来了："说了一大堆，还不是抓一些免费代理网站的万人骑代理，网上代码都烂大街了，而且代理质量肯定很差，能不能用还是个问题"。
#### 答:
















- [x] 持续集成中
## 交流
* 作者：小石头
* QQ：262627160
