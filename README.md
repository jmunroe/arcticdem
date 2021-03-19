# arcticdem

Python script scrapes the Apache directory listing at

[http://data.pgc.umn.edu/elev/dem/setsm/ArcticDEM/mosaic/v3.0/2m/](http://data.pgc.umn.edu/elev/dem/setsm/ArcticDEM/mosaic/v3.0/2m/)

to create a text file `urls.txt` with each line contain the full URL to each tile.

Uses the python packages requests and  bs4 (BeautifulSoup).

It takes about 6 mins to run the script to the output `urls.txt` has also been included in this repo.
