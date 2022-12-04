# 微博言论研究

[TOC]



## 摘要

本实验主要进行在相对无平台干预和引导下的微博言论研究。随着微博用户数量的快速增长，网民所携带的一些情感和观点对社会的影响越来越大，尤其是一些涉及到公众人身安全的负面情绪，可能会影响到社会的稳定，因此进行微博情感分析意义重大。微博情感分析的内容包括微博语料的获取，微博语料的预处理，信息特征探索，网络文本挖掘。本实验以卡塔尔世界杯为话题背景，检测评论信息有用性作为目标，从发表时间、扩散力，评论和回复的信息效用特征，情感得分等角度得到分析结果，概括相关特征作为具有决定性的影响变量。评论的信息有用性检测已经越来越重要，对评论文本内容进行挖掘与审核，能正确引导用户合理讨论，发送文明评论，有助于营造和谐稳定的网络环境，这也能凸显言论研究的学术价值和商业价值。



## 导论

### 研究对象

本实验进行舆情发展趋势研究，所选择的网站实证对象为微博平台，它是目前热门的社交平台之一。具有用户热门评论，楼层回复，评论点赞等功能。



### 研究的背景

舆论，主要有两种代表性观点。第一种观点认为舆论是一定范围内多数人的集合意识及共同意见，持这种观点的主要代表刘建明教授。第二种观点认为舆论并不是所说的简单的“公众意见”，而是众人对社会事务共同感悟的顽强意志。表现为同一种希望和追求，即民意。

研究舆论引导的发生，主要是要回答“舆论究竟需不需要引导”和“为什么会有舆论引导”这两个问题。国内学者一般都认同舆论需要引导这种观点，但在“为什么会有舆论引导”这个问题上有不同的看法。对于舆论的引导大致有以下几种认识。[1-4]

+ 第一：如何以社会深层意识引导社会浮动意识的问题。因为舆论是一种浮动意识，处于社会意识活动的泛化层面，人们随时都能感受到它的存在。
+ 第二：作为舆论主体的公众，应当能够自主的表现和表达，具有自主意识。这是能够视为舆论主体的必要条件，否则，公众意见也许并不是真正来自公众。
+ 第三：需要建立适当的舆论表达机制，允许人们合法地进行意见的表达和交流，使民意得到适当的宣泄和疏导。否则，轻者可能导致舆论以遥言、流言的形式出现从而成为社会不安定的因素，重者则可能造成对抗性的群体冲突事件，导致社会危机和结构性破坏。
+ 第四：舆论有正误之分，不是所有的舆论都是代表人民利益，能真实地反映社会事务的发展。正确鉴别不同舆论，对社会工作者至关重要。



### 意义

研究微博言论，就必须始终将社会公众的信念、态度、情绪或者集合意识作为关注和研究的重点。江泽民同志在中宣部举办的新闻工作研讨班上指出：“我们国家的报纸、广播、电视等是党、政府和人民的喉舌”，“必须按照党和人民的意志、利益进行舆论导向”。当前我国舆论环境的着深刻变化对社会稳定产生着重要影响，新兴舆论场就是一个高度敏感的复杂系统。在这个系统中，一个看似微不足道的麦克风，一条小道消息，通过新兴舆论场的发酵、催化，会迅速升温。如果引导不力或者不当，容易使局部问题扩大为全局性问题，使一般问题演变成政治性问题，使个人的偏激言论扩散为非理性的社会情绪，直接影响社会稳定。研究微博言论，有助于推进我国社会主义意识形态建设。[5-9]



## 关键词

舆论引导；舆情分析；微博言论；议题设置；引导能力



## 实验准备

### 需求分析

本实验主要进行三个方面实际操作：

+ 探索热门事件与网民关注度关系。
+ 探索信息特征，将话题词，艾特数，点赞数作为主要衡量指标。
+ 网络文本挖掘，包括 tf-idf计算，情感得分统计，搭建情感聚类模型等。



### 使用说明

先连续获取微博正文、发布者，转发数，评论数，点赞数等。并将结果写入文件、数据库等。如果还需要搜索，即：**搜索正文中包含指定关键词的微博**，可以指定搜索的时间范围。搜索结果数量巨大，对于非常热门的关键词，在一天的指定时间范围，可以获得**1000万**以上的搜索结果。1000万只是一天时间范围可获取的微博数量，如果想获取更多微博，可以加大时间范围，比如10天，最多可以获得1000万X10=1亿条搜索结果。对于大多数关键词，微博一天产生的相关搜索结果应该低于1000万，本程序可以获取指定关键词的全部或近似全部的搜索结果。



### 运行软件环境

- Python 3.10
- Pillow
- Pandas
- Spider
- scrapy
- Numpy

**本程序依赖 Scrapy 和 Pillow（>=8.1.1）**



### 获取cookie

1. 用Chrome打开 https://weibo.com/
2. 点击"立即登录", 完成私信验证或手机验证码验证, 进入新版微博。
3. 按F12打开开发者工具，在开发者工具的 Network  ->  Name  ->  weibo.cn  ->  Headers  ->  Request Headers，找到"Cookie:"后的值，这就是我们要找的cookie值，复制即可。



**获取旧版微博的Cookie**

1. 用Chrome打开<https://passport.weibo.cn/signin/login>

2. 输入微博的用户名、密码，登录。登录成功后会跳转到 https://m.weibo.cn
3. 按F12键打开Chrome开发者工具，在地址栏输入并跳转到 https://weibo.cn
4. 依此点击Chrome开发者工具中的Network  ->  Name中的weibo.cn  ->  Headers  ->  Request Headers，"Cookie:"后的值即为我们要找的cookie值，复制即可。



### 程序运行

在结束时可以保存进度，下次运行时会在程序上次的地方继续获取。

```bash
scrapy crawl search -s JOBDIR=crawls/search
```

如果想要保存进度，使用`Ctrl + C` 一次。按下`Ctrl + C`一次后，程序会继续运行一会，主要用来保存获取的数据，保存进度等操作，请耐心等待。下次再运行时，只要再运行上面的指令就可以恢复上次的进度。

直接运行 `scrapy crawl search` 也可以



### 文件说明

- Result：存放分析结果的文件夹
- weibo：存放爬虫代码的文件夹
- topic_yuntu.png：话题云图文件
- data.csv：Spider爬取到的评论信息文件
- Alalyse：存放不同分析处理代码的文件夹
- Environment：存放实验所需数据词典和爬取到的微博文件夹



### 输出说明

- 微博id：微博的id，为一串数字形式
- 微博bid：微博的bid
- 微博内容：微博正文
- 头条文章url：微博中头条文章的url，若某微博中不存在头条文章，则该值为 ' '
- 原始图片url：原创微博图片和转发微博转发理由中图片的url，若某条微博存在多张图片，则每个url以英文逗号分隔，若没有图片则值为''
- 视频url: 微博中的视频url和Live Photo中的视频url，若某条微博存在多个视频，则每个url以英文分号分隔，若没有视频则值为''
- 微博发布位置：位置微博中的发布位置
- 微博发布时间：微博发布时的时间，精确到天
- 点赞数：微博被赞的数量
- 转发数：微博被转发的数量
- 评论数：微博被评论的数量
- 微博发布工具：微博的发布工具，如iPhone客户端、HUAWEI Mate 20 Pro等，若没有则值为''
- 话题：微博话题，即两个#中的内容，若存在多个话题，每个url以英文逗号分隔，若没有则值为''
- @用户：微博@的用户，若存在多个@用户，每个url以英文逗号分隔，若没有则值为''
- 原始微博id：为转发微博所特有，是转发微博中那条被转发微博的id，那条被转发的微博也会存储，字段和原创微博一样，只是它的本字段为空
- 结果文件：保存在当前目录“结果文件”文件夹下以关键词为名的文件夹里
- 微博图片：微博中的图片，保存在以关键词为名的文件夹下的images文件夹里
- 微博视频：微博中的视频，保存在以关键词为名的文件夹下的videos文件夹里



## 爬取与预处理

### 数据获取方式

**相关理论：**浏览器进入微博官网，打开一个帖子。进入开发者工具，清除数据包后，向下拖动评论区可以发现微博的帖子采用的是懒加载模式。浏览器发送`GET`请求，服务器收到请求后返回数据一次返回固定的长度。当页面显示的长度大于浏览器返回包的长度时进行懒加载一次，加载一次浏览器发送一次`GET`请求，服务器返回一次数据。返回数据里的 `data.cards`包括了评论区里面的真实`reply`。找到这些回答的数据包以后，删除相应包的参数，可以发现请求的浏览器发出的请求的`url`，将`url`复制到筛选框内，筛选对应的包，可以找到所有请求评论评论的所有`url`。通过抓包分析到三个`url`即可得到请求评论区数据的请求包规律。 



**经过URL解码后确定到爬取请求网址**

```url
start_url = https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%23%E5%8D%A1%E5%A1%94%E5%B0%94%E4%B8%96%E7%95%8C%E6%9D%AF%23&page_type=searchall
```



### 数据基本信息

（简要介绍数据的基本信息，如数据文件类型，包含的内容等等）

`cards`为有逻辑编号的列表

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212031915815.png)



需要的帖子信息数据在`cards[0].mblog.text`

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202211261737305.png)



### 数据获取

读取数据使用了`requests.get`函数。通过`requests.get(url, headers)`构造一个向服务器请求资源的url对象。这个对象是手动生成的。这时候的返回的是一个包含服务器资源的Response对象。包含从服务器返回的所有的相关资源。

**获取数据代码：**

```python
def main():
        print('爬取懒加载节点{}的数据!'.format(i))
        start_url = f'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%23%E5%8D%A1%E5%A1%94%E5%B0%94%E4%B8%96%E7%95%8C%E6%9D%AF%23&page_type=searchall'
        headers = {
            'user-agent': ' ',
            'referer': ' '
        }
        response = requests.get(start_url, headers = headers).json()
        ic(response)
```

由于本机的`cmd`的下载会调入`Acaconda`模块，而`vscode`的控制台会调用此处`C:\Python310\python.exe`，需要手动加`Acaconda`路径，或者将`Acaconda`的环境变量暴露出去，就可以解决该问题

```cmd
&D:\Data\Acaconda\python.exe D:\Study\course\Python\NO8\get_data.py
```



相关 Spider 配置

```python
# U-A请求头
USER_AGENT = 'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'

# 不服从爬虫协议，解决拒绝访问
ROBOTSTXT_OBEY = False

# 对同一网址延迟请求的秒数，受RANDOMIZE_DOWNLOAD_DELAY影响(默认开启)，实际延迟时间为[0.5 * DOWNLOAD DELAY , 1.5 * DOWNLOAD_DELAY]
DOWNLOAD_DELAY = 5

# 每个域名能够被执行的最大并发数 默认8
CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 能被单个IP处理的并发请求数，默认0 代表无限制。
# I、如果不为零，那CONCURRENT_REQUESTS_PER_DOMAIN将被忽略，即并发数的限制是按照每个IP来计算，而不是每个域名
# II、该设置也影响DOWNLOAD_DELAY，如果该值不为零，那么DOWNLOAD_DELAY下载延迟是限制每个IP而不是每个域
CONCURRENT_REQUESTS_PER_IP = 16

# cookie（默认启用）
COOKIES_ENABLED = ''

# 开启管道
ITEM_PIPELINES = {
    'sprider.pipelines.SpriderPipeline': 300,
}
```



### 数据清洗与预处理

**数据解析**

 ```python
# 用户id
weibo['user_id'] = info[0].xpath('div[2]/a/@href').extract_first().split('?')[0].split('/')[-1]
# 评论内容
weibo['text'] = txt_sel.xpath('string(.)').extract_first().replace('\u200b', '').replace('\ue627', '')
# 文章URL
weibo['article_url'] = self.get_article_url(txt_sel)
# 位置
weibo['location'] = self.get_location(txt_sel)
# 艾特用户
weibo['at_users'] = self.get_at_users(txt_sel)
# 话题
weibo['topics'] = self.get_topics(txt_sel)
# 回复数
reposts_count = sel.xpath('.//a[@action-type="feed_list_forward"]/text()').extract()
# 创建时间
weibo['created_at'] = util.standardize_date(created_at)
 ```



**评论信息数据清洗**

提取`replies.text`内容，该内容即为评论信息

在线正则表达式测试 https://tool.oschina.net/regex#

要提取中文，测得正则式`[\u4e00-\u9fa5]+`，但是空格会造成输出换行，使用`.*?([\u4e00-\u9fa5]+).*`

```python
re.findall('.*?([\u4e00-\u9fa5]+).*',response.text)
```

注：本次实验共进行了五天的数据爬取，因网络波动的影响，有小部分时间段的少量数据未获取成功。



## 探索信息特征

网络文本挖掘是对网上大量文本进行表示、特征提取、内容总结、分类、聚类、关联分析、语义分析以及利用网络文本进行趋势预测等。

文本挖掘主要的技术包括：

1. 特征提取。将关于文本的元数据，分为描述性特征（如文本的名称、日期、大小、类型等）和语义性特征（如作者、标题、内容等）。描述性特征较易获取，语义性特征获取较难。
2. 文本分类。在给定的分类体系下，根据文本的内容确定文本所属类别的过程。文本分类是一个**有监督的学习**过程，它根据一个已经被标注的训练文档集合，找到文档特征和文档类别之间的关系模型，然后利用这种学习得到的关系模式对新的文档进行类别判断。文本分类主要有K近邻分类方法、贝叶斯分类方法、支持向量机（SVM）分类方法等。
3. 文本聚类。文本聚类的目的通常是将文档集分成一些簇的集合，使这些簇间的相似性最小，簇内的相似性最大。与文本分类不同的是，文本聚类没有事先定义好的类，所以文本聚类被称为**无监督的学习**。待聚类的文档通常用向量空间模型(VSM)表示。聚类算法主要有两类：层次聚类，如G-HAC算法；动态聚类，如K-均值算法。在层次聚类法中，将给定文档集合中的每个文档看作是一个具有单个成员的簇，这些簇构成了给定集合的一个聚类；计算聚类中每对簇之间的相似度；从中选取具有最大相似度的簇对，并将它们合并为一个新簇；重复以上各步，直至剩下一个簇为止。
4. 关联分析。是指从文档集合中找出不同词语之间的关系，如在Web上寻找作者与书名的出现模式。文本中出现的词往往存在一定的相关性，文本关联分析主要是实现Web页面信息的概念提升及多层关联规则的挖掘功能，发现展示属性值频繁地在给定数据集中一起出现的条件。文本挖掘在不同概念级别上将进行多层关联规则的挖掘，在页面集合中寻找不同词语之间的关系。文档之间的超链也反映了文档之间的某种联系，HTML文档中的超链接标记文本对链接页面具有一定的概括作用，通过对超链文本的分析，可以判断出页面之间的关系。Web内部也有一些结构信息有助于发现知识，超链接中的URL在一定程度上可以反映文档的类型。所以通过分析一个页面链接和被链接数量以及对象属性，可以用于网页归类，并且由此可获得有关不同网页间相似度及关联度的信息。
5. 文本总结。是指从文档中抽取关键信息，用简洁的形式对文档内容进行摘要或解释。这样，用户不需要浏览全文就可以了解文档或文档集合的总体内容。自动摘要有Extraction和Abstraction两种方法。前者是通过从原始文本提取句子的方法来生成摘要，实现比较简单，但存在着如何将提取出来的零散的句子组成连贯摘要的问题。后者是一种主要的摘要方法，也是文献摘要常见的主要方法。由于其生成的摘要中包含原文中所没有的句子，因此，它的智能化要求较前者高，实现也比较困难。
6. 趋势预测。是指通过对Web文档的分析，得到特定数据在某个历史时刻的情况或将来的取值趋势。趋势分析可以发现频繁模式或关联规则随时间的变化趋势，能够更加详细地描述规则的动态特性。文本挖掘技术目前主要应用在自动索引、自动文摘、信息检索、信息抽取、文档组织、主题跟踪等方面。由于网络上的焦点热点问题层出不穷，文本挖掘技术为深层次的分析提供了的技术支持和解决方案。



### 按天统计发贴个数

核心代码如下：

```python
dates1_df = pd.DataFrame({'日期': [key for key in date_dict1.keys()],
                        'Count': [value for value in date_dict1.values()]})
dates1_df
```

详情数据表如下：

|    日期    | 数量 |
| :--------: | :--: |
| 2022-11-20 | 2240 |
| 2022-11-21 | 3098 |
| 2022-11-22 | 3234 |
| 2022-11-23 | 2415 |
| 2022-11-24 | 1761 |

发贴量统计图如下。

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212011607111.png)

在这五天中，发帖量最大为22号，达到了3098。这是因为在此 `#卡塔尔世界杯#` 话题下的21号为开幕日，有英格兰VS 伊朗的竞赛。22号，有阿根廷 VS 沙特阿拉伯的竞赛。后场竞赛共有242万人观看并参与比分预测，远远大于其他比赛的观看人数（一般在 30 - 50 万人左右）。在观看人数基数陡增的背景下，由统计图可得知，有较多数量的用户也进行了发帖。



### 话题标签频率

核心代码：

```python
ht1_list = []
for line in comment['微博正文']:
    line_s = line.split('\n')
    for i in range(0, len(line_s)):
        if i == 0:
            lst = re.findall(r'(#.+?#)', line_s[i])
            if lst is not None:
                for each in lst:
                    ht1_list.append(each)
        if i == 2:
            lst = re.findall(r'(#.+?#)', line_s[i])
            if lst is not None:
                for each in lst:
                    ht1_list.append(each)      
ht1_list
```

经过统计，得出详细的频率表格，如下。

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212011619401.png)

数据集共使用了 3203 种标签，平均每个帖子包含的话题标签: 2.10，这是因为用户可以将多个标签添加到自己的一条评论里。在`#卡塔尔世界杯#`话题中的所有微博用户的活动都首先会带有该标签，其次多数用户会选择一到两个自己喜欢的标签，系统有时也会推荐相关标签供用户将选择。

经过统计，标签数使用数小于三次的共有：2633 种 ，占比：82%。使用数大于十次的标签数共有：140 种 ，占比：4.3%。根据排版习惯，过多的标签会降低自己正文内容的可阅读性。所以大部分的用户选择自己创建适合自己内容标签，这种标签的普遍被使用性不高，只有一小部分的标签才会被大量使用。



### 话题标签-Top10

核心代码如下：

```python
ht1_df.nlargest(11, 'Count').plot(kind = 'barh', 
            fontsize = 12,
            x = 'Hashtag',
            y = 'Count',
            figsize = (16,8),
            legend = None)
plt.title('话题标签Top10', fontsize = 24)
plt.xlabel('数量', fontsize = 20, color = 'blue')
plt.ylabel('#话题#', fontsize = 20, color = 'blue')
plt.tick_params(axis='both', labelsize=14)
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号
plt.show()
```

话题标签详情统计数据如下表：

|       话题名称        | 出现次数 |
| :-------------------: | :------: |
|    #卡塔尔世界杯#     |  12695   |
|       #世界杯#        |   2412   |
|        \#足球#        |   393    |
| \#阿根廷vs沙特阿拉伯# |   385    |
|     \#德国vs日本#     |   342    |
|    \#世界杯开幕式#    |   339    |
|        \#梅西#        |   325    |
|     \#围观世界杯#     |   312    |
|    \#英格兰vs伊朗#    |   299    |
|  \#卡塔尔vs厄瓜多尔#  |   250    |

话题标签 Top10 统计图如下。

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212011622360.png)

由话题标签统计图可知，话题标签的使用比较分化，但是很多个话题标签都是针对同一件事，或者是关键人物，及后续的进展。这些大量使用的标签都是发生在卡塔尔世界杯里。在几场受人关注的热门比赛中，参与此微博话题的人数大致相同。



### 艾特数研究

```python
# 找出所有 @
mt1_list = []
for line in comment['微博正文']:
    line_s = line.split('\n')
    for i in range(0, len(line_s)):
        if i == 0:
            lst = re.findall(r'(@.+?):', line_s[i])
            if lst is not None:
                for each in lst:
                    mt1_list.append(each)
        if i == 1:
            lst = re.findall(r'原始用户: (.+)',line_s[i])
            if lst is not None:
                for each in lst:
                    mt1_list.append('@' + each)
        if i == 2:
            lst = re.findall(r'(@.+?) ', line_s[i])
            if lst is not None:
                for each in lst:
                    mt1_list.append(each) 
mt1_list
```

经过统计，所有帖子共体艾特次数为26，平均每个帖子提到 0.00447 个用户。



### 艾特数-Top5

核心代码如下：

```python
mt1_df = pd.DataFrame({'用户': [user for user in mt1_fre.keys()],
                      'Count': [count for count in mt1_fre.values()]})

mt1_df = mt1_df.sort_values('Count', ascending=False).reset_index(drop=True)
mt1_df
```



详情统计数据如下表：

|                           话题名称                           | 出现次数 |
| :----------------------------------------------------------: | :------: |
|                         @智恒充电柜                          |    11    |
|                          @雪荞品牌                           |    9     |
| @共青团西南医科大学委员会微博//@西南医科大人文与管理学院分团委 |    5     |
|                     @欧陽龍森的@绿洲动态                     |    3     |
|                        @金达官方微博                         |    3     |



艾特数 Top5 统计图如下。

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212011626163.png)



**智恒充电柜，雪荞品牌**之所以多次出现是因为这些用户正以艾特自己的形式进行微博抽奖，以借助世界杯的话题加强自己品牌的宣传。

**共青团西南医科大学委员会微博**的多次出现是因为别人@她，或者转发自己的原始内容。



### 用户回复数时间线

核心代码如下：

```python
combine1_df = pd.DataFrame({'Date': date_list1_clean,
                    'Content': comment['微博正文'],
                   'Repost': comment['转发数'],
                   'Like': comment['点赞数'],
                   'Comment': comment['评论数']
                           })
combine1_df
```

用户回复数时间线绘制图如下。

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212011636638.png)

该数据将在下文和热力图一起对比。



### 评论数时间线

核心代码如下：

```python
combine1_df[::].plot(kind = 'line', 
                  x = 'Date',
                  y = 'Comment',
                  fontsize = 12,
                 figsize = (16,8),
                 legend = None)
plt.title('评论数时间线', fontsize = 24)
plt.xlabel('Date', fontsize = 20, color = 'blue')
plt.ylabel('Count', fontsize = 20, color = 'blue')
plt.tick_params(axis='both', labelsize=16)
plt.grid(True)
plt.show()
```



评论数时间线绘制图如下。

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212011638066.png)

该数据将在下文和热力图一起对比。



### 引发热门评论帖子-Top5

核心代码如下：

```python
number = 0
print('The top 5 most REPOST posts are:')
while number != 5:
    print('\nNo.' + str(number+1) + '.')
    print('日期: \t\t' + combine1_df.sort_values('Repost', ascending=False).reset_index(drop=True)['Date'][number])
    print('回复数: \t' + str(combine1_df.sort_values('Repost', ascending=False).reset_index(drop=True)['Repost'][number]))
    print('内容: \t\t' + combine1_df.sort_values('Repost', ascending=False).reset_index(drop=True)['Content'][number])
    number += 1
```

引发热门评论的帖子详情数据：

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212011645864.png)



### 引发热门回复帖子-Top5

核心代码如下：

```python
number = 0
print('The top 5 most REPOST posts are:')
while number != 5:
    print('\nNo.' + str(number+1) + '.')
    print('日期: \t\t' + combine1_df.sort_values('Repost', ascending=False).reset_index(drop=True)['Date'][number])
    print('回复数: \t' + str(combine1_df.sort_values('Repost', ascending=False).reset_index(drop=True)['Repost'][number]))
    print('内容: \t\t' + combine1_df.sort_values('Repost', ascending=False).reset_index(drop=True)['Content'][number])
    number += 1
```

引发热门回复的帖子详情数据：

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212011645230.png)



回复数时间线绘制图如下

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212011647799.png)

该数据将在下文和热力图一起对比。



### 评论区数据点赞数排序

核心代码如下：

```python
mean_ratings = comment.pivot_table(index='id',values=['转发数','评论数','点赞数']).sort_values(by='点赞数', ascending=False)
mean_ratings.head(10)
```

评论区数据点赞详细数据：

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212011758184.png)

该数据将在下文和热力图一起对比。



### 评论内容字符数大小

|  字符数   |  个数  | 占比 |
| :-------: | :----: | :--: |
|  小于20   | 1649个 | 13%  |
| 20<=n<50  | 5126个 | 40%  |
| 50<=n<100 | 3554个 | 28%  |
|  大于100  | 2419个 | 19%  |

分析收集到的数据发现，字符数介于 20到100 的占比约为`68%`，大部分评论文本长度为 `20-50` 个字左右，可见用户倾向于发表完整的感受或想法，更注重信息内容本身。不到`1/5`的用户会考虑根据热点主题进行针对性长篇评论。有13%用户的评论文本长度为20个字符以内。文字较短，部分用户对于评论表达的规范性和完整度不太关注。



### 综合回复数，点赞数，评论数三项

核心代码如下：

```python
repost1 = pd.Series(data = combine1_df[::-1]['Repost'].values, index = combine1_df[::-1]['Date'])
like1 = pd.Series(data = combine1_df[::-1]['Like'].values, index = combine1_df[::-1]['Date'])
comment1 = pd.Series(data = combine1_df[::-1]['Comment'].values, index = combine1_df[::-1]['Date'])
```

综合回复数，点赞数，评论数三项的绘制图如下

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212011649203.png)



由综合表得知，点赞数和评论数的极值点的出现，在时间线上高度接近。



## 数据分析及可视化

### 评论区热图

核心代码如下：

```python
yuntu_data = pd.DataFrame({'user_id':comment['user_id'],'点赞数':comment['点赞数'],'评论数':comment['评论数'],'转发数':comment['转发数']})
correlations = yuntu_data.corr()
sns.heatmap(correlations)
plt.show()
```

评论区热图的绘制图如下

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212011752934.png)



我们可以很快看到一些相关性：

1. 点赞数与转发数呈强正相关。
2. 点赞数与评论数之间存在强正相关。
3. 评论数与转发数之间存在轻微正相关。

有了这些信息，可以做一些观察。

1. 点赞数和评论数，转发数都强正相关，微博平台似乎会根据评论数，转发数来选择热门评论，这是一个有待探索的假设。
2. 具体的某个用户不会对该话题下的评论数、点赞数、转发数，两两之间构成联系。



### 评论云图

核心代码如下：

```python
file_name = "/Environment/data.csv"
with open(file_name, 'r', encoding='utf-8') as f:
    word_list = jieba.cut(f.read())
    result = " ".join(word_list)  # 分词用 隔开
    # 制作中文云词
    gen_stylecloud(text=result,
                   font_path='C:\\Windows\\Fonts\\simhei.ttf',
                   output_name='D:\Comment.png',
                   icon_name='fas fa-bell'
                   )  # 必须加中文字体，否则格式错误
```

评论云图的绘制图如下

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212031913862.png)

从传播学角度研究，网络媒体有丰富的符号化表达方式，评论大致可分为文字类和非文字类符号，收集分析数据后，发现关键词大部分为文字类的话题符号。话题符号有其独特语境，在语音、文字和语义方面不同于其他网络语言。可见话题时效性较高且表现稳定，主题相似度偏低。其中最受大家喜爱的是卡塔尔世界杯话题。



## 网络文本挖掘

### 情感分析

中文并不像英文那样词与词之间用空格隔开，因此中文分词词性标注往往是中文自然语言处理的第一步。一个好的分词系统是有效进行中文相关数据分析和产品开发的重要保证。BosonNLP 情感字典是基于微博、新闻、论坛等数据来源构建的词典，因此拿来对微博进行分析效果较好。在分词与词性标注中，新词识别与组合切分歧义是两个核心挑战。jieba分词 在这方面做了不少的优化，包括对特殊字符的处理，对比较有规律的构词方式的特征捕捉等。它通过使用在大规模无标注数据上的统计数据来改善有监督学习中的标注结果，也在我们的分词实现上有所应用。

核心代码：

```python
# 分类结果，词语的index作为key,词语的分值作为value，否定词分值设为-1
sen_word = dict()
not_word = dict()
degree_word = dict()
for word in sentence_dict.keys():
    if word in sentiment_dist.keys() and word not in neg_words and word not in degree_dic.keys():
        # 找出分词结果中在情感字典中的词
        sen_word[sentence_dict[word]] = sentiment_dist[word]
    elif word in neg_words and word not in degree_dic.keys():
        # 分词结果中在否定词列表中的词
        not_word[sentence_dict[word]] = -1
    elif word in degree_dic.keys():
        # 分词结果中在程度副词中的词
        degree_word[sentence_dict[word]] = degree_dic[word]
```

我尝试找出文档中的情感词、否定词以及程度副词，然后判断每个情感词之前是否有否定词及程度副词，将它之前的否定词和程度副词划分为一个组，如果有否定词将情感词的情感权值乘以-1，如果有程度副词就乘以程度副词的程度值，最后所有组的得分加起来，大于0的归于正向，小于0的归于负向。正向情感得分前三的评论如下：

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212021614530.png)

分析收集到的评论数据发现，信息有用性在不同程度上取决于个人的主观认知。评论信息中传递的大都是用户的经验与感受。



### TF-IDF

TF-IDF 用以评估字词对于一个文件集或一个语料库中的其中一份文件的重要程度。字词的重要性随着它在文件中出现的次数成正比增加，但同时会随着它在语料库中出现的频率成反比下降。TF-IDF 通过词频统计的方法得到某个词对一篇文档的重要性大小（没有考虑语义信息）。



**算法步骤如下：**

1. 切分词条
2. 总词频统计，即计算一共有多少词。计算每个词的词频即TF值：出现次数/总次数
3. 计算逆文档频率 IDF：Log(语料库的文档总数/（包含该词的文档数+1）)，IDF大概为丑化因子，用来区别在多少文档出现，权重小即区分度大。我在数值中已经做丑化，所以直接相乘。
4. 计算每个词的 tf * idf
5. 提取特征，需要先对字典由大到小排序，得到结果



核心代码如下：

```python
# 获取数据集
data = readwords_list("/Environment/data.csv")
test_list = []
for i in data:
    # 分词
    test_list.append(cut_word(i))
    # 特征提取
    # 实例化转换器
    transfer = TfidfVectorizer()
    new_data = transfer.fit_transform(test_list)
    names = transfer.get_feature_names_out()
    print('特征名称\n', names)
    print(new_data.toarray())
```

计算的得分如下。

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212021742628.png)





### K-Means模型

聚类是一个将数据集中在某些方面相似的数据成员进行分类组织的过程，聚类就是一种发现这种内在结构的技术，聚类技术经常被称为无监督学习。k均值聚类是最著名的划分聚类算法，由于简洁和效率使得他成为所有聚类算法中最广泛使用的。给定一个数据点集合和需要的聚类数目k，k由用户指定，k均值算法根据某个距离函数反复把数据分入k个聚类中。



**常用聚类算法对比**

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212031756128.png)



**K-Means 通常被称为劳埃德算法，算法有三个步骤**

1. 先随机选取K个对象作为初始质心的聚类中心，最基本的方法是从 X 数据集中选择k个样本。初始化完成后，K-Means 由两个其他步骤之间的循环组成。 
2. 计算每个样本与最近的质心之间的距离，把每个对象分配给距离它最近的聚类中心。
3. 通过取分配给每个先前质心的所有样本的平均值来创建新的质心。计算旧的和新的质心之间的差异，并且算法重复这些最后的两个步骤，直到该值小于阈值。算法重复这个步骤，直到质心不再显著移动，或没有（或最小数目）对象被重新分配给不同的聚类，或误差平方和局部最小。



**KNN 与 K-Means 的区别**

+ K近邻算法是有监督学习，属于分类算法。K均值算法是无监督学习，属于聚类算法。
+ K近邻算法是找与数据最近的K个点，如果多数属于某类，则归为该类，达到分类的效果。K均值算法是将所有数据归到距其最近的中心点，并不断迭代中心点以达到聚类的目的。



**安装**

cmd 指令 `pip install scikit-learn`

安装之前需要numpy和scipy库



核心代码如下：

```python
# 进行kmeans聚类。先聚4类
julei=KMeans(n_clusters=4) 
julei.fit(data)
# 获得聚类标签，即获得每个数据对应的每一类
label=julei.labels_ 
print(label)
# 获得聚类中心
center=julei.cluster_centers_
print(center)
```



获得的聚类标签和聚类中心如下。

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212031804755.png)



### 有效性评价

**有效性评价标准**

聚类算法属于无监督学习方法，不同的聚类数对聚类结果影响很大。所以需要进行聚类有效性评价。聚类评价指标比较多，常用的有：Rand指数、轮廓系数（Silhouette Coefficient）、Calinski-Harabaz 指数等等。



**轮廓系数进行聚类评价**

轮廓系数处于-1至1，越大表示簇间相似度高而不同簇相似度低，即聚类效果越好。

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212031808005.png)



### 模型优化

用不同的超参数找出最佳聚类数。

核心代码：

```py
def juleipingjia(n):
    # 计算每一个聚类下的轮廓系数
    julei=KMeans(n_clusters=n)
    julei.fit(data)
    label=julei.labels_
    lkxs=silhouette_samples(data,label,metric='euclidean')
    means=np.mean(lkxs)
    return means
```

不同的超参数下模型得分如下。

![](https://umrcoding.oss-cn-shanghai.aliyuncs.com/Obsidian/202212031810714.png)





## 实验结果分析

采集微博数据的方式主要通过微博公开的 api 和爬虫程序，采集到数据后需要对数据进行预处理操作，如分词、去停用词和句法分析等。对预处理后的数据进行情感分析的方法用了基于情感词典的方法。经过统计发现，点赞数与评论数，转发数呈强正相关，特殊用户不会对世界杯话题下的评论数、点赞数、转发数，两两构成强联系。遇到热门比赛时，在观看人数基数陡增的背景下，有较多数量的用户也进行了发帖，这时会伴随着评论数，点赞数，转发数的飙升。一篇帖子的标签数使用数也常小于三次。他们发帖首先会带有卡塔尔世界杯标签，多数用户还会选择一到两个自己喜欢的标签。大多数人会根据内容自己选择或创建适合自己标签，虽然话题标签的使用也比较分化，但是很多个话题标签都是针对同一件事。每个热门赛事都会有特有的话题出现。在世界杯中，微博的艾特数都非常非常少。还有大部分评论文本长度为 `20-50` 个字左右，用户倾向于发表完整的文字的感受或想法，更注重信息内容本身。不到10%的人对于评论表达的规范性和完整度不太关注。从传播学角度研究，网络媒体有丰富的符号化表达方式，收集分析数据后，发现关键词大部分为话题符号。如果打算使用这些数据来建立一个模型，那么最好在将其分解或者对其进行随机化。这是我们可以探索的另一个假设。

 

## 总结

为了监督和引导微博舆论，对微博内容进行情感分析是非常必要的。相关性有助于探索新的数据集，例如使用`seaborn`的热图，在很短时间就可以看到输入数据的相关性，并得到想法来探索问题，比较容易看到最强的相关性在哪里。本实验尚有许多值得改进的地方。例如评论区的分析中，文本字数占据实验重要贡献度，但是其他带有感情的特征项无法做到效果好的有用性检测，未能涵盖文本语言上的特征。在全面性上也有进一步提高的空间。用了 tf-idf 计算，情感得分统计，搭建情感聚类模型，对情感文本与含义进行了更深层次挖掘。如果要进行深度分析，应该再将原始数据分解或者对其进行随机化。并且在做聚类的时候对原始数据进行归一化，避免不同纲量对结果的影响，当我得到的聚类中心是利用归一化数据得到的聚类中心，那么在我后续的数据处理中需要对数据中心进行操作，应该需要对数据中心进行反归一化。虽然归一不归一影响不大。如果是别的方面的应用，还要进行下一步计算，那是需要反归一化的。



## 参考文献

<span name = "ref1">[1] 安璐. 融合主题与情感特征的突发事件微博舆情演化分析[Z].  </span>

<span name = "ref2">[2] 康伟. 突发事件舆情传播的社会网络结构测度与分析——基于“11·16校车事故”的实证研究[Z]. </span>

<span name = "ref3">[3] 黄晓斌. 文本挖掘在网络舆情信息分析中的应用[Z]. </span>

<span name = "ref4">[4] 曾润喜. 我国网络舆情研究与发展现状分析[Z]. </span>

<span name = "ref1">[5] 刘春波. 舆论引导论[Z]. </span>

<span name = "ref6">[6] 刘建明.社会舆论原理，北京： 华夏出版社. 2012年第6页 [Z]. </span>

<span name = "ref7">[7] 陈力丹.舆论学 — 舆论导向研究，北京：中国广播电视出版社. 1999年版. 第22-23页  [Z]. </span>

<span name = "ref8">[8] 叶暗.政府在突发事件处置中的舆论引导，《现代传播》. 2007年第4期. 第4页[Z]. </span>

<span name = "ref9">[9] 《十三大以来重要文献选编》（中册），北京：人民出版社年版，第—页 [Z].  </span>



