import heapq
from datetime import datetime, timedelta

def calculate_attention_rate(posts):
    """
    Calculate the attention rate for each post.
    Attention Rate = (new views + new comments) / time period in hours.
    """
    for post in posts:
        post['attention_rate'] = (
            (post['views'] + post['comments']) / post['time_frame']
        )

def get_trending_posts(posts, k=3):
    """
    Identify top-k trending posts using a max-heap (priority queue).
    """
    return heapq.nlargest(k, posts, key=lambda x: x['attention_rate'])

if __name__ == "__main__":
    # Example posts with views, comments, and time frame in hours
    posts = [
        {"post_id": "post001", "views": 100, "comments": 20, "time_frame": 2},
        {"post_id": "post002", "views": 200, "comments": 15, "time_frame": 1},
        {"post_id": "post003", "views": 50, "comments": 30, "time_frame": 4}
    ]

    calculate_attention_rate(posts)
    trending_posts = get_trending_posts(posts, k=2)
    print("Trending Posts:", trending_posts)