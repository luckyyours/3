import requests
from bs4 import BeautifulSoup
import pymysql
import lxml
def get_movies():
    # headers={
    #     'user-agent':'Mozilla/5.0 (windows NT 6.1；Win64;x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/52.0.2743.82 Safari/537.36',
    # 'Host':'movie.douban.com'
    # }
    movie_list=[]
    for i in range(0,10):
        link='https://movie.douban.com/top250?start='+str(i*25)+'&filter='
        aa=[]


        r=requests.get(link,timeout=10)
        # print(str(i+1),"页响应状态码：",r.status_code)
        soup=BeautifulSoup(r.text,"lxml")
        div_list=soup.find_all('div',class_='hd')

        for each in div_list:
            movie=each.a.span.text.strip()
            movie_list.append(movie)



    return movie_list
l=get_movies()
conn = pymysql.connect(host='localhost', user='root', password='123456', db='data', charset="utf8")
for i in range(len(l)):

            cur = conn.cursor()
            sql = "insert into app2_book(neirong)values('{0}')".format(l[i])
            cur.execute(sql)

            conn.commit()

            cur.close()
conn.close()


