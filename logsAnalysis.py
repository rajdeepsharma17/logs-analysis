#!/usr/bin/python
# # -*- coding: utf-8 -*-
import psycopg2


def popularArticle(cur):
    """
    This method prints list of most
    popular articles from log database.
    Args:
        cur: Cursor Object of connected database
    Returns:
        void
    """
    popular_articles = '''select title, res2.count from (
        select path, count(path) from (
            select * from log where status = '200 OK' and path != '/'
            ) as tab
            group by path order by count(path) desc limit 3
        ) as res2
        join articles on res2.path like '%' || slug || '%' order by
        res2.count desc;'''
    cur.execute(popular_articles)
    for (title, count) in cur.fetchall():
        print("    {} - {} views".format(title, count))
    print("-" * 70)


def popularAuthor(cur):
    """
    This method prints most popular
    article authors from all time.
    Args:
        cur: Cursor Object of connected database
    Returns:
        void
    """
    popular_authors = '''select name, sum(res3.count) as num
    from (select author, res2.count from (
        select path, count(path) from (
            select * from log where status = '200 OK' and path != '/'
            ) as tab
            group by path
        ) as res2
        join articles on res2.path like '%' || slug || '%') as res3
        join authors on res3.author = authors.id
        group by name order by num desc;'''
    cur.execute(popular_authors)
    for (name, count) in cur.fetchall():
        print("    {} - {} views".format(name, count))
    print("-" * 70)


def errorPercent(cur):
    """
    This method prints days on which 404 request percent
    is more than 1%.
    Args:
        cur: Cursor Object of connected database
    Returns:
        void
    """
    error_percent = '''select res.day, (res.failed::decimal/res.total)*100
        as error from (
        select a.day, a.count as failed, b.count as total from (
            select time::date as day, count(status) from log group by day
            ) as b join (
            select time::date as day, count(status) from log
            group by day, status having status != '200 OK'
            ) as a on a.day = b.day
        ) as res where (res.failed::decimal/res.total)*100 > 1;'''
    cur.execute(error_percent)
    for (date, percent) in cur.fetchall():
        print("    {} - {} percent".format(date, round(percent, 2)))
    print("-" * 70)


if __name__ == '__main__':
    try:
        db = psycopg2.connect(database="news")
        cur = db.cursor()
        print("> The most popular articles are as follows:\n")
        popularArticle(cur)
        print("> Authors Poularity: \n")
        popularAuthor(cur)
        print("> Failed requests more than 1 percent on following days:\n")
        errorPercent(cur)
        db.close()
    except psycopg2.DatabaseError, e:
        print("Something went wrong")
