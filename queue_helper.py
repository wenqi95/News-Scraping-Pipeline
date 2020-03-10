from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = ""
SCRAPE_NEWS_TASK_QUEUE_NAME = "NEWS_TASK_QUEUE"

def clearQueue(queue_url, queue_name):
    scrape_news_queue_client = CloudAMQPClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        if scrape_news_queue_client is not None:
            msg = scrape_news_queue_client.getMessage()
            if msg is None:
                print("Cleared %d messages." % num_of_messages)
                return
            num_of_messages += 1


if __name__ == "__main__":
    clearQueue(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)