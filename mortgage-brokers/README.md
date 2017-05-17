# Scraping 
This is the script for scraping data from [Mortgage Brokers](http://mortgage-brokers.credio.com/) website.

## Development
0. Install [Selenium](http://www.seleniumhq.org/)

   Ensure you have chrome
   
   Download [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

0. Install required packages

    ``` bash
    $ pip install selenium
    $ pip install beautifulsoup4
    ```

0. Clone and `cd` into the `web-scraping` repository

    ``` bash
    $ git clone git@github.com:zhengyu92/web-scraping.git
    $ cd web-scraping
    ```

0. Setup and run

    ``` bash
    $ python scraping-mortgage-brokers.py
    ```
    
0. Try it out using [Jupyter notebook](http://jupyter.org/)
