# Logs Analysis

Logs Analysis is  a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool
is a Python program using the **psycopg2** module to connect to the database.

## QuickStart

This project assumes you have `psycopg2` library and `news` database installed.
<ol>
<li> If not, follow along otherwise skip to step 2.
<ul>
<li> Install psycopg2 using <code>$ pip install psycopg2</code>
<li> Download data for news database
    <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">here</a>
<li>Extract newsdata.sql and cd into that directory in terminal.
<li> Run following command in terminal <code>$ psql -d news -f newsdata.sql</code>
</ul>
<li> Open the Logs Analsis folder containing logsAnalysis.py in terminal.
<li> Run the following command to obtain required results: <br> <code>$ python logsAnalysis.py</code>
</ol>

## Example

`$ python logsAnalysis.py`

> The most popular articles are as follows:
<ul>
<li>Candidate is jerk, alleges rival - 338647 views
<li>Bears love berries, alleges bear - 253801 views
<li>Bad things gone, say good people - 170098 views
</ul>

> Authors Poularity: 
<ul>
<li>Ursula La Multa - 507594
<li>Rudolf von Treppenwitz - 423457
<li>Anonymous Contributor - 170098
<li>Markoff Chaney - 84557
</ul>

> Failed requests more than 1 percent of total request on following days:
<ul>
<li>2016-07-17 - 2.26%
</ul>
