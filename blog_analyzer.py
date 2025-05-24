import os
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib

matplotlib.use('TkAgg')  # This forces GUI rendering
import nltk
from nltk.corpus import stopwords

# Download stopwords only once
nltk.download('stopwords')
STOP_WORDS = set(stopwords.words('english'))

# Basic stop words list (can be expanded or replaced with NLTK)
STOP_WORDS = {
    "the", "and", "is", "in", "of", "to", "a", "with", "this", "for", "on",
    "that", "it", "as", "was", "at", "by", "from", "an", "be", "has", "are",
    "but", "or", "not", "you", "we", "they", "he", "she", "his", "her", "its"
    "then", "these", "into", "using", "than"
}


# Load all blog text files
def load_blog_texts(folder_path):
    full_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                full_text += file.read().lower() + " "
    return full_text

# Get top word frequencies
def get_top_words(text, n=10):
    words = [
        word for word in text.split()
        if word.isalpha() and word not in STOP_WORDS
    ]
    return Counter(words).most_common(n)


# Plot a bar chart of top words
def plot_word_bar_chart(word_freq):
    if not word_freq:
        print("No data to plot.")
        return

    words, counts = zip(*word_freq)

    fig, ax = plt.subplots(figsize=(10, 5))  # Use subplots for more control
    ax.bar(words, counts, color='orange')
    ax.set_title("Top Words in Blog Posts")
    ax.set_xlabel("Words")
    ax.set_ylabel("Frequency")
    plt.xticks(rotation=45)

    plt.tight_layout()

    # Save the figure from the 'fig' object, not global state
    fig.savefig("top_words_chart.png")
    print("Saved: top_words_chart.png")

    plt.show()


def generate_wordcloud(text):
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud of Blog Content")
    plt.show()
    wc.to_file("wordcloud.png")
    print("Saved: wordcloud.png")


# Analyze sentiment using TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, polarity


# Run the complete analyzer
def run_blog_analyzer():
    folder = "data"
    blog_text = load_blog_texts(folder)

    print("\n📊 Top 10 Words:")
    top_words = get_top_words(blog_text)
    for word, count in top_words:
        print(f"{word}: {count}")

    plot_word_bar_chart(top_words)
    generate_wordcloud(blog_text)

    sentiment, score = analyze_sentiment(blog_text)
    print("DEBUG - Word frequency:", top_words)
    print(f"\n Overall Sentiment: {sentiment} (Polarity Score: {score:.2f})")


# Run the script
if __name__ == "__main__":
    run_blog_analyzer()
