# get_dongqiudi_article
使用python3配合requests、re、time、mysql、bs4等库，对懂球帝的文章进行有条件爬取，并存进远程mysql数据库中

程序详解：
采集懂球帝头条文章
存进mysql数据库
使用linux中的crontab每天定时执行

获得列表前n篇文章id
def get_list():

查找数据库文章aid是否已经存在，不存在返回None
def check_id(aid):

下载文章封面图片
def download_pic(url):

根据id获取文章内容
def get_content(url):

正则截取文章aid
def get_aid(x):
