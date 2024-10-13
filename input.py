import json

import feedparser

RSS_FEEDS = {
    "tech": [
        "https://feeds.arstechnica.com/arstechnica/technology-lab",
        "https://www.wired.com/feed/rss",
        "https://www.theverge.com/rss/index.xml"
    ],
    "business": [
        "https://www.cnbc.com/id/19746125/device/rss/rss.xml",
        "https://feeds.marketwatch.com/marketwatch/topstories/",
        "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml"
    ],
    "science": [
        "https://www.newscientist.com/feed/home/",
        "http://rss.sciam.com/ScientificAmerican-Global",
        "https://www.sciencealert.com/feed"
    ]
}


def fetch_content():
    print("Fetching content...")
    content = {}

    for category, feeds in RSS_FEEDS.items():
        for feed_url in feeds:
            print(f"Fetching content from {feed_url}")
            content[category] = [] if category not in content else content[category]
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:3]:
                article_title = entry.title
                article_content = entry.get("content", [{"value": entry.summary}])[0]["value"]
                article_link = entry.link
                content[category].append({"title": article_title, "content": article_content, "link": article_link})

    json.dump(content, open("example_data/content.json", "w"), indent=2)


if __name__ == "__main__":
    fetch_content()
    print(f"Content: {json.load(open('example_data/content.json'))}")
