import psycopg2

def popularArticle(cur):
    cur.execute('''select title, res2.count from (
        select path, count(path) from (
            select * from log where status = '200 OK' and path != '/'
            ) as tab 
            group by path order by count(path) desc limit 3
        ) as res2 
        join articles on res2.path like '%' || slug || '%' order by res2.count desc;''')
    posts = cur.fetchall()
    for i in range(len(posts)):
        print posts[i][0], "-", posts[i][1], "views"
    print

def popularAuthor(cur):
    cur.execute('''select name, sum(res3.count) as num from (select author, res2.count from (
        select path, count(path) from (
            select * from log where status = '200 OK' and path != '/'
            ) as tab 
            group by path
        ) as res2 
        join articles on res2.path like '%' || slug || '%') as res3 join authors on res3.author = authors.id group by name order by num desc;''')
    posts = cur.fetchall()
    for i in range(len(posts)):
        print posts[i][0], "-", posts[i][1]
    print

def errorPercent(cur):
    cur.execute('''select res.day, (res.failed::decimal/res.total)*100 as error from (
        select a.day, a.count as failed, b.count as total from (
            select time::date as day, count(status) from log group by day
            ) as b join (
            select time::date as day, count(status) from log group by day, status having status != '200 OK'
            ) as a on a.day = b.day
        ) as res where (res.failed::decimal/res.total)*100 > 1;''')
    posts = cur.fetchall()
    for i in range(len(posts)):
        print posts[i][0], "-", round(posts[i][1],2),"%"

if __name__ == '__main__':
    db = psycopg2.connect(database="news")
    cur = db.cursor()
    print("> The most popular articles are as follows:\n")
    popularArticle(cur)
    print("> Authors Poularity: \n")
    popularAuthor(cur)
    print("> Failed requests more than 1 percent of total request on followiing days:\n")
    errorPercent(cur)
    db.close()

