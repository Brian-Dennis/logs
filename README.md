## Synopsis

This project is for the Udacity Full Stack Web Developer Nanodegree program. It is a log analysis project that is meant to query a database giving the results of top authors, top articles and highest request errors. It is made with python using psycopg2.

## Installation

To install this all you have to do is clone this repository via ```git clone https://github.com/Brian-Dennis/logs``` or download the zip file of this repo. You will also need virtualbox from https://www.virtualbox.org/wiki/Downloads, and make sure you have the Udacity fullstack-nanodegree-vm provided in this repo https://github.com/udacity/fullstack-nanodegree-vm. after that you need to pull up a terminal window and go to the vagrant directory and run ```vagrant up``` then after that run ```vagrant ssh``` upon that finishing you mush ```cd vagrant/``` then to open the database you need to run ```psql news``` then hit enter and this should render a ```news=>``` prompt.

## SQL CREATE VIEWS

Once you have the vagrant opened in the terminal you are going to want to run ```psql news``` then to create the views and run the queries against the database you are going to want to copy and paste or type yourself in the terminal these commands:
```create or replace view slug_path as select a.slug, a.author, count(a.slug) from articles a, log l where l.path = concat ('/article/',a.slug) group by a.slug, a.author;``` then press enter.

```create view status_table as select date(time), count(l.status) as status_count from log l where l.status = '200 OK' group by date(time);``` then press enter.

```create view error_table as select date(time), count(l.status) as error_count from log l where l.status != '200 OK' group by date(time);``` then press enter.

```create view error_rates as select s.date, (sum(e.error_count)/(sum(s.status_count) + sum(e.error_count))) * 100.0 as percent from error_table e, status_table s where s.date = e.date group by s.date;``` then press enter.

## To get Results

run ```python logs.py``` or for a better rendering view run ```python3 logs.py```

## Credits

I used this site as a reference to see the functions in action.

W3schools Create Views - https://www.w3schools.com/sql/sql_view.asp demonstrates how to ```create views```<br>
W3schools count function - https://www.w3schools.com/sql/func_mysql_count.asp demonstrates the ```count``` function<br>
W3schools sum function - https://www.w3schools.com/sql/func_mysql_sum.asp demonstrates the ```sum``` function<br>
W3schools date function - https://www.w3schools.com/sql/func_mysql_date.asp demonstrates the <code>date</code> function<br>

I also used https://www.generatedata.com/ to generate some similar mock data to the project and imported the file into pgadmin4 to then test my queries with a GUI.

That brings me to my next tool that I used which was pgadmin 4 https://www.pgadmin.org/
