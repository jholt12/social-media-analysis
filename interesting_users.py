def calculate_user_scores(users, criteria):
    """
    Calculate scores for users based on selected criteria.
    Criteria example: {'posts': 'high', 'reading_level': 'high'}
    """
    for user, attributes in users.items():
        posts_weight = 0.7 if criteria.get('posts') == 'high' else 0.3
        reading_level_weight = 0.7 if criteria.get('reading_level') == 'high' else 0.3
        attributes['score'] = (
            attributes['posts'] * posts_weight +
            attributes['reading_level'] * reading_level_weight
        )

def filter_and_rank_users(users):
    """Filter and rank users by score."""
    sorted_users = sorted(users.items(), key=lambda x: x[1]['score'], reverse=True)
    return sorted_users

if __name__ == "__main__":
    # Example data
    users = {
        "user123": {"posts": 5, "reading_level": 10},
        "user456": {"posts": 2, "reading_level": 6},
        "user789": {"posts": 8, "reading_level": 7}
    }
    criteria = {"posts": "high", "reading_level": "high"}

    calculate_user_scores(users, criteria)
    ranked_users = filter_and_rank_users(users)
    print("Ranked Users:", ranked_users)