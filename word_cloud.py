from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(posts):
    """
    Generate a word cloud from a list of posts.
    """
    # Combine all posts into a single text
    text = " ".join(posts)

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # Example posts
    posts = [
        "Learning Python is fun and useful.",
        "Python is great for data analysis.",
        "Word clouds are a great way to visualize text data."
    ]
    generate_word_cloud(posts)