#!/usr/bin/env python3

import psycopg2


# defining database connection
def main():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    popular_articles(cursor)
    popular_authors(cursor)
    error_rates(cursor)
    db.close()


# defining popular_articles
def popular_articles(cursor):
    query = "SELECT a.title, s.count FROM articles a, slug_path s "
    query += "WHERE a.slug = s.slug ORDER BY s.count DESC limit 3"
    cursor.execute(query)
    q_result = cursor.fetchall()
    print("\nTop three articles of all?\n")
    for row in q_result:
        print('%s' % (row[0]), '--', row[1], 'views')


# defining popular_authors
def popular_authors(cursor):
    query = "SELECT a.name, sum(s.count) FROM slug_path s, authors a"
    query += " WHERE s.author = a.id GROUP BY a.name ORDER BY sum DESC"
    cursor.execute(query)
    q_result = cursor.fetchall()
    print("\nPopular Articles?\n")
    for row in q_result:
        print(row[0], '--', row[1], 'views')


# defining error_rates > 1%
def error_rates(cursor):
    query = "SELECT date, round(percent,2) FROM error_rates WHERE percent > 1"
    cursor.execute(query)
    q_result = cursor.fetchall()
    print("\nErrors were Over 1 percent during?\n")
    for row in q_result:
        print(row[0], '--', "{0}%".format(row[1]), "errors")


if __name__ == "__main__":
    main()
