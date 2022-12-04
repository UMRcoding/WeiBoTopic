# -*- coding: utf-8 -*-
BOT_NAME = 'weibo'
SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
LOG_LEVEL = 'ERROR'

# DOWNLOAD_DELAY代表访问完一个页面再访问下一个时需要等待的时间，默认为10秒。
DOWNLOAD_DELAY = 6

DEFAULT_REQUEST_HEADERS = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cookie': ' '
}

### 设置结果保存类型（可选）
# 第一个代表去重
# 第二个代表写入csv文件
# 第三个代表写入MySQL数据库
# 第四个代表写入MongDB数据库
# 第五个代表下载图片
# 第六个代表下载视频
# 后面的数字代表执行的顺序，数字越小优先级越高。
# 如果你只要写入部分类型，可以把不需要的类型用“#”注释掉，以节省资源
ITEM_PIPELINES = {
    'weibo.pipelines.DuplicatesPipeline': 300,
    'weibo.pipelines.CsvPipeline': 301,
    # 'weibo.pipelines.MysqlPipeline': 302,
    # 'weibo.pipelines.MongoPipeline': 303,
    # 'weibo.pipelines.MyImagesPipeline': 304,
    # 'weibo.pipelines.MyVideoPipeline': 305
}

# KEYWORD_LIST = ['单个关键词']
# KEYWORD_LIST = ['多关键词01', '多关键词02']
# KEYWORD_LIST = ['同时包含关键词01 同时包含关键词02']
# KEYWORD_LIST = ['#话题#']
# KEYWORD_LIST = 'keyword_list.txt'  # txt文件中每个关键词占一行。
KEYWORD_LIST = ['#卡塔尔世界杯#']

# 设置要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博
WEIBO_TYPE = 0

### 设置包含内容（可选）
# 筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博
CONTAIN_TYPE = 0

# 筛选微博的发布地区，精确到省或直辖市，值不应包含“省”或“市”等字，如想筛选北京市的微博请用“北京”而不是“北京市”，想要筛选安徽省的微博请用“安徽”而不是“安徽省”，可以写多个地区
# 具体支持的地名见region.py文件，注意只支持省或直辖市的名字，省下面的市名及直辖市下面的区县名不支持，不筛选请用“全部”
REGION = ['全部']

# 程序会搜索包含关键词且发布时间在起始日期和结束日期之间的微博
# 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含边界
START_DATE = '2022-11-23'
# 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含边界
END_DATE = '2022-11-23'

# 程序是否进一步搜索的阈值。
# 如果在某个搜索条件下，搜索结果很多，则搜索结果应该有50页微博，多于50页不显示。
# 当总页数等于50时，程序认为搜索结果可能没有显示完全，所以会继续细分。
# 比如，若当前是按天搜索的，程序会把当前的1个搜索分成24个搜索，每个搜索条件粒度是小时。
# 这样就能获取在天粒度下无法获取完全的微博。同理，如果小时粒度下总页数仍然是50，会继续细分，以此类推。
# 然而，有一些关键词，搜索结果即便很多，也只显示40多页。
# 所以此时如果FURTHER_THRESHOLD是50，程序会认为只有这么多微博，不再继续细分，导致很多微博没有获取。
# 因此为了获取更多微博，FURTHER_THRESHOLD应该是小于50的数字。
# 但是如果设置的特别小，如1，这样即便结果真的只有几页，程序也会细分，这些没有必要的细分会使程序速度降低。
# 因此，建议 FURTHER_THRESHOLD的值设置在40与46之间
# 若结果页数大于等于该值，则认为结果没有完全展示，细分搜索条件重新搜索以获取更多微博。
# 数值越大速度越快，也越有可能漏掉微博；数值越小速度越慢，获取的微博就越多。
FURTHER_THRESHOLD = 40

# 图片文件存储路径
IMAGES_STORE = './'

# 视频文件存储路径
FILES_STORE = './'

# 配置MongoDB数据库
# MONGO_URI = 'localhost'

# 配置MySQL数据库，以下为默认配置，可以根据实际情况更改，程序会自动生成一个名为weibo的数据库，如果想换其它名字请更改MYSQL_DATABASE值
# MYSQL_HOST = 'localhost'
# MYSQL_PORT = 3306
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = '123456'
# MYSQL_DATABASE = 'weibo'
