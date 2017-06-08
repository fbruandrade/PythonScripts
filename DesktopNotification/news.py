#!/usr/bin/python3
import feedparser
import notify2
import time
import os

def ParseFeed():
    # You can choose what is the best RSS feed for you to follow
    f = feedparser.parse('http://rss.home.uol.com.br/index.xml')

    ICON_PATH = os.getcwd() + '/icon.ico'
    notify2.init("News Notify")
    # For each post in feed
    for newsitem in f['items']:
        msg = newsitem['summary']+"\n"+newsitem['link']
        n = notify2.Notification(newsitem['title'],
                                 msg,
                                 icon=ICON_PATH)
        # Define the Item to show in Desltop Notification
        notify2.Notification(newsitem)
        # Set the urgency
        n.set_urgency(notify2.URGENCY_NORMAL)
        # Show the Notification
        n.show()
        # Set 15 seconds to stay alive the popup notification
        n.set_timeout(15000)
        # Go to sleep
        time.sleep(1200)

if __name__ == '__main__':
    ParseFeed()