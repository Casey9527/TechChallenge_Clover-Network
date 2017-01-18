#Technical Challenge from Clover Network
## Challenge
James Bond might be a super hero... to find out, determine if and when any particular super hero series will release more movies.

To complete the challenge: Write a program that queries the IMDB API for movie release dates of James Bond movies and compares the release dates to other super hero series. Determine if any super hero series has surpassed the movie release velocity of the James Bond franchise. You're free to use any keywords to define a super hero... for example... 'Batman', 'Superman', 'Fantastic Four'... etc.
Give us a short write up on how you arrived at your results.

For example: You can average the time between James Bond movie releases, and Batman movie releases and compare. If Batman movies have a shorter release cycle, on average, but fewer films in terms of quantity, project when Batman will surpass James Bond.

What we're looking for: We are looking at how you write code, use web services and manage data within your program. The program can be an app, a script, almost anything so long as we can run it and you can justify the results. Don't worry so much about output presentation.


## Solution
wrote a python script to do the task.
* First step: grab data from IMDB database
I query an API provided by MyAPIFilms (http://www.myapifilms.com). urllib2, and json package are used to open the url, load the data in json format from the site.
* Second step: data processing
For each movie series, I create a list to store dictionaries. Each dictionary stores information of each movie. It looks like {‘title’: title, ‘release_date’ : release_date }. The list looks like [{movie1}, {movie2}, ..]. Next I convert the release date from string format like “year-month-day” to datetime type. Note that if release_date field is missing, I assign it a default datetime “1910-01-01”, which is meaningless. Finally I sorted the list based on datetime value in each element in descending order. These process lie in function search_imdb_by_name().

* Third Step: compare algorithm
In function get_release_velocity(), it get each list we obtain in last step. It also get begin year and end year from main function. Then it iterates every movie in the list, compare if it is released between the begin year and end year. If so, increase the counter. Finally, return the counter. The main function is to parse command line parameters, and call related function, then output comparison results.

## Usage
``` python
python imdb.py <movie_series_1> <movie_series_2> begin_year end_year
e.g.
python imdb.py "batman" "james bond" 2008 2010
```
## Sample Output
Movie Name | release date 
--- | ---
The Batman | 2018-10-05 00:00:00
The Lego Batman Movie | 2017-02-08 00:00:00
Batman: Dante | 2016-08-05 00:00:00
Batman: The Killing Joke | 2016-07-24 00:00:00
Batman v Superman: Dawn of Justice | 2016-03-23 00:00:00
Batman: Bad Blood | 2016-03-22 00:00:00
Batman vs. Robin | 2015-04-14 00:00:00
Batman: Assault on Arkham | 2014-08-12 00:00:00
Batman: The Dark Knight Returns, Part 2 | 2013-01-18 00:00:00
Batman: Year One | 2011-09-27 00:00:00
Superman/Batman: Public Enemies | 2009-09-29 00:00:00
Batman: Beyond Batman|2005-07-04 00:00:00
Batman Begins|2005-06-14 00:00:00
Batman & Robin|1997-06-20 00:00:00
Batman Forever|1995-05-31 00:00:00
Batman Returns|1992-06-19 00:00:00
Batman|1989-06-23 00:00:00
James Batman|1966-10-26 00:00:00
Batman|1966-07-30 00:00:00
Batman|1943-07-16 00:00:00
****************************************************************************************************

Movie Name | release date 
--- | ---
James Bond is a Serb|2016-01-06 00:00:00
Spectre|2015-10-26 00:00:00
James Bond |2015-07-24 00:00:00
Jatt James Bond|2014-04-25 00:00:00
We're Nothing Like James Bond|2012-11-29 00:00:00
Skyfall|2012-10-25 00:00:00
James Bond: For Real|2006-11-22 00:00:00
Casino Royale|2006-11-14 00:00:00
Best Ever Bond|2002-11-22 00:00:00
Silhouettes: The James Bond Titles|2000-07-25 00:00:00
The James Bond Story|1999-10-09 00:00:00
GoldenEye|1995-11-16 00:00:00
30 Years of James Bond|1992-10-03 00:00:00
Octopussy|1983-06-05 00:00:00
James Bond In India|1983-01-25 00:00:00
Goldfinger|1964-09-17 00:00:00
Dr. No |1962-10-04 00:00:00
James Bond 25|1910-01-01 00:00:00
james bond 777|1910-01-01 00:00:00
James Bond: License to Thrill|1910-01-01 00:00:00
****************************************************************************************************


batman has released <1> movies from 2008 to 2010.

james bond has released <0> movies from 2008 to 2010.

batman is the more popular than james bond.



