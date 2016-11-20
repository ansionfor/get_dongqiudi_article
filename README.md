# get_dongqiudi_article
使用python3配合requests、re、time、mysql、bs4等库，对懂球帝的文章进行有条件爬取，并存进远程mysql数据库中

程序详解：

#获得列表前n篇文章id
def get_list():
    url = 'http://m.dongqiudi.com/api/mobile/tab/1/archives'
    list = requests.get(url)
    return list.json()['list']['articles']
