# Scraping 
This is the code for scraping data from [SIOR](http://www.sior.com/find-an-sior-member/find-an-individual-member/?search=4A1BE1CD-C83B-CA98-B2D7-9D082F5F7F91) website.

## Development
0. Install [Selenium](http://www.seleniumhq.org/)

   Ensure you have chrome
   
   Download [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   
0. Install required packages

    ``` bash
    $ pip install selenium
    $ pip install regex
    $ pip install pandas
    $ pip install beautifulsoup4
    ```

0. Clone and `cd` into the `web-scraping` repository

    ``` bash
    $ git clone git@github.com:zhengyu92/web-scraping.git
    $ cd web-scraping
    ```

0. Setup and run

    ``` bash
    $ python scraping-sior.py
    ```
    
0. Try it out using [Jupyter notebook](http://jupyter.org/)
