# get_dongqiudi_article
使用python3配合requests、re、time、mysql、bs4等库，对懂球帝的文章进行有条件爬取，并存进远程mysql数据库中

#程序详解：
##1.采集懂球帝头条文章
##2.存进mysql数据库
##3.使用linux中的crontab每天定时执行


###获得列表前n篇文章id
    def get_list():
        url = 'http://m.dongqiudi.com/api/mobile/tab/1/archives'
        list = requests.get(url)
        return list.json()['list']['articles']
        
###查找数据库文章aid是否已经存在，不存在返回None
    def check_id(aid):
        cur.execute("select sort from article where sort="+(aid))
        return cur.fetchone()
        
###下载文章封面图片
    def download_pic(url):

###根据id获取文章内容
    def get_content(url):
        content = requests.get(url).text
        soup = bfs(content, 'html.parser')
        title = soup.title.string
        author = soup.writer
        if (author == None):
            author = ''
        else:
            author = author.string
        time_1 = time.mktime(time.strptime(soup.time.string, '%Y-%m-%d %H:%M:%S'))
        content = soup.find('div', {'class':'con'})
        photo = soup.article.img
        if(photo == None):
            photo = ''
        else:
            photo = photo.get('src')
        data = [str(title), str(title), str(author), float(time_1), str(content), photo,2]
        return data
        
###正则截取文章aid
    def get_aid(x):
        return str(re.search(r'[0-9]{6,8}', str(x)).group())

###使用crontab定时采集
详细请看博客文章[Ansion 博客](http://ansion.cc/index.php/article/page/id/341.html) 
