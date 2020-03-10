## News Scraping Pipeline
Implemented a data pipeline with Python to monitor, scrapes and dedupes online news (with MongoDB, Redis, RabbitMQ);
# News Monitor: Use News API to get the lastest news URL
# Redis: Save collected news, and solve duplicated problem
# RabbitMQ: Receive news URL from News Monitor and send it to News Scrapers
# News Scrapers: Receive news URL from RabbitMQ and scrape the content from the website
# RabbitMQ: Receive news from News Scrapers
# News Deduper: Receive the scraped news from RabbitMQ and filter the similar contents using NLP-TFIDF
