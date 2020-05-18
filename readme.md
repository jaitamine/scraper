# Project

This is a web scraper project based on the Scrapy framework. The bbc news website articles are the resources being scraped and persisted in a local mongodb database. Alongside the scraper, there is a flask web api that fetches the articles based on keyword search by the user.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Installing

A step by step series of examples that tell you how to get a development env running. These steps are for windows. platform.

Navigate to your workspace directory.

Create a virtual environment
```
py -m virtualenv venv
```

Install all requirements for app.

```
Scripts\activate
pip install -r requirements.txt
```



### Run the scraper

Navigate to webScraper directory and run the following command:

```
scrapy crawl bbc
```

### Run the flask app

Navigate to searchApi directory and run the following command:

```
flask run
```


## Acknowledgments

* Thanks to https://github.com/TaiwanStat/Taiwan-news-crawlers for the generator methods in the web crawler.
* Thanks to https://github.com/nfaihi/bbc-crawler for the web api  search by keyword method.