import csv
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import jieba

def cut_word(text):
    text = " ".join(list(jieba.cut(text)))
    return text

def readwords_list(filepath):
    '''
    读取文件函数，以行的形式读取词表，返回列表
    :param filepath: 路径地址
    :return:
    '''
    data_list = []
    try:
        # 字典
        with open(filepath, 'r', encoding='utf-8-sig') as fp:
            reader = csv.DictReader(fp)
            for item in reader:
                item = item['微博正文']
                # item = re.findall('.*?([\u4e00-\u9fa5]+).*', item)[0]
                data_list.append(item)
    except Exception as e:
        print("\033[1;31m文件读取出错:\033[0m" + filepath)
        print(e)
    return data_list

def tf_idf():
    # 获取数据集
    data = readwords_list("../Environment/data.csv")

    # 文章分割，即分词
    test_list = []
    for i in data:
        test_list.append(cut_word(i))
    print('分词\n',test_list)

    # 特征提取
    # 实例化转换器
    transfer = TfidfVectorizer()
    new_data = transfer.fit_transform(test_list)

    names = transfer.get_feature_names_out()

    print('特征名称\n', names)
    print(new_data.toarray())

if __name__ == '__main__':
    tf_idf()